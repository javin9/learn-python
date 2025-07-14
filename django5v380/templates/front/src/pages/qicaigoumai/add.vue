<template>
<div :style='{"border":"1px solid #eee","padding":"20px","boxShadow":"0px 0px 0px #ccc,inset 0px 0px 0px 0px #eee","margin":"20px auto 0","borderRadius":"4px","background":"#fff","width":"1200px","position":"relative"}'>
    <el-form
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="80px"
    >
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="购买编号" prop="goumaibianhao">
              <el-input v-model="ruleForm.goumaibianhao" placeholder="购买编号" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="器材名称" prop="qicaimingcheng">
            <el-input v-model="ruleForm.qicaimingcheng" 
                placeholder="器材名称" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="品牌" prop="pinpai">
            <el-input v-model="ruleForm.pinpai" 
                placeholder="品牌" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="价格" prop="jiage">
            <el-input v-model="ruleForm.jiage" 
                placeholder="价格" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="数量" prop="shuliang">
            <el-input v-model="ruleForm.shuliang" 
                placeholder="数量" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="总计" prop="zongji">
              <el-input v-model="zongji" placeholder="总计" readonly></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="购买时间" prop="goumaishijian" >
              <el-date-picker
                  value-format="yyyy-MM-dd HH:mm:ss"
                  v-model="ruleForm.goumaishijian" 
                  type="datetime"
                  placeholder="购买时间">
              </el-date-picker>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="用户账号" prop="yonghuzhanghao">
            <el-input v-model="ruleForm.yonghuzhanghao" 
                placeholder="用户账号" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="用户姓名" prop="yonghuxingming">
            <el-input v-model="ruleForm.yonghuxingming" 
                placeholder="用户姓名" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"border":"0px solid #dfdfdf","padding":"10px","boxShadow":"0px 0px 0px #eee","margin":"0 0 8px 0","borderRadius":"8px","background":"none"}' label="手机号码" prop="shoujihaoma">
            <el-input v-model="ruleForm.shoujihaoma" 
                placeholder="手机号码" clearable ></el-input>
          </el-form-item>

      <el-form-item :style='{"padding":"0","margin":"20px 0 20px 0"}'>
        <el-button :style='{"border":"0","cursor":"pointer","padding":"0","boxShadow":"1px 2px 4px #ccc","margin":"0 20px 0 0","color":"#fff","outline":"none","borderRadius":"20px","background":"radial-gradient(circle, rgba(43,224,232,1) 0%, rgba(0,173,181,1) 100%)","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"1px solid #bbb","cursor":"pointer","padding":"0","boxShadow":"4px 4px 8px #eee","margin":"0","color":"#999","outline":"none","borderRadius":"20px","background":"#fff","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
      return {
        id: '',
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          goumaibianhao: this.getUUID(),
          qicaimingcheng: '',
          pinpai: '',
          jiage: '',
          shuliang: '',
          zongji: '',
          goumaishijian: '',
          yonghuzhanghao: '',
          yonghuxingming: '',
          shoujihaoma: '',
        },
        rules: {
          goumaibianhao: [
          ],
          qicaimingcheng: [
          ],
          pinpai: [
          ],
          jiage: [
            { validator: this.$validate.isNumber, trigger: 'blur' },
          ],
          shuliang: [
            { required: true, message: '数量不能为空', trigger: 'blur' },
            { validator: this.$validate.isIntNumer, trigger: 'blur' },
          ],
          zongji: [
            { validator: this.$validate.isNumber, trigger: 'blur' },
          ],
          goumaishijian: [
          ],
          yonghuzhanghao: [
          ],
          yonghuxingming: [
          ],
          shoujihaoma: [
          ],
          ispay: [
          ],
        },
      };
    },
    computed: {


        zongji:{
            get: function () {
                return 1*this.ruleForm.jiage*this.ruleForm.shuliang
            }
        },

    },
    created() {
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.ruleForm.goumaishijian = this.getCurDateTime()
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='goumaibianhao'){
              this.ruleForm.goumaibianhao = obj[o];
              continue;
            }
            if(o=='qicaimingcheng'){
              this.ruleForm.qicaimingcheng = obj[o];
              continue;
            }
            if(o=='pinpai'){
              this.ruleForm.pinpai = obj[o];
              continue;
            }
            if(o=='jiage'){
              this.ruleForm.jiage = obj[o];
              continue;
            }
            if(o=='shuliang'){
              this.ruleForm.shuliang = obj[o];
              continue;
            }
            if(o=='zongji'){
              this.ruleForm.zongji = obj[o];
              continue;
            }
            if(o=='goumaishijian'){
              this.ruleForm.goumaishijian = obj[o];
              continue;
            }
            if(o=='yonghuzhanghao'){
              this.ruleForm.yonghuzhanghao = obj[o];
              continue;
            }
            if(o=='yonghuxingming'){
              this.ruleForm.yonghuxingming = obj[o];
              continue;
            }
            if(o=='shoujihaoma'){
              this.ruleForm.shoujihaoma = obj[o];
              continue;
            }
          }
          this.ruleForm.shuliang = 0
        }
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
            if(json.yonghuzhanghao!=''&&json.yonghuzhanghao){
                this.ruleForm.yonghuzhanghao = json.yonghuzhanghao
            }
            if(json.yonghuxingming!=''&&json.yonghuxingming){
                this.ruleForm.yonghuxingming = json.yonghuxingming
            }
            if(json.shoujihaoma!=''&&json.shoujihaoma){
                this.ruleForm.shoujihaoma = json.shoujihaoma
            }
          }
        });
      },

    // 多级联动参数
      // 多级联动参数
      info(id) {
        this.$http.get('qicaigoumai/detail/${id}', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

          this.ruleForm.zongji = this.zongji
        var obj = JSON.parse(localStorage.getItem('crossObj'));
        var table = localStorage.getItem('crossTable');
        obj.shuliang = obj.shuliang - this.ruleForm.shuliang
        if(obj.shuliang<0){
          this.$message.error("数量不足");
          return
        }
      
        this.$http.post(table+`/update`, obj).then(res => {});
        //更新跨表属性
        var crossuserid;
        var crossrefid;
        var crossoptnum;
        this.$refs["ruleForm"].validate(valid => {
          if(valid) {
            if(this.type=='cross'){
                 var statusColumnName = localStorage.getItem('statusColumnName');
                 var statusColumnValue = localStorage.getItem('statusColumnValue');
                 if(statusColumnName && statusColumnName!='') {
                     var obj = JSON.parse(localStorage.getItem('crossObj'));
                     if(!statusColumnName.startsWith("[")) {
                         for (var o in obj){
                             if(o==statusColumnName){
                                 obj[o] = statusColumnValue;
                             }
                         }
                         var table = localStorage.getItem('crossTable');
                         this.$http.post(table+'/update', obj).then(res => {});
                     } else {
                            crossuserid=Number(localStorage.getItem('userid'));
                            crossrefid=obj['id'];
                            crossoptnum=localStorage.getItem('statusColumnName');
                            crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                     }
                 }
            }
            if(crossrefid && crossuserid) {
                 this.ruleForm.crossuserid=crossuserid;
                 this.ruleForm.crossrefid=crossrefid;
                 var params = {
                     page: 1,
                     limit: 10,
                     crossuserid:crossuserid,
                     crossrefid:crossrefid,
                 }
                 this.$http.get('qicaigoumai/list', {
                  params: params
                 }).then(res => {
                     if(res.data.data.total>=crossoptnum) {
                         this.$message({
                          message: localStorage.getItem('tips'),
                          type: 'success',
                          duration: 1500,
                         });
                          return false;
                     } else {
                         // 跨表计算
                          var obj = JSON.parse(localStorage.getItem('crossObj'));
                          var table = localStorage.getItem('crossTable');

                          obj.shuliang = parseFloat(obj.shuliang) - parseFloat(this.ruleForm.shuliang)

                          this.$http.post(table+`/update`,obj).then(res => {});
                          this.$http.post('qicaigoumai/add', this.ruleForm).then(res => {
                              if (res.data.code == 0) {
                                  this.$message({
                                      message: '操作成功',
                                      type: 'success',
                                      duration: 1500,
                                      onClose: () => {
                                          this.$router.go(-1);
                                      }
                                  });
                              } else {
                                  this.$message({
                                      message: res.data.msg,
                                      type: 'error',
                                      duration: 1500
                                  });
                              }
                          });
                     }
                 });
             } else {
                  var obj = JSON.parse(localStorage.getItem('crossObj'));
                  var table = localStorage.getItem('crossTable');

                  obj.shuliang = parseFloat(obj.shuliang) - parseFloat(this.ruleForm.shuliang)

                  this.$http.post(table+`/update`,obj).then(res => {});
                  this.$http.post('qicaigoumai/add', this.ruleForm).then(res => {
                     if (res.data.code == 0) {
                          this.$message({
                              message: '操作成功',
                              type: 'success',
                              duration: 1500,
                              onClose: () => {
                                  this.$router.go(-1);
                              }
                          });
                      } else {
                          this.$message({
                              message: res.data.msg,
                              type: 'error',
                              duration: 1500
                          });
                      }
                  });
             }
          }
        });
      },
      // 获取uuid
      getUUID () {
        return new Date().getTime();
      },
      // 返回
      back() {
        this.$router.go(-1);
      },
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  padding: 0 10px 0 0;
	  color: #666;
	  font-weight: 500;
	  width: 80px;
	  font-size: 14px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 80px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  border: 1px solid #00adb5;
	  border-radius: 4px;
	  padding: 0 12px;
	  outline: none;
	  color: #666;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 400px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  border: 1px solid #00adb5;
	  border-radius: 4px;
	  padding: 0 10px;
	  outline: none;
	  color: #666;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 200px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  border: 1px solid #00adb5;
	  border-radius: 4px;
	  padding: 0 10px 0 30px;
	  outline: none;
	  color: #666;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 200px;
	  font-size: 14px;
	  height: 40px;
	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
	  border: 1px solid #00adb5;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #00adb5;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 200px;
	  font-size: 32px;
	  line-height: 120px;
	  text-align: center;
	  height: auto;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  border: 1px solid #00adb5;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #00adb5;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 200px;
	  font-size: 32px;
	  line-height: 120px;
	  text-align: center;
	  height: auto;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  border: 1px solid #00adb5;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #00adb5;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 200px;
	  font-size: 32px;
	  line-height: 120px;
	  text-align: center;
	  height: auto;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  border: 1px solid #00adb5;
	  border-radius: 4px;
	  padding: 12px;
	  outline: none;
	  color: #666;
	  background: radial-gradient(circle, rgba(237,250,251,1) 35%, rgba(162,233,236,1) 100%);
	  width: 400px;
	  font-size: 14px;
	  min-height: 120px;
	}
</style>
