#!bin/bash

sleep 15

celery -A healthy_habit_tracker worker -l INFO -S django