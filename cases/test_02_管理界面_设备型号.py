import pytest
from selenium.webdriver.common.by import By
import time
from lib.webUI_smp import smpUI
from cfg import *
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def inDevModelMgr(): #初始化模块管理界面

    smpUI.login('byhy','sdfsdf')
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)

    yield

    return

@pytest.fixture(scope="function")
def delAddedDeviceModel():
    yield
    print('** 删除添加的设备型号')
    smpUI.del_first_item()

    return True

@pytest.fixture(scope="function")
def addpreviousModel():
    smpUI.login('byhy', 'sdfsdf')
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model('存储柜','elife-testcase','elife作为测试的添加用例')
    time.sleep(1)
    yield
    time.sleep(1)

    return


def test_SMP_device_model_001(inDevModelMgr, delAddedDeviceModel):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model(
        '存储柜',
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小'
    )

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == [
        '存储柜',
        "elife-canbinlocker-g22-10-20-40",
        '南京e生活存储柜-10大20中40小'
    ]


def test_SMP_device_model_002(inDevModelMgr, delAddedDeviceModel):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('存储柜','测试'*50,'南京e生活存储柜-10大20中40小')

    dms = smpUI.get_first_page_device_models()
    assert dms == [[
        '存储柜',
        '测试'*50,
        '南京e生活存储柜-10大20中40小'
    ]]


def test_SMP_device_model_003(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('存储柜','测'*101,'南京e生活存储柜-10大20中40小')

    dms = smpUI.get_first_page_device_models()
    assert dms == [[
        '存储柜',
        '测'*100,
        '南京e生活存储柜-10大20中40小'
    ]]


def test_SMP_device_model_101(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('电瓶车充电站','bokpower-charger-g22-220v450w','杭州bok 2022款450瓦 电瓶车充电站')

    dms = smpUI.get_first_page_device_models()
    assert dms == [[
        '电瓶车充电站',
        'bokpower-charger-g22-220v450w',
        '杭州bok 2022款450瓦 电瓶车充电站'
    ]]


def test_SMP_device_model_102(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('洗车站','njcw-carwasher-g22-2s','南京e生活2022款洗车机 2个洗车位')
    dms = smpUI.get_first_page_device_models()

    assert dms == [[
        '洗车站',
        'njcw-carwasher-g22-2s',
        '南京e生活2022款洗车机 2个洗车位'
    ]]


def test_SMP_device_model_103(inDevModelMgr, delAddedDeviceModel):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站')
    dms = smpUI.get_first_page_device_models()

    assert dms == [[
        '汽车充电站',
        'yixun-charger-g22-220v7kw',
        '南京易迅能源2022款7千瓦汽车充电站'
    ]]


def test_SMP_device_model_201(inDevModelMgr, delAddedDeviceModel):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站')
    time.sleep(1)

    smpUI.edit_device_type('njcw-carwasher-g22-2')

    time.sleep(1)

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == ['汽车充电站',
        'njcw-carwasher-g22-2',
        '南京易迅能源2022款7千瓦汽车充电站'
    ]
    time.sleep(1)


def test_SMP_device_model_202(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model('电瓶车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站')
    time.sleep(1)

    smpUI.edit_device_class('洗车站')

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == [
        '洗车站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站'
    ]


def test_SMP_device_model_203(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model("电瓶车充电站", "yixun-charger-g22-220v7kw", "南京易迅能源2022款7千瓦汽车充电站")
    time.sleep(1)

    smpUI.edit_device_desc('南京易迅能源2023款7千瓦电瓶车充电站')

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == [
        "电瓶车充电站", "yixun-charger-g22-220v7kw", "南京易迅能源2023款7千瓦电瓶车充电站"
    ]


def test_SMP_device_model_204(inDevModelMgr, delAddedDeviceModel):

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model("电瓶车充电站", "yixun-charger-g22-220v7kw", "南京易迅能源2022款7千瓦汽车充电站")
    time.sleep(1)

    smpUI.edit_device_class('洗车站')
    time.sleep(1)
    smpUI.edit_device_desc('南京e生活2022款洗车机 2个洗车位')

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == [
        '洗车站',
        "yixun-charger-g22-220v7kw",
        '南京e生活2022款洗车机 2个洗车位'
    ]


def test_SMP_device_model_205(inDevModelMgr, delAddedDeviceModel):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model("电瓶车充电站", "yixun-charger-g22-220v7kw", "南京易迅能源2022款7千瓦汽车充电站")
    time.sleep(1)

    smpUI.edit_device_class('洗车站')
    time.sleep(1)

    smpUI.edit_device_type('njcw-carwasher-g22-2s')
    time.sleep(1)

    smpUI.edit_device_desc('南京e生活2022款洗车机 2个洗车位')

    dms = smpUI.get_first_page_device_models()
    assert dms[0] == [
        "洗车站",
        "njcw-carwasher-g22-2s",
        "南京e生活2022款洗车机 2个洗车位"
    ]


def test_SMP_device_model_301(addpreviousModel):
    smpUI.del_first_item()
    time.sleep(3)

    firstpage = smpUI.get_first_page_device_models()
    assert firstpage == []

