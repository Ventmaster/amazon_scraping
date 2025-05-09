from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import time

# LambdaTest credentials
username = "eashan455"  # Replace with your LambdaTest username
access_key = "LT_BcH9xugwrTsjZ5Zd3jiwgzzjV4c1KqDbVTCyPqPibYBS6vD"  # Replace with your LambdaTest access key

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# LambdaTest capabilities
capabilities = {
    "platform": "Windows 10",
    "browserName": "chrome",
    "version": "latest",
    "name": "Amazon Product Scraping",  # Test name
    "build": "LambdaTest Build",  # You can name the build as per your preference
    "console": "true",
    "network": "true",
    "video": "true",  # Enables video recording of your test
}

# LambdaTest remote WebDriver URL
remote_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"

# Set up the remote WebDriver for LambdaTest
driver = webdriver.Remote(
    command_executor=remote_url,
    options=options
)

try:
    # Step 1: Navigate to Amazon India
    driver.get("https://www.amazon.in")

    # Step 2: Search for iPhone
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("iPhone")
    search_box.submit()

    # Step 3: Wait for search results and click on the first product image
    first_product_image = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img.s-image"))
    )
    first_product_image.click()

    # Wait for the page to load
    time.sleep(3)

    # Handle multiple windows (if opened)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

    # Step 4: Get page source after the product page loads
    page_source = driver.page_source

    # Step 5: Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the product name
    try:
        title = soup.find('span', attrs={'id': 'productTitle'})
        title_value = title.string
        title_string = title_value.strip().replace(',', '')
    except AttributeError:
        title_string = "NA"

    print("Product title = ", title_string)

    # Extract the price
    try:
        price_tag = soup.find('span', class_='a-price-whole')
        price = price_tag.get_text(strip=True).replace(',', '') if price_tag else "NA"
    except AttributeError:
        price = "NA"

    print("Product price = ", price)

except TimeoutException as e:
    print("TimeoutException: An element could not be found or interacted with in time.")
except NoSuchElementException as e:
    print("NoSuchElementException: The element was not found.")
except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    # Allow some time to observe result before quitting
    time.sleep(5)
    driver.quit()