# Smolepizza

Web Programming with Python and JavaScript

In this project I have built web application for handling a pizza restaurant online orders. Users are able to browse the restaurant's menu, add items to their cart, and submit their orders. Meanwhile, the site administrators are able to add and update menu items using Django Admin, and restaurant staff are able to view and change status of orders that have been placed by customers.

My web application support all of the available menu items for Pinnochio's Pizza & Subs.

Site users are able to register for the site with first and last name, password and unique username and email. Then they are able to login and log out of the website.

Once logged it, users see a representation of the restaurant's menu, and can choose a product diving in into corresponding categories. After that, they have to choose quantity, size and corresponding amount of toppings if required for choosen product. If chosen product is presented in different sizes, this is present by dropdown list with indication corresponding price. If it is a pizza with toppings there is a check if all toppings needed in specific case are chosen and not more than required. This check I have realized by JavaScript as it should by done on clients side. In the shopping cart user can see line totals calculated on quantity of chosen product and final total calculated on all shopping cart items totals. The contents of the shopping cart are saved even if a user closes the window.

Once there is at least one item in a user's shopping cart, they are able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total. After placing an order user is redirected to a page where he can see all his orders and their statuses.

As my personal touch, I have added some features which I describe below.

All loggged in users which have staff permissions, can see "All Orders" button, which is not available for standart accounts. In this section, all orders are displayed, can be filtered by their status and their status can be changed by staff users.

After order creating, an email is sent to user to inform about it.

Eventually I have created five Django apps: accounts, carts, orders, pizza (main project app), and products. I am using sqlite3 database, but this can be changed to any other if needed.

I haven't built my application's entire login and authentication system myself and used Django's built-in users and authentication system, but I created some form field validators by myself and added the ability to show errors only if they are actual, and it was not trivial problem as I have login and registration form on the same page and built in validators by default were showing errors for both forms, indifferently on which was submitted.

For more details, please see my screencast and review my code.

Thank you!