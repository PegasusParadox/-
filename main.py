import os
from selenium import webdriver #利用selenium做爬蟲
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from dotenv import load_dotenv
load_dotenv()
driver_path = 'D:\chromedriver_win32\chromedriver.exe'  #導入chrome driver才能開模擬器
browser = webdriver.Chrome(driver_path)
browser.get("https://tw.buy.yahoo.com/gdsale/PlayStation-5-9366951.html")
WebDriverWait(browser, 1,0.4).until(EC.presence_of_element_located((By.CLASS_NAME, "UhMenu__item___DEGdP.UhMenu__loginButton___1ArdI"))) #顯性等待 不然爬蟲跑太快了 抓不到元素
search_buy=browser.find_element(By.CLASS_NAME,"UhMenu__item___DEGdP.UhMenu__loginButton___1ArdI").click()
search_Id = browser.find_element(By.NAME,'username') #找到輸入帳號的位置 並先記錄之後要input
ac=os.getenv("yahoo_account")#從env提取帳號
search_Id.send_keys(ac) #輸入帳號   (到時候可以考慮利用腳步輸入多個帳號
browser.find_element(By.ID,'login-signin').click()
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'login-passwd'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
search_password = browser.find_element(By.ID,'login-passwd')
ps=os.getenv("yahoo_password")#從env提取密碼
search_password.send_keys(ps) #輸入密碼
browser.find_element(By.ID,'login-signin').click()
while 1:
    try:
        WebDriverWait(browser, 2,0.4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="isoredux-root"]/div/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div[9]/button[1]'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
        search_buy=browser.find_element(By.XPATH,'//*[@id="isoredux-root"]/div/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div[9]/button[1]').click()
        print("開始搶購")
        break
    except:
        print("還未定位到元素! 刷新")
        browser.refresh()

