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
1. Checked all screen sizes
2. Tried inputing incorrect data into form fields
3. Closed the page before checkout_success to see if web hook created the order
4. Tried to give a negative number in the quantity input
5. Tried to make a purchase when I wasn't logged in
6. Checked the website on different browsers (Safari, Chrome, Brave Browser)
7. Checked the website on different devices (PCs, Macbook, Different Iphone Models, Android Phones)


## Deployment

- Set the Debug Flag to False
- Set up Procfile
- Pushed the final code to github
- Create a new Heroku app.
- Set up my Config Vars
- Set up my database
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