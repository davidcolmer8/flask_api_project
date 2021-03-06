from flask import Flask, jsonify, request
import uuid
import click

def startApp(cli=False):
    app = Flask(__name__)
    return app

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
@app.route('/uuid/<string:input>', methods=['GET','POST'])
def addTradeID(input):
    print(input)
    return jsonify({'user':input})
   
if __name__ == "__main__":
    app.run(debug=True)