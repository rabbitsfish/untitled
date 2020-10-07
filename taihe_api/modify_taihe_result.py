import mitmproxy.http
import mitmproxy.ctx
import json

class ModifyTaiheResult:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'dl-music.3gtest2.gionee.com/api/artist/hotList' in flow.request.url:
            mitmproxy.ctx.log.warn('~~~~~~~~~~~~~~')
            mitmproxy.ctx.log.warn(flow.response.text)
            with open('a.txt', 'a') as f:
                f.write(flow.response.text + '\n')

addons = [
    ModifyTaiheResult(),
]