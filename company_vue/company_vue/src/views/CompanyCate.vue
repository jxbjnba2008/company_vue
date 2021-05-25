<template>
  <div style="background-color: #f6f6f6; display: grid;" v-title :data-title='items.companyInfo[0].company_type' v-if="items.companyInfo !== undefined && items.companyInfo.length>0">
    <Header />
  <div class="container m-t-md">
    <Left />
    <div class="elib-main">
        <div class="panel">
          <div class="npanel-body clearfix">
            <div class="page-col">
               <ul class="list-group">
                  <li class="list-group-item list-item" v-for="(item, i) in items.companyInfo" :key="i">
                    <div style="display: grid; padding: 5px 5px;">
                      <div class="title">
                          <a :href="'/company_detail/' + item.company_name" style="color: #212121">{{item.company_name}}</a>
                      </div>
                      <div class="tags-list">
                        <span class="zx-ent-tag blue">
                            {{item.company_status.replace('（在营、开业、在册）', '')}}
                        </span>
                        <span class="zx-ent-tag blue">
                            {{item.industry}}
                        </span>
                      </div>
                      <div class="relate-info">
                        <div class="rline">
                          <span class="f">
                            法定代表人：
                            <span class="fond">{{item.representative}}</span>
                          </span>
                          <span class="f">
                            注册资本：
                            <span class="fond">{{item.registered_capital}}</span>
                          </span>
                          <span class="f">
                            成立时间：
                            <span class="fond">{{item.establishment_date}}</span>
                          </span>
                        </div>
                        <div class="rline">
                          <span class="f">
                            电话：
                            <span class="fond">{{item.tel}}</span>
                          </span>
                          <span class="f">
                            邮箱：
                            <span class="fond"><Unfold :data="item.email.replace(new RegExp(',','gm'),'、')" :maxLen="20"></Unfold></span>
                          </span>
                        </div>
                        <div class="rline">
                          <span class="f">
                            地址：
                            <span class="fond">{{item.source_address}}</span>
                          </span>
                        </div>
                      </div>
                    </div>
                  </li>
               </ul>
            </div>

            <div class="center">
                <ul class="pagination">
                    <li @click="fisrtPage()">
                        <a aria-label="Previous" href="#">
                            <span aria-hidden="true">首页</span>
                        </a>
                    </li>
                    <li :class="pageNo<=1?'disabled':''" @click="prePage()">
                        <a aria-label="Previous" href="#">
                            <span aria-hidden="true">上一页</span>
                        </a>
                    </li>
                    <li>
                        <a style="cursor:default">
                          第{{pageNo}}页
                        </a>
                    </li>

                    <li :class="pageNo>=pageTotal?'disabled':''" @click="nextPage()">
                        <a aria-label="Next" href="#">
                          <span aria-hidden="true">下一页</span>
                        </a>
                    </li>

                    <li @click="finalPage()">
                        <a aria-label="Next" href="#">
                          <span aria-hidden="true">尾页</span>
                        </a>
                    </li>

                    <li>
                        <a style="cursor:default">共{{pageTotal}}页</a>
                    </li>
                </ul>
            </div>

          </div>

        </div>

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
    import Left from "../components/Left.vue";
    import Unfold from "../components/Spread.vue";
    import {GetPagePost} from "../apis/read.js";


    export default {
    name: "CompanyCate.vue",
    components: {
        Left,
        Header,
        Footer,
        Unfold,
        },

    data() {
      return {
        url: this.$route.path,
        pageNo: 1, //当前页码
        pageTotal: '', //总页数
        // rows: 200, //总条数
        pageSize: 10, //每页条数
        //显示分页按钮数
        // showPages: 11,
        //开始显示的分页按钮
        // showPagesStart: 1,
        //结束显示的分页按钮
        // showPageEnd: 100,
        title: '',
        items: {
          companyInfo: []
        }
      }
    },
    created() {
        this.getData();
    },

    methods:{
      getData:function (i){
              this.pageNo = i || this.pageNo;

              GetPagePost(this.url, this.pageNo, this.pageSize).then(resp => {
                  console.log("Page : resp.data.data", resp.data.data);
                  this.items.companyInfo = resp.data.data
                  this.pageTotal = resp.data.num
          });
        },
          //首页
      fisrtPage:function (){
        this.getData(1)
      },
      //当前页
      curPage:function (i){
          this.getData(i)
      },
      //上一页
      prePage:function (){
        if(this.pageNo>1){
            this.getData(--this.pageNo);
        }
      },

      //下一页
      nextPage:function (){
        if(this.pageNo<this.pageTotal){
            this.getData(++this.pageNo);
        }
      },
      //尾页
      finalPage:function (){
        this.getData(this.pageTotal)
      },
    }
}
</script>

<style scoped>
  .container {
      width: 1250px;
  }

  .m-t-md {
      margin-top: 20px;
  }

  .npanel-body{
    width: 100%;
  }

  .elib-main {
      width: 78%;
      float: left;
      margin-left: 1%;
  }

  .panel {
      /* border-radius: 6px; */
      box-shadow: none;
      /* border: solid 1px #eeeeee; */
      width: 100%;
  }

  ul.pagination {
      display: inline-block;
      padding: 0;
      margin: 0;
  }

  ul.pagination li {display: inline;}

  ul.pagination li a {
      color: black;
      float: left;
      padding: 4px 8px;
      text-decoration: none;
      border-radius: 5px;
      transition: background-color .3s;
      border: 1px solid #cccccc;
      margin: 0 4px;
      font-size: 14px;
  }

  ul.pagination li a.active {
      /*background-color: #128bed;*/
      color: white;
      border-radius: 5px;
  }

  ul.pagination li a:hover:not(.active) {background-color: #f8cfd0;}
  div.center {text-align: center;}


  .page-col {
      position: relative;
      min-height: 1px;
      float: left;
      padding-left: 0;
      padding-right: 0;
      width: 100%;
      margin-left: 0;
  }
  .list-group {
      border-radius: 2px;
  }
  .list-group {
      padding-left: 0;
      margin-bottom: 20px;
  }
  .list-group >li:hover{
      box-shadow: 5px 5px 30px rgba(38, 38, 38, 0.25);
      opacity: 0.96;
      -webkit-transform: translatex(25px);
      -moz-transform: translatex(25px);
      transform: translatex(1px)
  }

  .list-item {
      padding: 12px 15px;
      border-radius: 0px !important;
  }
  .list-group-item {
      border-color: #eeeeee;
  }
  .list-group-item {
      position: relative;
      display: block;
      margin-bottom: -1px;
      background-color: #fff;
      border: 1px solid #ddd;
  }
  .list-item .title {
      font-size: 18px;
      font-weight: bold;
      line-height: 25px;
      height: 20px;
      display: table-cell;
      vertical-align: top;
      color: #333;
  }
  .list-item .title>a {
      color: #3c4144;
      text-decoration: none;
  }
  .list-item .desc {
      font-size: 14px;
      margin-top: 10px;
  }
  .list-item .desc>a {
      margin-right: 15px;
      color: #666;
  }
  .list-item .desc>.time {
      float: right;
  }
  .list-item .desc>span {
      margin-right: 10px;
      color: #999;
  }

  .tags-list {
      float: left;
      /* max-width: 630px; */
  }

  .tags-list .zx-ent-tag {
      border-radius: 3px;
      float: left;
      padding: 2px 6px;
      font-size: 12px;
      line-height: 16px;
      margin-top: 12px;
      /* border: 1px solid #bd3134; */
      background: #fff0f0;
  }

  .blue {
      color: #bd3134;
  }

  .tags-list .zx-ent-tag+.zx-ent-tag {
      margin-left: 8px;
  }

  .relate-info {
      margin-top: 8px;
      line-height: 28px;
      color: #999;
      font-size: 14px;
  }
  .ntable-list .rline:not(:last-child) {
      margin-bottom: 5px;
  }
  .relate-info .f {
      margin-right: 50px;
  }
  .relate-info .fond {
      color: #666;
  }

</style>
