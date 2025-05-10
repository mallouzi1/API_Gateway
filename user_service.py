from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>')
def user(user_id):
    return jsonify({
        "user_id": user_id,
        "name": "Jane Doe",
        "email": "jane@example.com"
    })

if __name__ == '__main__':
    app.run(port=5003)
