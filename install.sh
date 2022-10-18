# Red Hat Enterprise Linux release 8.6 (Ootpa) image

# For rhel 8 based images
subscription-manager register --org=12345 --activationkey=RHEL

# Setup and install Python3, pip3, flask, and pyngrok on RHEL 8
ln -s /usr/bin/python3 /usr/bin/python
yum -y install python3-pip
pip3 install flask
pip3 install pyngrok

# Run ngrok
ngrok authtoken 12345

# Disable firewall for testing in dev
for i in stop disable; do systemctl $i firewalld; done

# Run ngrok
ngrok http 5000
