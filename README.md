
# Image Tagging System


This is an image tagging system that will help to add tags to images using Django restframework.

## Getting Started


These instructions will get you a copy of the project up and running on your local machine for testing purposes. See deployment for notes on how to deploy the project on system.

### Prerequisites


What things you need to install the software and how to install them

```
Python Version = 3.9
Django Version = 4.1.5
```

## Development Installations

### Ubuntu 20.04 LTS

Ubuntu development build instructions using an isolated virtual environment (tested on Ubuntu 20.04 LTS)::

Install Ubuntu dependencies

```
sudo apt-get update
sudo apt-get install python3-virtualenv python3-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpq-dev
```

Create and activate the virtualenv

```
python3 -m venv api_test_env
source api_test_env/bin/activate
```
git clone image_tagging_system

```
git clone https://github.com/parveenjangra290/image_tagging_system.git
cd image_tagging_system
```
Install pip dependencies and run migrations

```
pip install -r requirements.txt
pip install -e

python manage.py migrate
python manage.py runserver
```

Run test cases
```
python manage.py test
```

You can also interact with the API using command line tools such as curl.
```
# User Login
curl --location --request POST 'http://localhost:8000/api/v1/users/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "parveenjangra",
    "password": "admin@123"
}'
{"id":1,"username":"parveenjangra","email":"p@example.com","auth_token":"e64520d9ae2a52b89f0dff80d61e91de266e9287"}

# Tag Create
curl --location --request POST 'http://localhost:8000/api/v1/tag/' \
--header 'Authorization: Token e64520d9ae2a52b89f0dff80d61e91de266e9287' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "New Tag"
}'
{"message":"Tag Created Successfully"}

# Image Create
curl --location --request POST 'http://localhost:8000/api/v1/image/' \
--header 'Authorization: Token e64520d9ae2a52b89f0dff80d61e91de266e9287' \
--form 'image=@/Users/parveenjangra/Downloads/1645191503983.JPEG' \
--form 'description=This is testing'
{"id":20,"tags":[],"description":"This is testing","image":"/media/images/1645191503983_ZPPZKI9.JPEG"}

# Image Update
curl --location --request PUT 'http://localhost:8000/api/v1/image/update/10/' \
--header 'Authorization: Token e64520d9ae2a52b89f0dff80d61e91de266e9287' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "Update Image Description"
}'
{"id":10,"tags":[],"description":"Update Image Description","image":"/media/images/1645191503983.JPEG"}

# Image Search
curl --location --request GET 'http://localhost:8000/api/v1/images/search/?start_date=2023-01-09&end_date=2023-01-09' \
--header 'Authorization: Token e64520d9ae2a52b89f0dff80d61e91de266e9287'
{"data":[{"id":11,"tags":[],"description":"This is testing","image":"/media/images/1645191503983_3BGalnV.JPEG"},{"id":12,"tags":[],"description":"This is testing","image":"/media/images/1645191503983_UN11uIF.JPEG"}]}
```


## Authors

* **Parveen Kumar**
