from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver') # Call Driver
driver.get("https://www.google.com/") # Get url: www.gooogle.com
print (driver.title) # Print title is : Google

search = driver.find_element_by_name('q')
search.clear()
search.send_keys("selenium")
search.send_keys(Keys.RETURN)