# Inventory-Management-System

This is an Inventory Management System built with Flask and MySQL. It provides APIs to manage products, suppliers, purchases, sales, and users. The application allows CRUD operations on these entities and user authentication.

# Project Structure
<br>

**app.py** : Contains the Flask application and API endpoints.<br>
**config.py** : Configuration file for database connection. <br>
**requirements.txt** : Lists the required Python packages. <br>
<br>

# Features
<br>

-**User authentication** : Create users and log in with password hashing. <br>
-**Manage products** : Create, read, update, and delete products. <br>
-**Manage suppliers** : Create, read, update, and delete suppliers. <br>
-**Manage purchases** : Create, read, update, and delete purchases.  <br>
-**Manage sales** : Create, read, update, and delete sales. <br>


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
