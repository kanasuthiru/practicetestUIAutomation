 #Selenium UI Automation Framework (BDD - Behave)
 Overview

This project is a UI automation framework built using **Selenium WebDriver**, **Python**, and **Behave** (BDD-style testing).


### ✅ Automated Test Scenarios

- **Add and Delete Products in Cart**
- **User Registration and Login**
- **Add Address to Profile and Verify
## ✅ Test Case Coverage

| Feature                    | Pytest | BDD (Behave) |
|----------------------------|--------|--------------|
| Add/Delete Products (Cart) | ✅     | ❌           |
| Address                    | ✅     | ✅           |
| Registration & Login       | ❌     | ✅           |

🧪 Run Pytest Tests
pytest
Run a specific test: pytest pytest_testcases/test_cart.py

🧪 Run BDD Tests (Behave)
behave
Run a specific test:behave behave_test_cases/feature/login.feature

Test Case Types
✅ Positive Test Scenarios

Add  product to cart
Register with valid details
Login with correct credentials
valid shipping and billing address

❌ Negative Test Scenarios
 empty cart
Register with existing email/ invalid creds
Login with wrong creds
Submit address with missing fields

 Reports
After running tests, you can view the HTML report generated in the report.html file for detailed results.


### 📂 **Explanation of the Structure:**

- **`base/`**: Contains base page objects and common methods.
- **`behave_test_cases/`**: Contains BDD features and step definitions for login, registration, and address tests.
- **`conftest.py`**: Configuration and fixtures for both Pytest
- **`pages/`**: Page object models for various pages in the app(address, basket, home, etc.).
- **`pytest_testcases/`**: Contains the Pytest test cases for cart and address.
- **`report.html`**: HTML report of test results.
- also adds block using chrome extension

---

Let me know if you'd like this file created for you or if you need additional changes!

## 🚀 How to Run Tests

### 📌 Prerequisites

Install all dependencies:
```bash
pip install -r requirements.txt


├── base
│   ├── basepage.py
│   └── __init__.py
├── behave_test_cases
│   ├── environment.py
│   ├── feature
│   │   ├── billing_address.feature
│   │   ├── login.feature
│   │   ├── Register.feature
│   │   └── shipping_address.feature
│   └── steps
│       ├── address_steps.py
│       ├── __init__.py
│       ├── login_steps.py
│       └── register_steps.py
├── conftest.py
├── pages
│   ├── address_page.py
│   ├── basket_page.py
│   ├── billing_address_page.py
│   ├── home_page.py
│   ├── __init__.py
│   ├── myAccount_page.py
│   ├── shipping_address_page.py
│   └── shop_page.py
├── pytest.ini
├── pytest_testcases
│   ├── __init__.py
│   ├── test_billing_address.py
│   ├── test_cart.py
│   └── test_shipping_address.py
├── README.md
├── report.html
└── utils
    ├── common.py
    └── __init__.py
