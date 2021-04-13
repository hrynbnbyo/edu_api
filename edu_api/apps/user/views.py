from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as http_status

from edu_api.libs.geetest import GeetestLib
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