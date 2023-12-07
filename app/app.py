from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_str = f'{num1} + {num2}'
        elif operation == 'subtract':
            result = num1 - num2
            operation_str = f'{num1} - {num2}'
        elif operation == 'multiply':
            result = num1 * num2
            operation_str = f'{num1} * {num2}'
        elif operation == 'divide':
            result = num1 / num2
            operation_str = f'{num1} / {num2}'
        else:
            result = 'Invalid operation'
            operation_str = 'Invalid operation'

        return redirect(url_for('result', result=result, operation_str=operation_str))

@app.route('/result/<result>/<operation_str>')
def result(result, operation_str):
    return render_template('result.html', result=result, operation_str=operation_str)

@app.route('/back_to_calculator')
def back_to_calculator():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
