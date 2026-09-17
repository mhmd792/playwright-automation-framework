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

The repository root now exposes the same stable suite that CI runs:

```bash
pytest -v
```

That default command intentionally covers a small stable regression suite:

- `lesson6/test_reqres_api.py`
- `lesson10/test_e2e_purchaec.py`
- `lesson12/pages/test_side_menu.py`

Each lesson folder is still independent, so you can also run pytest from inside a specific lesson:

```bash
cd lesson10
pytest
```

### Optional local-only lessons

Some learning exercises need local infrastructure or manual interaction, so they are not part of the default CI suite:

- `lesson13/test_local_ai.py`
- `lesson 14/tests/test_rag_basic.py`
- interactive/browser-learning files under `lesson8/` and `lesson9/`

To run a local AI lesson, start Ollama first, then opt in explicitly:

```bash
export RUN_LOCAL_AI_TESTS=1
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_MODEL=llama3.1
pytest lesson13/test_local_ai.py -v
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
| `trace.zip` | Generated locally when you record a Playwright trace; ignored by git. |

## Notes

- Files/folders are named to match `lessonN` consistently (older names like
  `lesoon4`, `lesoon6`, `leson7`, and `lesson 11` were renamed for
  consistency — no content was removed).
- `__pycache__/`, `.pytest_cache/`, and `.env` are git-ignored; see
  `.gitignore`.
