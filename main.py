from flask import Flask, request, jsonify, make_response
import models

app = Flask(__name__)


@app.route('/api/cars', methods=['GET'])
def index():
    agents_obj = models.session.query(models.Agent).all()
    agents = [
        {
            'id': agent.id,
            'age': agent.age,
            'gender': agent.gender,
            'miles': agent.miles,
            'debt': agent.debt,
            'income': agent.income,
            'sales': agent.sales
        } for agent in agents_obj]

    return make_response(jsonify(agents))


if __name__ == '__main__':
    app.run(debug=True)