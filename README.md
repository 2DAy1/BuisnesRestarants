# Business Restaurants - Internal Service

This is an internal service for the company's employees to help them make decisions about where to have lunch. Employees can vote for the menu before leaving for lunch using a mobile app that interacts with the backend implemented in Django.

## Requirements

- Python (3.6 or higher)
- Django (3.x)
- Django Rest Framework (3.x)
- PostgreSQL (latest version)
- Docker and docker-compose (optional)

## Getting Started

Follow these steps to set up and run the system locally.

### 1. Clone the repository

```bash
git clone <https://github.com/2DAy1/BuisnesRestarants>
cd BuisnesRestarants
```
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows, use: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up the database
Create a PostgreSQL database and update the database settings in core/settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}

```
### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Create a superuser (optional)
If you want to access the Django admin interface, create a superuser with the following command:

```bash
python manage.py createsuperuser
```
### 7. Start the development server
```bash
python manage.py runserver
```
The development server should be running at http://localhost:8000/


### API Functionality
* Authentication: Allows users to register, log in, and obtain access tokens.
* Creating a restaurant: Allows restaurant owners to create their restaurant profiles.
* Uploading a menu for a restaurant: Allows restaurant owners to upload menus for each day.
* Creating an employee: Allows company employees to create their accounts.
* Getting the current day's menu: Retrieves the menu for the current day.
* Getting results for the current day: Retrieves the voting results for the current day. 

### Running Tests
To run the tests, use the following command:

```bash
pytest
```
### Docker (optional)
If you have Docker and docker-compose installed, you can also run the system using Docker containers. Make sure to update the DATABASES setting to use the appropriate container name for the PostgreSQL host.

```bash
docker-compose up --build
```
### Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
