"""示例 py 爬虫：静态演示数据，不依赖任何外部站点。

直接说明 TVBox py 爬虫的最小契约：
- 文件里必须有一个 class Spider；
- 每个方法返回字典，壳子会把字典转成 JSON；
- detailContent 里 vod_play_from / vod_play_url 的格式是：
  来源之间用 $$$ 分隔，同一来源的选集之间用 # 分隔，
  每集是 "集名$播放地址"。

把这个文件复制一份，换掉 VIDEOS 里的取数逻辑（改成 requests 抓
目标站并解析），就是一个能用的新源。
"""

VIDEOS = [
    {
        "id": "bunny",
        "name": "Big Buck Bunny（演示）",
        "pic": "https://picsum.photos/seed/bunny/300/450",
        "remarks": "动画 · 演示",
        "desc": "Blender 基金会开放电影片段，仅用于验证加载、分类、详情、播放链路。",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
    },
    {
        "id": "sintel",
        "name": "Sintel 预告（演示）",
        "pic": "https://picsum.photos/seed/sintel/300/450",
        "remarks": "奇幻 · 演示",
        "desc": "Blender 基金会开放电影 Sintel 官方预告，仅用于验证链路。",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
    },
    {
        "id": "tears",
        "name": "Tears of Steel（演示）",
        "pic": "https://picsum.photos/seed/tears/300/450",
        "remarks": "科幻 · 演示",
        "desc": "Blender 基金会开放电影片段，仅用于验证链路。",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
    },
]


def _vod(v):
    return {
        "vod_id": v["id"],
        "vod_name": v["name"],
        "vod_pic": v["pic"],
        "vod_remarks": v["remarks"],
    }


class Spider:
    def init(self, extend=""):
        pass

    def homeContent(self, filter):
        return {"class": [{"type_id": "all", "type_name": "全部"}]}

    def homeVideoContent(self):
        return {"list": [_vod(v) for v in VIDEOS]}

    def categoryContent(self, tid, pg, filter, extend):
        pg = max(1, int(pg or 1))
        per_page = 20
        items = VIDEOS[(pg - 1) * per_page:pg * per_page]
        total = len(VIDEOS)
        return {
            "list": [_vod(v) for v in items],
            "page": pg,
            "pagecount": (total + per_page - 1) // per_page,
            "limit": per_page,
            "total": total,
        }

    def detailContent(self, ids):
        vid = ids[0] if ids else ""
        v = next((x for x in VIDEOS if x["id"] == vid), VIDEOS[0])
        return {
            "list": [{
                "vod_id": v["id"],
                "vod_name": v["name"],
                "vod_pic": v["pic"],
                "vod_remarks": v["remarks"],
                "vod_content": v["desc"],
                "vod_play_from": "正片",
                "vod_play_url": "正片$" + v["url"],
            }]
        }

    def searchContent(self, key, quick, pg="1"):
        key = (key or "").lower()
        found = [v for v in VIDEOS if key in v["name"].lower() or key in v["id"]]
        return {"list": [_vod(v) for v in found]}

    def playerContent(self, flag, id, vipFlags):
        # 详情里已经给了直链，这里直接原样返回，parse=0 表示不用二次解析。
        return {"parse": 0, "url": id}

    def liveContent(self, url):
        return {}

    def localProxy(self, params):
        return [404, "text/plain", b""]

    def isVideoFormat(self, url):
        return True

    def manualVideoCheck(self):
        return False
