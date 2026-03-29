import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS   # ✅ upar import karo

app = Flask(__name__)
CORS(app)   # ✅ yaha likho (IMPORTANT)

def analyze_logs():
    df = pd.read_csv('dataset.csv')

    total_requests = len(df)
    suspicious = df[df['status_code'] >= 400]

    return {
        "total_requests": int(total_requests),
        "suspicious_requests": int(len(suspicious)),
        "attack_percentage": round((len(suspicious) / total_requests) * 100, 2)
    }

@app.route('/api/data')
def get_data():
    return jsonify(analyze_logs())

if __name__ == "__main__":
    app.run(debug=True)