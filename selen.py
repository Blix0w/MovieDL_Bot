from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from core_requests import get_dl_link_all
options = Options()
options.add_argument("-profile")
# put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field
options.add_argument("/home/julien/.mozilla/firefox/2q5haw0c.default-release")
driver = webdriver.Firefox(options=options)

driver.get(get_dl_link_all("django"))
time.sleep(4)
button = driver.find_element(By.ID, "subButton")
button.click()
driver.close()
