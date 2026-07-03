# Facebook Clone — Web Tech

A minimal **Facebook-style social feed** built with Flask for a web technologies course. Session-based login, hashed passwords, aggregated timelines, and per-user profiles — all without a heavyweight database layer.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)

## Features

- User login with **Werkzeug password hashing**
- Flask **sessions** for authenticated browsing
- Combined **home feed** from all registered users
- **Profile pages** per username
- Jinja2 templates + static CSS styling
- In-memory dict “database” for fast local demos

## Tech stack

| Layer | Choice |
|-------|--------|
| Backend | Flask |
| Auth | Werkzeug `generate_password_hash` / `check_password_hash` |
| Templates | Jinja2 (`templates/`) |
| Data | In-memory Python dict (proof-of-concept) |

## Quick start

```bash
pip install flask werkzeug
python app.py
```

Open **http://127.0.0.1:5000** — demo users `george` / `sam` (password: `hello1234`).

## Project layout

```
app.py           # Routes: home, login, profile
templates/       # home.html, login.html, profile.html
static/style.css
```

## Notes

Educational project — not production-hardened. Replace the in-memory store with a real database before any public deployment.

---

Built by [malimba](https://github.com/malimba)
