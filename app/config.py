import logging
import os


APP_NAME = os.getenv('APP_NAME')
DEBUG = os.getenv('ENVIRONEMENT') == 'DEV'
APPLICATION_ROOT = os.getenv('APPLICATION_APPLICATION_ROOT', '/application')
HOST = os.getenv('APPLICATION_HOST')
PORT = int(os.getenv('APPLICATION_PORT', '3000'))

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)