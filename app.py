from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)



@app.route('/')
def home():
    return jsonify({'studentId': '200557150'})

@app.route('/webhook/<date>')
def dateValidator(date):

    date = date.replace('_', '-')

    try:
        # Convert the date string to a date variable
        date_variable = datetime.strptime(date, "%Y-%m-%d").date()
        # Get today's date
        today = datetime.now().date()
        comparison_date = datetime.strptime("2026-03-25", "%Y-%m-%d").date()
        # Compare the dates
        if date_variable < today:
            return jsonify({'response':'The input date is in the past.'})
        elif date_variable > comparison_date:
             return jsonify({'response':'Please select a date between now and the next 2 years.'})
        
        return jsonify({'response':'Cool date!'})
    except ValueError:
        return jsonify({'response':'Invalid date format. Please provide date in the format YYYY-MM-DD.'})
