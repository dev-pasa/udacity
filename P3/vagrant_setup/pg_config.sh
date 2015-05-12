apt-get -qqy update
apt-get -qqy install python-pip
pip install flask==0.9
pip install sqlalchemy
pip install requests
pip install oauth2client

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd

