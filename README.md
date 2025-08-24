# Django E-commerce API

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-blue.svg)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-orange.svg)](https://jwt.io/)

API RESTful para sistema de e-commerce con autenticación JWT, arquitectura modular y preparada para producción.

## 🏗️ Arquitectura

```mermaid
graph TD
    A[Frontend] -->|REST API| B[Django DRF]
    B -->|JWT| C[Authentication]
    B -->|PostgreSQL| D[Database]
    B -->|Redis| E[Caching]