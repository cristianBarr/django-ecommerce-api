Django E-commerce API

API para sistema de comercio electrónico con autenticación JWT y PostgreSQL.

Características
- Gestión de productos
- Órdenes con autenticación JWT
- Configuración para producción

Tecnologías
- Python 3.10+
- Django 5
- Django REST Framework
- SimpleJWT

Instalación
```bash
git clone https://github.com/cristianBarr/django-ecommerce-api.git
cd django-ecommerce-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
