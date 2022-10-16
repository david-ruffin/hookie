#!/usr/bin/python3
from flask import Flask, request, jsonify
import json
import os
import time
import requests

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    user = "david-ruffin"
    cred = "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"
    webhook = request.json
    #print('<<<< WEBHOOK >>>>')
    #print('\r')
    #print(json.dumps(webhook))
    #print('\r')
    #print('<<<<   END   >>>>')
    #print('\r')
    #return jsonify('Thanks!')
    if webhook["action"] == "created":
        time.sleep(2)
        # Create branch protection for the master branch in the repo
        branch_protection = {
            "required_status_checks": {"strict": True, "contexts": ["default"]},
            "enforce_admins": False,
            "required_pull_request_reviews": None,
            "restrictions": None,
        }
        session = requests.session()
        session.auth = (user, cred)
        response_1 = session.put(
            webhook["repository"]["url"] + "/branches/default/protection",
            json.dumps(branch_protection),
        )
        if response_1.status_code == 200:
            print(
                "Branch protection created successfully. Status code: ",
                response_1.status_code,
            )

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
