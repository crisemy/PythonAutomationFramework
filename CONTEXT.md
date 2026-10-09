# CONTEXT.md — PythonAutomationFramework (Legacy Selenium POM, 2023)

> First artifact for the 2026 modernization effort. Read this before touching code.
> Goal (per owner): update this 2023 framework to the **latest Selenium version** and prove it still works in **2026**. No code changes yet — context only.

## 1. What this repo is

- Owner's **first self-made Selenium + Python framework**, built ~Jan–Mar 2023 (last commit `92c1ab9`, 2023-03-07, "Improvement in the README file", branch `master`).
- Remote: `https://github.com/crisemy/PythonAutomationFramework.git`
- Target SUT: **https://python.org** — single E2E flow: search "Jobs" → assert `h2 == 'Search Python.org'` → click logo → empty search → assert title again.
- Pattern: **Page Object Model (POM)** + pytest + explicit waits + screenshot + Allure (docs only, no live integration).
- Era assumptions: Python 3.7, manual `chromedriver 2.45` install into `$PATH`, Selenium 3.x/early-4.x style API.

## 2. Current file map (11 files, ~9 KB of code)

```
.
├── README.md               # Setup guide (Python 3.7, pip install selenium/pytest/allure, manual chromedriver)
├── config.yml              # url: python.org / webdriver: webdriver.Chrome()  (string, not evaluated)
├── config_options.py       # ConfigOptions: yaml.load() at class-body, base_url + web_d
├── test_pom_home.py        # Only test: fixture environment_setup + test_search_option
├── pages/
│   ├── __init__.py         # empty
│   ├── base_page.py        # BasePage(driver): go() -> driver.get(url)
│   ├── base_element.py     # BaseElement(driver,value,by): find/input_text/click/text, 5s explicit waits
│   └── python_home_page.py # PythonHomePage(BasePage, ConfigOptions): search_input, go_button, go_logo_image, assert_title
├── reports/reports.txt     # placeholder ("Allure .xml/.html go here")
├── screenshot/             # screenshot.txt placeholder + FinalScreen.png (225 KB, committed artifact)
├── PythonProjects.iml      # stale IntelliJ module file (package was once called PythonProjects)
└── .gitignore              # .cache, __pycache__, *.pyc, *.iml, pages/.cache/, screenshot/.png (missing leading * — ineffective)
```

Missing (notable): `requirements.txt` / `pyproject.toml`, `conftest.py`, `pytest.ini`, any `venv/`, no CI.

## 3. How it (used to) work

1. `ConfigOptions` reads `config.yml` → `base_url = 'https://' + cfg['url']` → `'https://python.org'`.
2. `test_pom_home.py::environment_setup` spins `webdriver.Chrome()`, wraps in `PythonHomePage(driver)`, calls `.go()`, maximizes, `yield`s, then screenshots + `quit()`.
3. `PythonHomePage` exposes 4 lazy element properties, each constructing a `BaseElement` (which `find()`s immediately with `WebDriverWait(...,5).until(visibility_of_element_located)`).
4. Test types "Jobs", clicks submit, asserts `h2` text, clicks logo, clicks submit with empty input, asserts again.

### Locators (against 2023 python.org — MUST re-validate in 2026)

| Property       | By          | Value                |
|----------------|-------------|----------------------|
| search_input   | CSS_SELECTOR| `input#id-search-field` |
| go_button      | ID          | `submit`             |
| go_logo_image  | CLASS_NAME  | `python-logo`        |
| assert_title   | CSS_SELECTOR| `h2`                 |

## 4. Known breakages (why it won't run as-is in 2026)

These are facts observed 2026-10-09, env Python 3.12.7 / pytest 8.2.2 / PyYAML 6.0.1 / **selenium NOT installed**:

| # | Issue | File:line | Detail |
|---|-------|-----------|--------|
| 1 | Broken imports | `test_pom_home.py:2-3`, `pages/python_home_page.py:3` | `from PythonProjects.pages...` / `from PythonProjects.config_options` — no `PythonProjects/` package exists. Must become `from pages...` or `from config_options...` (+ fix `PythonProjects.iml`). |
| 2 | `yaml.load()` without Loader | `config_options.py:7` | Raises `TypeError` on PyYAML ≥ 6. Must be `yaml.safe_load(...)`. Also file opened with bare relative `'config.yml'` — breaks under pytest rootdir changes. |
| 3 | Dead config webdriver value | `config.yml:4`, `test_pom_home.py:22` | `cfg['webdriver']` is the literal string `"webdriver.Chrome()"`; commented-out usage never evaluated it. Fixture ignores it and calls `webdriver.Chrome()` directly. |
| 4 | Hardcoded macOS screenshot path | `test_pom_home.py:36` | `/Users/cristiannadj/Desktop/.../screenshot/FinalScreen.png` — fails on Windows/Linux. Must be repo-relative (`screenshot/`). |
| 5 | Global fixture state | `test_pom_home.py:12,17` | `global python_home_page` + bare `yield` (no value). Fragile; should be proper fixture return / `request` / `conftest.py`. |
| 6 | No driver management | `README.md:32-36` | 2023 manual chromedriver 2.45 flow. Selenium ≥ 4.6 (current in 2026 is 4.x) ships **Selenium Manager** — no manual driver needed, but code should add `Service`/`Options` handling. |
| 7 | Stale selectors + no headless/CI options | `python_home_page.py`, whole repo | python.org DOM may have changed since 2023; no `--headless`, no wait tuning, 5 s timeout may be short. |
| 8 | `.gitignore` typo | `.gitignore:6` | `screenshot/.png` matches nothing; should be `screenshot/*.png` (and probably keep one `.gitkeep`). Committed `FinalScreen.png` proves it. |
| 9 | No dependency pinning | repo-wide | No `requirements.txt`; README says bare `pip install selenium`, `pytest`, `allure-pytest`. Repro in 2026 requires pinned `selenium>=4`, `pytest`, `pyyaml`, `allure-pytest`. |

Minor: `base_element.py:29` has `5). until(...)` (space before attribute — legal but sloppy); `BaseElement.find()` returns `None` instead of element; `text` re-reads stale `web_element` without re-find.

## 5. Environment snapshot (2026-10-09)

- OS shell: `win32` / pwsh, repo at `C:\Crisarch\Programming\PythonAutomationFramework\PythonAutomationFramework`
- `python --version` → **3.12.7**; `pytest 8.2.2` present; `PyYAML 6.0.1` present; `selenium` **not installed**; `allure-pytest` not installed.
- Git: clean tree, `master`, shallow history reviewed (features 01/config, 06/allure, 09/screenshot).

## 6. Agreed modernization scope (awaiting owner call)

1. Pin + install latest Selenium 4.x (+ `pytest`, `pyyaml`, `allure-pytest`) via `requirements.txt`.
2. Fix imports, `yaml.safe_load`, repo-relative paths, screenshot dir.
3. Adopt Selenium Manager (`Service`/`Options`, headless flag, no manual chromedriver).
4. Re-validate python.org locators live; adjust waits/page objects.
5. Prove green `pytest` run in 2026; then decide on Allure/report + CI extras.

**Explicit hold:** do NOT edit source code until owner says so. This `CONTEXT.md` is the only new file in this step.

## 7. Quick re-entry commands

```powershell
# from repo root:
python --version; pytest --version
pip install -U selenium pytest pyyaml allure-pytest
pytest -v test_pom_home.py
```
