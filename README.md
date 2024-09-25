# Backend Test
 - This app enables customers to make orders of items and a confirmation message sent to them containing **Order No**

# Important configurations

### OAuth2
 - In google cloud console, set up an OAuth2 application Credentials <https://console.cloud.google.com/apis/credentials>
 - Assign the following scopes when creating OAuth consent screen: 
    ```
        'openid',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/userinfo.email'
    ```
 - Copy your `client_id` and `client_secret` to use them in your `.env` file, check `.env.example` file for guide.

 ### PostgreSQL DB Setup example
    ``` 
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'postgres',
                'HOST': 'db',
                'PORT': '5432',
            }
        }
    ```

### Afrikastalking API setup
  - Enter values in your `.env` file, check `.env.example` file for guide.
    ```
        AFRIKASTALKING_USERNAME="username"
        AFRIKASTALKING_API_KEY="API_KEY"
        AFRIKASTALKING_APP_ID="App ID"
    ```

# Quick setup
 - Follow these steps to setup locally:
    - Clone the repo: `git clone git@github.com:mutemip/backend-test.git`
    - Navigate into project directory: `cd backend-test`
    - To build docker images for our app and postgres run: check `Dockerfile` and `docker-compose.yml`
        - `docker build .`
        - `docker compose up -d --build`
    - Run `makemigrations` command: `docker-compose exec web python manage.py makemigrations`
    - Run `migrate` command: `docker-compose exec web python manage.py migrate`
    - Create super user: `docker-compose exec web python manage.py createsuperuser`

- Everything should be running well here.

## API Endpoints:
 - To login via google use: <http://localhost:8000/google-login> Endpoint
 - On a successful login, you'll be directed to user profile endpoint: <http://localhost:8000/api/user/profile/> 
 - To create customer use: <http://localhost:8000/api/customer/> Endpoint
 - To make an order user: <http://localhost:8000/api/order/> Endpoint

 ** Check this Scribe walkthrough of the API: ** <https://scribehow.com/shared/Complete_Backend_test_overview__cphgVdKpReeqjwThRt3ctA>

 ## Hosted the API on pythonanywhere PAAS platform
  - Live link: https://mutemi.pythonanywhere.com/api
    - Customer: <https://mutemi.pythonanywhere.com/api/customer/>
    - Order: <https://mutemi.pythonanywhere.com/api/order/>


  
