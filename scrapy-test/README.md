### 安装

```bash
pipenv install scrapy
pipenv shell

```

### scrapy 命令

```bash
scrapy startproject project_name
scrapy genspider spider_name domain
scrapy genspider [options] <name> <domain>
# 必须在项目目录下运行
cd /scrapy-test/tutorial$ scrapy crawl quotes

```

如果要使用 pipeline，需要在 settings.py 中配置

```text
ITEM_PIPELINES = {
    "tutorial.pipelines.TutorialPipeline": 300,
}
```

```bash
docker run -d -p 3306:3306 \
--name scrapy_mongo  \n
-v /Users/liujianwei/Documents/docker_data/scrapy_mongo:/data/db \n
-e MYSQL_ROOT_PASSWORD=123456 \n
mongo
# docker run --name some-mongo -v /my/own/datadir:/data/db -d mongo
# docker run -d -p 27017:27017 --name scrapy_mongo -v /Users/liujianwei/Documents/docker_data/scrapy_mongo:/data/db  -e MYSQL_ROOT_PASSWORD=123456 mongo
# 96f59a5c372e6e8b2f90c7831822e87627e9622b8544bffdebcde9fc071c4a61
# docker run -d -p 27017:27017 --name scrapy_mongo -v /Users/liujianwei/Documents/docker_data/scrapy_mongo:/data/db  mongo
```

### 动态请求头

middlewares.py

```python
# MyUserAgentMiddleware
```

settings.py

```python
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.MyUserAgentMiddleware': 543,  # 编号越小，优先级越高
}
```
