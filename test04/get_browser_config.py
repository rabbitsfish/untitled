import mitmproxy.http
import mitmproxy.ctx
import json
class GetBrowserConfig(object):
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if ''