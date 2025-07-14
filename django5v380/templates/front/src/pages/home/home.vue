<template>
<div class="home-preview" :style='{"width":"100%","margin":"20px 0 0","flexWrap":"wrap","justifyContent":"center","display":"flex"}'>




	
<div class="news" :style='{"border":"0px solid #dfdfdf","padding":"20px 0","boxShadow":"0px 0px 0px #eee","margin":"0px auto 0px auto","overflow":"hidden","borderRadius":"0px","background":"url(http://codegen.caihongy.cn/20221123/02b65dd190a741a1ae9c37c17624c5aa.jpg) fixed no-repeat center top,#d4f2f3","width":"100%","position":"relative","height":"auto","order":"6"}'>
	<div v-if="false" class="idea newsIdea" :style='{"padding":"0","margin":"0 auto","flexWrap":"wrap","background":"none","display":"flex","width":"1200px","justifyContent":"space-between"}'>
		<div class="box1" :style='{"width":"1200px","margin":"0 auto","position":"absolute","top":"74px","background":"#08b344","height":"1px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"padding":"0","margin":"40px auto","borderRadius":"4px 4px 0 0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20221123/8ac6eb514177419daf62911e596cd805.png) no-repeat center top","width":"1200px","lineHeight":"50px","position":"relative","height":"50px"}'>
		<span :style='{"padding":"0","fontSize":"24px","color":"#fff","textShadow":"0px 0px 0px #eee","background":"none"}'>新闻资讯</span>
	</div>
	
	
	
	
	
	
	
	
	
	<!-- 样式八 -->
	<div v-if="newsList.length" class="list list8 index-pv1" :style='{"cursor":"pointer","padding":"0px","margin":"0 auto","flexWrap":"wrap","background":"none","display":"flex","width":"1200px","justifyContent":"space-between","height":"auto"}'>
	  <div @click="toDetail('newsDetail', newsList[0])" v-if="newsList.length>0" :style='{"padding":"10px","margin":"0 0px 20px","borderRadius":"8px","background":"none","display":"flex","width":"49%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <div :style='{"width":"calc(100% - 260px)","padding":"10px 40px","borderRadius":"30%","background":"rgba(255,255,255,.9)","height":"auto","order":"2"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","fontSize":"14px","lineHeight":"24px","textOverflow":"ellipsis","fontWeight":"bold"}'>{{newsList[0].title}}</div>
	      <div :style='{"overflow":"hidden","color":"#666","background":"none","fontSize":"14px","lineHeight":"24px","textIndent":"2em","height":"168px"}'>{{newsList[0].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"center"}'>{{newsList[0].addtime.split(" ")[0]}}</div>
	    </div>
	    <img :style='{"width":"240px","objectFit":"cover","borderRadius":"100%","height":"240px"}' :src="baseUrl + newsList[0].picture" >
	  </div>
	  <div @click="toDetail('newsDetail', newsList[1])" v-if="newsList.length>1" :style='{"padding":"10px","margin":"0 0px 20px","borderRadius":"8px","background":"none","display":"flex","width":"49%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <img :style='{"width":"240px","objectFit":"cover","borderRadius":"100%","height":"240px","order":"2"}' :src="baseUrl + newsList[1].picture" >
	    <div :style='{"width":"calc(100% - 260px)","padding":"10px 40px","borderRadius":"30%","background":"rgba(255,255,255,.9)","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","fontSize":"14px","lineHeight":"24px","textOverflow":"ellipsis","fontWeight":"bold"}'>{{newsList[1].title}}</div>
	      <div :style='{"fontSize":"14px","lineHeight":"24px","overflow":"hidden","color":"#666","textIndent":"2em","height":"168px"}'>{{newsList[1].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"center"}'>{{newsList[1].addtime.split(" ")[0]}}</div>
	    </div>
	  </div>
	  <div @click="toDetail('newsDetail', newsList[2])" v-if="newsList.length>2" :style='{"padding":"10px","margin":"0 0px 0px","borderRadius":"8px","background":"none","display":"flex","width":"49%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <div :style='{"width":"calc(100% - 260px)","padding":"10px 40px","borderRadius":"30%","background":"rgba(255,255,255,.9)","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","fontSize":"14px","lineHeight":"28px","textOverflow":"ellipsis","fontWeight":"bold"}'>{{newsList[2].title}}</div>
	      <div :style='{"fontSize":"14px","lineHeight":"24px","overflow":"hidden","color":"#666","textIndent":"2em","height":"168px"}'>{{newsList[2].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"center"}'>{{newsList[2].addtime.split(" ")[0]}}</div>
	    </div>
	    <img :style='{"width":"240px","objectFit":"cover","borderRadius":"100%","height":"240px"}' :src="baseUrl + newsList[2].picture" >
	  </div>
	  <div @click="toDetail('newsDetail', newsList[3])" v-if="newsList.length>3" :style='{"padding":"10px","margin":"0 0px 0","borderRadius":"8px","background":"none","display":"flex","width":"49%","justifyContent":"space-between","height":"auto"}' class="list-item animation-box">
	    <img :style='{"width":"240px","objectFit":"cover","borderRadius":"100%","height":"240px"}' :src="baseUrl + newsList[3].picture" >
	    <div :style='{"width":"calc(100% - 260px)","padding":"10px 40px","borderRadius":"30%","background":"rgba(255,255,255,.9)","height":"auto"}'>
	      <div :style='{"whiteSpace":"nowrap","overflow":"hidden","color":"#333","textAlign":"center","fontSize":"14px","lineHeight":"24px","textOverflow":"ellipsis","fontWeight":"bold"}'>{{newsList[3].title}}</div>
	      <div :style='{"overflow":"hidden","color":"#666","background":"none","fontSize":"14px","lineHeight":"24px","textIndent":"2em","height":"168px"}'>{{newsList[3].introduction}}</div>
	      <div :style='{"fontSize":"12px","lineHeight":"24px","color":"#999","textAlign":"center"}'>{{newsList[3].addtime.split(" ")[0]}}</div>
	    </div>
	  </div>
	</div>
	
	
	
	<div @click="moreBtn('news')" :style='{"border":"0px solid #ffa100","cursor":"pointer","boxShadow":"0px 0px 0px #ddd5c6,inset 0px 0px 0px 0px #ffa100","padding":"0 20px","margin":"40px auto 40px","borderRadius":"0px","textAlign":"center","background":"#00adb5","display":"block","width":"130px","lineHeight":"44px"}'>
		<span :style='{"color":"#fff","background":"none","fontSize":"16px"}'>查看更多</span>
		<i v-if="true" :style='{"color":"#fff","fontSize":"16px","display":"inline-block"}' class="el-icon-d-arrow-right"></i>
	</div>
	
</div>


<div class="lists" :style='{"border":"1px solid #eee","padding":"0px","boxShadow":"0px 0px 0px #eee","margin":"40px 0 0","overflow":"hidden","borderRadius":"4px","background":"#fff","width":"850px","position":"relative","height":"auto","order":"8"}'>
	<div v-if="false" class="idea" :style='{"padding":"0px","margin":"0 auto","flexWrap":"wrap","background":"none","display":"flex","width":"1200px","justifyContent":"space-between"}'>
		<div class="box1" :style='{"width":"1200px","position":"absolute","top":"74px","background":"#08b344","height":"1px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"padding":"0","margin":"10px auto","textAlign":"center","background":"url(http://codegen.caihongy.cn/20221123/8ac6eb514177419daf62911e596cd805.png) no-repeat center top","width":"calc(100% - 20px)","lineHeight":"50px","position":"relative","height":"50px"}'>
	  <span :style='{"padding":"0","fontSize":"24px","color":"#fff","textShadow":"0px 0px 0px #eee","background":"none"}'>健身教练展示</span>
	</div>
	
	
	
	
	
	<!-- 样式四 -->
	<div class="list list4 index-pv1" :style='{"width":"100%","padding":"0px","margin":"20px 0 0","background":"#fff","height":"auto"}'>
		<div v-if="jianshenjiaolianList.length>0" class="list-4-item animation-box" @click="toDetail('jianshenjiaolianDetail', jianshenjiaolianList[0])" :style='{"width":"570px","margin":"0 10px","position":"relative","float":"left","display":"none","height":"570px"}'>
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenjiaolianList[0].zhaopian.substr(0,4)=='http'" :src="jianshenjiaolianList[0].zhaopian.split(',')[0]" alt="" />
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenjiaolianList[0].zhaopian?jianshenjiaolianList[0].zhaopian.split(',')[0]:'')" alt="" />
			<div class="list-4-item-title line1" :style='{"color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"44px","fontSize":"18px","position":"absolute"}'>{{jianshenjiaolianList[0].jiaolianxingming}}</div>
			<div class="list-4-item-title line1" :style='{"color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"44px","fontSize":"18px","position":"absolute"}'>价格/节课:{{jianshenjiaolianList[0].sijiaojiage}}</div>
		</div>
		<div :style='{"width":"100%","margin":"0 0 10px","display":"inline-block","height":"275px"}' class="list-4-body">
			<div v-if="jianshenjiaolianList.length>1" @click="toDetail('jianshenjiaolianDetail', jianshenjiaolianList[1])" class="list-4-item animation-box item-2" :style='{"cursor":"pointer","width":"49%","margin":"0px","position":"relative","display":"inline-block","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenjiaolianList[1].zhaopian.substr(0,4)=='http'" :src="jianshenjiaolianList[1].zhaopian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenjiaolianList[1].zhaopian?jianshenjiaolianList[1].zhaopian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenjiaolianList[1].jiaolianxingming}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格/节课:{{jianshenjiaolianList[1].sijiaojiage}}</div>
			</div>
			<div v-if="jianshenjiaolianList.length>2" @click="toDetail('jianshenjiaolianDetail', jianshenjiaolianList[2])" class="list-4-item animation-box item-3" :style='{"cursor":"pointer","margin":"0px","display":"inline-block","width":"49%","position":"relative","float":"right","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenjiaolianList[2].zhaopian.substr(0,4)=='http'" :src="jianshenjiaolianList[2].zhaopian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenjiaolianList[2].zhaopian?jianshenjiaolianList[2].zhaopian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenjiaolianList[2].jiaolianxingming}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格/节课:{{jianshenjiaolianList[2].sijiaojiage}}</div>
			</div>
		</div>
		<div :style='{"width":"100%","margin":"10px 0 0","display":"inline-block","height":"275px"}' class="list-4-body">
			<div v-if="jianshenjiaolianList.length>3" @click="toDetail('jianshenjiaolianDetail', jianshenjiaolianList[3])" class="list-4-item animation-box item-4" :style='{"cursor":"pointer","width":"49%","margin":"0","position":"relative","display":"inline-block","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenjiaolianList[3].zhaopian.substr(0,4)=='http'" :src="jianshenjiaolianList[3].zhaopian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenjiaolianList[3].zhaopian?jianshenjiaolianList[3].zhaopian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenjiaolianList[3].jiaolianxingming}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格/节课:{{jianshenjiaolianList[3].sijiaojiage}}</div>
			</div>
			<div v-if="jianshenjiaolianList.length>4" @click="toDetail('jianshenjiaolianDetail', jianshenjiaolianList[4])" class="list-4-item animation-box item-5" :style='{"cursor":"pointer","margin":"0","display":"inline-block","width":"49%","position":"relative","float":"right","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenjiaolianList[4].zhaopian.substr(0,4)=='http'" :src="jianshenjiaolianList[4].zhaopian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenjiaolianList[4].zhaopian?jianshenjiaolianList[4].zhaopian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenjiaolianList[4].jiaolianxingming}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格/节课:{{jianshenjiaolianList[4].sijiaojiage}}</div>
			</div>
		</div>
	</div>
	
	
	
	
	
	
	<div @click="moreBtn('jianshenjiaolian')" :style='{"border":"0px solid #ccc","cursor":"pointer","boxShadow":"0px 0px 0px #ddd5c6,inset 0px 0px 0px 0px #ffa100","margin":"20px auto 20px -175px","borderRadius":"0px","textAlign":"center","background":"none","display":"none","width":"100%","lineHeight":"44px"}'>
		<span :style='{"padding":"0 0 0 10px","borderColor":"#ccc","margin":"0","color":"#333","background":"#eee","borderWidth":"0","display":"inline-block","width":"100px","fontSize":"16px","lineHeight":"40px","borderStyle":"solid","height":"40px"}'>查看更多</span>
		<i v-if="true" :style='{"padding":"0 20px 0 0","borderColor":"#ccc","margin":"0 0 0 -10px","color":"#333","borderWidth":"0","background":"#eee","display":"inline-block","width":"40px","fontSize":"16px","lineHeight":"40px","borderStyle":"solid","height":"40px"}' class="el-icon-d-arrow-right"></i>
	</div>
	

</div>
<div class="lists" :style='{"border":"1px solid #eee","padding":"0px","boxShadow":"0px 0px 0px #eee","margin":"40px 0 0","overflow":"hidden","borderRadius":"4px","background":"#fff","width":"850px","position":"relative","height":"auto","order":"8"}'>
	<div v-if="false" class="idea" :style='{"padding":"0px","margin":"0 auto","flexWrap":"wrap","background":"none","display":"flex","width":"1200px","justifyContent":"space-between"}'>
		<div class="box1" :style='{"width":"1200px","position":"absolute","top":"74px","background":"#08b344","height":"1px"}'></div>
		<div class="box2" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box3" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box4" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box5" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box6" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box7" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box8" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box9" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
		<div class="box10" :style='{"width":"20%","background":"#fff","display":"none","height":"80px"}'></div>
	</div>
	
	<div class="title" :style='{"padding":"0","margin":"10px auto","textAlign":"center","background":"url(http://codegen.caihongy.cn/20221123/8ac6eb514177419daf62911e596cd805.png) no-repeat center top","width":"calc(100% - 20px)","lineHeight":"50px","position":"relative","height":"50px"}'>
	  <span :style='{"padding":"0","fontSize":"24px","color":"#fff","textShadow":"0px 0px 0px #eee","background":"none"}'>健身器材展示</span>
	</div>
	
	
	
	
	
	<!-- 样式四 -->
	<div class="list list4 index-pv1" :style='{"width":"100%","padding":"0px","margin":"20px 0 0","background":"#fff","height":"auto"}'>
		<div v-if="jianshenqicaiList.length>0" class="list-4-item animation-box" @click="toDetail('jianshenqicaiDetail', jianshenqicaiList[0])" :style='{"width":"570px","margin":"0 10px","position":"relative","float":"left","display":"none","height":"570px"}'>
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenqicaiList[0].tupian.substr(0,4)=='http'" :src="jianshenqicaiList[0].tupian.split(',')[0]" alt="" />
			<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenqicaiList[0].tupian?jianshenqicaiList[0].tupian.split(',')[0]:'')" alt="" />
			<div class="list-4-item-title line1" :style='{"color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"44px","fontSize":"18px","position":"absolute"}'>{{jianshenqicaiList[0].qicaimingcheng}}</div>
			<div class="list-4-item-title line1" :style='{"color":"#fff","left":"0","textAlign":"center","bottom":"0","background":"rgba(0,0,0,.3)","width":"100%","lineHeight":"44px","fontSize":"18px","position":"absolute"}'>价格:{{jianshenqicaiList[0].jiage}}</div>
		</div>
		<div :style='{"width":"100%","margin":"0 0 10px","display":"inline-block","height":"275px"}' class="list-4-body">
			<div v-if="jianshenqicaiList.length>1" @click="toDetail('jianshenqicaiDetail', jianshenqicaiList[1])" class="list-4-item animation-box item-2" :style='{"cursor":"pointer","width":"49%","margin":"0px","position":"relative","display":"inline-block","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenqicaiList[1].tupian.substr(0,4)=='http'" :src="jianshenqicaiList[1].tupian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenqicaiList[1].tupian?jianshenqicaiList[1].tupian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenqicaiList[1].qicaimingcheng}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格:{{jianshenqicaiList[1].jiage}}</div>
			</div>
			<div v-if="jianshenqicaiList.length>2" @click="toDetail('jianshenqicaiDetail', jianshenqicaiList[2])" class="list-4-item animation-box item-3" :style='{"cursor":"pointer","margin":"0px","display":"inline-block","width":"49%","position":"relative","float":"right","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenqicaiList[2].tupian.substr(0,4)=='http'" :src="jianshenqicaiList[2].tupian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenqicaiList[2].tupian?jianshenqicaiList[2].tupian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenqicaiList[2].qicaimingcheng}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格:{{jianshenqicaiList[2].jiage}}</div>
			</div>
		</div>
		<div :style='{"width":"100%","margin":"10px 0 0","display":"inline-block","height":"275px"}' class="list-4-body">
			<div v-if="jianshenqicaiList.length>3" @click="toDetail('jianshenqicaiDetail', jianshenqicaiList[3])" class="list-4-item animation-box item-4" :style='{"cursor":"pointer","width":"49%","margin":"0","position":"relative","display":"inline-block","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenqicaiList[3].tupian.substr(0,4)=='http'" :src="jianshenqicaiList[3].tupian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenqicaiList[3].tupian?jianshenqicaiList[3].tupian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenqicaiList[3].qicaimingcheng}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格:{{jianshenqicaiList[3].jiage}}</div>
			</div>
			<div v-if="jianshenqicaiList.length>4" @click="toDetail('jianshenqicaiDetail', jianshenqicaiList[4])" class="list-4-item animation-box item-5" :style='{"cursor":"pointer","margin":"0","display":"inline-block","width":"49%","position":"relative","float":"right","height":"275px"}'>
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-if="jianshenqicaiList[4].tupian.substr(0,4)=='http'" :src="jianshenqicaiList[4].tupian.split(',')[0]" alt="" />
				<img :style='{"width":"100%","objectFit":"cover","float":"left","height":"100%"}' v-else :src="baseUrl + (jianshenqicaiList[4].tupian?jianshenqicaiList[4].tupian.split(',')[0]:'')" alt="" />
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>{{jianshenqicaiList[4].qicaimingcheng}}</div>
				<div class="list-4-item-title line1" :style='{"padding":"240px 0 0","color":"#333","left":"0","textAlign":"center","bottom":"0","background":"url(http://codegen.caihongy.cn/20221123/0744ada234f94fe8b693f4180b0d73f3.png) no-repeat center top","width":"100%","lineHeight":"24px","fontSize":"18px","backgroundSize":"100% 100%","position":"absolute","height":"100%"}'>价格:{{jianshenqicaiList[4].jiage}}</div>
			</div>
		</div>
	</div>
	
	
	
	
	
	
	<div @click="moreBtn('jianshenqicai')" :style='{"border":"0px solid #ccc","cursor":"pointer","boxShadow":"0px 0px 0px #ddd5c6,inset 0px 0px 0px 0px #ffa100","margin":"20px auto 20px -175px","borderRadius":"0px","textAlign":"center","background":"none","display":"none","width":"100%","lineHeight":"44px"}'>
		<span :style='{"padding":"0 0 0 10px","borderColor":"#ccc","margin":"0","color":"#333","background":"#eee","borderWidth":"0","display":"inline-block","width":"100px","fontSize":"16px","lineHeight":"40px","borderStyle":"solid","height":"40px"}'>查看更多</span>
		<i v-if="true" :style='{"padding":"0 20px 0 0","borderColor":"#ccc","margin":"0 0 0 -10px","color":"#333","borderWidth":"0","background":"#eee","display":"inline-block","width":"40px","fontSize":"16px","lineHeight":"40px","borderStyle":"solid","height":"40px"}' class="el-icon-d-arrow-right"></i>
	</div>
	

</div>


</div>
</template>

<script>
  export default {
    //数据集合
    data() {
      return {
        baseUrl: '',
        newsList: [],

        jianshenjiaolianList: [],
        jianshenqicaiList: [],
      }
    },
    created() {
      this.baseUrl = this.$config.baseUrl;
      this.getNewsList();
      this.getList();
    },
    //方法集合
    methods: {
		getNewsList() {
			this.$http.get('news/list', {params: {
				page: 1,
				limit: 4,
			order: 'desc'}}).then(res => {
				if (res.data.code == 0) {
					this.newsList = res.data.data.list;
					
					
				}
			});
		},
		getList() {
          let autoSortUrl = "";
			
			this.$http.get('jianshenjiaolian/list', {params: {
				page: 1,
				limit: 4,
			}}).then(res => {
				if (res.data.code == 0) {
					this.jianshenjiaolianList = res.data.data.list;
					
					// 商品列表样式五
					
				}
			});
			this.$http.get('jianshenqicai/list', {params: {
				page: 1,
				limit: 4,
			}}).then(res => {
				if (res.data.code == 0) {
					this.jianshenqicaiList = res.data.data.list;
					
					// 商品列表样式五
					
				}
			});
		},
		toDetail(path, item) {
			this.$router.push({path: '/index/' + path, query: {detailObj: JSON.stringify(item)}});
		},
		moreBtn(path) {
			this.$router.push({path: '/index/' + path});
		}
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
	
		.recommend {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
        }
        
        .list5 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				filter: brightness(1.1);
				transform: rotate(0deg);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				opacity: 0.75;
				transition: all 0.3s ease-in-out 0s;
			}
		}
		
		.news {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list3 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list6 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list6 .swiper-button-next {
				left: auto;
				right: 10px;
			}
			
			.list6 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				filter: brightness(1.1);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: all 0.3s ease-in-out 0s;
			}
		}
	
		.lists {
			.list3 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list3 .swiper-button-prev::after {
				color: #08b344;
			}
			
			.list3 .swiper-button-next {
				left: auto;
				right: 10px;
        }
        
        .list3 .swiper-button-next::after {
				color: #08b344;
			}
			
			.list5 .swiper-button-prev {
				left: 10px;
				right: auto;
			}
			
			.list5 .swiper-button-prev::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 .swiper-button-next {
            left: auto;
            right: 10px;
			}
			
			.list5 .swiper-button-next::after {
				color: rgb(64, 158, 255);
			}
			
			.list5 {
				.swiper-slide-prev {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-next {
					position: relative;
					z-index: 3;
				}
		
				.swiper-slide-active {
					position: relative;
					z-index: 5;
				}
			}
			
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				-webkit-perspective: 1000px;
				perspective: 1000px;
				opacity: 0.75;
				transition: all 0.3s ease-in-out 0s;
			}
		}
	}
</style>
