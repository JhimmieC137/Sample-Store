# Sample-Store
Sample-Store is a django project that creates a store for registered users to buy products, change their profile details and check their transaction history. It contains two applications. The 'store' app to display all available products, links to buy them and the 'userprofile' app that takes care of everthing concerning registeration, login, logout, user profile and others.      

# To run this application
Clone the repo, create a virtual environment, install the dependencies using 'pip install -r requirements.txt', configrue the settings file by connecting it to a database engine and then run the server with 'python manage.py runserver'. Templates were added for the different enpoints to show how the worked. 

Create a superuser with 'python manage.py create superuser', log into the admin console and populate the database with details on products. Sign up with the Api and login. 

# API endpoints
For the store app
- Home ('/store'):
  Returns all details on available products
  
- Create_order ('/store/create_order/<int:id>'):
  Takes in the id of a particular product to make an order object and register's it to the in currently logged in user 
  
For the userprofile app
- Registration ('/accounts/register'):
  This endpoint gets the requiered form to register a user and also accepts POST request to store that user's data retrieved from the form. It redricts to the Home page   on successful a login attempt.
  
- Login ('/accounts/login'):
  This gets the required form for a user to login and also accepts POST requests required for the Login action.
  
- Logout ('/accounts/logout'):
  This gets the details of the currently logged in user, executes the log out action and redirects to the Login page.
  
- Dashboard ('/accounts/dashboard'):
  On successful login, this gets the details of the the currently logged in user, returns all profile details of that user as well as a form to update those details.
  
- History ('/accounts/history'):
  On successful login, this gets the details on all products registered to the current user's profile.
