#!/bin/bash

virtualenv -p python3 bot
source bot/bin/activate
pip install -r requirements.txt
