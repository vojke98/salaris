#!/bin/bash

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@salaris.com', '#tpo2021')" | python manage.py shell