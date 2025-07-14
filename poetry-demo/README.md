## 笔记

官网地址：https://python-poetry.org/docs/cli/#config

```bash
poetry init
# 创建虚拟环境 用当前的python版本
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

### 创建项目的流程

```bash
poetry init


# 创建虚拟环境 用当前的python版本
poetry env use python
# 查看虚拟环境
poetry env info
#这个命令会激活当前项目的虚拟环境。你需要在项目的根目录（包含 pyproject.toml 文件的目录）下运行它。激活后，你的终端会切换到该虚拟环境。
poetry env activate
# 安装一个模块
poetry add requests
poetry add black --group dev
# 清除缓存
poetry cache clear --all
```

/Users/liujianwei/.pyenv/shims:/Users/liujianwei/go/protoc-28.3-osx-x86_64/bin:/Users/liujianwei/Downloads/command-line-tools/ohpm/bin:/Users/liujianwei/Library/pnpm:/Users/liujianwei/go/bin:/Users/liujianwei/go/protoc-28.3-osx-x86_64/bin:/Users/liujianwei/Downloads/command-line-tools/ohpm/bin:/Users/liujianwei/Library/pnpm:/Users/liujianwei/go/bin:/Users/liujianwei/go/protoc-28.3-osx-x86_64/bin:/Users/liujianwei/Downloads/command-line-tools/ohpm/bin:/Users/liujianwei/Library/pnpm:/Users/liujianwei/go/bin:/Users/liujianwei/.nvm/versions/node/v18.18.2/bin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/usr/local/sbin:/Applications/Yunshu.app/Contents/Public:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin:/Library/Apple/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Applications/iTerm.app/Contents/Resources/utilities:/Users/liujianwei/.local/bin:/Users/liujianwei/.local/bin:/Users/liujianwei/.local/bin:/Users/liujianwei/.local/bin
