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

- **Wireframes**
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
2. Products Page
    - Has all of our products
    - Number of available prodcuts
    - A sorting feature to narrow down your search
3. Product Details Page
    - A picture of the product
    - Specify the quantity of the product you want
    - Specify the tier of the product if applicable
    - A product description
4. Cart Page
    - To look over the products you are about to buy
    - Ability to edit the cart if necessary
    - Move to checkout page
    - Your Username to make sure the items are delivered to the correct player
5. Checkout Page
    - Standart information necessary for payment
    - Order summary to once again make sure you don't have unnecessary items in your cart

## Future Features

1. Change the price in proportion of the tier you choose (If its an item that has a tier).
2. Add a an option to leave a review in the product details page.
3. Make product managment on the frontend, not just the admin panel.


## Marketing

1. ![Facebook Page](/media/Facebook_Page.png)
2. ![News Letter](/media/news_letter.png)
3. This is a B2C type business
4. As this is supposed to be an extension of an official site the best Marketing Strategy is by using Content Creators who already work closely with the Hypixel network


## Bugs
- When in mobile view if you click the search bar and switch to desktop view without touching anything, there are 2 search bars, it disappears when you click on anything, besides the second search bar
![Search Bar Bug](/media/search_bar_bug.png)


## Console Errors

- When checking the console on Brave Browser the console gives an error, that does not happen on other browsers or in a private browser window, it's a Browser specific error and it happens on almost every website, that error is not part of my code

![Console Error](/media/console_error.png)

- when checking the products page and products details page, a console error shows up that does not effect any functionality, I checked with my mentor, and tutoring, and we couldn't figure out why its showing up, regarless it does not effect functionality in any way

![Products Console Error](/media/products-console-error.png)

## Automated Testing

- Each page of the site was evaluated using Lighthouse to assess them on four metrics; Performance, Accessibility, Best Practices & Search Engine Optimization (SEO).

![lighthouse scores screenshot](/media/lighthouse%20score.png)

## Manual Testing
- 1.1) Clicked on products/shop now button to see if it opens the products page.
- 1.2) Tried and open product details page in favorite page and products page to see if it opens product details page.
- 1.3) Added products to cart to see if total purchase cost would update.
- 1.4) Clicked all available buttons in the navigation menu to see that they all open the correct pages.
- 1.5) Tried to open positive reviews in product details page to see if users can create and read them if they are logged in or update and delete them if they created them.
- 1.6) Tried to open negative reviews in product details page to so see if users can create and read them if they are logged in or update and delete them if they created them.
- 2.1) Tried registering several accounts to make sure the function was working correctly.
- 2.2) Tried inputing the wrong login information to test validation, tried entering the correct login information, tried logging out.
- 2.4) Registered multiple accounts to make sure the confirmation emails are being sent.
- 2.5) Tried changing user profile information, tried viewing order history to make sure its correct, checked that the profile information is being inputted if its saved in the user profile
- 3.1) Checked to make sure sorting worked as intended
- ![Sorting 1](/media/sorting_1.png)
- 3.2) Checked to make sure sorting by category worked  correctly
- ![Sorting 2](/media/sorting_2.png) ![Sorting 3](/media/sorting_3.png)
- 3.3) Tried searching for several products by name or description to make sure I find the correct ones
- ![Searching](/media/searching.png)
- 3.4) Tried searching several categories and descriptions to see how many products I find and if its accurate
- ![Product Count](/media/product_count.png)
- 3.5) Tried favoriting products, by being logged in as different users to make sure only logged in users favorites are shown
- 4.1) Tried negative numbers in the quantity input
- ![Quantity Input](/media/quantity_input.png)
- 4.2) Checked the cart while it was empty and when items of different types and tiers were added
- 4.3) Tried removing products from the cart and updating quantity
- 4.4) During check out their is a list of the products the user is buying so he knows if he added something he didn't intend to
- 4.5) Tried adding products of all categories and tiers to see if everything was being added correctly
- 4.6) Tried selecting and adding the same products of different tiers to see if they were being counted as seperate
- 4.7) Checked to see if the subtotal of the products in the cart page was accurate
- 4.8) Tried to make a purchase when I wasn't logged in, Tried to make a purchase without filling out the form


## Deployment

- Set the Debug Flag to False.
- Set up Procfile.
- Set up runtime.txt file with current python version.
- Updated my requirements.txt file with all libraries and their versions.
- Pushed the final code to github.
- Create a new Heroku app.
- Set up my database by adding Heroku Postgres to my heroku app
- Set up AWS
- Set up my Config Vars (DATABASE_URL, SECRET_KEY, STRIPE_SECRET_KEY, AWS_ACCESS_KEY_ID) just to name a few.
- Link the Heroku app to repository.
- Click on **Deploy**.

## Content

- All images and product descriptions were taken from Hypixel Skyblock Wiki

## Plagiarism

- A lot of code was taken from botique ado as it was exactly what I needed or universally accepted


## Credits
- Code Institute Tutor Support - The best help anyone could ask for.
- Stack OverFlow - How do people create anything without using this is beyond me
- My Mentor.