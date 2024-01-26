from flask import Flask, render_template, request

app = Flask(__name__)

def get_country_name(country_code):
    countries = {
        '555': 'USA',
        '380': 'UK',
        '333': 'France',
        '810': 'Japan',
        '490': 'Germany'
    }
    return countries.get(country_code, 'Unknown')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        country_code = phone_number[1:4]
        country_name = get_country_name(country_code)
        message = f'Телефон {phone_number} країна - {country_name}.'
        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
