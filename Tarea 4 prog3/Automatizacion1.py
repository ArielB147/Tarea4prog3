#Librerias
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#opciones de navegacion
class YoutubeAutomation(unittest.TestCase):
  
  def setUp(condicion):
    condicion.driver = webdriver.Chrome()
    condicion.driver.maximize_window()
    
  def test_outlook(condicion):
  
    driver = condicion.driver
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    condicion.assertIn("Google", driver.title)
    condicion.assertNotIn("No results found.", driver.page_source)
    
    #Buscar youtube
    searchBar = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    searchBar.send_keys("Youtube", Keys.ENTER)
    
    #Acceder al primer enlace
    firstLink = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.youtube.com/']")))
    firstLink.click()
    
    #Busqueda
    barra_busqueda = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    barra_busqueda.send_keys("elrubiusOMG")

    #Boton
    click_boton = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@id,'search-icon-legacy')]")))
    click_boton.click()

    #Acceder a el canal
    click_boton = wait.until(EC.presence_of_element_located((By.XPATH, "(//yt-formatted-string[@class='style-scope ytd-channel-name'][contains(.,'elrubiusOMG')])[1]")))
    click_boton.click()

    time.sleep(5)
    
  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":  unittest.main()