from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from decouple import config


app = Flask(__name__)
CORS(app)

DATABASE_CONFIG = {
    'dbname': config('DB_NAME'),
    'user': config('DB_USER'),
    'password': config('DB_PASSWORD'),
    'host': config('DB_HOST')
}


@app.route("/query", methods = ['POST'])
def query_prof():
    data = request.json
    department = data.get("department")
    rating = data.get("rating")
    ratingCount = data.get("ratingCount")
    wta = data.get("wta")

    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()

    query = "SELECT name, rating FROM professors WHERE department = %s AND rating >= %s AND rating_count >= %s AND would_take_again >= %s"
    cur.execute(query, (department, rating, ratingCount, wta))

    professor_and_rating = cur.fetchall()
    #row[0] = name row[1] = rating

    results = [{'name': row[0], 'rating': row[1]} for row in professor_and_rating]

    cur.close()
    conn.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
