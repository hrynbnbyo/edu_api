import random

from django_redis import get_redis_connection
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as http_status, serializers

from edu_api.libs.geetest import GeetestLib
from edu_api.utils.message import Message
from user.models import UserInfo
from user.serializers import UserModelSerializer
from user.utils import get_user_by_account

pc_geetest_id = "eceb3f15b58977f4ccbf2680069aa19d"
pc_geetest_key = "2193c33833d27bf218e80d400618f525"


class CaptchaAPIView(APIView):
    """
    极验验证码视图类
    """
    user_id = 0
    status = False

    def get(self, request):
        """获取验证码方法"""

        account = request.query_params.get('username')
        # 根据前端输入的账号来获取对应的用户
        user = get_user_by_account(account)

        if user is None:
            return Response({"msg": "用户不存在"}, status=http_status.HTTP_400_BAD_REQUEST)

        self.user_id = user.id
        # 构建一个验证码对象
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        self.status = gt.pre_process(self.user_id)
        # 响应获取的数据
        response_str = gt.get_response_str()
        return Response(response_str)

    def post(self, request):
        """比对验证码的方法"""
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.data.get(gt.FN_CHALLENGE, '')
        validate = request.data.get(gt.FN_VALIDATE, '')
        seccode = request.data.get(gt.FN_SECCODE, '')
        account = request.data.get("account")
        user = get_user_by_account(account)

        if user:
            result = gt.success_validate(challenge, validate, seccode, user.id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)


class UserAPIView(CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserModelSerializer


class SendMessageAPIView(APIView):
    def get(self,request):
        phone = request.query_params.get("phone")
        flag = request.query_params.get("flag")
        print(flag,type(flag))
        print(flag == "1")
        if flag == '0':
            user = UserInfo.objects.filter(phone=phone)
            print(user)
            print(not user)
            if not user:
                return Response("手机号不存在，请重新输入或前往注册",status=http_status.HTTP_400_BAD_REQUEST)
        elif flag == '1':
            user = UserInfo.objects.filter(phone=phone)
            print(user)
            if user:
                return Response("手机号存在，请前往登录",status=http_status.HTTP_400_BAD_REQUEST)

        # 获取redis链接
        redis_connection = get_redis_connection("sms_code")
        # 1.60秒限制判断
        phone_code = redis_connection.get("sms_%s" % phone)
        redis_connection.get("sms_%s" % phone)
        # 2.生成验证码
        if phone_code:
            return Response({"message":"您已经在60秒内发送过验证码了~"})
        code = "%06d" % random.randint(0,999999)
        # 3.存redis
        redis_connection.setex(f"sms_{phone}",60,code)
        redis_connection.setex(f"mobile_{phone}",600,code)
        # 4.发送短信验证码
        # message = Message("40d6180426417bfc57d0744a362dc108")
        # status = message.send_message(phone, code)
        # status = status.json()
        # print(status)
        # 5.返回结果
        return Response({"message":"发送短信成功"})



class PhoneLoginAPIView(APIView):
    def post(self,request):
        phone = request.data.get("phone")
        code = request.data.get("sms_code")
        from django_redis import get_redis_connection
        connection = get_redis_connection("sms_code")
        redis_code = connection.get(f"mobile_{phone}")
        if redis_code.decode() != code:
            return Response("验证码不正确", status=http_status.HTTP_400_BAD_REQUEST)
        user = UserInfo.objects.get(phone=phone)
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({"username":user.username,"token":token})

