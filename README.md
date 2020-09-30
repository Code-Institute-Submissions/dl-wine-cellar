# Wine Cellar - Milestone Four Project

You can view the deployed web application [here](https://dl-wine-cellar.herokuapp.com/)!

***

The purpose of this project is to create an online wine store that allows users to view a list of wines, additional details for each wine, add a selection of wines to a shopping cart and place an order. 
The web application uses HTML, CSS, Javascript & Bootstrap for the Front-End connecting to a Postgres database using Python Django Framework.

***

## UX

The primary objective of the application is to allow wine to be purchased, any user can place an order but registered users will receive a discount on their first order.

### Strategy

#### User Stories

- As a site user, I want to be able to view all wines, so that I can select some to purchase
- As a site user, I want to be able to view reviews for wines, so that I can make a decision on which wines to purchase
- As a site user, I want to be able to register for an account
- As a site user, I want to be able to filter wines by type and grape.
- As a site user, I want to be able to search by name or description

- As a registered user, I want to be able to login so that I can view my account
- As a registered user, I want to be able to logout so that my account is secure
- As a registered user, I want to be able to view my order history so that I can reorder the same items
- As a registered user, I want to be able to reset my password in case I forget it
- As a registered user, I want to be able to leave a review for a product I have purchased

- As a store owner, I want to be able to add, edit and delete wines from the store.

### Scope

The scope of the project is derived from the user stories outlined in the strategy plane above. At this stage of the UX process, we decide what features will be provided now and what will be provided at some point in the future.

### Structure

The structure chosen is a simple layout with a main header section containing the navigation and the a main content section.

### Skeleton

At this stage, [wireframes](https://github.com/LawlessXD/dl-wine-cellar/blob/master/wireframes/WineCellarWireframes.pdf) were created using Balsamiq for each of the different scenarios below;
- Home
- Wine 
- Wine Detail  
- Login
- Register
- Add Wine

The design in each of the [wireframes](https://github.com/LawlessXD/dl-wine-cellar/blob/master/wireframes/WineCellarWireframes.pdf)  is divided into two sections; Header and Content. The header will be the same throughout each of the different views.

### Surface

The colours used on the site were generated using the [Adobe colour wheel](https://color.adobe.com/create) to compliment the main background image on the home page.

The colours generated can be viewed [here](https://github.com/LawlessXD/dl-wine-cellar/blob/master/design/Adobe%20Colour%20wheel.JPG).
  
## Features 

The features implemented in the application are listed below:
- Home page: This is used as the landing page for the application and displays a background image with call to action for users to shop now.
- Navigation: This allows the user to navigate through the application with different options displayed for users that are logged in.
- Login: This allows a registered user to log in to the application.
- Register: This allows new users to create an account.
- Logout: This allows a user to logout from the application.
- Add Wine: This allows a registered user to add a wine.
- Edit wine: This allows a user to edit their own wine. If the current user is not the author, an error message is displayed below the navigation bar.
- Delete wine: This allows a store owner to delete a wine from the store. If the current user is not a superuser, an error message is displayed.
- Toast messages: Bootstrap Toast messages are used to display messages to the user when carrying out different functions such as adding an item to the cart or editing an item.
- Search bar: This allows any user to search by name, description, country or grape of the wine.
- Filtering: User can filter by category or grape.
- Sorting: User can sort by price, rating, name or country.
- Stripe: Stripe payment system.

The features that will be implemented at a later date are listed below:
- Add discount section to the cart based on a users order history.
- Shipping addresses, allow a registered user to select shipping address based on list or create a new shipping address.
- Billing addresses, allow a registered user to select billing address based on list or create a new billing address.
- Like/Unlike a wine: Allow a user to like and unlike a wine, these will be stored in favourites on user profile.
- Review section: Display a list of user reviews for each wine and allow registered users leave a review on a wine previously purchased.
- Pagination: Add pagination to the site as the number of wines increase.

___

## Technologies Used

### Languages
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)** - Used as markup for the website
- **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Used to add style to the page and position elements
- **[jQuery](https://jquery.com/)** - Used in conjunction with Bootstrap V4 Framework
- **[Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Used for form validation, back to top button, stripe functionality.
- **[Python](https://www.python.org/)** - Used for different functions of the web application.


### Libraries
- **[Django](https://www.djangoproject.com/)** - Uses the Django framework for each application.
- **[Bootstrap](https://getbootstrap.com/)** - Used throughout the site for responsive design
- **[Stripe](https://www.stripe.com/)** - Used to accept test payments on the site.
- **[Font Awesome](https://fontawesome.com/)** - Used to enhance the UX 
- **[Google Fonts](https://fonts.google.com/)** - imported into CSS

### Tools
- **[VSCode](https://code.visualstudio.com/)** - Used as IDE for project
- **[Git](https://git-scm.com/)** - Used for version control throughout the project
- **[Balsamiq](https://balsamiq.com/)** - Used to create wireframes

___

## Testing

### Chrome DevTools

**Chrome Devtools** was used to simulate how the website displayed on different devices with emphasis on Large Laptop (17.3") & Mobile screen sizes. It was also used as the main debugging tool when content was displayed incorrectly e.g. login, register form were hidden behind the header.

### Manual Testing
The website was tested on a Samsung A50 Android Device and the resulting layout is similar to the iPhone 8 within Chrome Devtools. It was also tested on Amazon Fire tablet.

Each of the below devices were tested using Chome DevTools;
- Samsung S5 (360 x 640)
- iPhone 5/5E (320 x 568)
- iPhone 6/7/8 (375 x 667)
- iPhone 6/7/8 Plus (414 x 736)
- iPhone X (375 x 812)

Each of the user journeys below were tested manually;

- As a site user, I want to be able to view all wines, so that I can select some to purchase.
All wines are visible by navigating to the All Wines page using the navigation bar or by using the Shop Now Call to Action.

- As a site user, I want to be able to register for an account
This was tested using a temp email account and the confirm email was successfully received after submitting the registration details.

- As a site user, I want to be able to filter wines by type and grape
This was tested from the navigation menu, filtering by Red, White or Sparking. Filtering is also available by Grape under each Type. 

- As a site user, I want to be able to search by name or description
This was tested by entering a name of a wine and by entering a random string such as Italy which not only returned Italian wines but also any wine that had Italy in the description.

- As a registered user, I want to be able to login so that I can view my account
I was able to login by entering by username or email and password used at registration.

- As a registered user, I want to be able to logout so that my account is secure.
This was tested once logged in and sign out was successful.

- As a registered user, I want to be able to view my order history so that I can reorder the same items.
Any orders placed while logged in are saved to the user profile.

- As a registered user, I want to be able to reset my password in case I forget it.
This was successfully tested by clicking the forgot password URL.

- As a store owner, I want to be able to add, edit and delete wines from the store.
As a superuser, I was able to login and add a wine then edit and delete it.

Throughout the development of the web application, print statements were used to output variables to the console. 

Setting Debug=True in the settings.py for the Django application allows any routing issues to be corrected. This was particularly useful to resolve indentation issues in urls.py and views.py in the different applications.

### Browser Compatibilty

The web application was tested on Google Chrome, Firefox, Microsoft Edge and Microsoft Internet Explorer. The layout and behaviour was found to be consistent across each of the browsers.

## Deployment

The project was developed locally using Visual Studio Code. Git was downloaded from https://git-scm.com/ and installed locally for version control. In parallel, a repository also called dl-wine-cellar was created on GitHub.

The project workspace was initialised using git init command from the cmd terminal within VS Code.

To connect the local git repository to GitHub repository, the following command was executed from the cmd terminal.

``` shell
git remote add origin https://github.com/LawlessXD/dl-wine-cellar.git
```

Each time a new feature was added the files would be added to the staging area using git add \* from the cmd line.

The features were then committed with a suitable message using;

``` shell
git commit -m "Added allauth templates".
```

The changes were pushed to the remote repository using;

``` shell
git push -u origin master 
``` 

initially and using git push for each subsequent push.

### How to deploy this application locally

Before you can run this application on your own machine, you must meet the following requirements;
- Use a suitable IDE e.g. VS Code, GitPod etc.
- Have Git installed. 
- Have Python installed.
- Have PIP installed.
- Have a Stripe account
- Have ngrok installed.

#### Steps

1. Create a local project folder
2. Navigate to main page for the repository https://github.com/LawlessXD/dl-wine-cellar
3. Click "Code"
4. Copy the URL.
5. Open folder to the project folder where you would like to Clone the repository.
6. Open terminal within your local IDE
6. Execute the below on the command line;
``` shell
git clone https://github.com/LawlessXD/dl-wine-cellar.git 
```
7. The project will now be cloned.
8. Alternatively, you can Download a ZIP of the repository, extract the folder and open with your preferred IDE.
9. Open a CMD terminal, and create a virtual environment using the below command
``` shell
python -m venv venv
```
10. Activate the virtual environment using the below command
``` 
venv\Scripts\activate   
```
11. Upgrade PIP if required
``` shell
pip install --upgrade pip.
```
12. Install the modules in the requirements file
``` shell
pip install -r requirements.txt
```
13. Load the categories fixture
``` shell
python3 manage.py loaddata categories.json
```
14. Load the grapes fixture
``` shell
python3 manage.py loaddata grapes.json
```
15. Load the wines fixture
``` shell
python3 manage.py loaddata wines.json
16. Apply migrations for the database
``` shell
python3 manage.py migrate
``````
17. run ngrok to setup a tunnel to your local server using the below command on the terminal
``` shell
ngrok http 127.0.0.1:8000
``````
This will generate a public URL that can be used to tunnel to your local server. The URL can be retrieved by entering http://127.0.0.1:4040/inspect/http into your browser.

This URL will need to be used to setup a webhook in Stripe for accepting payments.

The URL will also need to be added to the ALLOWED_HOSTS variable in settings.py for the application.

Note, each time your run Ngrok, a new URL is generated which will need to be updated in settings.py and the endpoint in stripe.

18. Create environment variables in your IDE e.g. for settings.json in VSCode on windows
``` shell
    "terminal.integrated.env.windows": {
        "SECRET_KEY": "AAAAAAAAAAAAAAAAA",
        "DEVELOPMENT": "1",
        "STRIPE_PUBLIC_KEY": "BBBBBBBBBBBBB",
        "STRIPE_SECRET_KEY": "CCCCCCCCCCCC",
        "STRIPE_WH_SECRET": "DDDDDDDDDDDDD"
``````

The secret key can be generated randomly used an online generator tool such https://miniwebtool.com/django-secret-key-generator/

The Stripe variables can be retrieved from the developers section within your Stripe account.

19. To run the application, use the below command on the terminal within the IDE
``` shell
python3 manage.py runserver
```
20. Open the URL generated using ngrok previously.

### Heroku

The application is hosted on [Heroku](heroku.com) and was deployed as follows; 

1. Created an account at [Heroku](heroku.com) 
2. Clicked "New" and "Create new app"
3. **App name** - Entered "dl-wine-cellar" as the app name (This must be unique on Heroku).
4. **Region** - Selected "Europe".
5. Clicked "Create App".
6. Click on resources and add "Heroku Postgres" which will be used for the production database.
6. **Deployment Method** - Leave as default "Use Heroku CLI".
7. Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).
8. Enter heroku login at the command line and enter your credentials when prompted.
9. Create a local `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
10. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.
11. Add to Heroku remote using terminal command `heroku git:remote -a dl-wine-cellar`
12. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
13. Enter the following variables;

| Key | Value |
 --- | ---
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLIC_KEY | `<your_public_key_on_stripe>`
STRIPE_SECRET_KEY | `<your_secret_key_on_stripe>`
STRIPE_WH_SECRET | `<your_public_key_on_stripe>`
USE_AWS | `TRUE`
AWS_ACCESS_KEY_ID | `<your_access_key_on_AWS>`
AWS_SECRET_ACCESS_KEY | `<your_secret_key_on_AWS>`

14. Pushed local git repository to Heroku using terminal command `git push heroku master`
15. The application is now deployed and can be viewed on [Heroku](https://dl-wine-cellar.herokuapp.com/).

## Credits

### Content

I would like to credit [Chris Zielinski](https://www.github.com/ckz8780/) as the code used throughout the application is largely derived from the Boutique Ado project with tweaks to CSS and HTML.

The back to top button was further customised based on this [Codepen](https://codepen.io/matthewcain/pen/ZepbeR)

The wine details on the site are taken from [Supervalu](https://supervalu.ie/) and [O'Briens](https://www.obrienswine.ie/)

### Media

The wine images on the site are taken from [Supervalu](https://supervalu.ie/) and [O'Briens](https://www.obrienswine.ie/)

### Acknowledgment 

I would like to thank my mentor [Precious Ijege](https://code-institute-room.slack.com/team/USMD0GEAD) for his guidance and support. 