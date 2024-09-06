# Inventory-Management-System

This is an Inventory Management System built with Flask and MySQL. It provides APIs to manage products, suppliers, purchases, sales, and users. The application allows CRUD operations on these entities and user authentication.

# Project Structure
<br>

- **app.py** : Contains the Flask application and API endpoints.<br>
- **config.py** : Configuration file for database connection. <br>
-   **requirements.txt** : Lists the required Python packages. <br>
<br>

# Features
<br>

- **User authentication** : Create users and log in with password hashing. <br>
- **Manage products** : Create, read, update, and delete products. <br>
- **Manage suppliers** : Create, read, update, and delete suppliers. <br>
- **Manage purchases** : Create, read, update, and delete purchases.  <br>
- **Manage sales** : Create, read, update, and delete sales. <br>


## Technologies Used

- **Flask**: A micro web framework for Python.
- **mysql-connector-python**: MySQL driver for Python.
- **Werkzeug**: Provides utilities for password hashing and checking.



## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
```

### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure the Database
- Ensure you have MySQL installed and running.
- Ensure that the config.py file in your project directory contains the correct database credentials.

## API Endpoints

### User Authentication
- POST /login: Authenticate a user and receive a login response.
- POST /create_user: Create a new user with a hashed password

### Products
- GET /products: Retrieve all products.
- GET /products/<product_id>: Retrieve a product by ID.
- POST /products: Create a new product.
- PUT /products/<product_id>: Update a product by ID.
- DELETE /products/<product_id>: Delete a product by ID.

### Suppliers
- GET /suppliers: Retrieve all suppliers.
- GET /suppliers/<supplier_id>: Retrieve a supplier by ID.
- POST /suppliers: Create a new supplier.
- PUT /suppliers/<supplier_id>: Update a supplier by ID.
- DELETE /suppliers/<supplier_id>: Delete a supplier by ID.

### Purchases
- GET /purchases: Retrieve all purchases.
- GET /purchases/<purchase_id>: Retrieve a purchase by ID.
- POST /purchases: Create a new purchase.
- PUT /purchases/<purchase_id>: Update a purchase by ID.
- DELETE /purchases/<purchase_id>: Delete a purchase by ID.

##3 Sales
- GET /sales: Retrieve all sales.
- GET /sales/<sale_id>: Retrieve a sale by ID.
- POST /sales: Create a new sale.
- PUT /sales/<sale_id>: Update a sale by ID.
- DELETE /sales/<sale_id>: Delete a sale by ID.


### Usage

1. Run the Flask application:
```bash
python app.py
```

The server will start on http://localhost:80. Access the API using tools like Postman or cURl.

## Testing with Postman

###Create a User
- Open Postman.
- Set the request type to POST.
- Enter the URL: http://localhost:80/create_user.
- In the Body tab, select raw and JSON format.
- Provide the JSON payload:
  ```bash
{
    "username": "testuser",
    "password": "testpassword"
}
```
