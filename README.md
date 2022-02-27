# Here is the Heroku link:
## https://frozen-hamlet-09935.herokuapp.com/
# If you want to run this locally without Heroku:
### Install the packages from requirements.txt in the terminal
### Obtain an API KEY from The Movie DB
1.	Create a directory somewhere on your computer called hw6.
2.	In that directory, run `git init` and `heroku create` to set up a Heroku app and git repository.
3.	Run the command to add a database to your app: `heroku addons:create heroku-postgresql:hobby-dev`
4.	Run `heroku config` and copy the database URL into your .env like we did in class.
### In your main directory do the following:
```
git init
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku config
```
### Copy and paste the DATABASE_URL somewhere
### Make sure there is a 'ql' (without single quotes) after postgres
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
### You should see a webpage with a random popular movie
### It should have the title, poster, tagline, genre, and Wikipedia URL
### Lastly, if you refresh the page, there should be a different random popular movie
### However, the size of the list of popular movies is 20,
### so there is a chance for the same movie to appear back-to-back