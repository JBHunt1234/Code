# -*- encoding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Supplier(db.Model):
    __tablename__ = 'Suppliers'
    SupplierID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(255))
    City = db.Column(db.String(255))
    Country = db.Column(db.String(255))

@app.route('/searchsuppliers')
def search_suppliers():
    return render_template('searchSuppliers.html')

@app.route('/get_suppliers_by_city')
def get_suppliers_by_city():
    city = request.args.get('city')
    suppliers = Supplier.query.filter_by(City=city).all()
    
    suppliers_data = [{
        'SupplierID': supplier.SupplierID, 
        'CompanyName': supplier.CompanyName, 
        'City': supplier.City, 
        'Country': supplier.Country
    } for supplier in suppliers]
    
    return jsonify(suppliers_data)

if __name__ == '__main__':
    db.create_all() 
    app.run(host='0.0.0.0', port=5005, debug=True)
