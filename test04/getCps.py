import mitmproxy.http
import mitmproxy.ctx
import os
import chardet
class GetCps:
    def __init__(self):
        filename = 'a.txt'
        if os.path.exists(filename):
            os.remove(filename)

    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     if flow.request.url.startswith('http://zhuoyan-3g.gionee.com'):
    #         return
    #     if flow.request.url.startswith('https://osapi-3g.gionee.com'):
    #         return
    #     if flow.request.url.startswith('http://update.gionee.com'):
    #         return
    #     if flow.request.url.startswith('https://3g.gionee.com'):
    #         return
    #     with open('a.txt', 'a') as f:
    #         f.write(flow.request.url + '\n')
    #         f.flush()

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.url.startswith('http://zhuoyan-3g.gionee.com'):
            return
        if flow.request.url.startswith('https://osapi-3g.gionee.com'):
            return
        if flow.request.url.startswith('http://update.gionee.com'):
            return
        if flow.request.url.startswith('https://3g.gionee.com'):
            return
        with open('a.txt', 'a') as f:
            f.write(flow.request.url + '\n')
            result = flow.response.raw_content
            if chardet.detect(result)['encoding'] and chardet.detect(result)['encoding'] != 'utf-8':
                result = flow.response.content.decode(chardet.detect(result)['encoding'])
                mitmproxy.ctx.log.warn('++++')
                mitmproxy.ctx.log.warn(str(result))
            else:
                mitmproxy.ctx.log.warn('~~~~~~~~~~~~~~~~~~')
                mitmproxy.ctx.log.warn(str(result))

            #f.write(flow.response.text + '\n')
            # try:
            #     result = flow.response.content
            #     chardet.detect(result)
            #     # mitmproxy.ctx.log.warn(result)
            #     f.write(result + '\n')
            # except UnicodeEncodeError as e:
            #     mitmproxy.ctx.log.warn(chardet.detect(result)['encoding'])
            #     mitmproxy.ctx.log.warn(result)
            #     # f.write(result.decode('gbk', 'ignore').encode('utf-8') + '\n')
            f.flush()


addons = [
    GetCps(),
]
