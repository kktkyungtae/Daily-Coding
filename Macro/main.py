from selenium import webdriver
import pyautogui

#btn = pyautogui.confirm('시작')

driver=webdriver.Chrome('C://chromedriver.exe') #크롬 드라이버
driver.get('https://camping.gtdc.or.kr/DZ_reservation/reserCamping.php?xch=reservation&xid=camping_reservation') #접속할 url

#팝업 제거
xpath = "//input[@value='Y']" #테그+속성+속성값
driver.find_element_by_xpath(xpath).click() #클릭 함수

#팝업 제거
xpath = "//html/body/div[1]/div/div[2]/button"
driver.find_element_by_xpath(xpath).click()

#날짜 지정
xpath = "//button[@value='C:2020-11-26']"
driver.find_element_by_xpath(xpath).click()

#위치 지정
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[23]"
driver.find_element_by_xpath(xpath).click()

#구역
#A147  /html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[47]
#A148  /html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[48]
#A149  /html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[49]
#A150  /html/body/div[4]/table/tbody/tr/td[3]/div/div/div[4]/div/button[50]

#D701
#D702
#D703
#D704
#D705

#인원지정
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[7]"
driver.find_element_by_xpath(xpath).click()

# 1명 : /html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[2]
# 2명 : /html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[3]
# 3명 : /html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[4]
# 4명 : /html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[5]
# 5명 : /html/body/div[4]/table/tbody/tr/td[3]/div/div/table[1]/tbody/tr/td[4]/select/option[6]

#예약 기간
#2박3일
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[5]/select/option[2]"
driver.find_element_by_xpath(xpath).click()

#예약 기간
#3박4일
#xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[5]/select/option[3]"
#driver.find_element_by_xpath(xpath).click()

#다음단계
xpath = "//html/body/div[4]/table/tbody/tr/td[3]/div/div/div[6]/button[2]"
driver.find_element_by_xpath(xpath).click()