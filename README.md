# Hookie - GitHub solution with webshooks
<a href="https://opensource.org"><img height="150" align="right" src="https://opensource.org/files/OSIApprovedCropped.png" alt="Open Source Initiative Approved License logo"></a>

[![CodeFactor](https://www.codefactor.io/repository/github/zkoppert/auto-branch-protect/badge?s=c9ed51e74e4a59d7e3a0e766fe56b1237a53d1c4)](https://www.codefactor.io/repository/github/zkoppert/auto-branch-protect)  [![Total alerts](https://img.shields.io/lgtm/alerts/g/zkoppert/Auto-branch-protect.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zkoppert/Auto-branch-protect/alerts/)

Hookie is a simple web service that listens for organization events to know when a repo is created. When the repo is created, Hookie automates the protection of the main branch In addition, it notifies you with an @mention in an issue withing your repo that illustrates the protections that were added.

## Setup
- Configure Ngrok
  1. Create account at https://ngrok.com/
  2. Copy ONLY your ngrok token
  3. Add your ngrok token to `install.sh` file

- Run install script.sh
  1. Run the `install.sh` script on a RHEL 8 linux instance
  2. Copy the `Forwarding http` url (e.g., http://1234-123-123-123-123.ngrok.io)

- Add the following to the `hookie.py` script
  1. github username
  2. github token (only for testing)

- Configure webhooks in Github
  1. Create an organization secret if one does not exist already and assign it to relevant repositories.
  2. Navigate to repository `Settings` page.
  3. Navigate to `Webhooks`, under `Code, planning, and automation`.
  4. Click `Add webhook` button. (Confirm access/authorization by logging in, if prompted).
  5. Add the copied url (from the install script) and add it to the `Payload URL' field.
  5. Content type is `application/json`
  6. Under `Which events would you like to trigger this webhook?` select `Let me select individual events.` and select `Reposistories` and click `Update webhook`

## Running Application
- When creating a repo, make sure it is set to Public and add a readme file
- When the repo is created, it will create the `Branch protection rules` and add an @mention to the `Issue`.

## Related Documentation
- [GitHub APIv3](https://developer.github.com/v3/)
- [Web Hooks](https://developer.github.com/webhooks/)
- [API Status](https://www.githubstatus.com/)
- [Flask Docs](https://flask.palletsprojects.com/en/1.1.x/)
- [ngrok](https://ngrok.com/docs)

## Dependencies and Attribution
- Python3
- pip3
- Flask
- ngrok

## Notes and assumptions
- Github repo must be Public and a readme needs to be added. If not, error message will display what the issues are
- Disabled firewall for testing

## Bugs and improvements
- Payloads are capped at 25 MB. If your event generates a larger payload, a webhook will not be fired. This may happen, for example, on a create event if many branches or tags are pushed at once. We suggest monitoring your payload size to ensure delivery. See [webhooks docs](https://developer.github.com/webhooks/)
- There is a 1 second Delay built in to the code which is NOT ideal. It seems the code is checking for the main branch before it is finished creating.
- This could be done with AWS Lambda and an API Gateway.
