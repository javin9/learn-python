## 笔记

官网地址：https://python-poetry.org/docs/cli/#config

```bash
poetry init
poetry env use python
# 查看配置
poetry config --list
# cache-dir = "/Users/liujianwei/Library/Caches/pypoetry"
# experimental.system-git-client = false
# installer.max-workers = null
# installer.modern-installation = true
# installer.no-binary = null
# installer.parallel = true
# keyring.enabled = true
# solver.lazy-wheel = true
# virtualenvs.create = true
##  需要更改，改成放到项目目录下
# virtualenvs.in-project = null
# virtualenvs.options.always-copy = false
# virtualenvs.options.no-pip = false
# virtualenvs.options.no-setuptools = false
# virtualenvs.options.system-site-packages = false
# virtualenvs.path = "{cache-dir}/virtualenvs"  # /Users/liujianwei/Library/Caches/pypoetry/virtualenvs
# virtualenvs.prefer-active-python = false
# virtualenvs.prompt = "{project_name}-py{python_version}"
# warnings.export = true

poetry config virtualenvs.in-project true

# 删除虚拟环境
poetry env remove python

# 进入虚拟环境
poetry shell

# 展示依赖
poetry show --tree
poetry show requests --tree
# 安装依赖
poetry add requests fastapi

# 删除依赖
poetry remove requests

# 更新
poetry update requests

# 退出虚拟环境
exit

# 代码格式
poetry add black --group dev

# 导出requirements
poetry export -f requirements.txt -o requirements.txt --without-hashes

#
poetry install

# 运行
poetry run python  \ main.py
```
