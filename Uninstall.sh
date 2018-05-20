#!/usr/bin/env bash

sudo rm -rf venv/

echo 'ENTER MYSQL ROOT PASSWORD'
cd SetUp
mysql -u root -p < DropDb.sql
cd ..