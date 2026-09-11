from flask import Flask

from .sudoku import Sudoku


def create_app():
    app = Flask(__name__)

    from .routes import main

    app.register_blueprint(main)

    return app