<template>
  <div style="background-color: #f6f6f6;">
  <div>
      <div class="elib-left">
          <div class="nuser-left">
            <div class="navi-wrap">
              <b-nav class="navi">
                <ul class="nav m-b-lg">
					        <li class="active">
                    <a href="/">
                      <span class="pull-right text-muted">
                        <i class="fa fa-fw fa-angle-right text"></i>
                      </span>
                      <span class="pa pa-user"></span>
                      <span class="font-bold">首页</span>
                    </a>
                    <ul class="nav nav-sub dk" style="display: block;">
                      <li v-for="(item,index) in lables" :key="index" :class="item.link === now_url ? 'active':''">
                        <a :href="item.link">
                          <span id="d">{{item.lable}}</span>
                        </a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </b-nav>
            </div>
        </div>
      </div>
  </div>

  </div>
</template>

<script>
  export default {
      name: "Left",
      data() {
        return {
            now_url: this.$route.path,
            lables:[
              {
                'lable': '高新技术企业',
                'link': '/gaoxin'
              },
              {
                'lable': '科技型中小企业',
                'link': '/kj_xing'
              },
              {
                'lable': '独角兽企业',
                'link': '/dujiaoshou'
              },
              {
                'lable': '技术先进型服务企业',
                'link': '/js_xianjin'
              },
              {
                'lable': '瞪羚企业',
                'link': '/dengling'
              },
              {
                'lable': '创新型企业',
                'link': '/chuangxin'
              },
              {
                'lable': '科技小巨人企业',
                'link': '/kj_xiao'
              },
              {
                'lable': '专精特新企业',
                'link': '/zhaunjing'
              },
              {
                'lable': '雏鹰企业',
                'link': '/chuying'
              },
              {
                'lable': '企业技术中心',
                'link': '/js_qiye'
              },
              {
                'lable': '科技企业孵化器',
                'link': '/fuhuaqi'
              },
              {
                'lable': '技术创新示范企业',
                'link': '/js_chuangxin'
              },
              {
                'lable': '众创空间',
                'link': '/zhongchuang'
              },
              {
                'lable': '隐形冠军企业',
                'link': '/yinxing'
              },
              {
                'lable': '民营科技企业',
                'link': '/minying'
              },
              {
                'lable': '牛羚企业',
                'link': '/niuling'
              },
              {
                'lable': '专精特新小巨人企业',
                'link': '/zhaunjing_xiao'
              },
            ]
        }
    },
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.text-muted {
    color: #a1a8ac;
}

.pull-right {
    float: right !important;
}
.pa.pa-user {
    background-position: 18px -18px;
}
.pa {
    position: relative;
    display: inline-block;
    width: 18px;
    height: 18px;
    background-image: url(../assets/首页.png);
    background-size: 54px 36px;
    float: left;
    line-height: 40px;
    left: -8px;
    top: 3px;
}
.font-bold {
    font-weight: 600;
}

.elib-left {
    width: 198px;
    float: left;

}
.elib-left .nuser-left {
    padding-left: 1px;

}
.nuser-left .navi-wrap {
    width: 250px;
}

.nuser-left .navi-wrap {
    background: #fff;
    border: solid 1px #eee;
    position: relative;
    border-radius: 5px;
    /* max-height: 500px; */
    overflow-x: hidden;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
}
.m-b-lg {
    margin-bottom: 30px;
}
.nav {
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
}
.fa-fw {
    width: 1.28571429em;
    text-align: center;
}

.fa {
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.nav-sub  >li:hover{
    box-shadow: 5px 5px 30px rgba(38, 38, 38, 0.25);
    opacity: 0.9;
    -webkit-transform: translatez(25px);
    -moz-transform: translatez(25px);
    transform: translatez(25px)
}

.nuser-left .navi ul a{
  color: #333;
}
.nuser-left .navi ul ul a{
  color: #666;
}
.nuser-left .navi ul.nav li a > i{
  margin: -10px -5px -5px -15px;
}
.nuser-left .navi ul.nav li li a{
  padding-left: 38px;
}
.nuser-left .nav.nav-sub > li.active > a {
   background-color: #faf2f2;
   color: #94000c;
   border-right: solid 2px #94000c;
}
.nuser-left .nav > li.current > a {
   background-color: #faf2f2;
   color: #94000c;
}
.nuser-left .navi ul.nav li a {
  position: relative;
  display: block;
  padding: 8px 94px 7px 20px;
  font-weight: normal;
  text-transform: none;
  text-decoration: none;
  width:300px;
  height:40px;
  -webkit-transition: background-color 0.2s ease-in-out 0s;
  transition: background-color 0.2s ease-in-out 0s;
}
#d{
    font-size: 14px;
    //font-weight: bold;
}

</style>
