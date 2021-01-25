
from flask import Flask, jsonify, request,render_template
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
from flask import request

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/h-db'
}

initialize_db(app)
movies = Movie.objects()

@app.route('/',methods=['GET'])
def get_movies():
    if request.method == 'GET':

        name=request.form['nm']
        cast=request.form['casts']
        geners=request.form['geners']
        print(name,cast,geners)

    return render_template('index.html')


  


   
