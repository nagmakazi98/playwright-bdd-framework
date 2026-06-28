# playwright-bdd-framework
# Playwright + Pytest-BDD Automation Framework

##  Overview

This is a Behavior-Driven Development (BDD) test automation framework built using:

* Python
* Pytest
* pytest-bdd
* Playwright

It follows **Page Object Model (POM)** design for better maintainability and scalability.

---

##  Project Structure

```
Playwright-Assignment/
│
├── features/                # Gherkin feature files
│   ├── signup.feature
│   └── login.feature
│
├── step_definitions/        # Step definitions
│   ├── test_signup_steps.py
│   └── test_login_steps.py
│
├── pages/                   # Page Object classes
│   ├── signup_page.py
│   └── login_page.py
│
├── tests/
│   └── conftest.py          # Fixtures (Playwright setup)
│
├── reports/                 # Screenshots / reports
│
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd Playwright-Assignment
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

---

## Run Tests

```bash
pytest -v -s
```

Run specific test:

```bash
pytest step_definitions/test_signup_steps.py
```

---

## Features Covered

* User Signup
* User Login
* Form validation
* End-to-end UI flow

---

##  Framework Highlights

* BDD using Gherkin syntax
* Page Object Model (POM)
* Reusable fixtures using pytest
* Cross-browser support via Playwright
* Screenshot capture support
* Clean and scalable structure

---

##Screenshot Handling

Screenshots can be captured and stored in:

```
reports/
```

---

## Future Enhancements

* Add HTML reporting (Allure)
* CI/CD integration (Jenkins/GitHub Actions)
* Parallel execution
* Data-driven testing

---

##Author

Nagma Kazi
