from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/add', methods = ['POST'])
def addition():
    if request.method == 'POST':
        result = int(request.json['num1']) + int(request.json['num2'])

        return jsonify({'result' : result}) #returning result in json format

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 5000) 