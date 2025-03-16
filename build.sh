#!/bin/bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python modular_project/manage.py collectstatic --noinput
python modular_project/manage.py migrate