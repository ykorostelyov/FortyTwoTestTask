#!/bin/sh
python manage.py get_models_info grep da * 2>> stderr/$(date +%Y-%m-%d).dat