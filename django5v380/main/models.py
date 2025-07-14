#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    touxiang=VARCHAR
    xingbie=VARCHAR
    shoujihaoma=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class jianshenjiaolian(BaseModel):
    __doc__ = u'''jianshenjiaolian'''
    __tablename__ = 'jianshenjiaolian'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaolianxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教练姓名' )
    zhaopian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='照片' )
    xingbie=models.CharField ( max_length=255,null=False, unique=False, verbose_name='性别' )
    sijiaojiage=models.IntegerField  ( null=False, unique=False, verbose_name='价格/节课' )
    shangbanshijian=models.CharField ( max_length=255,null=False, unique=False, verbose_name='上班时间' )
    nianling=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年龄' )
    shengao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身高' )
    tizhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='体重' )
    gerenjianjie=models.TextField   (  null=True, unique=False, verbose_name='个人简介' )
    '''
    jiaolianxingming=VARCHAR
    zhaopian=VARCHAR
    xingbie=VARCHAR
    sijiaojiage=Integer
    shangbanshijian=VARCHAR
    nianling=VARCHAR
    shengao=VARCHAR
    tizhong=VARCHAR
    gerenjianjie=Text
    '''
    class Meta:
        db_table = 'jianshenjiaolian'
        verbose_name = verbose_name_plural = '健身教练'
class jiaolianyuyue(BaseModel):
    __doc__ = u'''jiaolianyuyue'''
    __tablename__ = 'jiaolianyuyue'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yuyuebianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='预约编号' )
    jiaolianxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教练姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    sijiaojiage=models.IntegerField  (  null=True, unique=False, verbose_name='私教价格' )
    yuyueshijian=models.DateTimeField  ( null=False, unique=False, verbose_name='预约时间' )
    jianshenkabianhao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='健身卡编号' )
    jianshenkamingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='健身卡名称' )
    jine=models.FloatField   (  null=True, unique=False, verbose_name='金额' )
    yue=models.FloatField   (  null=True, unique=False, verbose_name='余额' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    yuyuebianhao=VARCHAR
    jiaolianxingming=VARCHAR
    xingbie=VARCHAR
    sijiaojiage=Integer
    yuyueshijian=DateTime
    jianshenkabianhao=VARCHAR
    jianshenkamingcheng=VARCHAR
    jine=Float
    yue=Float
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    beizhu=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'jiaolianyuyue'
        verbose_name = verbose_name_plural = '教练预约'
class jianshenka(BaseModel):
    __doc__ = u'''jianshenka'''
    __tablename__ = 'jianshenka'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jianshenkabianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='健身卡编号' )
    jianshenkamingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='健身卡名称' )
    jine=models.IntegerField  (  null=True, unique=False, verbose_name='金额' )
    kaikariqi=models.DateField   (  null=True, unique=False, verbose_name='开卡日期' )
    yonghuzhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    '''
    jianshenkabianhao=VARCHAR
    jianshenkamingcheng=VARCHAR
    jine=Integer
    kaikariqi=Date
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihaoma=VARCHAR
    '''
    class Meta:
        db_table = 'jianshenka'
        verbose_name = verbose_name_plural = '健身卡'
class chongzhixinxi(BaseModel):
    __doc__ = u'''chongzhixinxi'''
    __tablename__ = 'chongzhixinxi'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    jianshenkabianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='健身卡编号' )
    jianshenkamingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='健身卡名称' )
    jine=models.FloatField   ( null=False, unique=False, verbose_name='金额' )
    chongzhishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='充值时间' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihaoma=VARCHAR
    jianshenkabianhao=VARCHAR
    jianshenkamingcheng=VARCHAR
    jine=Float
    chongzhishijian=DateTime
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'chongzhixinxi'
        verbose_name = verbose_name_plural = '充值信息'
class jianshenqicai(BaseModel):
    __doc__ = u'''jianshenqicai'''
    __tablename__ = 'jianshenqicai'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qicaimingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='器材名称' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    jiage=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    shuliang=models.IntegerField  ( null=False, unique=False, verbose_name='数量' )
    shiyongfangfa=models.TextField   (  null=True, unique=False, verbose_name='使用方法' )
    shoushenxiaoguo=models.TextField   (  null=True, unique=False, verbose_name='瘦身效果' )
    qicaijieshao=models.TextField   (  null=True, unique=False, verbose_name='器材介绍' )
    '''
    qicaimingcheng=VARCHAR
    tupian=VARCHAR
    pinpai=VARCHAR
    jiage=Float
    shuliang=Integer
    shiyongfangfa=Text
    shoushenxiaoguo=Text
    qicaijieshao=Text
    '''
    class Meta:
        db_table = 'jianshenqicai'
        verbose_name = verbose_name_plural = '健身器材'
class qicaijieyong(BaseModel):
    __doc__ = u'''qicaijieyong'''
    __tablename__ = 'qicaijieyong'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jieyongbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='借用编号' )
    qicaimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='器材名称' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    shuliang=models.IntegerField  ( null=False, unique=False, verbose_name='数量' )
    jieyongshijian=models.DateTimeField  ( null=False, unique=False, verbose_name='借用时间' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    jieyongbianhao=VARCHAR
    qicaimingcheng=VARCHAR
    pinpai=VARCHAR
    shuliang=Integer
    jieyongshijian=DateTime
    beizhu=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qicaijieyong'
        verbose_name = verbose_name_plural = '器材借用'
class qicaiguihai(BaseModel):
    __doc__ = u'''qicaiguihai'''
    __tablename__ = 'qicaiguihai'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jieyongbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='借用编号' )
    qicaimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='器材名称' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    shuliang=models.CharField ( max_length=255,null=False, unique=False, verbose_name='数量' )
    guihaishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='归还时间' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    '''
    jieyongbianhao=VARCHAR
    qicaimingcheng=VARCHAR
    pinpai=VARCHAR
    shuliang=VARCHAR
    guihaishijian=DateTime
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihaoma=VARCHAR
    crossuserid=BigInteger
    crossrefid=BigInteger
    '''
    class Meta:
        db_table = 'qicaiguihai'
        verbose_name = verbose_name_plural = '器材归还'
class qicaigoumai(BaseModel):
    __doc__ = u'''qicaigoumai'''
    __tablename__ = 'qicaigoumai'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    goumaibianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='购买编号' )
    qicaimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='器材名称' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    shuliang=models.IntegerField  ( null=False, unique=False, verbose_name='数量' )
    zongji=models.FloatField   (  null=True, unique=False, verbose_name='总计' )
    goumaishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='购买时间' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    goumaibianhao=VARCHAR
    qicaimingcheng=VARCHAR
    pinpai=VARCHAR
    jiage=Float
    shuliang=Integer
    zongji=Float
    goumaishijian=DateTime
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihaoma=VARCHAR
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'qicaigoumai'
        verbose_name = verbose_name_plural = '器材购买'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '新闻资讯'
class discussjianshenjiaolian(BaseModel):
    __doc__ = u'''discussjianshenjiaolian'''
    __tablename__ = 'discussjianshenjiaolian'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=VARCHAR
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussjianshenjiaolian'
        verbose_name = verbose_name_plural = '健身教练评论表'
