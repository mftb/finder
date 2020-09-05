# Python

## Initial Setup

```
cd python
virtualenv venv3 -p python3.7
source venv3/bin/activate
```

## Run Tests
```
cd python
source venv3/bin/activate
pip install -r dev-requirements.txt
pytest --durations=0
```

## Check for PEP8 linting
```
cd python
source venv3/bin/activate
pip install -r dev-requirements.txt
flake8 . --exclude=venv*
```

## Solution Demo
```
cd python
virtualenv venv3 -p python3.7
source venv3/bin/activate
python demo.py
```

# Big Data
[Solution Description](https://docs.google.com/document/d/1Io5rWqaCnKasAFAW2xRw0WWMQ5-hruKQBzL62VhYIb8/edit?usp=sharing)
