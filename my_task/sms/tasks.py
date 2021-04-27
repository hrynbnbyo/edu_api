from edu_api.settings import constants
from edu_api.utils.message import Message
from my_task.main import app


# celery的任务必须定义在tasks文件中，别的文件名不识别
@app.task(name="send_mail")  # name 指定当前异步任务的名称  如果不给，则使用默认的函数名作为任务名
def send_mail():
    """异步发送邮件的方法"""
    print("邮件已发送")
    return "mail"


@app.task(name="send_msg")
def send_msg(phone, code):
    print("短信发送")
    message = Message(constants.API_KEY)
    print(constants.API_KEY)
    print(phone,code)
    status = message.send_message(phone, code)
    print(status)
    return "hello"

