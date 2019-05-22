from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://services.dps.ohio.gov/BMVOnlineServices/VR/Availability/Passenger/Check")

NewPlate = driver.find_element_by_id('NewPlateNumber')
Button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[1]/div[2]/fieldset/div/button')
wait = WebDriverWait(driver, 0.7)

for x in range(100, 1000):
    NewPlate.send_keys(x)
    Button.click()
    NewPlate.clear()
    try:
        wait.until(EC.presence_of_element_located((By.ID, 'SelectedImage')))
    except:
        continue
    print(x)

# to split the string...
# copy/paste results into s
# s = 'string'
# n = 3
# sl = [s[i:i+n] for i in range(0, len(s), n)]
# result = ', '.join(sl)
# print(sl)
