import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")
    yield driver
    driver.quit()

def assert_amount(driver, search_term, expected_count):
    search_box = driver.find_element(By.ID, "searchField")
    
    search_box.clear()
    
    search_box.send_keys(search_term)
    
    search_box.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "content"))
    )

    results = driver.find_elements(By.CLASS_NAME, "content")

    assert len(results) == int(expected_count), f"Błąd: Oczekiwano {expected_count} wyników, ale znaleziono {len(results)}."

    for product in results:
        description = product.find_element(By.CLASS_NAME, 'description')
        print(description.text)

def test_store(setup):
    driver = setup

    assert_amount(driver, "Laptop", "3")
    assert_amount(driver, "NoteBook", "2")
    assert_amount(driver, "Gaming", "1")
