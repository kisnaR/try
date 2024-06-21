from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    age = int(request.form['age'])
    hrs = int(request.form['hrs'])
    flag = 1
    response = ""

    if age == 1 or age == 2:
        if hrs in [11, 12, 13, 14]:
            response = "YOU HAVE A HEALTHY AMOUNT OF SLEEP"
        else:
            response = '''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
            YOU SHOULD HAVE 11 TO 14 HOURS OF SLEEP'''
            flag = 0
    elif age in range(3, 6):
        if hrs in [10, 11, 12, 13]:
            response = "YOU HAVE A HEALTHY AMOUNT OF SLEEP"
        else:
            response = '''YOU DO NOT HAVE A HEALTHY AMOUNT OF SLEEP
            YOU SHOULD HAVE 10 TO 13 HOURS OF SLEEP'''
            flag = 0
    elif age in range(6, 13):
        if hrs in [9, 11, 12]:
            response = "YOU HAVE A HEALTHY AMOUNT OF SLEEP"
        else:
            response = '''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
            YOU SHOULD HAVE 9 TO 12 HOURS SLEEP'''
            flag = 0
    elif age in range(13, 19):
        if hrs in [9, 11, 12]:
            response = "YOU HAVE A HEALTHY AMOUNT OF SLEEP"
        else:
            response = '''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
            YOU SHOULD HAVE 9 TO 12 HOURS OF SLEEP'''
            flag = 0
    elif age > 18:
        if hrs in [7, 8]:
            response = "YOU HAVE A HEALTHY AMOUNT OF SLEEP"
        else:
            response = '''YOU DO NOT HAVE HEALTHY AMOUNT OF SLEEP
            YOU SHOULD HAVE 7 TO 8 HOURS OF SLEEP'''
            flag = 0

    if flag == 0:
        response += '''\n\n * * FACTS YOU MUST KNOW**
            1. NOT HAVING SUFFICIENT SLEEP CAN LEAD TO SLEEP DEPRIVATION WHICH AFFECTS 
            DAY-TO-DAY LIFE.
            2. HAVING MORE THAN 12 HOURS SLEEP CAN BE DANGEROUS. CORONARY HEART DISEASE,
            STROKE, AND DIABETES ARE FEW PROBLEMS WHICH MAY OCCUR.'''

    return response

if __name__ == '__main__':
    app.run(debug=True)