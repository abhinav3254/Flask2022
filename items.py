from distutils.log import debug
from flask import Flask
from flask import jsonify

app = Flask(__name__)

main_page = "Hello User welcome to Home Page"

@app.route('/')
def main():
    return main_page


cart_items = {
        'total_item' : '1',
        'item_name' : 'Pant',
        'item_price' : '$2000',
        'delivery_charges' : '$200',
        'discount' : '$100',
        'coupon' : 'NEWUSER50',
        'total_price' : '$2100'
    }
@app.route('/cart')
def cart():
    return jsonify(cart_items)


coupons = {
    'total_item' : '1',
        'item_name' : 'Pant',
        'item_price' : '$2000',
        'delivery_charges' : '$200',
        'discount' : '$100',
        'coupon' : 'NEWUSER50',
        'total_price' : '$2100'
}
@app.route('/coupons')
def coupons():
    return jsonify(coupons)

if __name__ == '__main__':
    app.run(debug = True)