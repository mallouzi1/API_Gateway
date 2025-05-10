from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Phone", "price": 499}
    ])

if __name__ == '__main__':
    app.run(port=5001)
