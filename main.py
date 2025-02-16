from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/length', methods=['GET'])
def get_length():
    name = request.args.get('name', '')
    return jsonify({"name": name, "length": len(name)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
