from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r'E:\Beautiful-soup\Driver\chromedriver.exe')
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.find_element_by_id('search').send_keys("Filhal")

driver.find_element_by_id('search-icon-legacy').click()
driver.find_element_by_link_text('FILHALL | Akshay Kumar Ft Nupur Sanon | BPraak | Jaani | Arvindr Khaira | Ammy Virk | Official Video').click()
time.sleep(30)
driver.quit()