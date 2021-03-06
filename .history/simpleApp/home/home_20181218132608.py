from flask import Flask, jsonify, request
import uuid
import click

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

#e.g. /uuid/XXXX where XXXX is anything that you try to ask for in api and you capture what XXXX is and log it.
@app.route('/uuid/<str;>', methods=['POST'])
def addTradeID():
    print(request.get_json())
    return jsonify(request.get_json())

if __name__ == "__main__":
    app.run(debug=True)