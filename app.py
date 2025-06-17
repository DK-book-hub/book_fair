from flask import Flask, render_template
import json

app = Flask(__name__)

def load_fairs():
    with open('data/fairs.json', 'r', encoding='utf-8') as f:
        fairs = json.load(f)
    fairs.sort(key=lambda x: x['date'], reverse=True)
    return fairs[:4]

@app.route('/')
def home():
    fairs = load_fairs()
    return render_template('home.html', fairs=fairs)

@app.route('/fair/<int:fair_id>')
def fair_detail(fair_id):
    with open('data/fairs.json', 'r', encoding='utf-8') as f:
        fairs = json.load(f)
    fair = next((f for f in fairs if f['id'] == fair_id), None)
    return render_template('fair_detail.html', fair=fair)

if __name__ == '__main__':
    app.run(debug=True)
