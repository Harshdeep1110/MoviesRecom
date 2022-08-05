from flask import Flask,jsonify,request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    
liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route('/get-movies')
def fetch_movies():
    return jsonify({
        "data":all_movies[0],
        "status":"Success"
    })

if __name__ == "__main__":
    app.run(debug = True)