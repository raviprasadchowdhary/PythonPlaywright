# Setup Guide - Python Playwright Testing Framework

This guide will help you set up the Python Playwright testing framework from scratch, whether you're using **VS Code** or **PyCharm**.

---

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Setup for VS Code](#setup-for-vs-code)
- [Setup for PyCharm](#setup-for-pycharm)
- [Running Tests](#running-tests)
- [Common Issues & Solutions](#common-issues--solutions)
- [Enhancing the Framework](#enhancing-the-framework)

---

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.8 or higher** - [Download here](https://www.python.org/downloads/)
  - ⚠️ **Important**: During installation, check "Add Python to PATH"
- **Git** - [Download here](https://git-scm.com/downloads)
- **Node.js** (for Playwright browsers) - [Download here](https://nodejs.org/)

### Verify Installation
Open a terminal/command prompt and run:
```powershell
python --version    # Should show Python 3.8+
pip --version       # Should show pip version
git --version       # Should show git version
```

---

## Setup for VS Code

### Step 1: Install VS Code
Download and install [Visual Studio Code](https://code.visualstudio.com/)

### Step 2: Install VS Code Extensions
Open VS Code and install these extensions:
1. **Python** (by Microsoft) - Essential for Python development
2. **Pylance** (by Microsoft) - Python language server
3. **Python Test Explorer** - Visual test runner
4. **Playwright Test for VSCode** (optional) - Playwright integration

**How to install extensions:**
- Press `Ctrl+Shift+X` to open Extensions
- Search for each extension name
- Click "Install"

### Step 3: Clone the Repository
```powershell
# Open VS Code terminal (Ctrl+`)
cd C:\Users\YourUsername\Documents  # or your preferred location
git clone https://github.com/raviprasadchowdhary/PythonPlaywright.git
cd PythonPlaywright
```

### Step 4: Open Project in VS Code
```powershell
code .
```

### Step 5: Create Virtual Environment

**Option A: Using VS Code Command Palette**
1. Press `Ctrl+Shift+P`
2. Type "Python: Create Environment"
3. Select "Venv"
4. Choose your Python interpreter (Python 3.8+)
5. Wait for environment creation

**Option B: Using Terminal**
```powershell
# In VS Code terminal (Ctrl+`)
python -m venv .venv
```

### Step 6: Activate Virtual Environment

**PowerShell (Windows):**
```powershell
.venv\Scripts\Activate.ps1
```

**If you get execution policy error:**
```powershell
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
.venv\Scripts\Activate.ps1
```

**Bash/Linux/Mac:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt.

### Step 7: Select Python Interpreter in VS Code
1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose the one from `.venv` folder (e.g., `.\venv\Scripts\python.exe`)

### Step 8: Install Python Dependencies
```powershell
# Make sure (.venv) is showing in terminal
pip install --upgrade pip
pip install -r requirements.txt
```

**If requirements.txt doesn't exist or is outdated:**
```powershell
pip install pytest pytest-playwright playwright
pip install pytest-html pytest-xdist pytest-rerunfailures pytest-timeout
pip install pytest-cov allure-pytest pytest-mock faker python-dotenv jsonschema
```

### Step 9: Install Playwright Browsers
```powershell
playwright install
```

This will download Chromium, Firefox, and WebKit browsers (~500MB).

### Step 10: Verify Installation
```powershell
# Check pytest is installed
pytest --version

# Check installed packages
pip list
```

### Step 11: Run Your First Test
```powershell
# Run a specific test
python -m pytest Playwright/Framework/Tests/test_e2eFlowHybridFramework.py::test_e2eTest_createOrderAndVerify -v

# Run all tests
python -m pytest
```

---

## Setup for PyCharm

### Step 1: Install PyCharm
Download and install [PyCharm](https://www.jetbrains.com/pycharm/download/)
- **Community Edition** (Free) works perfectly
- **Professional Edition** has additional features

### Step 2: Clone the Repository

**Option A: From Welcome Screen**
1. Click "Get from VCS"
2. Enter repository URL: `https://github.com/raviprasadchowdhary/PythonPlaywright.git`
3. Choose local directory
4. Click "Clone"

**Option B: Using Terminal**
```powershell
cd C:\Users\YourUsername\Documents
git clone https://github.com/raviprasadchowdhary/PythonPlaywright.git
```

Then open the folder in PyCharm: `File > Open > Select PythonPlaywright folder`

### Step 3: Configure Python Interpreter

1. **Open Settings**
   - `File > Settings` (Windows/Linux)
   - `PyCharm > Preferences` (Mac)
   - Or press `Ctrl+Alt+S`

2. **Create Virtual Environment**
   - Navigate to: `Project: PythonPlaywright > Python Interpreter`
   - Click gear icon ⚙️ > `Add Interpreter > Add Local Interpreter`
   - Select `Virtualenv Environment`
   - Choose `New environment`
   - Location: `<ProjectRoot>\.venv`
   - Base interpreter: Python 3.8 or higher
   - Click `OK`

### Step 4: Install Dependencies

PyCharm will detect `requirements.txt` and show a banner to install packages.

**Option A: Using Banner**
- Click "Install requirements" in the banner

**Option B: Manual Installation**
1. Open Terminal in PyCharm (`Alt+F12`)
2. Run:
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Option C: If requirements.txt is missing:**
```powershell
pip install pytest pytest-playwright playwright
pip install pytest-html pytest-xdist pytest-rerunfailures pytest-timeout
pip install pytest-cov allure-pytest pytest-mock faker python-dotenv jsonschema
```

### Step 5: Install Playwright Browsers
In PyCharm terminal:
```powershell
playwright install
```

### Step 6: Configure Pytest as Test Runner

1. Open Settings (`Ctrl+Alt+S`)
2. Navigate to: `Tools > Python Integrated Tools`
3. Under "Testing":
   - Default test runner: Select `pytest`
4. Click `OK`

### Step 7: Run Configuration

**Create Run Configuration for Tests:**
1. Click `Run > Edit Configurations`
2. Click `+` > `Python tests > pytest`
3. Configure:
   - **Name**: "Run All Tests"
   - **Target**: "Script path" → Select `Playwright` folder
   - **Python interpreter**: Select your `.venv` interpreter
   - **Working directory**: Project root
4. Click `OK`

### Step 8: Run Your First Test

**Option A: Using Right-Click**
1. Navigate to test file in Project Explorer
2. Right-click on test function
3. Select `Run 'pytest for test_...'`

**Option B: Using Run Configuration**
1. Select your run configuration from dropdown
2. Click green Run button ▶️

**Option C: Using Terminal**
```powershell
python -m pytest Playwright/Framework/Tests/test_e2eFlowHybridFramework.py::test_e2eTest_createOrderAndVerify -v
```

---

## Running Tests

### Basic Commands

```powershell
# Run all tests
python -m pytest

# Run specific test file
python -m pytest Playwright/Framework/Tests/test_e2eFlowHybridFramework.py

# Run specific test function
python -m pytest Playwright/Framework/Tests/test_e2eFlowHybridFramework.py::test_e2eTest_createOrderAndVerify

# Verbose output
python -m pytest -v

# Show print statements
python -m pytest -s

# Run tests by marker
python -m pytest -m smoke
python -m pytest -m e2e
```

### Advanced Commands

```powershell
# Run tests in parallel (4 workers)
python -m pytest -n 4

# Generate HTML report
python -m pytest --html=report.html --self-contained-html

# Run with code coverage
python -m pytest --cov=. --cov-report=html

# Retry failed tests (2 retries with 1 second delay)
python -m pytest --reruns 2 --reruns-delay 1

# Run in headed mode (see browser)
python -m pytest --headed

# Use different browser
python -m pytest --browser_name=firefox
python -m pytest --browser_name=webkit
```

### VS Code Test Explorer

1. Click Test icon in sidebar (flask icon)
2. Tests will auto-discover
3. Click ▶️ next to any test to run it
4. View results in Test Explorer

### PyCharm Test Runner

1. Right-click on `Playwright` folder
2. Select `Run 'pytest in Playwright'`
3. View results in Run panel at bottom
4. Green checkmarks = passed tests
5. Red X = failed tests

---

## Common Issues & Solutions

### Issue 1: `pytest: command not found` or `The term 'pytest' is not recognized`

**Cause**: Virtual environment not activated or pytest not installed.

**Solution**:
```powershell
# Activate virtual environment first
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate   # Linux/Mac

# Install pytest
pip install pytest pytest-playwright
```

### Issue 2: `PowerShell execution policy error`

**Error**: 
```
.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system
```

**Solution**:
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate virtual environment
.venv\Scripts\Activate.ps1
```

### Issue 3: `Executable doesn't exist` - Playwright browsers not installed

**Error**:
```
Executable doesn't exist at C:\Users\...\ms-playwright\chromium-1200\chrome-win64\chrome.exe
```

**Solution**:
```powershell
# Install Playwright browsers
playwright install

# If still fails, reinstall playwright
pip uninstall playwright
pip install playwright
playwright install
```

### Issue 4: `ImportError` or `ModuleNotFoundError`

**Error**:
```
ModuleNotFoundError: No module named 'pytest'
```

**Cause**: Wrong Python interpreter or packages not installed.

**Solution**:

**VS Code:**
1. Press `Ctrl+Shift+P`
2. "Python: Select Interpreter"
3. Choose `.venv` interpreter
4. Reinstall packages: `pip install -r requirements.txt`

**PyCharm:**
1. Settings > Project Interpreter
2. Ensure `.venv` is selected
3. Install missing packages from package list

### Issue 5: `argument --tracing: conflicting option string`

**Cause**: `pytest-playwright` plugin already defines `--tracing` option.

**Solution**: This was fixed in `conftest.py` by renaming to `--custom-tracing`

If you still see this, update your `conftest.py`:
```python
parser.addoption(
    "--custom-tracing",  # Changed from --tracing
    action="store",
    default="on",
    choices=["on", "off"],
    help="Enable or disable Playwright tracing (on/off)",
)
```

### Issue 6: Tests fail with timeout

**Solution**:
```powershell
# Increase timeout
python -m pytest --timeout=300

# Or disable timeout for debugging
python -m pytest --timeout=0
```

### Issue 7: `pip` is broken or corrupted

**Solution**:
```powershell
# Remove and recreate virtual environment
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

### Issue 8: Python not in PATH

**Solution**:
1. Find Python installation path:
   - Windows: Usually `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx`
2. Add to PATH:
   - Windows: `System Properties > Environment Variables > Path > New`
   - Add both: `C:\...\Python3xx` and `C:\...\Python3xx\Scripts`
3. Restart terminal/IDE

---

## Enhancing the Framework

### Add New Test File

1. Create test file in appropriate folder (e.g., `Playwright/Framework/Tests/`)
2. Name it `test_*.py` (must start with `test_`)
3. Import necessary modules:
```python
import pytest
from playwright.sync_api import Playwright, expect
```

### Add New Page Object

1. Create file in `Playwright/Framework/PageObjects/`
2. Follow POM pattern:
```python
class MyPage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self):
        self.page.goto("https://example.com")
    
    def perform_action(self):
        self.page.click("button")
```

### Add Test Data

1. Create JSON file in `Playwright/Framework/Data/`
2. Load in test:
```python
import json

with open("Playwright/Framework/Data/mydata.json") as f:
    data = json.load(f)
```

### Add Custom Markers

1. Create/edit `pytest.ini`:
```ini
[pytest]
markers =
    smoke: Smoke tests
    regression: Regression tests
    your_custom_marker: Description
```

2. Use in tests:
```python
@pytest.mark.your_custom_marker
def test_something():
    pass
```

### Add Dependencies

```powershell
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Debugging Tests

**VS Code:**
1. Set breakpoint (click left of line number)
2. Right-click test > "Debug Test"
3. Use Debug toolbar to step through

**PyCharm:**
1. Set breakpoint (click left of line number)
2. Right-click test > "Debug 'test_name'"
3. Use Debug panel to inspect variables

**Command Line:**
```powershell
# Run with debugger
python -m pytest --pdb

# Show local variables on failure
python -m pytest -l

# Verbose with print statements
python -m pytest -v -s
```

---

## Project Structure

```
PythonPlaywright/
├── .venv/                      # Virtual environment (created by you)
├── Playwright/
│   ├── Framework/
│   │   ├── Data/              # Test data (JSON, etc.)
│   │   ├── PageObjects/       # Page Object Model classes
│   │   └── Tests/             # Test files
│   │       ├── conftest.py    # Pytest fixtures & configuration
│   │       └── test_*.py      # Test files
│   ├── API_Testing/           # API tests
│   ├── part1/                 # Basic tests
│   └── Part2/                 # Advanced tests
├── utils/                     # Utility classes
├── logs/                      # Test logs (auto-generated)
├── screenshots/               # Failure screenshots (auto-generated)
├── videos/                    # Test recordings (auto-generated)
├── traces/                    # Playwright traces (auto-generated)
├── requirements.txt           # Python dependencies
├── pytest.ini                 # Pytest configuration
└── README.md                  # Project documentation
```

---

## Next Steps

1. ✅ Run the sample test to verify setup
2. ✅ Explore existing tests in `Playwright` folder
3. ✅ Read `TESTING_GUIDE.md` for advanced features
4. ✅ Check `QUICK_REFERENCE.md` for common commands
5. ✅ Start writing your own tests!

---

## Getting Help

- **Pytest Documentation**: https://docs.pytest.org/
- **Playwright Python**: https://playwright.dev/python/
- **Stack Overflow**: Tag questions with `playwright` and `pytest`
- **GitHub Issues**: Report issues in the repository

---

## Troubleshooting Checklist

Before asking for help, verify:

- [ ] Python 3.8+ is installed (`python --version`)
- [ ] Virtual environment is activated (see `(.venv)` in terminal)
- [ ] All packages are installed (`pip list`)
- [ ] Playwright browsers are installed (`playwright install`)
- [ ] Using correct Python interpreter (VS Code/PyCharm settings)
- [ ] Test file starts with `test_` and functions start with `test_`
- [ ] Working directory is project root
- [ ] No syntax errors in code

---

**Happy Testing! 🎭**

*Last Updated: December 2025*
