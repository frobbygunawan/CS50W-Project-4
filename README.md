# CS50W-Project-4
The source for the starter code can be found at [CS50W Project 4](https://cs50.harvard.edu/web/2020/projects/4/network/)

## Project Overview
The project uses Python (Django) as the backend, Bootstrap, and Javascript for asynchronous call to backend. The idea is to create a website which function similar to Twitter, and less focus was directed for the aesthetic of the clone. The below set up direction was adapted from the CS50W project guidelines.

## Setup
In the distribution code is a Django project called project4 that contains a single app called network.

First, open up network/urls.py, where the URL configuration for this app is defined. A few URLs were already written, including a default index route, a /login route, a /logout route, and a /register route.

Take a look at network/views.py to see the views that are associated with each of these routes. The index view for now returns a mostly-empty index.html template. The login_view view renders a login form when a user tries to GET the page. When a user submits the form using the POST request method, the user is authenticated, logged in, and redirected to the index page. The logout_view view logs the user out and redirects them to the index page. Finally, the register route displays a registration form to the user, and creates a new user when the form is submitted. All of this is done for you in the distribution code, so you should be able to run the application now to create some users.

Run python manage.py runserver to start up the Django web server, and visit the website in your browser. Click “Register” and register for an account. You should see that you are now “Signed in as” your user account, and the links at the top of the page have changed. How did the HTML change? Take a look at network/templates/network/layout.html for the HTML layout of this application. Notice that several parts of the template are wrapped in a check for if user.is_authenticated, so that different content can be rendered depending on whether the user is signed in or not. You’re welcome to change this file if you’d like to add or modify anything in the layout!

Finally, take a look at network/models.py. This is where you will define any models for your web application, where each model represents some type of data you want to store in your database. We’ve started you with a User model that represents each user of the application. Because it inherits from AbstractUser, it will already have fields for a username, email, password, etc., but you’re welcome to add new fields to the User class if there is additional information about a user that you wish to represent. You will also need to add additional models to this file to represent details about posts, likes, and followers. Remember that each time you change anything in network/models.py, you’ll need to first run python manage.py makemigrations and then python manage.py migrate to migrate those changes to your database.
