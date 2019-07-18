from flask import Flask, jsonify 
import uuid
import click

app = Flask(__name__)

@click.command()
#@click.option('--')
#@app.route('/', methods=['GET'])
def home():
    """home page"""
    return 'server is running'

@app.route('/uuid')
def getUUID():
    id = uuid.uuid1()
    return id
    # return jsonify(
    #     {
    #         "id": uuid.uuid1()
    #     }
    # )
app.run(debug=True)