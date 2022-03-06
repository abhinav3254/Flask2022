from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    return 'Welcome to DashBoard'

kolkata = [
    {
        'long':'22.0089E',
        'lat':'80.1254N'
    },
    {
        'Country':'India',
        'state':'West Bengal',
        'Population':'22.5 Million',
        'Capital':'Yes',
        'name' : 'vivek'
    }
]

@app.route('/ccu',methods=['GET'])
def kolkata1():
    return jsonify(kolkata)

if __name__ == '__main__':
    app.run(debug=True)