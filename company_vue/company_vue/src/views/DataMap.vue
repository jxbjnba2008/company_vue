<template>
  <div style="background-color: #f6f6f6;" v-title data-title="数据地图">
    <Header />
    <div class="container c-t-cd">
<!--      <Left />-->

      <div class="hello">
        <div class="drop-box">
          <b-dropdown id="dropdown" text="数 据 地 图 企 业 标 签" variant="light" class="m-2">
            <b-dropdown-item href="/map/gaoxin"><span class="a_text">高新技术企业</span></b-dropdown-item>
            <b-dropdown-item href="/map/kj_xing"><span class="a_text">科技型中小企业</span></b-dropdown-item>
            <b-dropdown-item href="/map/js_xianjin"><span class="a_text">技术先进型服务企业</span></b-dropdown-item>
            <!--          <b-dropdown-divider></b-dropdown-divider>-->

          </b-dropdown>
        </div>
        <!-- 初始化echarts需要个有宽高的盒子 -->
        <div ref='mapbox' class="mapbox"></div>
      </div>
    </div>
    <div style="margin-top: 10%"></div>
    <Footer />
  </div>
</template>


<script>
    // const echarts = require('echarts');
    import * as echarts from 'echarts/lib/echarts';
    import 'echarts/lib/chart/map';
    import 'echarts/map/js/china.js';
    import jsonp from 'jsonp';
    import Header from "../components/Header";
    import Footer from "../components/Footer";
    import {GetInfoPost} from "../apis/read";
    import {formatter} from "../utils/date";

    const option = {
      title:{
        text:"企业数据地图",
        top: "5%",
        left: "5%",
        // link:"https://blog.csdn.net/image_fzx",
        // subtext:"疫情期间找工作---work hard!!!!",
        // sublink:"https://blog.csdn.net/image_fzx"
      },
// ----------   series：地图数据可视化，添加data数据    ---------------------

      series:[{
        name:"",
        type:'map', // 告诉echarts 要去渲染的是一个地图
        map:'china',// 告诉echarts  要去渲染中国地图
        label:{    // 控制对应地区的汉字
          show:true,
          color:'#333333',// 控制地区名的字体颜色---黑色，省名字
          fontSize:12
        },
        itemStyle:{      // 地图板块的颜色和边框---灰色，各个省界线
          areaColor:'#cd5c5c',
          borderColor:'#d78865'
        },
        roam:true,
        zoom: 1,// 控制地图的放大和缩小
        emphasis:{    // 控制鼠标滑过之后的背景色和字体颜色--白色
          label:{
            color:'#cb1919',
            fontSize:12
          },
          itemStyle:{
            areaColor:'#f5d07d'   //  滑动到哪个地区就显示
          }
        },
        data:[]    // 用来展示后台给的数据的 {name:xx,value:xxx}
      }],

//-----------    visualMap：视觉映射，每个颜色代表什么含义   -----------------------------
      visualMap:[{
        type:'piecewise',
        show:true,
        bottom: "5%",
        left: "5%",
        // splitNumber:4
        pieces:[           // 分段
          {min:10000},
          {min:1000,max:9999},
          {min:100,max:999},
          {min:10,max:99},
          {min:1,max:9}
        ],
        // align:'right',// 默认left
        // orient:'horizontal' 默认竖直
        // left right 这些属性控制 分段坐在的位置
        // showLabel:false
        // textStyle:{}
        inRange:{
          symbol:'rect',
          color:['#ffa997','#ac1313']   //   浅红~~深红色
        },
        itemWidth:20,
        itemHeight:10
      }],

//-------------------------------------------------------------------
      tooltip:{
        trigger:'item'
      },
      toolbox: {
        show: true,
        orient: 'vertical',
        right: "5%",
        top: 'center',
        feature: {
          dataView: {
            // readOnly: true
          },
          // restore: {},
          saveAsImage: {},
        },
      },
    };

    export default {
      name: 'DataMap',
      components: {
        Header,
        Footer,
      },
      data() {
        return {
          now_url: this.$route.path,
          params: {
            url: this.$route.path,
            key: ''
          },

        }
      },
      mounted() {
        GetInfoPost(this.params).then(response => {
          option.series[0].data = response.data.data.map(item=>({name:item.name,value:item.value}));
          option.series[0].name = response.data.company_type
          console.log("mychart = ", option.series[0].data);
          this.mychart.setOption(option);
        });

        // this.getData();// 为什么不再created
        this.mychart = echarts.init(this.$refs.mapbox);
        this.mychart.setOption(option)
      },
      methods:{

        getData(){
          jsonp('https://interface.sina.cn/news/wap/fymap2020_data.d.json?_=1580892522427',{},(err,data)=>{
            if(!err){             // 代表请求数据成功
              console.log(data);
              let list = data.data.list.map(item=>({name:item.name,value:item.value}))
              console.log(list);
              option.series[0].data = list;
              this.mychart.setOption(option);
              // 这行代码能执行的前提是 DOM已经渲染完成，只有DOM渲染完成才能够执行 echarts初始化
            }
          })
        }
      }
    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.c-t-cd {
  margin-top: 1%;
}
.hello {
  margin-left: -5%;
}
.drop-box {
  display:inline;
  position: relative;
  left: 30px;
  top: 15px;
}
.mapbox {
  width: 950px;
  height: 666px;
  margin-left: 20%;
  margin-top: -5%;
}
.a_text {
  font-size: 15px;
}
</style>

