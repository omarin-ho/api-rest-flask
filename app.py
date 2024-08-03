from flask import Flask, jsonify, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    calculo = celsius * 9/5 + 32
    return calculo

def fahrenheit_to_celsius(fahrenheit):
    calculo = (fahrenheit -32 )* 5/9
    
@app.route('/convert', methods = ['POST'])
def convert_temp():
    data = request.get_json()
    input_temp=data.get('temperature')
    
    if data['type'] == 'celsius':
        result = celsius_to_fahrenheit(input_temp)
        output_unit = 'fahrenheit'
    
    if data['type'] == 'fahrenheit':
        result = fahrenheit_to_celsius(input_temp)
        output_unit = 'celsius'
        
    return jsonify({"temperature": result, "unit": output_unit})


if __name__ == '__main__':
    app.run(debug=False)
    
    
    
#ESTO ESTA EN PRODUCTIVO...