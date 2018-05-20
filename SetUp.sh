#!/usr/bin/env bash

echo '___________________________________________________'
echo '|          SETTING UP VIRTUAL ENVIRONMENT         |'
echo '___________________________________________________'

sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo virtualenv venv
sudo source venv/bin/activate


echo '___________________________________________________'
echo '|                INSTALLING PACKAGES              |'
echo '___________________________________________________'

sudo apt-get install python-dev libmysqlclient-dev
sudo pip3 install -r requirenments.txt


echo '___________________________________________________'
echo '|                    SETTING UP DB                |'
echo '___________________________________________________'

echo 'ENTER MYSQL ROOT PASSWORD'
sudo mysql -u root -p < SetUp/SetUpDb.sql
sudo mysql -u courseMapUser -p1111 < SetUp/SetUpUsers.sql

cd SetUp
sudo python3 addFirstUser.py
cd ..

