from celery import shared_task

from habits.models import Habit
from habits.services import sending_notifications_to_telegram


@shared_task
def daily_send_message():
    habits = Habit.objects.filter(periodicity='daily')
    for habit in habits:
        chat_id = habit.user.chat_id
        sending_notifications_to_telegram(chat_id, habit)


@shared_task
def weekly_send_message():
    habits = Habit.objects.filter(periodicity='weekly')
    for habit in habits:
        chat_id = habit.user.chat_id
        sending_notifications_to_telegram(chat_id, habit)
