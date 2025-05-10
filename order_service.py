from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders/<int:order_id>')
def order(order_id):
    return jsonify({
        "order_id": order_id,
        "products": [1, 2],
        "total": 1498
    })

if __name__ == '__main__':
    app.run(port=5002)
