const menu = {
  list() {
    return [
      {
        backMenu: [
          {
            child: [
              {
                appFrontIcon: 'cuIcon-newshot',
                buttons: ['新增', '查看', '修改', '删除'],
                menu: '用户',
                menuJump: '列表',
                tableName: 'yonghu',
              },
            ],
            menu: '用户管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-form',
                buttons: ['新增', '查看', '修改', '删除', '查看评论'],
                menu: '健身教练',
                menuJump: '列表',
                tableName: 'jianshenjiaolian',
              },
            ],
            menu: '健身教练管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-keyboard',
                buttons: ['查看', '修改', '删除', '审核'],
                menu: '教练预约',
                menuJump: '列表',
                tableName: 'jiaolianyuyue',
              },
            ],
            menu: '教练预约管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-news',
                buttons: ['新增', '查看', '修改', '删除'],
                menu: '健身卡',
                menuJump: '列表',
                tableName: 'jianshenka',
              },
            ],
            menu: '健身卡管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-phone',
                buttons: ['查看', '修改', '删除'],
                menu: '充值信息',
                menuJump: '列表',
                tableName: 'chongzhixinxi',
              },
            ],
            menu: '充值信息管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-similar',
                buttons: ['新增', '查看', '修改', '删除'],
                menu: '健身器材',
                menuJump: '列表',
                tableName: 'jianshenqicai',
              },
            ],
            menu: '健身器材管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-explore',
                buttons: ['查看', '修改', '删除', '审核'],
                menu: '器材借用',
                menuJump: '列表',
                tableName: 'qicaijieyong',
              },
            ],
            menu: '器材借用管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-qrcode',
                buttons: ['查看', '修改', '删除'],
                menu: '器材归还',
                menuJump: '列表',
                tableName: 'qicaiguihai',
              },
            ],
            menu: '器材归还管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-list',
                buttons: ['查看', '修改', '删除'],
                menu: '器材购买',
                menuJump: '列表',
                tableName: 'qicaigoumai',
              },
            ],
            menu: '器材购买管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-link',
                buttons: ['新增', '查看', '修改', '删除'],
                menu: '轮播图管理',
                tableName: 'config',
              },
              {
                appFrontIcon: 'cuIcon-cardboard',
                buttons: ['新增', '查看', '修改', '删除'],
                menu: '新闻资讯',
                tableName: 'news',
              },
            ],
            menu: '系统管理',
          },
        ],
        frontMenu: [
          {
            child: [
              {
                appFrontIcon: 'cuIcon-news',
                buttons: ['查看', '私教预约'],
                menu: '健身教练列表',
                menuJump: '列表',
                tableName: 'jianshenjiaolian',
              },
            ],
            menu: '健身教练模块',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-discover',
                buttons: ['查看', '借用', '购买'],
                menu: '健身器材列表',
                menuJump: '列表',
                tableName: 'jianshenqicai',
              },
            ],
            menu: '健身器材模块',
          },
        ],
        hasBackLogin: '是',
        hasBackRegister: '否',
        hasFrontLogin: '否',
        hasFrontRegister: '否',
        roleName: '管理员',
        tableName: 'users',
      },
      {
        backMenu: [
          {
            child: [
              {
                appFrontIcon: 'cuIcon-keyboard',
                buttons: ['查看'],
                menu: '教练预约',
                menuJump: '列表',
                tableName: 'jiaolianyuyue',
              },
            ],
            menu: '教练预约管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-news',
                buttons: ['查看', '充值'],
                menu: '健身卡',
                menuJump: '列表',
                tableName: 'jianshenka',
              },
            ],
            menu: '健身卡管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-phone',
                buttons: ['查看', '支付'],
                menu: '充值信息',
                menuJump: '列表',
                tableName: 'chongzhixinxi',
              },
            ],
            menu: '充值信息管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-explore',
                buttons: ['查看', '归还'],
                menu: '器材借用',
                menuJump: '列表',
                tableName: 'qicaijieyong',
              },
            ],
            menu: '器材借用管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-qrcode',
                buttons: ['查看'],
                menu: '器材归还',
                menuJump: '列表',
                tableName: 'qicaiguihai',
              },
            ],
            menu: '器材归还管理',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-list',
                buttons: ['查看', '支付'],
                menu: '器材购买',
                menuJump: '列表',
                tableName: 'qicaigoumai',
              },
            ],
            menu: '器材购买管理',
          },
        ],
        frontMenu: [
          {
            child: [
              {
                appFrontIcon: 'cuIcon-news',
                buttons: ['查看', '私教预约'],
                menu: '健身教练列表',
                menuJump: '列表',
                tableName: 'jianshenjiaolian',
              },
            ],
            menu: '健身教练模块',
          },
          {
            child: [
              {
                appFrontIcon: 'cuIcon-discover',
                buttons: ['查看', '借用', '购买'],
                menu: '健身器材列表',
                menuJump: '列表',
                tableName: 'jianshenqicai',
              },
            ],
            menu: '健身器材模块',
          },
        ],
        hasBackLogin: '是',
        hasBackRegister: '否',
        hasFrontLogin: '是',
        hasFrontRegister: '是',
        roleName: '用户',
        tableName: 'yonghu',
      },
    ];
  },
};
export default menu;
