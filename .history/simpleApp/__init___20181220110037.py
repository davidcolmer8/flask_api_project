import os

from flask import Flask
from flasgger import Swagger


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        """Example endpoint returning a list of colors by palette
        This is using docstrings for specifications.
        ---
        parameters:
        - name: palette
            in: path
            type: string
            enum: ['all', 'rgb', 'cmyk']
            required: true
            default: all
        definitions:
        Palette:
            type: object
            properties:
            palette_name:
                type: array
                items:
                $ref: '#/definitions/Color'
        Color:
            type: string
        responses:
        200:
            description: A list of colors (may be filtered by palette)
            schema:
            $ref: '#/definitions/Palette'
            examples:
            rgb: ['red', 'green', 'blue']
        """
        return 'Hello, World!'

    return app
