from Pageobjects.Discuz_homepage  import  homeDiscuz
from selenium.webdriver .common .by import By
import time
from framework.logger import Logger
logger=Logger(logger="HomePage").getlog()
class HomePage(homeDiscuz):
    def taopaio(self,zhuti,xx1,xx2,xx3):
        self.click(*self.home_page_button_search_default)
        self.click(*self.home_page_button3_search_bublishpostbt )
        self.click(*self.home_page_button4_search_vote)
        self.sendkeys(zhuti,*self.home_page_input_search_vote_style )
        self.sendkeys(xx1,*self.home_page_input_search_vote_choice1)
        self.sendkeys(xx2,*self.home_page_input_search_vote_choice2)
        self.sendkeys(xx3,*self.home_page_input_search_vote_choice3)
        self.jihuo2()
        self.sendkeys(zhuti,*self.home_page_input_search_vote_body)
        self.jihuo()
        self.click(*self.home_page_button5_search_vote_submit)
        self.logger.info("投票系列操作成功")
    def laqu(self):
        result=self.gettexts(*self.home_page_input_search_vote_result)
        choicetext=self.gettexts(*self.home_page_input_search_vote_choicetext)
        styletext=self.gettext(*self.home_page_input_search_vote_styletext)
        self.logger.info("投票主题%s"%styletext)
        for h in range(0,len(choicetext)):
              if not( result[h].text==''or '提交'in result[h].text):
                   self.logger.info("选项%s"%result[h].text)
              if not (choicetext[h].text == '' or '提交' in choicetext[h].text):
                   self.logger.info( '结果%s'%choicetext[h].text)
        return result
    def zhucaoz(self, ss):  # 主操作
        self.sendkeys(ss, *self.home_page_input_search)
        self.click(*self.home_page_button_search_submit)
        self.jihuo()
        self.click(*self.home_page_button_search_posttitle)
        self.jihuo()
        biaoti = self.gettext(*self.home_page_text_search_posttitle)
        return biaoti
    def delet(self): #删除帖子
        self.click(*self.home_page_button_search_choosepost)
        self.click(*self.home_page_button_search_del)
        self.click(*self.home_page_button_search_ture)
        self.logger.info("删除帖子成功")
    def add(self,Hpassword,bkname):
        self.click(*self.home_page_button_search_admin_center)
        self.jihuo()
        # if self.driver.title=='登陆管理中心':
        self.sendkeys(Hpassword, *self.home_page_input_search_adminpassword)
        self.click(*self.home_page_button7_search_loginadmin)
        self.jihuo()
        self.click(*self.home_page_button8_search_forum)
        self.jihuo2()
        self.click(*self.home_page_button9_search_addbk)
        self.clear(*self.home_page_input_search_bkname)
        self.sendkeys(bkname, *self.home_page_input_search_bkname)
        self.click(*self.home_page_button10_search_bksubmit)
        self.logger.info("运行成功")
    def tuichu(self): #推出推出
        self.jihuo()
        self.click(*self.home_page_button11_search_adminexit)
        self.jihuo()
        self.click(*self.home_page_tuichu_search_loc)
    def new(self,biaoti,neirong):  #用户发帖回帖
        self.click(*self.home_page_button14_search_newbk)
        time.sleep(2)
        self.sendkeys(biaoti,*self.home_page_input_search_posttitle)  # 输入用户
        time.sleep(2)
        self.sendkeys(neirong, *self.home_page_input_search_postbody)
        time.sleep(3)
        self.click(*self.home_page_button_search_bublishpost)
        self.sendkeys(neirong, *self.home_page_input_search_postbody)
        time.sleep(3)
        self.click(*self.home_page_button4_search_reply)
        replytext = self.gettext(*self.home_page_button4_search_reply)
        self.logger.info("发布成功")
        return replytext
    def zhucaozuo(self,litter,neirong,huifu):  #发帖回复
        self.sendkeys(litter, *self.home_page_input_search_posttitle)
        self.sendkeys(neirong, *self.home_page_input_search_postbody)
        self.click(*self.home_page_button_search_bublishpost)
        self.sendkeys(huifu, *self.home_page_input_search_replybody)
        time.sleep(15)
        self.click(*self.home_page_button4_search_reply)
        replytext=self.gettext(*self.home_page_button4_search_reply)
        self.logger.info("回复成功")
        return replytext
    def search1(self,user,password,litter,neirong,huifu):
        self.logins(user,password)
        self.default()
        reply=self.zhucaozuo(litter,neirong,huifu)
        self.exit()
        return reply
    def search2(self,Huser,Hpassword,bkname,user,biaoti,neirong):
        self.adminlogin(Huser,Hpassword)
        self.default()
        self.delet()
        self.add(Hpassword,bkname)
        self.tuichu()
        self.jihuo()
        self.logins(user,Hpassword)
        reply=self.new(biaoti,neirong)
        return reply
    def search3(self, Huser, Hpassword, ss):
        self.adminlogin(Huser, Hpassword)
        s = self.zhucaoz(ss)
        self.exit()
        return s
    def search4(self):
        self.adminlogin('admin','123456')
        self.taopaio('北京，你好','赞','中','差')
        reust=self.laqu()
        return reust

