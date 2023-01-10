import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():  # put application's code here
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com',
                       'sdg':'sgddsgsd'})


if __name__ == '__main__':
    app.run()
