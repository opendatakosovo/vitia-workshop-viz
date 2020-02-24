from flask import Flask
from flask import render_template, Response
import json
from urllib2 import urlopen

app = Flask(__name__)


@app.route('/')
def home():
    return 'Shiko kodin dhe ndjek instruksionet'

@app.route('/piechart')
def piechart():

    #TODO: Kthe render_template ne piechart.html dhe kthe rezultatin
    #Kerkesa duhet te behet ne API dhe te kthehet rezultati si JSON
    #Per kete eshte importuar libraria json dhe te perdoret metoda json.loads(rezultati)
    #para se te kthehet rezultati si parameter
    url = 'http://0.0.0.0:5050/prokurimi'
    rezultati = urlopen(url).read()
    json_result = json.loads(rezultati)

    return render_template('piechart.html', result=json_result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
