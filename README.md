# Django-BugClaim-Server
This is a "Bug Claim Server" which gives all general features for a Bug Bounty platform should have.

The backend is completely build on Django using Django Rest Framework
### Features
* 5 different roles defined i.e Root Admin, Root Moderator, Company Admin, Company Moderator and Researcher
* Login/Registration for researcher
* Login/Registration for company only by admin or admin moderator(permission)
* Login/Registration for company moderator by only company admin(permission)
* Login/Registration for researcher
* Profile GET and Update by User(for all different roles only by owner)



## Backend Setup
1. Clone this repository: `git clone https://github.com/CybSec-NITW/Bugclaim-Server.git`.
2. Change the current directory to `backend` folder: `cd ./Bugclaim-Server`.
3. Create a virutal environment and install all backend dependencies with pipenv: `pipenv install`.
4. Start the virtual environment: `pipenv shell`.
5. Run `python manage.py makemigrations`.
6. Run `python manage.py migrate`.
7. Create a superuser: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`.


## Backend API Documentation
API Documentation is generated using the default tool provided by Django Rest Framework.

### View The API documentation
1. Make sure that the Backend Server is running.
2. Navigate to the [localhost:8000/docs/](localhost:8000/docs/)
