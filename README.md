# Flask Devops Project

## Getting started

Set up python virtual env:

```bash
python3 -m venv .venv
./venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the .env from .env.sample:

```bash
cp .env.sample .env
```

Start the application:

```bash
flask run --host=0.0.0.0 --port=5000 --debug
```

Access the applications: <http://localhost:5000>

## Unit Tests

To run the unit tests:

```bash
pytest tests/ -v
```
