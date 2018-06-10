# -*- coding: utf-8 -*-
 
import logging # Logging
import time # Time
import sys
 
 
# Logger in Datei und auf die Konsole
logger = logging.getLogger("Logfile")
logger.propagate = False
logger.setLevel(logging.DEBUG)
 
 
fileHandler = logging.FileHandler(logger.name + ".log", mode='w')
fileHandler_format = logging.Formatter('%(asctime)s_%(levelname)s: %(message)s', datefmt='%H:%M:%S')
fileHandler.setFormatter(fileHandler_format)
 
consoleHandler = logging.StreamHandler(sys.stdout)
 
consoleHandler.setFormatter(fileHandler_format)
 
# Remove existing loggers
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
 
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)
 
 
logger.info('Hello')
logger.warning('World')
logger.error('Foobar')
 
logging.shutdown()