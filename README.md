# Playwright Automation Framework

A personal learning workspace for practicing UI and API test automation with
**Playwright**, **Selenium**, and **pytest** in Python. Each `lessonN/`
folder is a self-contained exercise from a different point in the course —
they are not meant to import from one another.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

Some lessons read credentials from a `.env` file (see `lesson11/.env` for an
example using the public SauceDemo test account).

## Running tests

Each lesson folder is independent, so run pytest from inside it:

```bash
cd lesson10
pytest
```

## Folder guide

| Folder | Topic |
| --- | --- |
| `lesson3.py` | Plain Python practice: conditional/dict logic (no browser). |
| `lesson4.py` | Plain Python practice: validating a list of API-call results. |
| `lesson6/` | API testing with `requests` against reqres.in (raw scripts + pytest tests). |
| `lesson7/` | Selenium WebDriver basics: locators, login flows, waits. |
| `lesson8/tests/` | Playwright sync API basics: page actions, API requests, tracing. |
| `lesson9/tests/` | Playwright assertions (`expect`), Inspector, tracing, hybrid UI+API tests. |
| `lesson10/` | Page Object Model with Playwright + pytest fixtures (login, inventory, checkout). |
| `lesson11/` | POM continued: `.env`-based config, fixtures, checkout page object. |
| `training.py`, `test_car.py` | Small pytest fixture/parametrize exercises. |
| `trace.zip` | Sample Playwright trace, viewable with `playwright show-trace trace.zip`. |

## Notes

- Files/folders are named to match `lessonN` consistently (older names like
  `lesoon4`, `lesoon6`, `leson7`, and `lesson 11` were renamed for
  consistency — no content was removed).
- `__pycache__/`, `.pytest_cache/`, and `.env` are git-ignored; see
  `.gitignore`.
