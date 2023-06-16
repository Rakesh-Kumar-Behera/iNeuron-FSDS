from flask import Flask,request,render_template

app = Flask(__name__)

#Routes
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return 'We are ineuron FSDS 2.0 batch'

@app.route('/demo' , methods = ['POST'])
def math_operation():
    if request.method == 'POST':
        #for accessing value from json --> request.json
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']

        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        elif operation == 'subtract':
            result = num1 - num2

        return f"The operation is {operation} and the result is {result}"

@app.route('/operation' , methods = ['POST'])
def arithmatic_operation():
    if request.method == 'POST':
        #for accessing value from html form --> request.form
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        elif operation == 'subtract':
            result = num1 - num2

        #return f"The operation is {operation} and the result is {result}"
        return render_template('results.html' , result = result)
    

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 5000) 

    #cloud local ip where the app in running - 0.0.0.0
    #system local IP - 127.0.0.1
    #by default flask port = 5000