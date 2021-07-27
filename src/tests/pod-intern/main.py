import platform
import pathlib
import socket
import json
import flask
import psutil
from flask import request

def byte_to_mb(b):
    return (b // 1024) // 1024

def get_info():
    p = pathlib.Path()

    virtual_memory = psutil.virtual_memory()
    memory = {
        'total_memory': byte_to_mb(virtual_memory.total),
        'available_memory': byte_to_mb(virtual_memory.available),
        'percent': virtual_memory.percent
    }

    info = {
        'current_path': str(p.cwd()),
        'platform_info': platform.platform(),
        'ip': socket.gethostbyname(socket.gethostname())
    }

    info.update(memory)

    return info

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test')
def publish():
    result = get_info()
    return flask.jsonify({ 'info': result })

if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")