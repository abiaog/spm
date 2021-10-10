#!/bin/python3

import datetime
import logging

logger = logging.getLogger('Auto')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('run.log')
fh.setLevel(logging.DEBUG) 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


logger.debug('debug message')

