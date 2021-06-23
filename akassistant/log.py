#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.config
import sys


class AKLogger:
    is_debug = False
    logging_config = {
        'version': 1.0,
        'formatters': {
            'generic': {
                'format': '%(asctime)s [%(levelname)s] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S]',
                'class': 'logging.Formatter',
            },
            'debug': {
                'format': '%(asctime)s [%(pathname)s:%(lineno)d] [%(funcName)s] [%(levelname)s] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S]',
                'class': 'logging.Formatter',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
                'stream': sys.stdout,
            },
        },
        'loggers': {
            'AKAssistant.root': {
                'handlers': ['console'],
                'level': 'INFO',
            },
        },
    }

    @staticmethod
    def init():
        logging.config.dictConfig(AKLogger.logging_config)

    @staticmethod
    def enable_debug():
        AKLogger.is_debug = True
        AKLogger.logging_config['handlers']['console']['formatter'] = 'debug'
        AKLogger.logging_config['loggers']['AKAssistant.root']['level'] = 'DEBUG'
        AKLogger.init()

    @staticmethod
    def enable_log_file(file_path: str):
        AKLogger.logging_config['handlers']['file'] = {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'debug' if AKLogger.is_debug else 'generic',
            'encoding': 'utf-8',
            'filename': file_path,
            'interval': 1,
            'backupCount': 30,
            'when': 'D',
        }
        AKLogger.logging_config['loggers']['AKAssistant.root']['handlers'].append('file')
        AKLogger.init()


AKLogger.init()
logger = logging.getLogger('AKAssistant.root')
