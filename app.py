from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to execute SQL queries
def execute_query(query):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/")
def home():
    return "Chat Assistant is running!"

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    user_query = data.get("query", "").lower()

    # Simple keyword-based mapping to SQL
    if "all users" in user_query:
        sql_query = "SELECT * FROM users;"
    elif "count users" in user_query:
        sql_query = "SELECT COUNT(*) FROM users;"
    else:
        return jsonify({"error": "Query not understood"}), 400

    result = execute_query(sql_query)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses a dynamic port
    app.run(host="0.0.0.0", port=port)
