#!/bin/sh
XDG_SESSION_TYPE=x11
nitrogen --restore &
picom &
flameshot &
unclutter --timeout 2 &
volti &
