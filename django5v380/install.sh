#!/bin/bash

# python ./init.py initdb && \
# python ./manage.py makemigrations && \
# python ./manage.py migrate --fake-initial && \
# python ./init.py initsql && \
python ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='abo').exists() or User.objects.create_superuser('abo', 'abo@example.com', 'abo')"

# 等待用户按下任何键（可选的）
read -p "Press any key to continue..."
