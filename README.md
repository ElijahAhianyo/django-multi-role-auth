<h1 align="center">Django Multi Role Authentication 👋</h1>

This project shows how i implemented multi-role authentication in django django rest framework.

## USE CASE:
The system has four different portals(admin,patient,staff, support) which requires users have respective roles in order to log in.
A user can have multiple roles.
To login, a seperate endpoint is provided for each portal where the role is checked and user authenticated. This returns a jwt token. 
For eg. 
admins login using `/admin/auth/login`
staff login using `/staff/auth/login`



## Install and Run

1. Get the source code on to your machine via git.

    ```shell
    git clone https://github.com/ElijahAhianyo/django-multi-role-auth.git && cd django-multi-role-auth
    ```

2. Create virtual environment and install dependencies
```sh
#using virtual environment
python3 -m venv .virtualenv
#activate virtual environment
source ./.virtualenv/bin/activate
#install dependencies
pip install -r requirements.txt
```

3. Migrate and run application
```sh
cd app
python manage.py migrate
python manage.py runserver
```



## TO-DO:
- Add unit tests
- enforce static typing