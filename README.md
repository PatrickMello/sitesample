# Site Sample

Simple site sample to illustrate how use a free HTML template with Django application.


## Run

### Create the virtualenv

```shell
$ cd [your-env-folder-supimpa]
$ virtualenv -p `which python3` env_name
```

### Running the app

```shell
$ cd [your-local-repository-clone-folder]
$ source [your-env-folder-supimpa]
(env_name) $ pip install -r requirements
(env_name) $ ./manage.py migrate
(env_name) $ ./manage.py createsuperuser
   ... type some info ...
(env_name) $ ./manage.py runserver
```