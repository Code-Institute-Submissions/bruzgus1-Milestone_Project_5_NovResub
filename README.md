# Hypixel Skyblock Minion Shop Website

[View the live project here.]()

This websites purpose is to be treated as an official extension to the Hypixel Store that you can find [Here](https://store.hypixel.net/). On this website Hypixel Skyblock players will be able to buy minions and their upgrades for their island without the risk of being scammed like with the unofficial websites

**User Goals:**

- To see what kind of minions and minion upgrades he can buy
- To be able to freely navigate the website
- to buy his/her desired minions and their upgrades

**Site Owner Goals:**

- To inform the user of the minions he can buy
- to help the user find what they are looking for
- to be able to accept and fulfill an order

![how the website looks on diffrent devices](/media/am-i-responsive.png)

- **Wireframes For the Important Pages**
    - Home Page Wireframe - [View](/media/home_page.png)
    - Products Page Wireframe - [View](/media/products_page.png)
    - Cart Page Wireframe - [View](/media/cart_page.png)
    - Checkout Page Wireframe - [View](/media/checkout_page.png)
    - Profiles Page Wireframe - [View](/media/profiles_page.png)


## Model Relationship Diagram

![Model Diagram](/media/relational_database_diagram.png)


## Features

1. Home Page
    - Has the purpose of the website highlighted
    - ![Home Page](/media/home_page_1.png)
2. Products Page
    - Has all of our products
    - ![Product Page](/media/products_page_1.png)
    - Number of available prodcuts
    - ![Product Count](/media/product_count.png)
    - A sorting feature to narrow down your search
    - ![Sorting](/media/sorting_1.png)
    - Ability to favorite products so you can find them easier next time you are shopping
    - ![Favorite](/media/favorite_button.png)
3. Product Details Page
    - A picture of the product
    - Specify the quantity of the product you want
    - ![Quantity](/media/quantity_input.png)
    - Specify the tier of the product if applicable
    - A product description
    - Ability to leave Positive/Negative Reviews to give your feedback
4. Cart Page
    - look over the products you are about to buy
    - ![Cart Overview](/media/cart_overview.png)
    - Your Username to make sure the items are delivered to the correct player
    - ![Buying AS](/media/buying_as.png)
    - Ability to edit the cart if necessary
    - Move to checkout page
5. Checkout Page
    - Standart information necessary for payment
    - ![Payment Form](/media/payment_form.png)
    - Order summary to once again make sure you don't have unnecessary items in your cart
    - ![Order Summary](/media/order_summary.png)
6. Authentication
    - Log in/Log out pages for user authentication achieved using allauth
    - Registration page achived using allauth

## Future Features

1. Change the price in proportion of the tier you choose (If its an item that has a tier).
3. Make product managment on the frontend, not just the admin panel.


## Marketing

1. ![Facebook Page](/media/Facebook_Page.png)
2. ![News Letter](/media/news_letter.png)
3. This is a B2C type business
4. As this is supposed to be an extension of an official site the best Marketing Strategy is by using Content Creators who already work closely with the Hypixel network


## Bugs
- When in mobile view if you click the search bar and switch to desktop view without touching anything, there are 2 search bars, it disappears when you click on anything, besides the second search bar
![Search Bar Bug](/media/search_bar_bug.png)
- When getting the order confirmation email the user profile is not being attashed and instead says "none" ![Ordr Confirmation Bug](/media/order_confirmation_bug.png)


## Console Errors

- When checking the console on Brave Browser the console gives an error, that does not happen on other browsers or in a private browser window, it's a Browser specific error and it happens on almost every website, that error is not part of my code

![Console Error](/media/console_error.png)

- when checking the products page and products details page, a console error shows up that does not effect any functionality, I checked with my mentor, and tutoring, and we couldn't figure out why its showing up, regarless it does not effect functionality in any way

![Products Console Error](/media/products-console-error.png)

## Automated Testing

- Each page of the site was evaluated using Lighthouse to assess them on four metrics; Performance, Accessibility, Best Practices & Search Engine Optimization (SEO).

![lighthouse scores screenshot](/media/lighthouse%20score.png)

## Manual Testing
- 1.1) Clicked on products/shop now button to see if it opens the products page. Result: PASSED
- 1.2) Tried and open product details page in favorite page and products page to see if it opens product details page. Result: PASSED
- 1.3) Added products to cart to see if total purchase cost would update. Result: PASSED
- 1.4) Clicked all available buttons in the navigation menu to see that they all open the correct pages. Result: PASSED
- 1.5) Tried to open positive reviews in product details page to see if users can create and read them if they are logged in or update and delete them if they created them. Result: PASSED
- 1.6) Tried to open negative reviews in product details page to so see if users can create and read them if they are logged in or update and delete them if they created them. Result: PASSED
- 2.1) Tried registering several accounts to make sure the function was working correctly. Result: PASSED
- 2.2) Tried inputing the wrong login information to test validation, tried entering the correct login information, tried logging out. Result: PASSED
- 2.4) Registered multiple accounts to make sure the confirmation emails are being sent. Result: PASSED
- 2.5) Tried changing user profile information, tried viewing order history to make sure its correct, checked that the profile information is being inputted if its saved in the user profile. Result: PASSED
- 3.1) Checked to make sure sorting worked as intended. Result: PASSED
- ![Sorting 1](/media/sorting_1.png)
- 3.2) Checked to make sure sorting by category worked  correctly. Result: PASSED
- ![Sorting 2](/media/sorting_2.png) ![Sorting 3](/media/sorting_3.png)
- 3.3) Tried searching for several products by name or description to make sure I find the correct ones. Result: PASSED
- ![Searching](/media/searching.png)
- 3.4) Tried searching several categories and descriptions to see how many products I find and if its accurate. Result: PASSED
- ![Product Count](/media/product_count.png)
- 3.5) Tried favoriting products, by being logged in as different users to make sure only logged in users favorites are shown. Result: PASSED
- 4.1) Tried negative numbers in the quantity input. Result: PASSED
- ![Quantity Input](/media/quantity_input.png)
- 4.2) Checked the cart while it was empty and when items of different types and tiers were added. Result: PASSED
- 4.3) Tried removing products from the cart and updating quantity. Result: PASSED
- 4.4) During check out their is a list of the products the user is buying so he knows if he added something he didn't intend to. Result: PASSED
- 4.5) Tried adding products of all categories and tiers to see if everything was being added correctly. Result: PASSED
- 4.6) Tried selecting and adding the same products of different tiers to see if they were being counted as seperate. Result: PASSED
- 4.7) Checked to see if the subtotal of the products in the cart page was accurate. Result: PASSED
- 4.8) Tried to make a purchase when I wasn't logged in, Tried to make a purchase without filling out the form. Result: PASSED


## Deployment

### Stripe (Payments API) setup

Prior to deploying the application to Heroku, you create a Stripe account to use the payment processing functionality - note: the application is set for test payments only. Follow the steps below to create an account and to retrieve the necessary keys you will need later.

1. Create an account at [Stripe](https://dashboard.stripe.com/register)

2. Goto the [account dashboard](https://dashboard.stripe.com/test/dashboard).

3. Click the _Developers_ link then [API keys](https://dashboard.stripe.com/test/apikeys)

4. You will see two keys; `Publishable key` and `Secret key`. Keep these private, you will need them later when setting environment variables in Heroku.

| Stripe Key | Maps to Environment Key |
| ---------- | ----------------------- |
| Publishable key | STRIPE_PUBLIC_KEY |
| Secret key | STRIPE_SECRET_KEY |

### Heroku Deployment
#### In your workspace
1. Set the Debug Flag to False.
2. Create a .env file and input these variables: SECRET_KEY, DATABASE_URL, STRIPE_WH_SECRET, STRIPE_WB_SECRET, STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY
3. Set up Procfile with the following code "web: gunicorn app_name.wsgi:application"
4. Set up runtime.txt file with current python version.
5. Update requirements.txt file with all libraries and their versions with the console command "pip freeze > requirements.txt"
6. Add the URL for your deployed site to ALLOWED_HOSTS in settings.py file to make everything run smoothly, it should look something like this
```python
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
```
- Pushed the code to github.
#### In Heroku
1. Create a new Heroku app.
2. Set up my database by clicking "Recources" and adding Heroku Postgres to heroku app
3. Navigate to the Settings tab on the top horizontal bar, we will be adding the required _environment variables_ here.
4. Click the _'Reveal Config Vars'_ button and add the below variables:
- ![Variables](/media/variables.png)
5. Link the Heroku app to repository, to do this nagivate to "Deploy" scroll down and find "Deployment method" once you do click on "Github" and input your Github details. You will be prompted to search for the repo name. Once you have selected the repo, you are set to deploy from your github repository
6. Scroll a bit further down and find "Manual deploy" once you sellect the branch "main" and click "Deploy Branch"
7. To enable product images to be uploaded you will need to install django-storages and use Amazon S3 to store media files. Follow [this excellent guide](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf) to set this up. Follow all the steps for creating an S3 bucket, assigning access, and retrieving the keys to access it. Once you have the access keys you can proceed to the step below.
8. You will need to create some additional environment variables in Heroku
- ![Variables 2](/media/variables_2.png)
- ![Variables 3](/media/variables_3.png)
9. In your workspace add the if statement located in folder "minion_shop" in file "settings.py" from lines 179-201, and once again push to github to update your repository
10. In heroku nagivate to "Deploy" Scroll a bit further down and find "Manual deploy" once you do select the branch "main" and click "Deploy Branch"

## Content

- All images and product descriptions were taken from Hypixel Skyblock Wiki

## Plagiarism

- A lot of code was taken from botique ado as it was exactly what I needed or universally accepted
- some of the README.md file was taken and influenced by this [README.md File](https://github.com/Code-Institute-Submissions/django-ecommerce-1#readme)


## Credits
- Code Institute Tutor Support - The best help anyone could ask for.
- Stack OverFlow - How do people create anything without using this is beyond me
- My Mentor.