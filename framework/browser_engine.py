import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import  Logger
logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.') )
    chrome_driver_path=dir +'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path )
        browser=config.get('browserType','browserName')
        logger.info('you had select %s browser.'%browser)
        url=config.get('testServer','URL')
        logger.info('the test server url is: %s'%url)
        if browser =='Firefox':
            logger.info('Starting firefox browser.')
        elif browser =='Chrome':
            self.driver = webdriver .Chrome (self.chrome_driver_path )
            logger.info("打开浏览器")
        elif browser =='IE':
            self.driver =webdriver .Ie(self .chrome_driver_path )
            logger.info('Starting IE browser')
        self.driver.get(url)
        logger.info('Open url: %s' %url)
        self.driver.maximize_window()
        logger.info('Maximize the current window.')
        self.driver.implicitly_wait(10)
        logger.info('Set implicitly wait 10 seconds.')
        return self.driver
    def quit_browser(self):
        logger.info('New,Close and quit the browser')
        self.driver.quit()