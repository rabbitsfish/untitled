import yaml
from appium import webdriver
import logging.config
import os
import warnings
import time
CON_LOG = os.path.join(os.path.dirname(__file__), 'config/log.conf')
print('CON_LOG:', CON_LOG)
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
app_package_data = None
app_activity_data = None
def appium_desired_caps():
    with open('config/desired_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps = {}

    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformName'] = data['platformName']
    global app_package_data, app_activity_data
    desired_caps['appPackage'], app_package_data = data['appPackage'], data['appPackage']
    desired_caps['appActivity'], app_activity_data = data['appActivity'], data['appActivity']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['automationName'] = data['automationName']
    app_dir = os.path.join(os.path.dirname(__file__), data['app'])
    desired_caps['app'] = app_dir
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['newCommandTimeout'] = data['newCommandTimeout']
    #desired_caps['udid'] = udid
    logging.info('start app...')
    warnings.simplefilter("ignore", ResourceWarning)
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % str(4723), desired_caps)
    driver.implicitly_wait(3)
    return driver

if __name__ == '__main__':
    driver = appium_desired_caps()
    time.sleep(10)
    content_list = []
    for i in range(119):
        driver.swipe(400, 1, 400, 1200)
        time.sleep(2)
        elem = driver.find_element_by_id('com.android.browser:id/notification_normal_hotword_txt_11')
        content = elem.text
        elem.click()
        logging.info('click......')
        if content not in content_list:
            content_list.append(content)
            logging.info('content %s' % content)
        else:
            logging.info('content_repeat %s' % content)
        time.sleep(2)
        logging.info('content length %s' % content_list.__len__())