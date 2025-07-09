# BDD Automation Framework – Python + Behave + Selenium

This repository contains a Behavior-Driven Development (BDD) automation framework using:

✅ Python  
✅ Behave (Cucumber-like BDD tool for Python)  
✅ Selenium WebDriver  
✅ Gherkin syntax (.feature files)  
✅ VS Code as editor

This framework automates login testing on the [saucedemo website](https://www.saucedemo.com/).

## 📂 Project Structure

bdd_framework/
│
├── features/
│ ├── environment.py
│ ├── example.feature
│ └── steps/
│ └── test_steps.py
│
├── requirements.txt
└── README.md

## 💻 Prerequisites

✅ Python 3.9+ installed  
✅ Google Chrome browser installed  
✅ ChromeDriver installed and accessible via PATH  
✅ VS Code recommended for editing

## ⚙️ Installation

### 1. Clone this Repository

### 2. Create Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
Install all required Python packages:

pip install -r requirements.txt
Your requirements.txt should contain:

# requirements.txt
behave
selenium
allure-behave

📝 Writing Feature Files
Features are written in Gherkin syntax.

Example:
features/example.feature
Feature: Login functionality on saucedemo

  Scenario: User logs in with valid credentials
    Given the user is on the saucedemo login page
    When the user enters username "standard_user" and password "secret_sauce"
    Then the user should see the products page
🐍 Step Definitions
Your Python steps go in:
features/steps/test_steps.py
Example code:
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('the user is on the saucedemo login page')
def step_open_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then('the user should see the products page')
def step_verify_products(context):
    header = context.driver.find_element(By.CLASS_NAME, "title").text
    assert header == "Products", "Login failed or products page not loaded"
    context.driver.quit()

⚡ How to Run Tests
Activate your virtual environment first.
.\venv\Scripts\activate

python -m behave
✅ Method 2 — Direct executable (Windows)

.\.venv\Scripts\behave.exe
✅ Method 3 — Specific Feature File

python -m behave features/example.feature
✅ Environment Variables (Optional)
Instead of hardcoding credentials in your feature files, you can store secrets in environment variables.


$env:SAUCE_USERNAME = "standard_user"
$env:SAUCE_PASSWORD = "secret_sauce"
Then update your step definitions to read:


import os

username = os.environ["SAUCE_USERNAME"]
password = os.environ["SAUCE_PASSWORD"]
And your .feature file could simply say:


When the user logs in
instead of including usernames/passwords directly.

✅ Allure Reporting (Optional)
Generate Allure results:


behave -f allure_behave.formatter:AllureFormatter -o allure-results
Then:


allure serve allure-results
🛠 Troubleshooting
✅ behave : The term 'behave' is not recognized

→ Either:

.\.venv\Scripts\behave.exe
or:

python -m behave
✅ ModuleNotFoundError: No module named 'behave'

→ Install behave:


pip install behave
✅ ModuleNotFoundError: No module named 'selenium'

→ Install selenium:

pip install selenium
🔥 Example Run
Sample output:

Feature: Login functionality on saucedemo

  Scenario: User logs in with valid credentials
    Given the user is on the saucedemo login page
    When the user enters username "standard_user" and password "secret_sauce"
    Then the user should see the products page

1 feature passed, 1 scenario passed