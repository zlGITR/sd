from Pageobjects.Base import  BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
logger=Logger(logger="homeDiscuz").getlog()
class homeDiscuz(BasePage):
    home_page_input_search_user = (By.ID ,'ls_username')
    home_page_input_search_password = (By.ID, 'ls_password')
    home_page_button_search_loc = (By.XPATH ,'//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em')#点击登陆
    home_page_tuichu_search_loc =(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(18)')  # 点击退出
    home_page_button_search_default = (By.XPATH, '//*[@id="category_1"]/table/tbody/tr[1]/td[2]/h2/a')  # 点击默认板块
    home_page_input_search_posttitle = (By.ID, 'subject')  # 帖子标题
    home_page_input_search_postbody = (By.ID, 'fastpostmessage')#帖子内容
    home_page_button_search_bublishpost = (By.CSS_SELECTOR, ".ptm button")  #点击发布
    home_page_input_search_replybody = (By.ID, 'fastpostmessage')  # 输入回复信息
    home_page_button4_search_reply = (By.ID, 'fastpostsubmit')  # 点击回复
    home_page_button_search_choosepost = (By.NAME, 'moderate[]')  # 选择贴子
    home_page_button_search_del = (By.CSS_SELECTOR, '#mdly > p:nth-child(6) > strong:nth-child(1) > a')  # 点击删除
    home_page_button_search_ture = (By.ID, 'modsubmit')  # 点击确认
    home_page_button_search_admin_center = (By.CSS_SELECTOR, '#um > p:nth-child(2) > a:nth-child(16)')  # 点击管理中心
    home_page_input_search_adminpassword = (By.NAME, 'admin_password')  # 登陆管理模块
    home_page_button7_search_loginadmin = (By.CSS_SELECTOR, '#loginform > p.loginnofloat > input')  # 点击登陆
    home_page_button8_search_forum = (By.ID, 'header_forum')  # 点击论坛
    home_page_button9_search_addbk = (By.CSS_SELECTOR, '.lastboard a')  # 点击添加新模块
    home_page_input_search_bkname = (By.NAME, 'newforum[1][]')  # 输入模块名字
    home_page_button10_search_bksubmit = (By.ID, 'submit_editsubmit')  # 点击提交
    home_page_button11_search_adminexit = (By.XPATH, '//*[@id="frameuinfo"]/p[1]/a')  # 管理员退出
    home_page_button14_search_newbk = (By.CSS_SELECTOR, '#category_1 > table > tbody > tr:nth-last-child(2) > td:nth-child(2) > h2 > a')#新板块发帖
    home_page_input_search = (By.ID, 'scbar_txt')  # 搜索内容
    home_page_button_search_submit = (By.ID, 'scbar_btn')  # 点击搜索
    home_page_button_search_posttitle=(By.XPATH ,'//*[@id="44"]/h3/a/strong/font') #点击匹配帖子标题
    home_page_text_search_posttitle=(By.ID,'thread_subject') #匹配帖子标题文本
    home_page_button3_search_bublishpostbt = (By.ID, 'newspecial')
    home_page_button4_search_vote = (By.CSS_SELECTOR, '#editorbox > ul > li:nth-child(2) > a')
    home_page_input_search_vote_style = (By.ID, 'subject')
    home_page_input_search_vote_choice1=(By.CSS_SELECTOR ,'#pollm_c_1 > p:nth-child(1) > input')
    home_page_input_search_vote_choice2=(By.CSS_SELECTOR ,'#pollm_c_1 > p:nth-child(2) > input')
    home_page_input_search_vote_choice3=(By.CSS_SELECTOR ,'#pollm_c_1 > p:nth-child(3) > input')
    home_page_input_search_vote_body = (By.CSS_SELECTOR, 'body')
    home_page_button5_search_vote_submit = (By.NAME, 'topicsubmit')
    home_page_input_search_vote_result = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody>tr>td:nth-child(2)')
    home_page_input_search_vote_choicetext = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody>tr>td:last-of-type')
    home_page_input_search_vote_styletext = (By.CSS_SELECTOR, '.ts>span')
    def adminlogin(self,Huser,Hpassword):    # 管理员登陆
        self.sendkeys(Huser, *self.home_page_input_search_user)  # 输入用户
        self.sendkeys(Hpassword, *self.home_page_input_search_password)
        self.click(*self.home_page_button_search_loc)
        self.logger.info("登陆成功")
    def logins(self,user,Hpassword): #用户登陆
        self.sendkeys(user, *self.home_page_input_search_user)  # 输入用户
        self.sendkeys(Hpassword, *self.home_page_input_search_password)
        self.click(*self.home_page_button_search_loc)
    def exit(self):   #点击退出
        self.click(*self.home_page_tuichu_search_loc)
    def default(self):   #点击默认板块
        self.click(*self.home_page_button_search_default)
