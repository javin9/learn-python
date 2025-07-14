## sqlalchemy-demo

[官方文档](https://docs.sqlalchemy.org/en/14/core/type_basics.html)

```bash
docker run -d -p 3306:3306  --name my_mysql -v /Users/liujianwei/Documents/docker_data/flask_demo_mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql
```

￥ RFV5tgb

### 解决 mysqlclient 安装问题

https://github.com/PyMySQL/mysqlclient

```bash
$ # Assume you are activating Python 3 venv
$ brew install mysql-client pkg-config
$ export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"
$ pip install mysqlclient
```

链接数据库必须加驱动

```bash
mysql+cymysql://root:123456@localhost:3306/test_flask
```

### sqlalchemy

https://www.bilibili.com/video/BV1XM411f7M5/?spm_id_from=pageDriver&vd_source=27ad0c2e60f0082737adc9a8c17c2741

```bash

```
