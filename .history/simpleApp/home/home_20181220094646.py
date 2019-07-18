from flask import Flask, jsonify, request
import uuid
from app import app

@app.route('/', methods=['GET'])
def home():
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
    return 'server is running'

@app.route('/uuid')
def getUUID():
    return jsonify(
        {
        "id": uuid.uuid4()
        }
)      

    #e.g. /uuid/XXXX where XXXX is anything that you try to ask for in api and you capture what XXXX is and log it.
@app.route('/uuid/<string:input>', methods=['GET','POST'])
    def addTradeID(input):
        print(input)
        return jsonify({'user':input})