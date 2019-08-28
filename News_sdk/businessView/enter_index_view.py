from News_sdk.baseView import base_view
from selenium.webdriver.common.by import By
import logging
class EnterIndexView(base_view.BaseView):
    enter_index_data = (By.ID, 'com.dl.infostreamdemo:id/view_api')
    first_news_display_data = (By.ID, 'com.dl.infostreamdemo:id/tv_normal_refresh_header_status')
    def enter_index_data_click(self):
        elem = self.find_element_news(self.enter_index_data)
        if elem:
            elem.click()
        else:
            logging.info('not found %s' % self.enter_index_data[1])