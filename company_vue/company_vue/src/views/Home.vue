<template>

  <div style="background-color: #f6f6f6; display: grid;" v-title data-title="GalaxyInfo-科技企业查询_工商信息_企业信息_创投上市资讯_行业分析">
    <!-- <div class="header"> -->
    <Header />
<!--    </div> -->

    <div class="container c-t-cd">
      <div style="margin-left: 0%">
        <Left />
      </div>
      <div class="comp-main">
        <div class="row c-d">

          <div class="slide" >
            <input class="prev" type="button" value="<" v-on:click="prev()" />

            <div v-for="(imgUrl, index) in bannerList" v-show="index===mark" :key="index" class="slideshow">
                  <a target="_blank" :href="items.hangyeItems[index].url.replace('https://www.iyiou.com/analysis', 'info_more/hangye')">
                    <img :src=imgUrl style="width:100%; height:100%;" :alt="items.hangyeItems[index].title">
                    <span class="news-text" :title="items.hangyeItems[index].title">{{items.hangyeItems[index].title}}</span>
                  </a>
            </div>

            <input class="next" type="button" value=">" v-on:click="next()" />

            <div class="bar">
                 <span v-for="(item, index) in bannerList" :class="{ 'active':index===mark }" :key="index"></span>
            </div>
          </div>

          <section class="col-xs-6">
              <ul class="panel comp-panel">
                <div class="panel-header b-b">
                  <a class="more right-info" href="/info_more/hangye">More ></a>
                  <h4 style="font-weight: bold" title="行业资讯">行业资讯</h4>
                </div>
                <ul class="list-group">
                  <li class="list-group-item list-item" v-for="(item,i) in items.hangyeItems" :key="i">

                      <div class="title">
                        <a target="_blank" style="color: #1d1f21;font-weight:650;font-size: 14.5px;" :href="item.url.replace('https://www.iyiou.com/analysis', 'info_more/hangye')">{{item.title}}</a>
                      </div>
                      <div class="desc1" style="margin-top: 25px;">
                        <a>{{item.type}}</a>
                        <span>{{item.author}}</span>
                        <span class="time">{{formatter(item.time, 'yyyy-MM-dd')}}</span>
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
    <div style="">
      <Footer />
    </div>


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
            mark: 0,

            bannerList:[
              require("../assets/left.png"),
              require("../assets/right.png"),
              require("../assets/mid.png"),
              require("../assets/next.png"),
              ],

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
            hangyeParams:{
                url: this.$route.path,
                key: 'hangye'
            },
            items: {
                shangshiItems:[],
                rongziItems:[],
                hangyeItems:[]
            },
        }
    },
    methods: {
        autoPlay () {
          this.mark++;
          if (this.mark === 4) { //当遍历到最后一张图片置零
            this.mark = 0
          }
        },
        play () {
          setInterval(this.autoPlay, 2500)
        },
        change (i) {
          this.mark = i
        },
        next(){
          this.mark++;
          if(this.mark >= this.bannerList.length){
            this.mark=0;
          }
        },
        prev(){
          this.mark--;
          if(this.mark < 0){
            this.mark=this.bannerList.length-1;
          }
        },

      },

    created () {
        //this.now_url = this.$router.path;
        console.log("now_url = ", this.now_url);
        this.play()
        // GetInfoPost(this.shangshiParams).then(response => {
        //     this.items.shangshiItems = response.data.data;
        //     console.log("shangshi = ", this.items.shangshiItems);
        // });

        // GetInfoPost(this.rongziParams).then(response => {
        //     this.items.rongziItems = response.data.data;
        //     console.log("rongzi = ", this.items.rongziItems);
        // });

        GetInfoPost(this.hangyeParams).then(response => {
            this.items.hangyeItems = response.data.data;
            console.log("shangshi = ", this.items.hangyeItems);
        });

      },

    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.header {
   width: 99vw;
   height: 5vw;
}

.c-t-cd {
    margin-top: 1vw;
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
    width: 56%;
    float: left;
    padding-left: 0.5vw;
}
.elib-content {
    background: #fff;
}
.comp-panel {
    margin-bottom: 20px;
    padding-left: 0vw;
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
    margin-left: 0%;
    margin-right: 0%;
}
.col-xs-6 {
    width: 100%;
    margin-top: 10px;
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
    margin-left: 52.3%;
}

.list-item .desc1>a {
    margin-left: -110%;
    float: left;
    color: #999;
}

.list-item .desc1>span {
    margin-left: -60%;
    float: left;
    color: #999;
}
.list-item .desc1>.time {
    float: left;
    margin-left: 55%;
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

.slide {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    // margin-top: 50px;
    overflow: hidden;
    position: relative;
  }
  .slideshow {
    width: 100%;
    height: 100%;
  }
  // li {
  //   position: absolute;
  // }
  img {
    width: 100%;
    height: 100%;
  }
  .bar {
    position: absolute;
    width: 100%;
    bottom: 10px;
    margin: 0 auto;
    z-index: 10;
    text-align: end;
  }
  .bar span {
    width: 20px;
    height: 5px;
    border: 1px solid;
    background: white;
    display: inline-block;
    margin-right: 10px;
  }
  .active {
    background: #bfd6b6 !important;
  }

  .prev,.next{
    position: absolute;
    top: 40%;
    cursor: pointer;
    background-color: rgba(31,45,61,.35);
    border-radius: 10%;
    font-size: 25px;
    font-weight: normal;
    color: white;
    border: hidden;
    line-height: 2;

  }
  .prev{
    left: 0px;
  }
  .next{
    right: 0px;
  }

  .news-text {
      position: absolute;
      display: inline-block;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 11px 104px 11px 16px;
      font-size: 16px;
      line-height: 18px;
      background-color: rgba(0, 0, 0, 0.4);
      color: #fff;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
  }

</style>
