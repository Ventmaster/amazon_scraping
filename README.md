# Amazon Product Scraping and Automated Testing with Selenium

This project uses **Selenium WebDriver** and **BeautifulSoup** to scrape product details from Amazon India, with the ability to run tests locally or on **LambdaTest**. The scripts automate the process of searching for an iPhone or Galaxy device on Amazon, navigating to the product page, and extracting the product title and price.

---

## 📂 Files Overview

| File Name              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `app1.py`              | Automates scraping the first listed **iPhone** product on Amazon.in         |
| `app2.py`              | Automates scraping the first listed **Galaxy** product on Amazon.in         |
| `lambdatest_for_iphone.py` | Runs the iPhone scraping test on **LambdaTest's cloud Selenium grid** |
| `lambdatest_for_galaxy.py` | Runs the Galaxy scraping test on **LambdaTest's cloud Selenium grid** |
---

## ✅ Automated Test Cases

### 🧪 Test Case 1: iPhone Product Flow

- Navigate to [Amazon India](https://www.amazon.in)
- Search for "iPhone"
- Click the first product listed
- Retrieve and print the **product name** and **price**
- (LambdaTest support available via `lambdatest_for_iphone.py`)

### 🧪 Test Case 2: Galaxy Product Flow

- Navigate to [Amazon India](https://www.amazon.in)
- Search for "Galaxy"
- Click the first product listed
- Retrieve and print the **product name** and **price**
- (LambdaTest support available via `lambdatest_for_iphone.py`)

---

## 🛠️ Technologies Used

- **Language**: Python
- **Automation Framework**: Selenium
- **HTML Parsing**: BeautifulSoup
- **Cloud Testing**: LambdaTest
- **Browser**: Google Chrome (both headless and GUI)

---

## 🔄 Parallel Execution

To execute Test Case 1 and Test Case 2 **in parallel**, you can use Python’s `multiprocessing` module.
