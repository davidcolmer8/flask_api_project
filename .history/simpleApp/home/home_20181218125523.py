from flask import Flask, jsonify, request
import uuid
import click
import request

app = Flask(__name__)

@click.command()
#@click.option('--')
@app.route('/', methods=['GET'])
def home():
    """home page"""
    return 'server is running'

@app.route('/uuid')
def getUUID():
    return jsonify(
        {
            "id": uuid.uuid1()
        }
    )

@app.route('/trades', methods=['POST'])
def addTradeID():
    return jsonify(request.get_json())

if __name__ == "__main__":
    app.run(debug=True)