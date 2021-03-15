<template>
  <div style="background-color: #f6f6f6;">
    <Header />
  <div class="container m-t-md">
    <Left />
    <div class="elib-main">
        <div class="panel elib-content">
          <div class="npanel-body clearfix">
              <table class="ntable">
                  <tbody>
                      <tr>
<!--                        <th width="20">序号</th>-->
                        <th width="160">企业名称</th>
                        <th width="80">企业类型</th>
                        <th width="80">企业电话</th>
                        <th width="80">企业邮箱</th>
                      </tr>
                      <tr v-for="(item, i) in items.companyInfo" :key="item.i">
<!--                        <td class="text-center">{{i+1}}</td>-->
                        <td class="text-center">
                            <a :href="'/company_detail/' + item.company_name" style="color: #94000c">{{item.company_name}}</a>
                        </td>
                        <td class="text-center">{{item.company_type}}</td>
                        <td class="text-center">{{item.tel}}</td>
                        <td class="text-center" style="white-space: pre-line;">{{item.email.split(',').join('\n')}}</td>
                      </tr>
                  </tbody>
              </table>
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
  <div style="margin-top: 1200px"></div>
  <Footer />

  </div>
</template>

<script>
    import Header from "../components/Header.vue";
    import Footer from "../components/Footer.vue";
    import Left from "../components/Left.vue";
    import {GetPagePost} from "@/apis/read.js";


    export default {
    name: "CompanyCate.vue",
    components: {
        Left,
        Header,
        Footer
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
        items: {
          companyInfo: []
        }
      }
    },
    created() {
        this.getData()
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
      background: #fdeeee;
      border: #faeded 1px solid;
      border-collapse: collapse;
      padding: 12px 12px 12px 12px;
      font-weight: normal;
      color: #444;
      line-height: 19px;
      font-size: 15px;
  }
  .elib-main {
      width: 850px;
      float: right;
      margin-left: 16px;
  }
  .elib-content {
      background: #ffffff;
  }

  .panel {
      border-radius: 10px;
      box-shadow: none;
      border: solid 1px #eeeeee;
      width: 110%;
  }
  .text-center {
      text-align: center;
  }
  .ntable td {
      padding: 10px 10px 11px 10px;
      border: #faeded 1px solid;
      word-break: break-all;
      font-size: 14px;
      line-height: 1.6;
      color: #222;
      word-wrap: break-word;
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
        border: 1px solid #94000c;
        margin: 0 4px;
        font-size: 14px;
    }

    ul.pagination li a.active {
        /*background-color: #128bed;*/
        color: white;
        border-radius: 5px;
    }

    ul.pagination li a:hover:not(.active) {background-color: #c6646d;}
    div.center {text-align: center;}

</style>
