# 写一个新 py 爬虫

把 `example.py` 复制一份改名（例如 `my_site.py`），只改取数部分：

1. `homeContent`：返回分类，格式 `{"class": [{"type_id": "xxx", "type_name": "分类名"}]}`。
2. `homeVideoContent` / `categoryContent`：返回 `{"list": [vod, ...]}`，每个 vod 至少有 `vod_id`、`vod_name`、`vod_pic`、`vod_remarks`；分类还要带 `page`、`pagecount`、`limit`、`total`。
3. `detailContent`：返回 `{"list": [vod]}`，vod 里加 `vod_play_from` 和 `vod_play_url`；来源之间用 `$$$` 分隔，同一来源的选集之间用 `#` 分隔，每集写成 `集名$播放地址`。
4. `searchContent`：按关键字过滤后返回同样的 `{"list": [...]}`。
5. `playerContent`：返回 `{"parse": 0, "url": "直链"}`；需要解析接口二次解析时返回 `{"parse": 1, "url": "待解析地址"}`。

kus 里可以直接用的库：标准库、requests、lxml、beautifulsoup4、pyquery、pycryptodome。别的第三方库先别 import，会加载失败。

写完后在 `config.json` 的 `sites` 里加一项，`api` 写这个文件的 jsDelivr 地址，`key` 不要和已有的重复。
