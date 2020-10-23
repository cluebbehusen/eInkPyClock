import os


def create_log_dir():
    if not os.path.exists('logs'):
        os.makedirs('logs')


def request_log(message):
    create_log_dir()
    with open('logs/requests.log', 'a') as log_file:
        log_file.write(message + '\n')


def general_log(message):
    create_log_dir()
    with open('logs/general.log', 'a') as log_file:
        log_file.write(message + '\n')
