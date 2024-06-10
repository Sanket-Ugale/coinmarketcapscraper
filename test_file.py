from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_start_scraping_view():
    driver = webdriver.Chrome('/path/to/chromedriver')  # replace with the path to your ChromeDriver
    driver.get('http://localhost:8000/api/taskmanager/start_scraping')  # replace with the URL of your StartScrapingView

    # Find the input elements
    coins_input = driver.find_element_by_name('coins')

    # Input some data
    coins_input.send_keys('bitcoin, ethereum')
    coins_input.send_keys(Keys.RETURN)

    # Check the response
    assert 'job_id' in driver.page_source

    driver.quit()