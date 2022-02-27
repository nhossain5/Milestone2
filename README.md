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