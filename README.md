#Viradjango ✌️ 🐍


### Template Structure


| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | Django Project & Backend Config            |
| `/backend/api`       | Django App (`/api`)                        |
| `/src`               | Vue App .                                  |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point (`/`)         |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |

## Prerequisites

Before getting started you should have the following installed and running:
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)



Setup
```

$ pipenv install --dev && pipenv shell
$ python manage.py migrate
$ python manage.py loaddata
```

## Running Development Servers

```
$ python manage.py runserver
```

appcc contains the data link for the chart
## Deploy

* Set `ALLOWED_HOSTS` on [`backend.settings.prod`](/backend/settings/prod.py)


python manage.py runserver --settings=backend.settings.prod