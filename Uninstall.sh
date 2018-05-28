#!/usr/bin/env bash

sudo rm -rf ./venv/

echo '___________________________________________________'
echo '|                    DROPPING UP DB               |'
echo '___________________________________________________'

echo 'ENTER MYSQL ROOT PASSWORD'
sudo mysql -u root -p < SetUp/DropDb.sql