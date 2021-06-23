#!/usr/bin/python
# -*- coding: utf-8 -*-

import gettext
import os
from mitmproxy import proxy, options
from mitmproxy.master import Master
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import core

from akassistant.core import AKAssistant

if __name__ == '__main__':
    lang = gettext.translation('AKAssistant', localedir='i18n', languages=['zh-CN'])
    lang.install()
    opts = options.Options(
        listen_host='127.0.0.1',
        listen_port=8091,
        confdir=os.path.join(os.getcwd(), "conf")
    )
    opts.add_option("body_size_limit", int, 0, "")
    opts.add_option("keep_host_header", bool, True, "")
    pconf = proxy.config.ProxyConfig(opts)
    # m = DumpMaster(None)
    m = Master(None)
    m.server = proxy.server.ProxyServer(pconf)
    m.addons.add(AKAssistant())
    try:
        m.run()
    except KeyboardInterrupt:
        m.shutdown()
