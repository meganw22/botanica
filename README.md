# Botanica Houseplants
![header](https://github.com/meganw22/botanica/assets/141934888/99761b8f-da72-45c3-a88d-1f033d5c4560)

**Find the deployed project [here](https://botanica-fa2bcebcf990.herokuapp.com/)!**

## Introduction
The e-commerce application "Botanica" is an online store that specialises in selling a selection of indoor plants, for both novice plant owners and experienced green thumbs. The business model focuses on providing customers with a wide range of plants and plant care tips, providing a user-friendly platform for users to enjoy a seamless shopping experience complete with nature in mind
Below is a detailed overview of the e-commerce business model underlying the application.

### Business Model Type: B2C (Business to Consumer)

Botanica operates as a B2C e-commerce business, selling products directly to consumers from product browsing to payment and delivery.

## Business Model Canvas

| Component            | Description                                                   |
|----------------------|---------------------------------------------------------------|
| **Key Partners**     | Plant suppliers, courier services, payment processors (Stripe)|
| **Key Activities**   | Product sourcing, order processing, website maintenance, customer support |
| **Key Resources**    | Inventory, e-commerce platform, customer database, marketing content |
| **Value Propositions** | Quality plants and accessories, educational content, user-friendly shopping experience |
| **Customer Relationships** | Email marketing, social media engagement |
| **Channels**         | Website, email, social media                                  |
| **Customer Segments**| Plant enthusiasts, home decor enthusiasts, pet owners         |
| **Cost Structure**   | Product procurement, website maintenance, marketing expenses, shipping costs |
| **Revenue Streams**  | Product sales, delivery fees                                  |


This comprehensive e-commerce business model ensures that Botanica can effectively serve its customers while maintaining a profitable and sustainable operation.

## User Stories
### Project Purpose 
- The development of Botanica Houseplants is driven by a clear and well-defined purpose to address the needs of the target audiences, which include customers, registered users, and administrators.
- Each user story is used to improve the user experience, streamline processes, and provide features that cater to the specific needs of these groups.
- An agile tool was used in the method of planning this project which can be observed in the image and further explanation is provided below:

![user-stories](https://github.com/meganw22/botanica/assets/141934888/de29d90b-9d64-4285-95dc-28c7e9b5a270)

### As a customer
1. I want to view products and add items to my shopping bag depending on size and cost. This allows me to easily browse and select products based on my preferences, allow me to make informed decisions.
2. I want to update or remove products from my bag before checking out. This provides me the flexibility to modify my orders as needed, ensuring my shopping bag contains only the items I want to purchase.
3. I want to view my shopping bag and see the price of each item, delivery cost and grand total of my bag. This offers transparency on the total cost before making a purchase, enabling me to review and manage my budget effectively.
4. I want to be able to make an informed decision on my purchase and see product descriptors. This provides detailed information about the products to aid in decision-making, helping me choose products that best meet my needs and preferences.
5. I want to be able to view the plant blog for tips on plant maintenance. This offers additional value through expert advice on plant care, allowing me to learn how to better care for my plants, leading to higher satisfaction.
6. I want to view the webpages in a consistent manner, so navigation is structured well and is intuitive and easy to follow, enabling me to easily find the information or products I am looking for.

### As a registered user
1. I want to be able to read, update, or delete my personal information. This ensures that I have control over my personal data, allowing me to keep my information up-to-date and maintain privacy.
2. I want to receive feedback after making a purchase, so I know whether my transaction was successful or if there was an issue. This provides reassurance on the transaction status, allowing me to respond to the issue if required.
3. I want to be able to read, write, update, and delete my comments on plant blog posts. This enhances interaction and engagement with the blog content, enabling me to participate in discussions and share my thoughts.
4. I want to buy products through a secure checkout. This ensures that my payment information is protected, and that my data is secure.
5. I want to be able to like and comment on plant blogs for more user interaction. This gives sense of community and engagement with the content, allowing me to interact with blog posts and other users, enhancing my experience.

### As an Administrator
1. I want to manage user roles and permissions, so I can control who has access to different parts of the website and its functionalities. This ensures the website runs smoothly with appropriate access controls, allowing me to assign roles to maintain security and efficiency.
2. I want to ensure that customers have a simple signup/login process with any errors displayed to the user. This provides good user experience through a seamless registration process and reduces barriers for new users to sign up.
3.  I want to manage the blog section of the website, where I can post articles about plant care tips, new arrivals, and other relevant information for customers. This keeps the content fresh and informative, driving engagement and return visits.

## Entity Relationship Diagrams (ERD)
The backend of this project is primarily constructed using Python and the Django framework. It employs Django Models to manage the interaction with the database, facilitating the passing of information to and from the database. The following Entity-Relationship Diagram (ERD) provides a visual representation of the models created in this project and shows how they are interconnected.
![ERD-botanica](botanica-ERD.png)
Created using dbdiagram.io

## User Experience
Good user experience is very important to me, I like to have practical simplicity with easy navigation to encourage website visitors to explore the website with good intentions of making a purchase.
I know I have achieved my goals of good user experience and have received  feedback from test users about the design and layout of the website.

### Colour Scheme
I chose to keep my colours in keeping with nature and decided on earthy greens, whites and greys with a contrasting peach colour to accent all the buttons in the site.
![colour-scheme](https://github.com/meganw22/botanica/assets/141934888/262625f6-d1e4-4530-9961-48df02592e62)

### Font
Using Google fonts, I selected the font 'Fredoka' to use throughout the website. I found it to be a simple, quirky and very easy to read.

### Wireframes

# Features
## Base Template
The base template has been implemented to be used on every page within the website, this gives a clean smooth user experience allowing users to always know where to navigate to.
Within the Nav Bar, the title of the webpage has a link to return the user back to the homepage.

![nav-bar](https://github.com/meganw22/botanica/assets/141934888/48307d51-d40c-494d-9146-26fc21ac3d10)

There are list items including options to `Shop all Plants`, explore `Categories`, visit `The Plant Blog`, use the search bar to find a specific plant, navigate to your `bag` and discover the user profile.

![nav-categories](https://github.com/meganw22/botanica/assets/141934888/56b43ef7-835e-43d8-8530-f7505802deaa)


## User Login/Logout Pages
To login, the user has to select the user icon on the nav bar and click login:

![user-no-login](https://github.com/meganw22/botanica/assets/141934888/e26fa413-fc60-434f-80ee-ad8bfd512f02)

They will be directed to this page, where if necessary they will need to sign up first. There is no multi-factor authentication active for Botanica's sign up page.

![sign-in-page](https://github.com/meganw22/botanica/assets/141934888/2c9a9887-8635-49e1-923f-da2255db207c)

Once logged in the user has more access and can proceed to checkout, edit their profile and like and leave comments on the blog. The user is given conformation of successful login through a toast message:

![login-toast](https://github.com/meganw22/botanica/assets/141934888/d18f9a69-a26b-45e7-a37e-91692a63b5b6)

To Sign out, the user has to navigate to the nav bar user icon and select the dropdown button to Log out:

![user-logged-in](https://github.com/meganw22/botanica/assets/141934888/60f5bcad-329d-4df9-9bf2-c04d51efa8d6)

They will need to confirm the sign out through a secondary sign out page. User log out is confirmed with a toast message:

![signout-yes](https://github.com/meganw22/botanica/assets/141934888/580e0562-7e60-4f5e-bfab-055687cd3bef)


## Plant Products
Botanica has a variety of plants to choose from including plant features and requirements such as light levels, how easy or difficult a plant is to care for and whether the plant is safe around pets. These options are neatly displayed as filter items:

![all-plant-filters](https://github.com/meganw22/botanica/assets/141934888/80661631-179a-4df6-a7e4-dcf98fbcc76d)

Each plant has a rendered view of the plant name, scientific name, filter selections, an image of the selected plant and a brief description.

![med-fern-page](https://github.com/meganw22/botanica/assets/141934888/433367fd-e101-47f6-a4f4-288331e1e361)

Once the user is satisfied with their choice they are able to add the plant directly to their bag and are given the option to choose a height and a quantity between 1-99 items. Or the user can take a shortcut link to the plant blog if they require more advice with purchasing.
Once the user has added a product to their bag, a success message will be displayed confirming the item has been added to the bag.

![success-add-bag](https://github.com/meganw22/botanica/assets/141934888/b0ce84d5-9dbc-4e63-994c-8e2bde0e580a)


## The Plant Blog
![plant-blog](https://github.com/meganw22/botanica/assets/141934888/40d0b5f1-7799-4ac8-9cd2-d09c1b3c8eb1)


The Plant blog can be accessed via the nav bar and has several posts created to inform the user of tips and tricks for maintaining their plants. Once logged in users can comment and like posts. The blog provides a greater sense of community with other plant enthusiasts who need help with their plants too.
Registered users can delete their comments and unlike posts if they so wish and only a user with Admin access can create, update or delete posts.

![blog-likes-comments](https://github.com/meganw22/botanica/assets/141934888/7cc7b384-5f9c-477a-94b2-6eec209f266a)

## User Profile
The users profile can be viewed through clicking the User Icon in the Nav Bar and selecting `View Profile`
When the Users profile renders, it shows options to `Manage Addresses`, `Edit Details`, `Delete Profile` and provides a comprehensive `Order History`

![login-user-profile](https://github.com/meganw22/botanica/assets/141934888/ffb09b0c-b67c-469f-a039-f754e2975874)


## Checkout
The Checkout page is made up of a validation form for the user to submit their name, address and payment details through a Stripe Integrated Payment system. 

The User has the ability to choose an existing address or enter a new address. 

![checkout-new](https://github.com/meganw22/botanica/assets/141934888/db702578-b5e8-421a-a377-fbcf0451daf9)

The existing address is saved from the users first order:

![checkout-existing](https://github.com/meganw22/botanica/assets/141934888/da5441c9-a9bd-49bb-a354-30d41c55754a)

Double authentication has been applied and when submitting the correct card number and valid form details the user is directed to a secure confirmation page:

![checkout-2-auth](https://github.com/meganw22/botanica/assets/141934888/fc94286a-61ed-403f-92da-a100494449df)

If the user choses fail, the user is redirected to the checkout page and prompted to try a different card and try again.
Once the user clicks `complete` on the dual authentication pop up, they are directed to a `Success page` with their order details:

![success-order](https://github.com/meganw22/botanica/assets/141934888/cf641ba5-08d8-40b1-a8b0-8d71186a032a)


## Facebook Business page
I have created a Facebook Business page to market my website, find the link to the market [here](https://www.facebook.com/profile.php?id=61561624593985&is_tour_dismissed)

![Botanica-facebook-1](https://github.com/meganw22/botanica/assets/141934888/1b77c361-07cc-4ba0-a397-109cde5facb4)
![Botanica-facebook-2](https://github.com/meganw22/botanica/assets/141934888/ff953272-6695-4631-a40e-47ca4c2d1c3a)


## Future Implementations

# Full Deployment to Heroku:
To make the locally running website active on a permanent server I needed to take multiple steps to for successful deployment:
-	Setting up an app in Heroku to deploy to an interactive public website.
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
### Ongoing Deployment troubleshooting
After the initial deployment, changes to the css in the static files may change and when the next auto build is sent to heroku these changes are always pushed.
- In the terminal, log in to heroku using `heroku login -i` and then use `heroku run python manage.py collectstatic --noinput`.
- Open up your app in Heroku, click `more` button and restart all dynos.
### Send New Migrations to Heroku
- If you find your latest migrations are not working on the deployed site, test the heroku migrations by `heroku run python3 manage.py showmigrations --app botanica`
- Login to Heroku through you IDE (`heroku login -i`) and makemigrations using `heroku run python3 manage.py makemigrations --app botanica`
- then migrate using `heroku run python3 manage.py migrate --app botanica`
- Rerun show migrations command and confirm migrations are completed.

## Main Technologies Used
1. HTML & CSS
2. Bootstrap
3. JavaScript
4. Python
5. Django
6. Heroku
7. Elephant SQL
8. Stripe
9. AWS Buckets and IAM
10. Chrome Dev tools

# Testing
For the full range of Testing, see [TESTING.md](TESTING.md)

## Credits
- Code Institute Boutique Ado project template and guidance
- Pexels for free stock images
- Many very helpful websites including W3Schools, Stack Overflow, YouTube, Shopify and Django documentation
- And finally to my Mentor, Luke Buchanan - Thank you!
