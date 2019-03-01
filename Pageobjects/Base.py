from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time,os.path
logger=Logger(logger="BasePage").getlog()
#基类，父类
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger=logger
    #后退
    def back(self):
        self.driver.back()
        self.logger.info("页面后退")
    def forward(self):
        self.driver.forward()
    def open_url(self,url):
        self.driver.get(url)
        self.logger.info("打开网页："+url)
    def quit_browser(self):
        self.driver.quit()
    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            self.get_windows_img()
            print(e)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
        except Exception as e:
            self.get_windows_img()
            print(e)
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
        except Exception as e:
            self.get_windows_img()
            print(e)
    #查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            self.logger.info("%s找到页面元素:%s"%(self,loc))
            return self.driver.find_element(*loc)
        except:
            self.get_windows_img()
            self.logger.error("%s页面未能找到%s元素"%(self,loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
            self.logger.info("%s找到页面元素:%s" % (self, loc))
            return self.driver.find_elements(*loc)
        except:
            self.get_windows_img()
            self.logger.error("%s页面未能找到%s元素" % (self, loc))

    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
        except Exception as e:
            print(e)
            self.get_windows_img()
    def jihuo(self):
        for handles in self.driver.window_handles:
            self.driver.switch_to_window(handles)
    def jihuo2(self):
        self.driver.switch_to.frame(0)
    def gettext(self,*loc):
        el=self.find_element(*loc)
        try:
            return el.text
        except Exception as e:
            print(e)
            self.get_windows_img()
    def gettexts(self,*loc):
        el = self.find_elements(*loc)
        try:
            return el
        except Exception as e:
            print(e)
            self.get_windows_img()
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rp=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path +rp+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name )
            logger.info("有截屏并且保存的路径是/screenshots/")
        except Exception as e:
            self.get_windows_img()
            logger.error("%s截屏失败%s"%e)