# Django-Store

# Project Name - Django Backend

This Django project serves as the backend for the web application.

## Project Overview

- The Django backend provides RESTful APIs to interact with the database and manage data for the frontend application.

## Installation

1. Clone the repository: `git clone https://github.com/eladh23/Django-Store.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`

## Configuration

1. Rename `.env.example` to `.env` and configure the environment variables like database credentials, API keys, etc.

## Database Setup

1. Apply migrations: `python manage.py migrate`
                     `python manage.py makemigrations `   
2. Create a superuser: `python manage.py createsuperuser`

## Running the Server

Run the development server: `python manage.py runserver`

## API Endpoints

- `/products/` - Fetch all products or add a new product (POST)
- `/products/<product_id>/` - Retrieve, update, or delete a specific product by ID

