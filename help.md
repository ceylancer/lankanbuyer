## Note before the log:
The tutorial was conducting using **pipenv** (which we have to deal with an 
external file named *PipFile*) However the following command didn't work for me
(even though after installing pipenv with `pip3 install pipenv` command)
```
pipenv shell
```

However, I install pipenv with `sudo`
```
sudo pip3 install pipenv
```

Now everything is ok
These are the steps I have done for this project 
# Log
## 1) Install **pipenv**
```
sudo pip3 install pipenv
```
## 2) Open pipenv shell
```
pipenv shell
```

## 3) install dependent packages
We need to install `django`, `djangorestframework`, `django-rest-knox` packages
For this I used the following command to install them
```
pipenv install django djangorestframework django-rest-knox
```

## 4) create project 'buyermanager'
```
django-admin startproject buyermanager
```

after that, Go to `buyermanager` directory with `cd buyermanager` command.
Then, inside that run the commands to create a app (django concept)

## 5) Create an app called 'buyers'
```
python manage.py startapp buyers
```

Project structure is
```
├── buyermanager
└── buyers
```
'buyermanager' is the core of the project. In here, there is a `settings` file
In that, you have to add the `buyers` app and `rest_framework` under installed apps
(`INSTALLED_APPS`)

