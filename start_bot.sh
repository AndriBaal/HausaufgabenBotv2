#!/bin/bash
cd /home/ubuntu/hausaufgaben_v2
tmux new-session -d -s bot \; send-keys "python3 /home/ubuntu/hausaufgaben_v2/main.py" Enter
tmux attach-session -t bot