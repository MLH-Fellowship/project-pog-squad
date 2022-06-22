#!/bin/bash

tmux kill-server
cd /root/project-pog-squad
git fetch && git reset origin/main --hard > /dev/null
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
tmux new -d -s portfolio
tmux send -t portfolio "flask run --host=0.0.0.0" Enter
