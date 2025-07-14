import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import jianshenjiaolianList from '../pages/jianshenjiaolian/list'
import jianshenjiaolianDetail from '../pages/jianshenjiaolian/detail'
import jianshenjiaolianAdd from '../pages/jianshenjiaolian/add'
import jiaolianyuyueList from '../pages/jiaolianyuyue/list'
import jiaolianyuyueDetail from '../pages/jiaolianyuyue/detail'
import jiaolianyuyueAdd from '../pages/jiaolianyuyue/add'
import jianshenkaList from '../pages/jianshenka/list'
import jianshenkaDetail from '../pages/jianshenka/detail'
import jianshenkaAdd from '../pages/jianshenka/add'
import chongzhixinxiList from '../pages/chongzhixinxi/list'
import chongzhixinxiDetail from '../pages/chongzhixinxi/detail'
import chongzhixinxiAdd from '../pages/chongzhixinxi/add'
import jianshenqicaiList from '../pages/jianshenqicai/list'
import jianshenqicaiDetail from '../pages/jianshenqicai/detail'
import jianshenqicaiAdd from '../pages/jianshenqicai/add'
import qicaijieyongList from '../pages/qicaijieyong/list'
import qicaijieyongDetail from '../pages/qicaijieyong/detail'
import qicaijieyongAdd from '../pages/qicaijieyong/add'
import qicaiguihaiList from '../pages/qicaiguihai/list'
import qicaiguihaiDetail from '../pages/qicaiguihai/detail'
import qicaiguihaiAdd from '../pages/qicaiguihai/add'
import qicaigoumaiList from '../pages/qicaigoumai/list'
import qicaigoumaiDetail from '../pages/qicaigoumai/detail'
import qicaigoumaiAdd from '../pages/qicaigoumai/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'jianshenjiaolian',
					component: jianshenjiaolianList
				},
				{
					path: 'jianshenjiaolianDetail',
					component: jianshenjiaolianDetail
				},
				{
					path: 'jianshenjiaolianAdd',
					component: jianshenjiaolianAdd
				},
				{
					path: 'jiaolianyuyue',
					component: jiaolianyuyueList
				},
				{
					path: 'jiaolianyuyueDetail',
					component: jiaolianyuyueDetail
				},
				{
					path: 'jiaolianyuyueAdd',
					component: jiaolianyuyueAdd
				},
				{
					path: 'jianshenka',
					component: jianshenkaList
				},
				{
					path: 'jianshenkaDetail',
					component: jianshenkaDetail
				},
				{
					path: 'jianshenkaAdd',
					component: jianshenkaAdd
				},
				{
					path: 'chongzhixinxi',
					component: chongzhixinxiList
				},
				{
					path: 'chongzhixinxiDetail',
					component: chongzhixinxiDetail
				},
				{
					path: 'chongzhixinxiAdd',
					component: chongzhixinxiAdd
				},
				{
					path: 'jianshenqicai',
					component: jianshenqicaiList
				},
				{
					path: 'jianshenqicaiDetail',
					component: jianshenqicaiDetail
				},
				{
					path: 'jianshenqicaiAdd',
					component: jianshenqicaiAdd
				},
				{
					path: 'qicaijieyong',
					component: qicaijieyongList
				},
				{
					path: 'qicaijieyongDetail',
					component: qicaijieyongDetail
				},
				{
					path: 'qicaijieyongAdd',
					component: qicaijieyongAdd
				},
				{
					path: 'qicaiguihai',
					component: qicaiguihaiList
				},
				{
					path: 'qicaiguihaiDetail',
					component: qicaiguihaiDetail
				},
				{
					path: 'qicaiguihaiAdd',
					component: qicaiguihaiAdd
				},
				{
					path: 'qicaigoumai',
					component: qicaigoumaiList
				},
				{
					path: 'qicaigoumaiDetail',
					component: qicaigoumaiDetail
				},
				{
					path: 'qicaigoumaiAdd',
					component: qicaigoumaiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
