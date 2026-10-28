# tvbox-sources

TVBox 接口仓库：把 py 爬虫放进 `py/`，把站点写进 `config.json`，kus / TVShell 就能直接用。

## 仓库结构

```text
config.json        # 接口文件，壳子里填的就是这个文件的地址
py/
  example.py       # 示例 py 爬虫（静态演示数据，可直接跑通整条链路）
  README.md        # 写新 py 时照着这个模板改
```

## 在壳子里怎么用

接口地址（二选一，国内建议用 jsDelivr 那条）：

```text
https://cdn.jsdelivr.net/gh/xiaochwn/tvbox-sources@main/config.json
https://raw.githubusercontent.com/xiaochwn/tvbox-sources/main/config.json
```

- kus：设置里粘贴上面任一地址，回首页刷新。
- TVShell：接口管理里填同样的地址。

## 上传自己的 py

1. 在 GitHub 网页上进 `py/` 点 Add file → Upload files，上传你的 `.py` 文件（也可以直接在网页上新建文件粘贴源码）。
2. 在 `config.json` 的 `sites` 里加一项，`api` 写这个 py 的地址，例如：

```json
{
  "key": "my_site",
  "name": "我的源",
  "type": 3,
  "api": "https://cdn.jsdelivr.net/gh/xiaochwn/tvbox-sources@main/py/my_site.py",
  "searchable": 1,
  "quickSearch": 0,
  "changeable": 1,
  "ext": ""
}
```

`key` 不能和已有的重复；`api` 里的文件名要和你上传的文件名完全一致。

## 更新后怎么生效

改完 py 或 `config.json` 后不用重新打包 App，重启一下 App（或重新加载接口）就会拉新版。
注意 jsDelivr 有几分钟缓存，刚改完如果还是旧数据，等几分钟再试，或者临时改用 raw 地址验证。

## 注意事项

- 这个仓库是公开的：任何人拿到链接都能看到里面的文件，**不要把账号、密码、Cookie、Token 写进 py 或 config.json**。
- py 文件必须是 TVBox 格式：定义一个 `class Spider`，实现 `homeContent`、`homeVideoContent`、`categoryContent`、`detailContent`、`searchContent`、`playerContent`，返回字典；kus 里已内置 requests、lxml、beautifulsoup4、pyquery、pycryptodome。
