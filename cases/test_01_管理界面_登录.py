import time

from selenium.webdriver.common.by import By
from lib.webUI_smp import smpUI
import pytest

# 用户名密码输入正确-成功登录
def test_SMP_login_001():
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhy','sdfsdf')

    nav = smpUI.wd.find_elements(By.TAG_NAME, "nav")
    assert nav != []

@pytest.fixture
def clearAlert():
    yield
    try:
        smpUI.wd.switch_to.alert.accept()
    except Exception as e:
        print(e)


# 用户名/密码缺失 - 生成提示
def test_SMP_login_101(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login(None,'sdfsdf')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '请输入用户名'


def test_SMP_login_102(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhy', None)
    time.sleep(2)
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '请输入密码'


def test_SMP_login_103(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login(None, None)
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '请输入用户名'


# 用户名/密码多一位/少一位
def test_SMP_login_201(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhy', 'sdfsdf1')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名或者密码错误'


def test_SMP_login_202(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhy', 'sdfsd')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名或者密码错误'


def test_SMP_login_203(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhyy', 'sdfsdf')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名不存在'


def test_SMP_login_204(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byh', 'sdfsdf')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名不存在'


# 用户名/密码大小写不匹配
def test_SMP_login_301(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('BYHY', 'sdfsdf')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名不存在'


def test_SMP_login_302(clearAlert):
    smpUI.wd.implicitly_wait(5)
    smpUI.login('byhy', 'SDFSDF')
    alert = smpUI.wd.switch_to.alert
    assert alert.text == '登录失败： 用户名或者密码错误'
