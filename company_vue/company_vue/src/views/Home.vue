<template>
  <div style="background-color: #f6f6f6;" v-title data-title="首页 Galaxy Information">
  <Header />
  <div class="container c-t-cd">
    <div style="margin-left: -3%">
      <Left />
    </div>
      <div class="comp-main">
        <div class="row c-d">
          <section class="col-xs-6">
            <ul class="panel comp-panel">
              <div class="panel-header b-b">
                <a class="more right-info" href="/info_more/shangshi">More ></a>
                <h4 style="font-weight: bold">上市信息</h4>
              </div>
              <ul class="list-group">
                <li class="list-group-item list-item" v-for="(item,i) in items.shangshiItems" :key="i">
                    <div class="img">
                      <img :src="item.img_base" alt="上市动态">
                    </div>
                    <div class="title">
                      <a target="_blank" style="color: #1d1f21;font-weight:650;font-size: 14.5px;" :href="item.link">{{item.title}}</a>
                    </div>
                    <div class="desc1" style="margin-top: 25px;">
                      <a>{{item.desc1}}</a>
                      <span>{{item.desc2}}</span>
                      <span class="time">{{formatter(item.time, 'yyyy-MM-dd')}}</span>
                    </div>
                </li>
              </ul>
            </ul>
          </section>
          <br>
          <section class="col-xs-6">
            <ul class="panel comp-panel">
              <div class="panel-header b-b">
                <a class="more right-info" href="/info_more/rongzi">More ></a>
                <h4 style="font-weight: bold">创投资讯</h4>
              </div>
              <ul class="list-group">
                <li class="list-group-item list-item" v-for="(item,i) in items.rongziItems" :key="i">
                    <div class="title">
                      <a target="_blank" style="color: #1d1f21;font-weight: 650;font-size: 14.5px;" :href="item.url">{{item.title}}</a>
                    </div>
                    <div class="desc2">
                      <div>
                        <a :href="item.url" style="color: #535863; text-decoration: none;">{{item.des}}</a>
                      </div>
                      <span class="time" style="margin-top: 10px;">{{formatter(item.event_time, 'yyyy-MM-dd')}}</span>
                    </div>
                </li>
              </ul>
            </ul>
          </section>
        </div>
      </div>
    <div style="margin-right: -4%">
      <Right />
    </div>

  </div>
  <div style="margin-top: 60%"></div>
  <Footer />

  </div>
</template>

<script>
    import Header from "../components/Header.vue";
    import Footer from "../components/Footer.vue";
    import {GetInfoPost} from "../apis/read";
    import Left from "../components/Left.vue";
    import Right from "../components/Right.vue";
    import {formatter} from "../utils/date.js";

    export default {
      name: 'Home',
      components: {
        Left,
        Right,
        Header,
        Footer,
        },

      data() {
        return {
            formatter,
            now_url: this.$route.path,
            shangshiParams: {
                url: this.$route.path,
                key: 'shangshi'
            },
            rongziParams:{
                url: this.$route.path,
                key: 'rongzi'
            },
            items: {
                shangshiItems:[],
                rongziItems:[]
            },
        }
    },
      created () { // setup相当与beforecreate、created; props：来自爸爸的爱（父组件传入的内容）;context：当前组件拥有的内容
        //this.now_url = this.$router.path;
        console.log("now_url = ", this.now_url);

        GetInfoPost(this.shangshiParams).then(response => {
            this.items.shangshiItems = response.data.data;
            console.log("shangshi = ", this.items.shangshiItems);
        });

        GetInfoPost(this.rongziParams).then(response => {
            this.items.rongziItems = response.data.data;
            console.log("rongzi = ", this.items.rongziItems);
        });
      },

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

//.container {
//    width: 1250px;
//    height: 300px;
//}

.c-t-cd {
    margin-top: 1%;
}

.npanel-body{
  padding: 20px 15px;
  width: 100%;
}

.ntable {
    width: 100%;
    margin: 0 auto;
    margin-bottom: 20px;
}
.ntable .tx {
    text-align: center;
    width: 10px;
}
.ntable th {
    text-align: center;
    background: #F2F9FC;
    border: #E4EEF6 1px solid;
    border-collapse: collapse;
    padding: 12px 12px 12px 12px;
    font-weight: normal;
    color: #444444;
    line-height: 19px;
    font-size: 15px;
}
.comp-main {
    width: 61%;
    float: left;
}
.elib-content {
    background: #fff;
}
.comp-panel {
    margin-bottom: 20px;
}
.panel {
    border-radius: 1px;
    box-shadow: none;
    //border: solid 1px #eeeeee;
    width: 100%;
}
.text-center {
    text-align: center;
}
.ntable td {
    padding: 10px 10px 11px 10px;
    border: #E4EEF6 1px solid;
    word-break: break-all;
    font-size: 14px;
    line-height: 1.6;
    color: #222;
    word-wrap: break-word;
}
.c-d {
    margin-top: 1px;
}

.row {
    margin-left: 1%;
}
.col-xs-6 {
    width: 100%;
}
.panel-header.b-b {
    border-bottom: 0px solid #eeeeee;
    border-top: 1px solid #eeeeee;
    border-left: 1px solid #eeeeee;
    border-right: 1px solid #eeeeee;
}

.panel-header {
    color: #333;
    //border-bottom: none;
    background: #fffcf5;
    border-radius: 1px;
    border: solid 1px #bbbbbb
}
.list-group {
    border-radius: 2px;
    margin-right: 1px;
}
.panel > .list-group .list-group-item {
    border-width: 0.2px 0;
    border-radius: 0;
}

.panel .list-group-item {
    //border-color: #eaeaea;
    border-radius: 1px;
    border: solid 0 #eaeaea;
}
.list-item .img {
    width: 65px;
    height: 65px;
    float: left;
    margin-right: 10px;
}
.list-item .img>img {
    width: 100%;
}
.list-group >li:hover{
    box-shadow: 5px 5px 30px rgba(38, 38, 38, 0.25);
    //opacity: 0.96;
    -webkit-transform: translatex(25px);
    -moz-transform: translatex(25px);
    transform: translatex(10px)
}

.list-item .title {
    font-size: 16px;
    line-height: 20px;
    height: 1px;
    display: table-cell;
    vertical-align: bottom;
    color: #333;
}
.list-item .title>a {
    color: #3c4144;
    text-decoration: none;
}

.list-item .desc1 {
    font-size: 14px;
    margin-top: 15px;
    margin-left: 60%;
}

.list-item .desc1>a {
    margin-right: 35px;
    color: #999;
}

.list-item .desc1>span {
    margin-right: 10px;
    color: #999;
}
.list-item .desc1>.time {
    float: left;
    margin-left: -119%;
}
.list-item .desc2 {
  font-size: 14px;
  margin-top: 15px;
}

.list-item .desc2>a {
  margin-right: 35px;
  color: #999;
}

.list-item .desc2>span {
  margin-right: 10px;
  color: #999;
}
.list-item .desc2>.time {
  float: left;
}
.b-b {
    border-bottom: 1px solid #eeeeee;
}
.panel-header h4, .panel-header .h4 {
    margin-top: 1px;
    margin-bottom: 0px;
    font-weight: normal;
    display: inline-block;
    line-height: 50px;
    margin-left: 15px;
}

h4, .h4 {
    font-size: 16px;
}
.panel-header .right-info {
    line-height: 48px;
    margin-right: 15px;
}
.right-info {
    float: right !important;
}
.comp-panel .panel-header>.more {
    color: #94000c;
    float: right;
    font-size: 14px;
    font-weight: bold;
}
</style>
