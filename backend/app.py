from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

data = pd.read_csv("crime_data.csv")

@app.route('/')
def home():
    return '✅ Flask API is running! Try /api/data?state=BIHAR&year=2001'

@app.route('/api/data', methods=['GET'])
def get_data():
    state = request.args.get('state')
    year = int(request.args.get('year'))

    filtered = data[(data['State'] == state) & (data['Year'] == year)]
    crime_types = ['Rape', 'K&A', 'DD', 'AoW', 'AoM', 'DV', 'WT']

    result = [{ "type": ct, "value": int(filtered[ct].sum()) } for ct in crime_types]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
