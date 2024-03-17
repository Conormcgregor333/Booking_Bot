from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
BASE_URL="https://www.booking.com/index.html?aid=2167732&label=f59a7ad0df5e11eea48ba748eb3d9a3d"


os.environ['PATH']+=r"C:\SeleniumDrivers"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get(BASE_URL)
driver.maximize_window()
#The below try and exception block will close the sign up op up!!

try:
    # Wait for the pop-up to appear
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'c0528ecc22'))
    )
    
    # Close the pop-up (assuming there's a close button)
    close_button = popup.find_element(By.XPATH,'//*[@id="b2indexPage"]/div[18]/div/div/div/div[1]/div[1]/div/button')
    close_button.click()
except Exception as e:#do nothing if pop up not there
    pass
     
 #To put the place we are going
place='seoul'
to_visit=driver.find_element(By.XPATH,'//*[@id="ss"]')
to_visit.clear()
to_visit.send_keys(f'{place}')

#To select dates
check_in=driver.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div')
check_in.click()
start_date='2024-03-20'
go_date=driver.find_element(By.CSS_SELECTOR,f'td[data-date="{start_date}"]')
go_date.click()
end_date='2024-04-30'
return_date=driver.find_element(By.CSS_SELECTOR,f'td[data-date="{end_date}"]')
return_date.click()

#to select number of people
ppl=driver.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[3]')
ppl.click()
ad_neg=driver.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[1]')
for i in range(1,2):
    ad_neg.click()
adult=2
childern=2
rooms=2
ad_pos=driver.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]')
for i in range(1,adult):
    ad_pos.click()
#child=driver.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[2]/div/div[2]/button[2]')
#for i in range(1,childern+1):
#    child.click()
room=driver.find_element(By.XPATH,'//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div[2]/button[2]')
for i in range(1,rooms):
    room.click()
                
search=driver.find_element(By.XPATH,'//*[@id="frm"]/div[1]/div[4]/div[2]/button')
search.click()



 
   