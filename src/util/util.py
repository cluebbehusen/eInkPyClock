from datetime import datetime
import os

eink_width = 400


def create_log_dir():
    if not os.path.exists('logs'):
        os.makedirs('logs')


def request_log(message):
    create_log_dir()
    with open('logs/requests.log', 'a') as log_file:
        log_file.write(str(datetime.now()) + message + '\n')


def general_log(message):
    create_log_dir()
    with open('logs/general.log', 'a') as log_file:
        log_file.write(str(datetime.now()) + message + '\n')
