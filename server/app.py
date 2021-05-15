from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
	return jsonify({"message":"Hello World!"})

@app.route('/hello')
def hello_user():
	return jsonify({"message":"Hello user!"})


if __name__ == "__main__":
    app.run(host ='0.0.0.0',port=5005, debug=True)