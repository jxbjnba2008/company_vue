<template>
<div id="CompanySearch" style="background-color: #f6f6f6;">
    <Header />
    <div class="container m-t-md">
    <Left />
    <div class="elib-main">
        <div class="panel elib-content">
          <div class="npanel-body clearfix">
              <table class="ntable">
                  <tbody>
                      <tr>
                        <th width="20">序号</th>
                        <th width="160">企业名称</th>
                        <th width="80">企业类型</th>
                        <th width="80">企业电话</th>
                        <th width="80">企业邮箱</th>
                      </tr>
                      <tr v-for="(item, i) in searhResult.items" :key="item.i">
                        <td class="text-center">{{i+1}}</td>
                        <td class="text-center">
                            <a :href="'/company_detail/' + item.company_name" style="color: #94000c">{{item.company_name}}</a>
                        </td>
                        <td class="text-center">{{item.company_type}}</td>
                        <td class="text-center">{{item.tel}}</td>
                        <td class="text-center">{{item.email}}</td>
                      </tr>
                  </tbody>
              </table>
              <div>
                  <a style="font-size: 10px">*默认最多显示10条数据</a>
              </div>
          </div>
        </div>
      </div>

    </div>

<!--    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>-->
<!--    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>-->
    <Footer  style="margin-top: 900px;"/>

</div>

</template>


<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Left from "../components/Left.vue";
import { GetInfoPost } from "../apis/read.js";

export default {
  name: "CompanySearch",
  components: {
    Header,
    Footer,
    Left
  },
  data() {
        return {
            now_url: this.$route.path,
            headerData: {},
            searchParma: {
                url: this.$route.path,
                key: this.$route.query.q
                },
            searhResult: {
                items:[]
            }
        }
    },
  created () {
      console.log("this.searchParma = ", this.searchParma);
      GetInfoPost(this.searchParma).then(resp => {
          console.log("in Search resp.data.data = ", resp.data.data);
          this.searhResult.items = resp.data.data
  });
  }
};
</script>
<style lang="scss" scoped>
  .container {
      width: 1250px;
  }

  .m-t-md {
      margin-top: 20px;
  }
  .elib-main {
      width: 850px;
      float: right;
      margin-left: 16px;
  }
  .elib-content {
      background: #ffffff;
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
  .panel {
      border-radius: 1px;
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

</style>
