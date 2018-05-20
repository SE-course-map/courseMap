#!/bin/bash

echo '___________________________________________________'
echo '|          SETTING UP VIRTUAL ENVIRONMENT         |'
echo '___________________________________________________'

sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo virtualenv venv
sudo chmod -R 777 venv/


echo '___________________________________________________'
echo '|                INSTALLING PACKAGES              |'
echo '___________________________________________________'

sudo apt-get install python-dev libmysqlclient-dev
./venv/bin/pip install -r requirenments.txt


echo '___________________________________________________'
echo '|                    SETTING UP DB                |'
echo '___________________________________________________'

echo 'ENTER MYSQL ROOT PASSWORD'
sudo mysql -u root -p < SetUp/SetUpDb.sql
sudo mysql -u courseMapUser -p1Qwert123asd., < SetUp/SetUpUsers.sql

cd SetUp
../venv/bin/python3 addFirstUser.py
cd ..

