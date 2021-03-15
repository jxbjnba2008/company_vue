<template>
      <div class="eo-home-right">
          <div class="eo-briefing m-b-32">

            <div class="eo-title-box fz18">
              <span class="span-line">快 讯</span>
                <a href="/info_more/info" style="margin-left: 127px;color: #94000c;font-size: 14px">更多></a>
            </div>
            <div class="ranking_wrap ranking_roll">
            <vue-seamless-scroll :data="items.InfoItems" class="seamless-warp" :class-option="classOption">
                <ul v-for="(item,i) in items.InfoItems" :key="i" style="list-style: none;margin-left: -35px;margin-bottom:0">
                    <li class="eo-bottom-dashed">
                        <a class="eo-line-clamp-2" :href="item.url" target="_blank">{{item.title}}</a>
                        <span class="time">
                          {{formatter(item.time, 'yyyy-MM-dd')}}
                        </span>
                    </li>
                </ul>
            </vue-seamless-scroll>
            </div>
        </div>
      </div>
</template>

<script>
    import {GetInfoPost} from "@/apis/read.js";
    import {formatter} from "../utils/date.js";
    import vueSeamlessScroll from 'vue-seamless-scroll'

    export default {
      name: "Right",
      components: {    //组件
            vueSeamlessScroll
      },
      data() {
        return {
            formatter,
            now_url: this.$route.path,
            InfoParams:{
                url: this.$route.path,
                key: 'info'
            },
            items: {
                InfoItems:[],
            },
        }
      },
      computed: {

      classOption () {
           return {
            step: 0.5, // 数值越大速度滚动越快
            limitMoveNum: 2, // 开始无缝滚动的数据量 this.dataList.length
            hoverStop: true, // 是否开启鼠标悬停stop
            direction: 1, // 0向下 1向上 2向左 3向右
            openWatch: true, // 开启数据实时监控刷新dom
            singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
            singleWidth: 0, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
            waitTime: 1000 // 单步运动停止的时间(默认值1000ms)
          }
        }
      },
      created () {
        console.log("now_url = ", this.now_url);

        GetInfoPost(this.InfoParams).then(response => {
            this.items.InfoItems = response.data.data;
            console.log("InfoItems = ", this.items.InfoItems);
        });
      },
      // mounted() {
      //   this.scroll()
      // },

  methods: {
          scroll:function () {
              let area = document.getElementById('wrapper');
              let iliHeight = 24;//单行滚动的高度
              let speed = 50;//滚动的速度
              let time;
              let delay= 0;
              area.scrollTop=0;
              area.innerHTML+=area.innerHTML;//克隆一份一样的内容
              function startScroll(){
                time=setInterval(scrollUp,speed);
                area.scrollTop++;
              }
              function scrollUp(){
                if(area.scrollTop % iliHeight===0){
                  clearInterval(time);
                  setTimeout(startScroll,delay);
                }else{
                  area.scrollTop++;
                  if(area.scrollTop >= area.scrollHeight/2){
                    area.scrollTop =0;
                  }
                }
              }
              setTimeout(startScroll,delay)
        },
      },

  }

</script>

<style scoped lang="scss">
.ranking_roll {
    max-height: 600px;
    overflow: hidden;
}
.eo-home-right {
  width: 21%;
  margin-left: auto;
}
.eo-briefing {
    padding: 15px 12px 12px;
    box-sizing: border-box;
    border: 1px solid #eaeaea;
    overflow: hidden;
    background: #fffcf5;
}
.m-b-32 {
    margin-bottom: 32px;
}
.eo-title-box {
    font-size: 24px;
    color: #333;
    position: relative;
    font-weight: 700;
}
.eo-title-box.fz18 {
    font-size: 18px;
    line-height: 18px;
    margin-bottom: 24px;
}
.eo-title-box .span-line:after {
    content: "";
    position: absolute;
    top: 26px;
    left: 0px;
    width: 21%;
    height: 4px;
    border-radius: 4px;
    background: #d25720;
    color: #f04b00;
}

.eo-briefing .brief-lists-scroll {
    position: relative;
    transition: top 0.5s;
}
li {
    padding: 8px 0;
}
li a {
    font-family: PingFangSC,serif;
    font-size: 12px;
    line-height: 10px;
    max-height: 40px;
        //line-height: 50px;
    text-align: center;
    color: #505050;
}
li .time {
    font-family: SourceSansPro-Regular,serif;
    font-size: 5px;
    color: #818080;
    //line-height: 16px;
    display: flex;
    align-items: center;
    margin-left: 140px;
}
.eo-bottom-dashed {
    border-bottom: 1px dotted rgb(250, 122, 122);
}
.eo-line-clamp-2 {
    text-decoration:none;
    color: #e07a7a;
}

.seamless-warp{
  width: 100%;
  height: calc(100% - 16px);
  overflow: hidden;
}
</style>
