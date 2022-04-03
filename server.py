import flask_app
from flask_app.controllers import c_run_games
from flask_app.controllers import c_ninjas
from flask_app.controllers import c_pirates
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)
