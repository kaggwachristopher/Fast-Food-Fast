from app.app import app
from flask import jsonify


@app.errorhandler(400)
def invalid_json(self):
    return jsonify({'Invalid input': 'please insert valid json'}), 400


if __name__ == '__main__':
    app.run(debug=True)
