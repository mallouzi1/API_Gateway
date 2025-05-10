from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/products')
def get_products():
    response = requests.get('http://localhost:5001/products')
    return jsonify(response.json())

@app.route('/api/orders/<int:order_id>')
def get_order(order_id):
    response = requests.get(f'http://localhost:5002/orders/{order_id}')
    return jsonify(response.json())

@app.route('/api/userinfo/<int:user_id>')
def get_user(user_id):
    response = requests.get(f'http://localhost:5003/users/{user_id}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
