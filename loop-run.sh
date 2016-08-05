#!/bin/sh

while true
do
  python ./soccer.py 1>> LOG 2>&1
  sleep 30s
done
