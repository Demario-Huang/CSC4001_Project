from .BlackBox_Testing import test_code
from .BlackBox_Testing import test_register
from .BlackBox_Testing import test_login
from .BlackBox_Testing import test_logout
from .BlackBox_Testing import test_update
from .BlackBox_Testing import test_sendEmail
from .BlackBox_Testing import test_SetQuestion

class request:
    POST = {}
    GET = {}
    def __init__(self):
        self.POST = {}
        self.GET = {}

def test():
    data = {}

    # 1. test views.code()
    if (test_code.test() == 1):
        data["test-code()"] = "PASS"
    else:
        data["test-code()"] = "FAILED"
    
    # 2. test view.register
    if (test_register.test() == 1):
        data["test-register()"] = "PASS"
    else:
        data["test-register()"] = "FAILED"

    # 3. test views.login()
    if (test_login.test() == 1):
        data["test-login()"] = "PASS"
    else:
        data["test-login()"] = "FAILED"

    # 4. test views.lougout()
    if (test_logout.test() == 1):
        data["test-out()"] = "PASS"
    else:
        data["test-out()"] = "FAILED"

    # 5. test views.update()
    if (test_update.test() == 1):
        data["test-update()"] = "PASS"
    else:
        data["test-update()"] = "FAILED"

    # # 6. test sendEmail()
    # if (test_sendEmail.test() == 1):
    #     data["test-sendEmail()"] = "PASS"
    # else:
    #     data["test-sendEmail()"] = "FAILED"

    # 7. test SetQuestion()
    if (test_SetQuestion.test() == 1):
        data["test_SetQuestion()"] = "PASS"
    else:
        data["test_SetQuestion()"] = "FAILED"

    return data

    