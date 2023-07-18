**This project creates models based on JSON input.**
**It is also able to return JSON representation of models stored in database.**
**It uses Django and Django Rest Framework.**

## Quick Start:

- Go to console and clone the repository:
```
git clone https://github.com/4Tomek/rest_api_test.git
```
- Go into the repository and create virtual environment:
```
cd rest_api_test/project
python -m venv venv
```
- Activate scripts:
```
venv\Scripts\activate 
```
- Install dependencies:
```
pip install -r requirements.txt
```
- To migrate and fill tables into db.sqlite3 enter sequentially:
```
python manage.py makemigrations api
python manage.py migrate
```
- Run server:
```
python manage.py runserver
```
- Now copy JSON from the file 'test_data.json' and paste it into the textfield on this endpoint: 
```
http://127.0.0.1:8000/import/
```
- This will create objects in Django database
- Now you can display all objects of certain model from the database:
```
http://127.0.0.1:8000/detail/(model_name)/

for example: http://127.0.0.1:8000/detail/AttributeValue/
```
- You can also display individual object of this model selected by id:
```
http://127.0.0.1:8000/detail/(model_name)/(id)/

for example: http://127.0.0.1:8000/detail/AttributeValue/2/
```