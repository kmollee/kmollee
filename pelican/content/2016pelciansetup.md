Title: 2016 Pelcian setup
Category: Programming
Tags: pelican
Slug: 2016_pelican_setup
Authors: Lee

這邊紀錄一下有關於 pelcian 、 github gh-pages 及 disqus 串接

- [pelican](https://github.com/getpelican/pelican) : Pelican is a static site generator, written in Python.
- [github](https://github.com) : web-based Git repository hosting service
- [disqus](https://disqus.com)  pronounced "discuss", is a service and tool for web comments and discussions

目標 : 以 pelican 產生靜態網站, 並使用 github gh-pages 來當作 host service, 最後加入 disqus 評論系統

1. pelican 本身預設並沒有加入搜索功能，加入`tipue_search` plugin 即可
2. 假如已經在 github gh-pages 佈署, 可在該倉儲 `settings` 觀看使用建立成功, 相關設定 ref [GitHub Pages Basics/User, Organization, and Project Pages](https://help.github.com/articles/user-organization-and-project-pages/)
3. 假如需自訂 domain 請在 倉儲內加入 `CNAME` 檔案，內部請填入轉址 url, 當然還是需要你將自己的 domain dns 轉到相對應
4. disqus 服務要在 publishconf.py 設定
~~~python
DISQUS_SITENAME = ""
RELATIVE_URLS = False
~~~
