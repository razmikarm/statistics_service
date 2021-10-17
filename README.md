# Statistics service

Statistics service is designed to collect, store and represent statistics of views, clicks, and their cost for each day.

## Installation

Create a virtual environment for python with [virtualenv](https://virtualenv.pypa.io/en/latest/) module.

```bash
python -m virtualenv [your-python-environment-name]
```

Activate new created environment.

```bash
. [your-python-environment-name]/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Run

Run Statistics service in activated virtual environment:
```bash
python manage.py runserver
```

## Usage

To send API requests to statistics service, use endpoint `/api/statistic/`. Endpoint supports 3 method of requests: `GET`, `POST` and `DELETE`.

### GET method

> This method is designed to represent already collected statistics.

Send simple `GET` request to get all collected statistics.

Example:
```bash
curl -X GET '127.0.0.1:8000/api/statistic/'
```
Result:
```json
[
    {
        "date": "2021-10-10",
        "views": 87,
        "clicks": 12,
        "cost": 74.9,
        "cpc": 624.17,
        "cpm": 86.09
    },
    {
        "date": "2021-10-12",
        "views": 54,
        "clicks": 2,
        "cost": 35.4,
        "cpc": 1770.0,
        "cpm": 65.56
    },
    {
        "date": "2021-10-14",
        "views": 300,
        "clicks": 60,
        "cost": 650.98,
        "cpc": 1084.97,
        "cpm": 216.99
    },
    {
        "date": "2021-10-22",
        "views": 154,
        "clicks": 82,
        "cost": 134.2,
        "cpc": 163.66,
        "cpm": 87.14
    }
]
```
Use `date_after` (starting date) or `date_before` (ending date) Query parameters to filter results. 
> `Note` Both parameters are inclusive

Example:
```bash
curl -X GET '127.0.0.1:8000/api/statistic/?date_after=2021-10-12&date_before=2021-10-14'
```
Result:
```json
[
    {
        "date": "2021-10-12",
        "views": 54,
        "clicks": 2,
        "cost": 35.4,
        "cpc": 1770.0,
        "cpm": 65.56
    },
    {
        "date": "2021-10-14",
        "views": 300,
        "clicks": 60,
        "cost": 650.98,
        "cpc": 1084.97,
        "cpm": 216.99
    }
]
```

### POST method

> This method is designed to add new statistics

Parameters:

__date__ `required`: Date of collected statistics | Format: `YYYY-MM-DD`

__views__ `optional`: Count of views in given date | Type: `Integer`

__clicks__ `optional`: Count of clicks in given date | Type: `integer`

__cost__ `optional`: Amount of money for given clicks represented in `rubles` with accuracy of `kopeks` | Types: `Float`, `Integer`

> `Note` Cost can't have more than 2 digits after the floating point

Example:
```bash
curl -X POST '127.0.0.1:8000/api/statistic/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "date": "2021-10-14",
    "views": 300,
    "clicks": 60,
    "cost": 650.98
}'
```
Result:
```json
{
    "date": "2021-10-14",
    "views": 300,
    "clicks": 60,
    "cost": 650.98,
    "cpc": 1084.97,
    "cpm": 216.99
}
```
### DELETE method
> This method is designed to wipe all statistics
```bash
curl -X DELETE '127.0.0.1:8000/api/statistic/'
```