# Create Flask App

Simple project to get started with your Flask App.

At the moment the sample project can register a user, log in a user and logout.

Styling done using [Bootstrap 5.3.3](https://getbootstrap.com/).

It's set up to use [SQLite3](https://www.sqlite.org) but can easily be changed to use your preferred database.

Create Flask App uses blueprints which means your project is ready to go big, it's easy to scale. It's great for both
small and large applications.

---

## Getting Started

Create your virtual environment and activate it. Then:

```
pip install -r requirements.txt
flask db init
flask db migrate -m "message"
flask db upgrade
python app.py
```

This will start the app in debug mode and is ready for you to use. First you should go
to [localhost:5000/register](http://localhost:5000/register) to register a new user. After that you will be able to log in
going to [localhost:5000/login](http://localhost:5000/login). The home page is protected by the ```@login_required``` decorator
of the Flask-Login package so that only logged-in users can see it.

## Easy to start

You only need to clone this repo, install the requests.txt file and run the database commands, and you're done. I
recommend using the latest versions (I will do my best to keep it updated as quickly as I can).

The starter project has:

1. Register Page
2. Login Page
3. Home Page
4. Users Admin Page
5. API
6. **BONUS** Logout *(not actually a page)*

After every update to the [models.py](https://github.com/Gl0deanR/flask-starter-app/blob/main/flaskstarterapp/models.py) 
file you need to run in your terminal virtual environment:
```
flask db migrate -m "migrate message"
flask db upgrade
```
this will look for changes in the database models and apply them to your database.

---

## Todo

- [ ] Create demo web application
- [ ] Work on code
- [ ] Add more features
- [ ] Work on README.md

---

## Inspired by [Create React App](https://github.com/facebook/create-react-app)
