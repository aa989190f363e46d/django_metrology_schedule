# Deployment to Heroku

```shell
heroku create --region eu <optional_appname>
```

You'll get a remote repository named `heroku` added to your git repo, handy!

3. Add required dependencies

```shell
pipenv install gunicorn dj-database-url psycopg2-binary whitenoise
```

4. Add [`Procfile`](https://devcenter.heroku.com/articles/procfile)

Sample `./Procfile`:

```shell
web: gunicorn config.wsgi --log-file -
```

6. Setup environment on Heroku
- generate secret key to use in production:

```shell
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```

- set it up on Heroku:

```shell
heroku config:set DJANGO_SECRET_KEY=<key_generated_above>
```

- turn off debug mode:

```shell
heroku config:set DJANGO_DEBUG=False
```

7. Check Django settings (`config/settings.py`)

These settings should respect environment:

- `SECRET_KEY` - `DJANGO_SECRET_KEY`
- `DATABASES` - `DATABASE_URL`
- `DEBUG` - `DJANGO_DEBUG`

`ALLOWED_HOSTS` should include Heroku, i.e.:

```python
ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]
```

- whitenoise (for static files)

See http://whitenoise.evans.io/en/stable/django.html

---

Refer to [`1cf40e34`](https://github.com/intyamo/django-news/commit/1cf40e3474c4c738f2afb7b7a61acb0aedf1fa38#diff-935426a2f59d34e9506987404f8d78b5b5b43431694101f5be37ad65af4cf193) if needed.


8. Push to Heroku

first time 

```sh
git remote add heroku https://git.heroku.com/<appname>.git
```

each time

```sh
git push heroku master
```

9. Migrations & Superuser

```sh
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

10. Start your web app and check its logs

```sh
heroku ps:scale web=1

heroku logs --tail
```
