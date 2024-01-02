from flask import render_template, url_for, request, flash, redirect
from controller.config import app, db, checkEmptyFields
from data.models.tables import CookedDish, Drink


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('/index.html')


@app.route('/menu/', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        info = request.form['item-info'] if 'item-info' in request.form else None
        option = request.form['option'] if 'option' in request.form else None
        if not checkEmptyFields(name, price, info, option):
            flash("Please fill all the fields before submitting", "error")
            return redirect(url_for("menu"))
        else:
            typeOfItem = {
                "dish": CookedDish(name, price, info),
                "drink": Drink(name, price, info)
            }

            item = typeOfItem[option]
            db.session.add(item)
            db.session.commit()
            return redirect(url_for("menu"))

    return render_template('/menu.html')


@app.route('/menu/catalogue', methods=['POST', 'GET'])
def catalogue():
    return render_template('/catalogue.html', dishes=CookedDish.query.all(), drinks=Drink.query.all())


@app.route('/order/')
def order():
    return render_template('/order.html')
