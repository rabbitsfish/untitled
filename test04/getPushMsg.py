import mitmproxy.http
import mitmproxy.ctx
import json
class GetPushMsg:
    '''修改push中id为0这一条的状态'''
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'm/api/push/get/msg' in flow.request.url:
            # mitmproxy.ctx.log.warn(flow.response.text)
            result = json.loads(flow.response.text)
            # result = '{"msg":"success","data":{"list":[{"id":12,"mt":"大图样式","st":"","nt":"BIG_IMG","p":"http://imgcdn.lkyxzb.com/2020/08-07/5c6bb35a6a66907f7ddc4b8ff7f933a2.png","jt":"H5","jd":"https://www.taptap.com","ext":"","es":1596874880106,"de":54000000,"sd":"1596813941000","ed":"1597937141000","is":true,"im":true,"en":true,"mob":true,"si":true,"ap":0},{"id":9,"mt":"音乐唤醒","st":"未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始未开始","nt":"BIG_IMG","p":"http://imgcdn.lkyxzb.com/2020/08-07/d06580f665784db3d62c9452f521efc4.png","jt":"DEEPLINK","jd":"banqumusic://com.meizu.media.music","ext":"","es":1596874880106,"de":54000000,"sd":"1596882792000","ed":"1596969240000","is":true,"im":true,"en":true,"mob":true,"si":true,"ap":0},{"id":6,"mt":"下载","st":"资讯2sub","nt":"SMALL_IMG","p":"http://imgcdn.lkyxzb.com/2020/07-10/2a4b91337db66ade978e5b79e6df4a1d.jpg","jt":"DOWNLOAD","jd":"https://d.taptap.com/latest","ext":"","es":1596907280106,"de":57600000,"sd":"1569945600000","ed":"1603814400000","is":true,"im":false,"en":true,"mob":false,"si":false,"ap":100},{"id":0,"mt":"","st":"","nt":"TXT","p":"","jt":"H5","jd":"","ext":"auto","es":1596907280106,"de":54000000,"sd":"1596871280106","ed":"1599549680106","is":false,"im":false,"en":true,"mob":false,"si":false,"ap":0}]},"code":0,"success":true}'
            li = result['data']['list']
            if len(li):
                for i in range(len(li)):
                    if li[i]['id'] == 0:
                        li[i]['en'] = False
                        break
            flow.response.set_text(json.dumps(result))
            mitmproxy.ctx.log.warn('~~~~~~~~~~~~~~~~~~~~~~~~')
            mitmproxy.ctx.log.warn(flow.response.text)

addons = [
    GetPushMsg()
]