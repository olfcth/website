## Get up and running!!

#### Project Clone

```commandline
/ $ git clone git@github.com:olfcth/website.git
```

#### Install Python Virtual Env

```commandline
/ $ cd website
/website $ python3.10 -m venv .venv
```

#### Setup Project

```commandline
/website $ source .venv/bin/activate    # relevant activate.bat or .sh as per OS / shell
(.venv) /website $ python manage.py makemigrations
(.venv) /website $ python manage.py migrate
```

#### Run Project

```commandline
(.venv) /website $ python manage.py runserver
```