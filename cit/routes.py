from flask import Flask,render_template, request
import requests
from cit import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    citate = None
    if request.method == 'POST':
        citate = get_citate()
    return render_template('home.html', citate=citate)
def get_citate():
    api_key = 'your_api_key'
    url = 'https://api.quotable.io/random'

    response = requests.get(url, verify=False, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "An error occurred while retrieving the citate. Please try again later."