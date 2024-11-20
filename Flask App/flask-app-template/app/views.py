# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask import render_template, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from app.models import db, Supplier  


# App modules
from app import app
# from app.models import Profiles

# App main route + generic routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/searchSuppliers')
def search_suppliers():
    return render_template('searchSuppliers.html')

@app.route('/searchsuppliers/results')
def search_suppliers_results():
    city = request.args.get('city')  
    suppliers = Supplier.query.filter_by(City=city).all()  
    return render_template('supplierSearchResult.html', suppliersData=suppliers)
