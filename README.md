# Botanica Houseplants
Find the deployed project [here](https://botanica-fa2bcebcf990.herokuapp.com/)!

## Introduction
Botanica is your go to online destination for the most vibrant houseplants. We offer a wide selection of indoor plants, for both novice plant owners and experienced green thumbs!
Enjoy our Plant care blog for tips and tricks to help you keep your plants thriving and enoy our seamless shopping experience complete with nature in mind.

## User Stories
### Customer
### Registered Customer
### Admin

## Entity Relationship Diagrams (ERD)
![ERD-botanica](botanica-ERD.png)
Created using dbdiagram.io

## User Experience
### Wireframes
#### home
#### products, bag, checkout, profile
### Colour Scheme
## Font

## Features
### Nav Bar, auth displays, products page, Facebook page, future

## Full Deployment to Heroku:
To make the locally running website active on a permanent server I needed to take multiple steps to for successful deployment:
-	Setting up an app in Heroku to deploy to a interactive public website.
-	Creation of an external database to store data in a structured way that can be easily accessed managed and updated
-	Setting up a hosting service for static and media files compatible with the Heroku server
### Created a database through ElephantSQL:
1.	Navigated to ElephantSQL.com, created a new instance called `botanica`
2.	Selected the ‘Tiny Turtle’ plan, left the tags blank and continued to the next page.
3.	Selected an AWS data centre with a region closest to me: ‘EU-West-1 (Ireland)
4.	After creating the instance, I copied the postgres database URL for later use.
### Created a new Heroku App:
1.	On the Heroku dashboard, I created a new app named ‘botanica’, matching the naming convention of my project.
2.	In the app settings tab, revealed the `Config Vars` and added the database URL under `Config Vars` with the key `DATABASE_URL`.
### Preparation of gitpod environment for deployment
1.	Installed `dj_database_url` and `psycopg2` through the terminal and added them to `requirements.txt`.
2.	Created a temporary `DATABASE_URL` in settings.py and created a superuser
3.	Ran commands to make migrations and migrate
4.	After running migrations, I confirmed that the ElephantSQL database was connected by checking `auth_user`.
5.	I installed `gunicorn`, created a `Procfile`, and added Heroku to allowed hosts in settings.py.
6.	Added, committed and pushed these changes to GitHub.
### Connecting to Heroku
1.	I logged in to Heroku from my IDE using `heroku git:remote -a botanica` command. Due to an IP mismatch error, I generated a new API token in Heroku settings.
2.	Finally, I deployed to Heroku with git push heroku main.
3.	Back in my IDE, I set a new secret key in Heroku Config Vars.
4.	I connected Heroku to GitHub and enabled automatic deployment.
### Creating an AWS S3 Bucket
1.	Created a new S3 Bucket called `botanica-plants`
2.	I configured CORS and set up a security policy for public access.
3.	Using AWS IAM, I created a group, applied a full access policy, and created a user to manage static and media files.
### IDE integration with AWS
1.	I installed `boto3` and `django-storages`, adding them to requirements.txt.
2.	Updated Heroku Config Vars with new static variables and removed the disable static file variable.
3.	Finally, I added AWS variables to settings.py, committed, and pushed these changes to Heroku.
By following these steps, I successfully deployed my website to Heroku and integrated AWS for static and media file hosting.


# Testing
For the full range of Testing, see [TESTING.md](TESTING.md)

## Credits
-
