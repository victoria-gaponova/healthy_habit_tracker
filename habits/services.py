import os

import telebot

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')


def sending_notifications_to_telegram(chat_id, habit):
    """Отправление уведомления пользователю о привычке в телеграм"""
    bot = telebot.TeleBot(TELEGRAM_API_TOKEN, parse_mode=None)
    bot.send_message(chat_id,
                     text=f'Пришло время привычки : {habit.action}.'
                          f'Привычку необходимо выполнять в {habit.place} в {habit.time}')
