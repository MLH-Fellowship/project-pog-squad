#!/bin/bash

tmux kill-session -t portfolio
cd MLH-portfolio-site
git fetch && git reset origin/main --hard > /dev/null
source env/bin/activate
pip3 install flask > /dev/null
pip3 install python-dotenv > /dev/null
tmux new -d -s portfolio
tmux send -t portfolio "flask run --host=0.0.0.0" Enter
deactivate
cd ..