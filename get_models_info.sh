#!/bin/sh
python manage.py get_models_info grep da >> stderr/$(date +%Y-%m-%d).dat