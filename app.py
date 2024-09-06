from flask import Flask, request, jsonify
import mysql.connector
from config import DATABASE_CONFIG
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

# Products Endpoints
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products WHERE product_id = %s', (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(product) if product else ('Product not found', 404)

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO products (product_name, quantity, price) VALUES (%s, %s, %s)',
        (new_product['product_name'], new_product['quantity'], new_product['price'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE products SET product_name = %s, quantity = %s, price = %s WHERE product_id = %s',
        (updated_product['product_name'], updated_product['quantity'], updated_product['price'], product_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_product) if cursor.rowcount else ('Product not found', 404)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id = %s', (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

# Suppliers Endpoints
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM suppliers')
    suppliers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(suppliers)

@app.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM suppliers WHERE supplier_id = %s', (supplier_id,))
    supplier = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(supplier) if supplier else ('Supplier not found', 404)

@app.route('/suppliers', methods=['POST'])
def create_supplier():
    new_supplier = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO suppliers (supplier_name, contact_info) VALUES (%s, %s)',
        (new_supplier['supplier_name'], new_supplier['contact_info'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_supplier), 201

@app.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    updated_supplier = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE suppliers SET supplier_name = %s, contact_info = %s WHERE supplier_id = %s',
        (updated_supplier['supplier_name'], updated_supplier['contact_info'], supplier_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_supplier) if cursor.rowcount else ('Supplier not found', 404)

@app.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM suppliers WHERE supplier_id = %s', (supplier_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

# Purchases Endpoints
@app.route('/purchases', methods=['GET'])
def get_purchases():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM purchases')
    purchases = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(purchases)

@app.route('/purchases/<int:purchase_id>', methods=['GET'])
def get_purchase(purchase_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM purchases WHERE purchase_id = %s', (purchase_id,))
    purchase = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(purchase) if purchase else ('Purchase not found', 404)

@app.route('/purchases', methods=['POST'])
def create_purchase():
    new_purchase = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO purchases (product_id, supplier_id, quantity, purchase_date) VALUES (%s, %s, %s, %s)',
        (new_purchase['product_id'], new_purchase['supplier_id'], new_purchase['quantity'], new_purchase['purchase_date'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_purchase), 201

@app.route('/purchases/<int:purchase_id>', methods=['PUT'])
def update_purchase(purchase_id):
    updated_purchase = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE purchases SET product_id = %s, supplier_id = %s, quantity = %s, purchase_date = %s WHERE purchase_id = %s',
        (updated_purchase['product_id'], updated_purchase['supplier_id'], updated_purchase['quantity'], updated_purchase['purchase_date'], purchase_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_purchase) if cursor.rowcount else ('Purchase not found', 404)

@app.route('/purchases/<int:purchase_id>', methods=['DELETE'])
def delete_purchase(purchase_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM purchases WHERE purchase_id = %s', (purchase_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

# Sales Endpoints
@app.route('/sales', methods=['GET'])
def get_sales():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(sales)

@app.route('/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sales WHERE sale_id = %s', (sale_id,))
    sale = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(sale) if sale else ('Sale not found', 404)

@app.route('/sales', methods=['POST'])
def create_sale():
    new_sale = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO sales (product_id, quantity, sale_date) VALUES (%s, %s, %s)',
        (new_sale['product_id'], new_sale['quantity'], new_sale['sale_date'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_sale), 201

@app.route('/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    updated_sale = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE sales SET product_id = %s, quantity = %s, sale_date = %s WHERE sale_id = %s',
        (updated_sale['product_id'], updated_sale['quantity'], updated_sale['sale_date'], sale_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_sale) if cursor.rowcount else ('Sale not found', 404)

@app.route('/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sales WHERE sale_id = %s', (sale_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

# User Authentication Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# Function to create a new user with hashed password (for testing purposes)
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (username, password) VALUES (%s, %s)',
        (username, hashed_password)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=80)
