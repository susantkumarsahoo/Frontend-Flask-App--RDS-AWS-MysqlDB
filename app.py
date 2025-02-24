from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# AWS RDS MySQL Database Configuration
db_config = {
    "host": "studentdb.xxxxxxxxxxxxxxxxxxxxx amazonaws.com",
    "user": "admin",
    "password": "Student123****",
    "database": "studentdb"
}

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Create a table (Run this only once before inserting data)
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            contact VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Route for Home Page (Form)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]

        # Insert data into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, contact) VALUES (%s, %s)", (name, contact))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("index.html")

# Run this function once to create the table
create_table()

if __name__ == "__main__":
    app.run(debug=True)














