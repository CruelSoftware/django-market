# django-market
Yandex market simplified django clone

# Setup

1. Configure your database or create as in config if you wish to use example data (project uses postgresql).

2.
```
    << pip install -r ../requirements/base.txt
    << pip install -r ../requirements/local.txt # if you will use local environment with DEBUG=True
    << python ./manage.py collectstatic
    << python ./manage.py makemigrations
    << python ./manage.py migrate
    << python ./manage.py dbrestore # to restore backup if you wish to use example data, also extract images to your media folder
```

3. Run your server.