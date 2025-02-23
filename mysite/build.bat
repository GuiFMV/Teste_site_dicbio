@echo off
python -m ensurepip --default-pip
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
