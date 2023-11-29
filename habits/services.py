import os

import requests


def sending_notifications_to_telegram(habit):
    """Отправление уведомления пользователю о привычке в телеграм"""
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_API_TOKEN')}/sendMessage?chat_id={habit.user.chat_id}&text={habit}"
    requests.get(url).json()
