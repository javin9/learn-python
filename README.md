## 常见问题

### pipenv 的常规使用

pipenv 的作用 https://blog.csdn.net/u013377887/article/details/109401030
用 pipenv 创建一个虚拟环境，这样就不会污染全局环境了，和项目绑定

````bash

## 初始化项目

### 2.5 创建虚拟目录

```bash
pipenv install #  安装虚拟环境
pipenv shell #激活虚拟环境
exit #退出虚拟环境
pipenv --venv #查看虚拟环境的路径
pipenv graph #查看依赖库
pipenv --rm #删除虚拟环境
pipenv install requests #安装requests库
pipenv install requests --dev #安装requests库，但是不会放到生产环境
````

如果 报 lock 失败，需要使用 sudo

```bash
sudo pipenv install
```
