from flask import Flask, render_template, request
from utils.hitung_hari import hitung_hari_sejak_lahir

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    days = None
    birthdate_str = None

    if request.method == 'POST':
        birthdate_str = request.form.get('birthdate')
        if birthdate_str:
            days = hitung_hari_sejak_lahir(birthdate_str)

    return render_template('index.html', days=days, birthdate=birthdate_str)

if __name__ == '__main__':
    app.run(debug=True)
