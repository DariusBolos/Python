from flask import render_template, url_for, request, flash, redirect
from controller.config import app, db, checkEmptyFields
from database.models.tables import CookedDish, Drink


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('/index.html')


@app.route('/menu/', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        info = request.form['item-info'] if 'item-info' in request.form else None
        if not checkEmptyFields(name, price, info):
            flash("Please fill all the fields before submitting", "error")
            return redirect(url_for("menu"))
        else:
            dish = CookedDish(name, price, info)
            db.session.add(dish)
            db.session.commit()
            return redirect(url_for("menu"))

    return render_template('/menu.html')


@app.route('/menu/catalogue', methods=['POST', 'GET'])
def catalogue():
    return render_template('/catalogue.html', items=CookedDish.query.all())


@app.route('/order')
def order():
    return render_template('/order.html')
