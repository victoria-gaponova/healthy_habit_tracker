#!/bin/bash

sleep 15

celery -A healthy_habit_tracker beat -l INFO -S django