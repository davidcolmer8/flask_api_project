from flask import Flask, jsonify 
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

@app.route('/trades', methods)
if __name__ == "__main__":
    app.run(debug=True)