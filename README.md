# Sample-Store
# Intro

# API endpoints
For the store app
- Home ('/store')
  Returns all details on available products
  
- Create_order ('/store/create_order/<int:id>')
  Takes in the id of a particular product to make an order object and register's it to the in currently logged in user 
  
For the userprofile app
- Registration ('/accounts/register')
  This endpoint gets the requiered form to register a user and also accepts POST request to store that user's data retrieved from the form. It redricts to the Home page   on successful a login attempt.
  
- Login ('/accounts/login')
  This gets the required form for a user to login and also accepts POST requests required for the Login action.
  
- Logout ('/accounts/logout')
  This gets the details of the currently logged in user, executes the log out action and redirects to the Login page.
  
- Dashboard ('/accounts/dashboard')
  On successful login, this gets the details of the the currently logged in user, returns all profile details of that user as well as a form to update those details.
  
- History ('/accounts/history')
  On successful login, this gets the details on all products registered to the current user's profile.
