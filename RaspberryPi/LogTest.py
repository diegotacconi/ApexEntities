import logging

# https://docs.python.org/3/library/logging.html#logging.basicConfig
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s.%(msecs)03d | %(levelname)-8s | %(message)s',
    handlers=[
        logging.FileHandler("/var/tmp/apex.log", mode='w'),
        logging.StreamHandler()
    ]
)

# https://docs.python.org/3/howto/logging.html
logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
