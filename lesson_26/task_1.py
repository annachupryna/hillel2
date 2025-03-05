from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("http://localhost:8000/dz.html")

driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
frame_1_input = driver.find_element(By.XPATH, "//input[@id='input1']")
frame_1_input.send_keys('Frame1_Secret')
frame_1_button = driver.find_element(By.XPATH, '//button')
frame_1_button.click()
frame_1_alert = Alert(driver)
assert frame_1_alert.text == 'Верифікація пройшла успішно!', 'текст в діалоговому вікні відрізняється від очікуваного'
frame_1_alert.accept()
driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.ID, 'frame2'))
frame_2_input = driver.find_element(By.XPATH, "//input[@id='input2']")
frame_2_input.send_keys('Frame2_Secret')
frame_2_button = driver.find_element(By.XPATH, '//button')
frame_2_button.click()
frame_2_alert = Alert(driver)
assert frame_2_alert.text == 'Верифікація пройшла успішно!', 'текст в діалоговому вікні відрізняється від очікуваного'

driver.quit()
