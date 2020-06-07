# twit-off-pt5

## Setup
```shell script
poetry install
```

```shell script
export FLASK_APP = twit_off_pt5
flask db init
flask db migrate
flask db upgrade
```

## Usage
```shell script
flask run
```