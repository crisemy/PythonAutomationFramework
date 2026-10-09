# Python Automation Framework

Original 2023 project by crisemy — first self-made Selenium + Python POM framework.
Modernized 2026-10-09 to **Selenium 4.51.0** and proven green against live python.org.

## What changed in 2026 (from 2023 PAF 0.1)

| Area | 2023 | 2026 |

|------|------|------|
| Selenium | 3.x style, manual `chromedriver 2.45` in `$PATH` | **4.51.0** via Selenium Manager (auto driver, no manual install). `webdriver.Chrome(service=Service(), options=...)` in `test_pom_home.py` |
| Python | 3.7 | **3.12.7**, isolated `.venv/` |
| Deps | bare `pip install selenium/pytest/allure-pytest` | pinned `requirements.txt`: `selenium==4.51.0`, `pytest==9.1.1`, `PyYAML==6.0.3`, `allure-pytest==2.16.2` |
| Imports | `from PythonProjects.pages...` (broken, no such package) | `from pages...` / `from config_options...` |
| Config | `yaml.load()` (crashes on PyYAML 6), `open('config.yml')` relative, dead `webdriver: webdriver.Chrome()` string | `yaml.safe_load()`, `Path(__file__).parent / "config.yml"`, `config.yml` now `url / browser / headless / timeout` |
| Waits | 5 s, `EC.element_to_be_clickable(locator=...)` (TypeError on Selenium 4), `5). until` typo, `find()` returns `None` | 10 s (configurable), positional `EC.element_to_be_clickable(self.locator)`, `find()` returns element |
| Test flow | `global python_home_page`, bare `yield`, hardcoded macOS screenshot path, immediate `h2` assert (races homepage `Get Started`) | fixture returns page object, repo-relative `screenshot/FinalScreen.png`, `WebDriverWait(url_contains("/search"))` after each nav, new `conftest.py --headless` flag + `HEADLESS=1` env |
| Locators | 2023 python.org | re-validated 2026-10-09 live: `input#id-search-field`, `#submit`, `.python-logo`, `h2` == `Search Python.org` — all still valid |
| Hygiene | `.gitignore` typo `screenshot/.png`, committed png | fixed to `screenshot/*.png`, added `.venv/`, `.pytest_cache/`, `allure-report/` (raw results stay in `reports/`) |

New files: `requirements.txt`, `conftest.py`, `CONTEXT.md`, `.venv/` (untracked).

## Setup (2026)

> Always use the repo `.venv/` interpreter. Bare `pytest` may resolve to
> another Python (e.g. Anaconda with pytest 8.2.2) and fail with
> `ModuleNotFoundError: No module named 'selenium'`.

```powershell
# from repo root (run once)
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\pip.exe install -r requirements.txt
```

## Run

```powershell
# headed
.\.venv\Scripts\python.exe -m pytest test_pom_home.py -v

# headless (CI)
.\.venv\Scripts\python.exe -m pytest test_pom_home.py -v --headless
# or: $env:HEADLESS=1; .\.venv\Scripts\python.exe -m pytest test_pom_home.py -v
```

Result 2026-10-09: **2 passed** (`test_search_option` E2E + `test_config_loads_base_url`), screenshot refreshed at `screenshot/FinalScreen.png`, Allure JSON verified in `reports/` via `.\.venv\Scripts\python.exe -m pytest test_pom_home.py -v --alluredir=reports/`.

`config.yml` options:

```yaml
url: python.org
browser: chrome
headless: false
timeout: 10
```

## Original 2023 notes (kept for history)

### Page Object Model (POM)

Built with the PO concept for interacting/maintaining code. Ref: <https://selenium-python.readthedocs.io/page-objects.html>

- `pages/base_page.py` — `go()` navigates
- `pages/base_element.py` — wraps explicit waits (`find`/`input_text`/`click`/`text`)
- `pages/python_home_page.py` — 4 locators: search input, GO button, logo, assert title
- `test_pom_home.py` — search "Jobs" → assert `h2 == 'Search Python.org'` → logo → empty search → assert again

### Explicit Waits

Uses `WebDriverWait` + `expected_conditions`. Ref: <https://www.selenium.dev/documentation/webdriver/waits/>

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "myDynamicElement")))
```

### Screenshot

Every run saves `screenshot/FinalScreen.png` via `driver.get_screenshot_as_file(...)` (now repo-relative, was a hardcoded macOS path in 2023).

### Allure (working — JSON via `allure-pytest`, HTML via Allure CLI)

`pytest --alluredir` only writes raw `*-result.json` / `*-container.json`
into `reports/` — it does not render HTML. To view the report you need the
Allure CLI (Java 17+ already present; `allure` binary was missing on 2026-10-09).

```powershell
# 1. collect results (always via .venv python; --clean-alluredir wipes stale runs)
.\.venv\Scripts\python.exe -m pytest test_pom_home.py -v --alluredir=reports/ --clean-alluredir

# 2. install viewer once (pick one)
# scoop:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force; irm get.scoop.sh | iex
scoop install allure
# manual: download allure-*.zip from github.com/allure-framework/allure2/releases,
# unzip to C:\allure and add C:\allure\bin to PATH

# 3. view
allure serve reports/
# or save static HTML:
allure generate reports/ -o allure-report --clean
allure open allure-report
```

Ref: <https://docs.qameta.io/allure/>
