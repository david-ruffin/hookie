#!/usr/bin/python3
from flask import Flask, request, jsonify
import json
import os
import time

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    webhook = request.json
    print('<<<< WEBHOOK >>>>')
    print('\r')
    print(json.dumps(webhook))
    print('\r')
    print('<<<<   END   >>>>')
    print('\r')
    return jsonify('Thanks!')
    if webhook["action"] == "created":
        time.sleep(1)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
