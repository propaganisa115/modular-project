#!/bin/bash
python -m pip install --upgrade pip
pip install django
pip install -r requirements.txt
cd modular_project
python manage.py collectstatic --noinput
python manage.py migrate