from flask import Flask, jsonify
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='nebula-redis', port=6379)

@app.route('/')
def stats():
    count = redis.incr('hits')
    return jsonify({
        "service": "Python Flask",
        "message": "I count things!",
        "visits": count,
        "hostname": os.getenv("HOSTNAME")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)