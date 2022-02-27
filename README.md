# Here is the Heroku link:
## https://frozen-hamlet-09935.herokuapp.com/
# If you want to run this locally without Heroku:
### Install the packages from requirements.txt in the terminal
### Obtain an API KEY from The Movie DB
### In your main directory do the following:
```
git init
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku config
```
### Copy and paste the DATABASE_URL somewhere
### Make sure there is a 'ql' (without apostrophes) after postgres
### Create a .env file in the main directory
### Inside the .env file, put:
```
export TMDB_KEY='your_API_key'
export DATABASE_URL='your_DATABASE_URL'
```
### Replace your_API_key with the API KEY you have obtained from The Movie DB
### Make sure to keep the apostrophes
### After saving, run the main.py file in the terminal
### Follow the HTML link by holding control and clicking on the link in the terminal
### You should see a webpage that asks for you to login
### Create an account in the Sign Up page
### After signing up, it will redirect you to the Login page again
### Then, login with the sign up information
### Now, you should see the home page with a random popular movie
### It should have the title, poster, tagline, genre, and Wikipedia URL
### At the bottom of the page, you can comment and give a rating 
### You can also look at reviews made by others
### At the top of the page, you can click Home or Profile
### Home takes you to the regular webpage that has a random popular movie
### Profile takes you to a webpage that has all your comments
### With the comments, it has a movie ID
### You can click on this movie ID to go to the TMDB page for that specific movie
### Lastly, if you refresh the home page, there should be a different random popular movie
### However, the size of the list of popular movies is 20,
### so there is a chance for the same movie to appear back-to-back
# How implementing my project differed from my expectations:
### I thought combining the flask-login components of the project
### with the other components of the project was going to be simpler
### I ended up using most of the information from the lengthy example
### to help me make the login session
# Technical issues and how I solved them:
### 1) I had to delete a couple whole projects
### because I did not know how to combine the features together
### I solved this by working slowly and going through the lengthy example thoroughly
### to make sure I was not just copy-pasting and knew what I was coding
### 2) While I was working with the databases, when I was making them
### or resetting them, I had to wait a while for the local or heroku pages to start up again
### I solved this by working diligently, if I was stuck on a problem, I would take a break,
### jog around, or do some activity; then I came back refreshed and tried finding
### the solutions again in stackoverflow or they were simple problems that went over my head