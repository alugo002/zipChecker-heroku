import pymysql
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from modules import convert_to_dict, get_zips, get_id
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'checkMyZip'
application = app

username = 'alexehtb_zipCodeChecker'
password = 'JesusWalks666'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = '127.0.0.1'
import os
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
uri = os.getenv("DATABASE_URL")
uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

Bootstrap(app)
db = SQLAlchemy(app)

zipsList = convert_to_dict("masterFile.csv")

class ZipForm(FlaskForm):
    name = StringField('Type in a zip code here', validators=[DataRequired()])
    submit = SubmitField('Submit')

pairs_list = []
for z in zipsList:
    pairs_list.append( (z['id'], z['zip']) )

@app.route('/', methods=['GET', 'POST'])
def index():
    def testdb():
        try:
            db.session.query('1').from_statement(text('SELECT 1')).all()
            return '<h1>It works.</h1>'
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
    zips = get_zips(zipsList)
    form = ZipForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name in zips:
            form.name.data = ""
            id = get_id(zipsList, name)
            return redirect( url_for('detail', id=id) )
        else:
            message = "That zip code is not in our database."
    return render_template('index.html', zips=zips, pairs=pairs_list, form=form, message=message)

@app.route('/zip/<num>')
def detail(num):
    try:
        zipsDict = zipsList[int(num)]
    except:
        return f"<h1>{num} Invalid zip code. Try putting a zip code from one of the listed cities.</h1>"
    return render_template('zips.html', zipC=zipsDict, ord=ord, urlTitle=zipsDict['zip'])

@app.route('/city/')
def city():
    return render_template('city.html', zipC=zipsDict, ord=ord, pairs=pairs_list, cityPairs=city_pairs_list)

if __name__ == '__main__':
    app.run(debug=True)
