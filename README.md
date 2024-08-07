# Company API

## Overview

This Django REST API project provides CRUD operations for managing company and employee data. It includes authentication, serialization, and various methods for interacting with the API using Postman.

## Tech Stack

- **Backend**: Django
- **Django REST Framework**: For building the API
- **PostgreSQL**: Database
- **JWT**: JSON Web Tokens for authentication
- **Postman**: API testing and development
- **Python**: Programming language
- **Virtualenv**: Virtual environment management

## Features

- **Serialization**: 
  - Utilizes Django REST Framework serializers for `Company` and `Employee` models.
  
- **API Endpoints**:
  - `GET` - Retrieve data from the API.
  - `POST` - Create new records in the API.
  - `PUT` - Update entire records.
  - `PATCH` - Update partial records.
  - `DELETE` - Remove records from the API.

- **JWT Authentication**:
  - Uses JSON Web Token (JWT) for secure API access.
  - Endpoints include:
    - `Token Obtain Pair` - `/api/token/`
    - `Token Refresh` - `/api/token/refresh/`

## Project Structure

### Django Project Structure

- `companyapi/`
  - `__init__.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`

- `api/`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `serializers.py`
  - `urls.py`
  - `views.py`
  - `migrations/`

### API Endpoints

- **Company**
  - `GET /company_/` - List all companies.
  - `POST /company_/` - Create a new company.
  - `GET /company_/1/` - Retrieve a specific company.
  - `PUT /company_/1/` - Update a specific company.
  - `PATCH /company_/1/` - Partially update a specific company.
  - `DELETE /company_/1/` - Delete a specific company.

- **Employee**
  - `GET /employee_/` - List all employees.
  - `POST /employee_/` - Create a new employee.
  - `GET /employee_/1/` - Retrieve a specific employee.
  - `PUT /employee_/1/` - Update a specific employee.
  - `PATCH /employee_/1/` - Partially update a specific employee.
  - `DELETE /employee_/1/` - Delete a specific employee.

## Implementation

### Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

### JWT Authentication

1. **Obtain JWT Tokens**:
   - **POST /api/token/** with valid credentials to get `access` and `refresh` tokens.

2. **Use Tokens**:
   - Include `Authorization: Bearer <your_access_token>` in headers for authenticated requests.

### Postman Testing

- **GET**: Retrieve data from the API.
- **POST**: Create new records. Example JSON body:
  ```json
  {
      "name": "Innovative Tech Solutions",
      "location": "San Francisco",
      "about": "Leading provider of innovative technology solutions.",
      "type_company": "SOFTWARE",
      "added_date": "",
      "active": true
  }
  ```
- **PUT**: Update records fully. Example JSON body:
  ```json
  {
      "name": "Updated Company Name",
      "location": "Updated Location",
      "about": "Updated About",
      "type_company": "Updated Type",
      "added_date": "",
      "active": false
  }
  ```
- **PATCH**: Update records partially. Example JSON body:
  ```json
  {
      "location": "New Location"
  }
  ```
- **DELETE**: Remove records.

## Models

### `Company` Model

- `id` (AutoField, Primary Key)
- `name` (CharField)
- `location` (CharField)
- `about` (TextField)
- `type_company` (CharField, Choices)
- `added_date` (DateTimeField, Auto now)
- `active` (BooleanField, Default True)

### `Employee` Model

- `name` (CharField)
- `email` (CharField)
- `address` (TextField)
- `phone` (CharField)
- `about` (TextField)
- `position` (CharField, Choices)
- `company` (ForeignKey to `Company`)

## Miscellaneous

- **Error Handling**: Detailed error messages are provided for invalid requests.
- **Testing**: Ensure all endpoints are tested using Postman to confirm functionality.
- **Documentation**: Updated documentation is provided for ease of use.

## Miscellaneous
- **Post Documentation Link:** https://documenter.getpostman.com/view/36902701/2sA3kdAdRq

---
