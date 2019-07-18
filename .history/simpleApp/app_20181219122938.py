from flask import Flask

from . import trades

def startApp(config=None):
    app = Flask('simpleApp', static_folder=None)
    return app
    @app.route('/', methods=['GET'])
def home():
    """home page"""
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


