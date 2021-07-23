import platform
import pathlib
import socket
import json
import flask
from flask import request


def get_info():
    p = pathlib.Path()

    info = {
        'current_path': p.cwd(),
        'platform_info': platform.platform(),
        'ip': socket.gethostbyname(socket.gethostname())
    }

    return info

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test')
def publish():
    result = get_info()
    return flask.jsonify({ 'info': result })

app.run(port=80)