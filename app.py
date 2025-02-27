from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your username
    'password': '9441915971@aA',  # Replace with your password
    'database': 'favorites_app'
}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    favorite = request.form.get('favorite')
    if not name or not favorite:
        return "Name and favorite are required", 400

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, favorite_item) VALUES (%s, %s)", (name, favorite))
        connection.commit()
        return "Data added successfully", 201
    except mysql.connector.Error as err:
        return f"Error: {err}", 500
    finally:
        cursor.close()
        connection.close()

@app.route('/admin', methods=['GET'])
def admin_view():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        return render_template('admin.html', users=data)
    except mysql.connector.Error as err:
        return f"Error: {err}", 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
