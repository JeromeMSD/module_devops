from flask import Flask, request

app = Flask(__name__)

dictionary = dict()

@app.route("/dictionary", methods=['GET'])
def get_dict():
	if request.method == 'GET':
		return str(dictionary)

@app.route("/dictionary/<value>", methods=['POST'])
def add(value):
	ret = "Hello, World !"
	if request.method == 'POST':
		dictionary[len(dictionary)] = value
		return "You had " + value + " to dictionary !"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
	ret = "Hello, World !"
	if request.method == 'POST':
		# values is a combinaison of form and args data
		value = str(request.form.get("key"))
		ret = ret + " \n You send " + value + " under 'key' key :)" 
	return ret

if __name__ == '__main__':
    app.run(debug=True)
