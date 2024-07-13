# Bus Ticket Booking System

This project is a Bus Ticket Booking System built using Django and Django REST Framework. It allows users to search for buses, block seats, and book tickets. The admin panel allows managing the buses, stops, seats, blockings, and bookings.

## Prerequisites

- Python 3.6+
- Django 3.2+
- pip (Python package installer)
- Virtualenv (recommended)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd bus_ticket_service
```

### 2. Create and Activate Virtual Environment

#### Create a virtual environment to isolate the project dependencies.
```sh
python -m venv venv
source venv/bin/activate  # On Unix or MacOS
.\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

#### Install the required dependencies using pip.

```sh
pip install -r requirements.txt
```

### 4. Configure the Database
By default, the project is configured to use SQLite. You can configure the database in bus_ticket_service/settings.py.

### 5. Apply Migrations

#### Apply the database migrations to create the necessary tables.

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

#### Create a superuser to access the Django admin panel.

```sh
python manage.py createsuperuser
```

### 7. Run the Development Server

```
python manage.py createsuperuser
```

### 8. Access the Admin Panel
Open your browser and go to http://127.0.0.1:8000/admin to access the admin panel. Use the superuser credentials to log in.


## Running Unit Tests

#### To run the unit tests for the project, use the following command:

```sh 
python manage.py test api
```

## Api Endpoints

### 1. User Registration
    
- URL: /register/
- Method: POST
- Data Params:
  - username: string
  - email: string
  - password: string

### 2. User Login

- URL: /login/
- Method: POST
- Data Params:
  - username: string
  - password: string


### 3. Buses

- URL: /api/buses/
- Methods: GET, POST
- Search Params: search, source, destination, ordering

### 4. Stops

- URL: /api/stops/
- Methods: GET, POST
- Search Params: search, bus, stop_name, ordering

### 5. Seats

- URL: /api/seats/
- Methods: GET, POST
- Search Params: search, bus, is_available, ordering

### 6. Blocking

- URL: /api/blockings/
- Methods: GET, POST
- Search Params: search, bus, pickup_point, ordering

### 7. Bookings

- URL: /api/bookings/
- Methods: GET, POST
- Search Params: search, blocking, ordering