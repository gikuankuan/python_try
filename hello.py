# 載入需要的套件
from selenium import webdriver

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome()
# 方法二：或是直接指定exe檔案路徑
#driver = webdriver.Chrome("C:\Users\User\Desktop\py\chromedriver")
driver.get("https://www.thsrc.com.tw/") # 更改網址以前往不同網頁
#driver.close() # 關閉瀏覽器視窗