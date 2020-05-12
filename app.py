import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from datetime import date
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  @app.route('/')
  def index():
    return ("Welcome to the Casting Agency Application!")


  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
    actors = Actor.query.all()
    
    if len(actors) == 0:
      abort(404)

    data=[]
    for actor in actors:
      actors_data = {
        'name': actor.name,
        'age': actor.age,
        'gender': actor.gender
      }
      data.append(actors_data)

    result = {
              'success': True,
              'actors': data
            }
    return jsonify(result)


  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
    movies = Movie.query.all()

    if len(movies) == 0:
      abort(404)
    
    data = []
    for movie in movies:
      movies_data = {
        'title': movie.title,
        'release date': movie.release_date.isoformat()
      }
      data.append(movies_data)

    result = {
              'success': True,
              'movies': data
              }
    return jsonify(result)


  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, id):
    actor = Actor.query.filter_by(id=id).first()

    if actor is None:
      abort(404)
    else:
      actor.delete()
    return jsonify({
                  'success': True,
                  'deleted': id
                  })


  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, id):
    movie = Movie.query.filter_by(id=id).first()

    if movie is None:
      abort(404)
    else:
      movie.delete()
    return jsonify({
                  'success': True,
                  'deleted': id
                  })


  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actors(payload):
    body = request.get_json()
    try:
      name, age, gender = body['name'], body['age'], body['gender']
      actor = Actor(name=name, age=age, gender=gender)
      actor.insert()
      actor_data = {
        'name': actor.name,
        'age': actor.age,
        'gender': actor.gender
      }
      return jsonify({
          'success': True,
          'new actor added': actor_data
      })
    except:
      abort(422)
    

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movies(payload):
    body = request.get_json()
    try:
      title, release_date = body['title'], body['release_date']
      movie = Movie(title=title, release_date=release_date)
      movie.insert()
      movie_data = {
        'title': movie.title,
        'release_date': movie.release_date.isoformat()
      }
      return jsonify({
        'success': True,
        'new movie added': movie_data
      })
    except:
      abort(422)


  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actors(payload, id):
    actor = Actor.query.filter_by(id=id).first()
    if actor is None:
      abort(404)
    else:
      body = request.get_json()
      actor.name = body['name']
      actor.age = body['age']
      actor.gender = body['gender']
      actor.update()
      return jsonify({
        'success': True,
        'updated': id
      })


  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movies(payload, id):
    movie = Movie.query.filter_by(id=id).first()
    if movie is None:
      abort(404)
    else:
      body = request.get_json()
      movie.title = body['title']
      movie.release_date = body['release_date']
      movie.update()
      return jsonify({
        'success': True,
        'updated': id
      })
  
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
                  "success": False,
                  "error": 422,
                  "message": "Unprocessable"
                  }), 422
  
  @app.errorhandler(404)
  def notfound(error):
        return jsonify({
                        "success": False, 
                        "error": 404,
                        "message": "Not Found"
                        }), 404
  @app.errorhandler(405)
  def notallowed(error):
    return jsonify({
                        "success": False, 
                        "error": 405,
                        "message": "Method Not Allowed"
                        }), 405

  @app.errorhandler(500)
  def internal_server_error(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "Internal Server Error"
          }), 500

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad Request"
          }), 400
  @app.errorhandler(AuthError)
  def auth_error(errors):
        return jsonify({
          "success": False,
          "error": errors.status_code,
          "message": errors.error['description']
          }), errors.status_code
  return app

app = create_app()


if __name__ == '__main__':
  app.run(debug=True)