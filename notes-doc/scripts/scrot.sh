#!/bin/bash
scrot -so /home/chrome/.img/temp.png
xclip -selection clipboard -t image/png /home/chrome/.img/temp.png

