#!/bin/bash
 
NAME="ram"
FLASKDIR=/home/ubuntu/skripsi
USER=root
GROUP=root
NUM_WORKERS=3
 
echo "Starting $NAME"
 
# Start your gunicorn
exec gunicorn ram:app -b 0.0.0.0:8080 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \