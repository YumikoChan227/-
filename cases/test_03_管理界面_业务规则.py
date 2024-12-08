import pytest
from selenium.webdriver.common.by import By
import time
from lib.webUI_smp import smpUI
from cfg import *
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def inServiceRuleMgr(): #初始化：登录并且定位到业务规则管理界面

    smpUI.login('byhy','sdfsdf')
    smpUI.wd.get(SMP_URL_SERVICE_RULE)

    yield

    return


@pytest.fixture(scope="function")
def delAddedServiceRule(): #清除： 删除因为测试而改变的测试环境

    yield

    print('** 删除添加的业务规则 **')

    smpUI.del_first_item()



def test_SMP_service_rule_001(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()


    smpUI.add_svc_rule(
        '全国 - 电瓶车充电费率1',
        '预付费-下发业务量',
        '0.1',
        '2',
        feeRate=['千瓦时','1']
    )

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['全国 - 电瓶车充电费率1',
                      '预付费-下发业务量',
                      {'最小消费':'0.1', '预估消费': '2', '费率':'单位：千瓦时 \n单价：1'},
                      '']


def test_SMP_service_rule_002(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        '南京-洗车机费率1',
        '预付费-下发费用',
        '2',
        '10'
    )

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['南京-洗车机费率1',
                      '预付费-下发费用',
                      {'最小消费':'2', '预估消费': '10'},
                      '']

def test_SMP_service_rule_003(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
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
            ['10L','小时','0.5']
        ]
    )

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['南京-存储柜费率1',
                      '后付费-上报业务量',
                      {'费率': '业务码：100L\n单位：小时 \n单价：2\n业务码：50L\n单位：小时 \n单价：1\n业务码：10L\n单位：小时 \n单价：0.5'},
                      '']


def test_SMP_service_rule_101(inServiceRuleMgr):
    # 点击添加按钮
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

    smpUI.del_first_item()

    dms = smpUI.get_first_page_svc_rules()

    assert dms == []


def test_SMP_service_rule_102(inServiceRuleMgr):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        '南京-洗车机费率1',
        '预付费-下发费用',
        '2',
        '10'
    )

    smpUI.del_first_item()

    dms = smpUI.get_first_page_svc_rules()

    assert dms == []

def test_SMP_service_rule_103(inServiceRuleMgr):
    # 点击添加按钮
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

    smpUI.del_first_item()
    dms = smpUI.get_first_page_svc_rules()
    assert dms == []


def test_SMP_service_rule_201(inServiceRuleMgr, delAddedServiceRule):
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

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info> .field> input').clear()
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info> .field> input').send_keys('全国 - 电瓶车充电费率2')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()


    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['全国 - 电瓶车充电费率2',
                      '预付费-下发业务量',
                      {'最小消费': '0.1', '预估消费': '2', '费率': '单位：千瓦时 \n单价：1'},
                      '']


def test_SMP_service_rule_202(inServiceRuleMgr, delAddedServiceRule):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        '全国 - 电瓶车充电费率1',
        '预付费-下发业务量',
        '0.1',
        '2',
        feeRate=['千瓦时', '11']
    )

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    smpUI.wd.find_element(By.CSS_SELECTOR,'.result-list-item-info> .field:last-child>input').clear()
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info> .field:last-child>input').send_keys('添加描述测试')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    #time.sleep(4)
    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['全国 - 电瓶车充电费率1',
                      '预付费-下发业务量',
                      {'最小消费': '0.1', '预估消费': '2', '费率': '单位：千瓦时 \n单价：11'},
                      '添加描述测试']


def test_SMP_service_rule_203(inServiceRuleMgr, delAddedServiceRule):

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

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('预付费-下发费用')

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['全国 - 电瓶车充电费率1',
                      '预付费-下发费用',
                      {'最小消费': '0.1', '预估消费': '2'},
                      '']


def test_SMP_service_rule_204(inServiceRuleMgr, delAddedServiceRule):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        '南京-洗车机费率1',
        '预付费-下发费用',
        '2',
        '10'
    )

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('预付费-下发业务量')

    calunit = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info> .fee-rate-list input')
    calunit.send_keys('kwh')

    priceunit = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info> .fee-rate-list input:nth-child(4)')
    priceunit.send_keys('1')

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()
    assert dms[0] == ['南京-洗车机费率1',
                      '预付费-下发业务量',
                      {'最小消费': '2', '预估消费': '10', '费率': '单位：kwh \n单价：1'},
                      '']


def test_SMP_service_rule_205(inServiceRuleMgr, delAddedServiceRule):
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

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('后付费-上报业务量')

    fee_rate_text1 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(2)')
    fee_rate_text1.send_keys('testcase')

    fee_rate_text2 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(4)')
    fee_rate_text2.send_keys('kwh')

    fee_rate_text3 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(6)')
    fee_rate_text3.send_keys('1')

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['全国 - 电瓶车充电费率1',
                      '后付费-上报业务量',
                      {
                          '费率': '业务码：testcase\n单位：kwh \n单价：1'},
                      '']

def test_SMP_service_rule_206(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
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

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('预付费-下发业务量')

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .field:nth-child(3) >input').send_keys('1')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .field:nth-child(4) >input').send_keys('10')
    smpUI.wd.find_element(By.CSS_SELECTOR,'.result-list .fee-rate-list  .fee-rate input:nth-child(2)').send_keys('kwh')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate-list  .fee-rate input:nth-child(4)').send_keys('0.1')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()
    assert dms[0] == ['南京-存储柜费率1',
                      '预付费-下发业务量',
                      {'最小消费': '1', '预估消费': '10', '费率': '单位：kwh \n单价：0.1'},
                      '']

def test_SMP_service_rule_207(inServiceRuleMgr, delAddedServiceRule):
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area> span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        '南京-洗车机费率1',
        '预付费-下发费用',
        '2',
        '10'
    )

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('后付费-上报业务量')
    fee_rate_text1 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(2)')
    fee_rate_text1.send_keys('testcase')

    fee_rate_text2 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(4)')
    fee_rate_text2.send_keys('kwh')

    fee_rate_text3 = smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .fee-rate input:nth-child(6)')
    fee_rate_text3.send_keys('1')

    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['南京-洗车机费率1',
                      '后付费-上报业务量',
                      {
                          '费率': '业务码：testcase\n单位：kwh \n单价：1'},
                      '']

def test_SMP_service_rule_208(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
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

    editBtn = smpUI.wd.find_element(By.CSS_SELECTOR,
                                    '.result-list-item> .result-list-item-btn-bar> .btn-no-border:nth-child(2)')
    editBtn.click()

    selectcase = Select(smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list #rule_type_id'))
    selectcase.select_by_visible_text('预付费-下发费用')


    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info .field:nth-child(3) input').send_keys('1')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list-item-info .field:nth-child(4) input').send_keys('10')
    smpUI.wd.find_element(By.CSS_SELECTOR, '.result-list .result-list-item-btn-bar> span:nth-child(1)').click()

    dms = smpUI.get_first_page_svc_rules()

    assert dms[0] == ['南京-存储柜费率1',
                      '预付费-下发费用',
                      {'最小消费': '1', '预估消费': '10'},
                      '']