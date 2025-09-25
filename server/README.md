# Backend (Django 5 + DRF) – Hospital Customizable App POC

## Quick Start (Windows)

```bat
cd diabetes_poc_full_ui
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Seed default configs:

```
POST http://127.0.0.1:8000/api/config/seed/
```

## APIs

- POST /api/config/seed/
- GET /api/config/effective/form/visit_opd/
- GET /api/config/effective/rules/visit_opd/
- GET /api/config/effective/workflow/visit_opd/
- POST /api/config/publish/{form|rule|workflow}/visit_opd/

- POST /api/runtime/rules/evaluate/visit_opd/

- POST /api/submit/forms/visit_opd/submit/  (header: Idempotency-Key)

- GET /api/clinical/patients/
- GET /api/clinical/visits/

- POST /api/orchestrator/process-now/
- GET /api/orchestrator/notifications/
- GET /api/orchestrator/tasks/

## Run tests

```
pytest  # if installed
# or
python manage.py test
```

## MySQL (optional)

Set `DB_URL` env var e.g.
```
set DB_URL=mysql://user:pass@localhost:3306/diabetes_poc
```