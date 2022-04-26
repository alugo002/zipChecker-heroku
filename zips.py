import pymysql
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from modules import convert_to_dict, get_zips, get_id
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'checkMyZip'

db_name = 'allZips.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

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
    zips = get_zips(zipsList)
    code = request.form.get("zipCode")
    if code in zips:
        id = get_id(zips, code)
        return redirect(url_for('zip', id=id))
    else:
        message = "That zip code is not in our database."

    return render_template('index.html', zips=zips, pairs=pairs_list, message=message, code=code)

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
