from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/api/cars', methods=['GET'])
def index():
    cars = [
        {'car1': {'model': 'xyz', 'price': 302, 'year': 2011}},
        {'car2': {'model': 'loro', 'price': 123, 'year': 2021}},
        {'car3': {'model': 'mcd', 'price': 1230, 'year': 2019}},
        {'car4': {'model': 'abc', 'price': 230, 'year': 2015}}
    ]
    return make_response(jsonify(cars))


if __name__ == '__main__':
    app.run(debug=True)