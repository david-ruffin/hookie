# This is for rhel8 image
# Red Hat Enterprise Linux release 8.6 (Ootpa)

subscription-manager remove --all
subscription-manager register --org=12345 --activationkey=RHEL
ln -s /usr/bin/python3 /usr/bin/python
yum -y install python3-pip
pip3 install flask
pip3 install pyngrok
ngrok authtoken 12345
systemctl stop firewalld
systemctl disable firewalld
