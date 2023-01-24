
# Django Rest Framework Url Shortener




## Routes
- All Shortened Links List

127.0.0.1:8000/api/all-links/

- Create New Shortened Link

127.0.0.1:8000/api/create-link

Json Data Example = {"title": "test2", "description": "test2", "main_url": "https://google.com", "shrtened_ur": "shorturl12", "edit_password": 54551215}

- Delete Shortened Link

127.0.0.1:8000/api/delete-link/[$edit_password]/

- Link Redirection

127.0.0.1:8000/api/redirect/[$shrtened_url]/

- Django Admin Panel

127.0.0.1:8000/admin

user : dhia@dhia.com
password : dhia@dhia.com
## Project Requirements

```bash
  pip install django
  pip install djangorestframework
```
    
## How To Run The Project

```bash
  git clone https://github.com/dhiabenmaati/Django-Url-Shortener-Api.git
  python manage.py runserver
```

