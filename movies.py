from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal


app = Flask(__name__)
application = app

moviesList = convert_to_dict("grossingMovies.csv")

pairs_list = []
for m in moviesList:
    pairs_list.append( (m['Index'], m['Title']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Highest Grossing Movies Per Year (2000's)")

@app.route('/year/<num>')
def detail(num):
    try:
        moviesDict = moviesList[int(num)]
    except:
        return f"<h1>{num} is invalid value for year. Year value treats year as number. For example, 2009 = 9 while 2010 = 10</h1>"
    return render_template('movies.html', gross=moviesDict, ord=ord, urlTitle=moviesDict['Title'])

if __name__ == '__main__':
    app.run(debug=True)
