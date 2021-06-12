# Django URL shortner
This is a simple url shortener application build with Django.

# How to Setup
1. Clone Project
```
git clone https://github.com/hossain-shuvo7860/DJEcomAPI.git
```

2. Go To Project Directory
```
cd DJEcomAPI
```
3. Create Virtual Environment
```
python3 -m venv venv
```
4. Active Virtual Environment
```
source venv/bin/activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Setup DATABASE settings from settings/core.py 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```
7. Migrate Database
```
python manage.py migrate
```
8. Create Super User
```
python manage.py createsuperuser
```
9. Run Project
```
python manage.py runserver
```
