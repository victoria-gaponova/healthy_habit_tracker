FROM python:3.11

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYCODE 1

RUN mkdir healthy_habit_tracker

WORKDIR healthy_habit_tracker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh