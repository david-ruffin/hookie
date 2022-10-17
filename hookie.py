#!/usr/bin/python3
# This flask script will accept webhooks from github account, create a rult to protect the renamed 'default' branch, and send an @mention in a repo issue
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
    if webhook is None:
        print("POST was not fomatted in JSON")
    # Confirm repo was created and repo is public
    if webhook["action"] == "created" and webhook["repository"]["visibility"] == "public":
        # Set a delay because it could create a 404
        time.sleep(1)
        # Also confirm branch isnt empty by checking via REST GET request
        session = requests.session()
        session.auth = (user, cred)
        response_0 = session.get(webhook["repository"]["url"] + "/branches")
        # If list is empty, exit script
        if len(response_0.text) <= 2:
            print("Error: Repo is empty and you cant create a branch protection rule to an empty branch. There needs to be at least 1 file found.")
            print("Exiting...")
        else:
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
            # If branch protection rules was successfully added
            if response_1.status_code == 200:
                print(
                    "Branch protection created successfully. Status code: ",
                    response_1.status_code,
                )
                # Add notiification issue
                if webhook["repository"]["has_issues"]:
                    issue = {
                        "title": "New Protection Added",
                        "body": "@"
                        + user
                        + " A new branch protection was added to the default branch.",
                    }
                    session = requests.session()
                    session.auth = (user, cred)
                    response_2 = session.post(
                        webhook["repository"]["url"] + "/issues", json.dumps(issue)
                    )
                    if response_2.status_code == 201:
                        print(
                            "Issue created successfully. Status code: ",
                        response_2.status_code,
                        )
                    else:
                        print(
                            "Unable to create issue. Status code: ",
                        response_2.status_code,
                        )
                else:
                    print(
                        "This repo has no issues so one cannot be created at this time."
                    )
            else:
                print("Branch is not public")
    else:
        # Inform user that repo needs to be public when created
        print("Error: Repo needs to be public when it is created to create branch protection rule")
        print("Exiting...")
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
