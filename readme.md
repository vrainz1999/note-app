# Installation guide

Make venv
```
python3 -m venv .venv
```

change your source
```
source .venv/bin/activate
```

If that not working, you can try this <a href="https://docs.python.org/3/library/venv.html">DOCS</a>

install requirements 
```
pip install -r requirements.txt
```

Migrate database 
```
python3 manage.py migrate
python3 manage.py makemigrations
```

# Running server

Open terminal, and go inside ``mynote`` folder
```
python3 manage.py runserver
```

Your app run default in localhost:8000