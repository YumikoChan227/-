import pytest
from selenium.webdriver.common.by import By
import time
from lib.webUI_smp import smpUI
from cfg import *
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def inMachineMgr(): #初始化：登录并且定位到业务规则管理界面

    smpUI.login('byhy','sdfsdf')
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)


    # 添加设备
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model(
        '存储柜',
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小'
    )

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model(
        '电瓶车充电站',
        'bokpower-charger-g22-220v450w',
        '杭州bok 2022款450瓦 电瓶车充电站'
    )

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model(
        '洗车站',
        'njcw-carwasher-g22-2s',
        '南京e生活2022款洗车机 2个洗车位'
    )

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model(
        '汽车充电站',
        'yixun-charger-g22-220v7kw',
        '南京易迅能源2022款7千瓦汽车充电站'
    )

    # 添加计费规则
    smpUI.wd.get(SMP_URL_SERVICE_RULE)

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_svc_rule(
        '全国 - 电瓶车充电费率1',
        '预付费-下发业务量',
        '0.1',
        '2',
        feeRate=['千瓦时', '1']
    )

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_svc_rule(
        '南京-洗车机费率1',
        '预付费-下发费用',
        '2',
        '10'
    )

    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_svc_rule(
        '南京-存储柜费率1',
        '后付费-上报业务量',
        None,
        None,
        feeRate=[
            ['100L', '小时', '2'],
            ['50L', '小时', '1'],
            ['10L', '小时', '0.5']
        ]
    )

    yield

    smpUI.wd.get(SMP_URL_DEVICE_MODEL)
    smpUI.del_first_item()

    time.sleep(1)
    smpUI.del_first_item()

    time.sleep(1)
    smpUI.del_first_item()

    time.sleep(1)
    smpUI.del_first_item()

    smpUI.wd.get(SMP_URL_SERVICE_RULE)
    time.sleep(1)
    smpUI.del_first_item()

    time.sleep(1)
    smpUI.del_first_item()

    time.sleep(1)
    smpUI.del_first_item()



    return

@pytest.fixture(scope="function")
def delAddedDeviceModel():
    yield
    smpUI.wd.get(SMP_URL_MACHINE)
    print('** 删除添加的设备')
    smpUI.del_first_item()

    return True

def test_SMP_machine_001(inMachineMgr,delAddedDeviceModel):
    smpUI.wd.get(SMP_URL_MACHINE)
    smpUI.wd.implicitly_wait(5)
    addBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if addBtn.text == '添加':
        addBtn.click()

    smpUI.add_machine(
        '电瓶车充电站', 'bokpower-charger-g22-220v450w', '全国 - 电瓶车充电费率1','testcase001','testcase001_desc')

    time.sleep(1)
    dms = smpUI.get_first_page_device_models_device()
    print(dms)
    assert dms[0][0:3] == ['电瓶车充电站',
                           'bokpower-charger-g22-220v450w',
                           'testcase001']
    assert  dms[0][3:]==['全国 - 电瓶车充电费率1','testcase001_desc']

def test_SMP_machine_002(inMachineMgr, delAddedDeviceModel):

    smpUI.wd.get(SMP_URL_MACHINE)
    smpUI.wd.implicitly_wait(5)
    addBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if addBtn.text == '添加':
        addBtn.click()

    smpUI.add_machine(
        '洗车站', 'njcw-carwasher-g22-2s', '南京-洗车机费率1', 'testcase002', 'testcase002_desc')

    time.sleep(1)
    dms = smpUI.get_first_page_device_models_device()
    print(dms)
    assert dms[0]== ['洗车站',
                           'njcw-carwasher-g22-2s',
                           'testcase002','南京-洗车机费率1', 'testcase002_desc']


def test_SMP_machine_003(inMachineMgr, delAddedDeviceModel):

    smpUI.wd.get(SMP_URL_MACHINE)
    smpUI.wd.implicitly_wait(5)
    addBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if addBtn.text == '添加':
        addBtn.click()

    smpUI.add_machine(
        '存储柜', 'elife-canbinlocker-g22-10-20-40', '南京-存储柜费率1', 'testcase003', 'testcase003_desc')

    time.sleep(1)
    dms = smpUI.get_first_page_device_models_device()
    print(dms)
    assert dms[0]== ['存储柜',
                           'elife-canbinlocker-g22-10-20-40',
                           'testcase003','南京-存储柜费率1', 'testcase003_desc']

def test_SMP_machine_004(inMachineMgr, delAddedDeviceModel):

    smpUI.wd.get(SMP_URL_MACHINE)
    smpUI.wd.implicitly_wait(5)
    addBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if addBtn.text == '添加':
        addBtn.click()

    smpUI.add_machine(
        '电瓶车充电站', 'bokpower-charger-g22-220v450w', '南京-存储柜费率1', 'testcase004', 'testcase004_desc')

    time.sleep(1)
    dms = smpUI.get_first_page_device_models_device()
    print(dms)
    assert dms[0]== ['电瓶车充电站',
                           'bokpower-charger-g22-220v450w',
                           'testcase004','南京-存储柜费率1', 'testcase004_desc']