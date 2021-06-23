#!/usr/bin/python
# -*- coding: utf-8 -*-

from types import FunctionType
from mitmproxy import http

from akassistant.log import logger

_: FunctionType

class AKAssistant:
    def __init__(self):
        self.__version = '0.0.1'
        startup_msg = [
            _("Starting Arknights Assistant"),
            _("*****************************************"),
            _(" * Arknights Assistant"),
            _(" * Created By @LightningRS <me@ldby.site>"),
            _(" * Version: {}").format(self.__version),
            _("*****************************************"),
        ]
        logger.info('\n'.join(startup_msg))

    def request(self, flow: http.HTTPFlow):
        logger.info(flow.request.url)
