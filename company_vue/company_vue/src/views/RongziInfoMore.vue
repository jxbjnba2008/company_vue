<template>
    <div style="background-color: #f6f6f6;" v-title data-title="创投资讯">
      <Header />
      <div class="container m-t">
          <div class="row">
            <div class="col-md-12">
                <ul class="breadcrumb" style="background:none;border:none;">
                  <li>
                      <a style="color: #94000c;font-weight: bold" href="/">
                        首页->
                      </a>
                  </li>
                  <li>
                      <a href="/info_more/rongzi" style="color:#181818;font-weight: bold">融资信息</a>
                  </li>
                </ul>
            </div>
            <div class="page-col">
            <RongziFenleiTag />
               <ul class="list-group">
                  <li class="list-group-item list-item" v-for="(item, i) in items.rongziItems" :key="i">
                      <div class="title">
                          <a target="_blank" style="color: #1d1f21;font-weight: 650" :href="item.url">
                            {{item.title}}
                          </a>
                      </div>
                      <div class="desc">
                          <div>
                              <a style="color: #535863; text-decoration: none;cursor:default">{{item.des}}</a>
                              <a rel="noopener noreferrer" :href="item.url" class="primary-text">查看详情</a>
                          </div>
                          <span style="float: left; margin-top: 10px; color: #94000c">{{item.event_type}}</span>
                          <span class="time" style="margin-top: 10px;">{{formatter(item.event_time, 'yyyy-MM-dd')}}</span>
                      </div>
                  </li>
               </ul>
            </div>
            <div class="center" style="margin: auto; margin-top: 60px">
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
                          <a style="cursor:default">第{{pageNo}}页</a>
                      </li>

                      <li :class="pageNo>=pageTotal?'disabled':''" @click="nextPage()">
                          <a aria-label="Next" href="#">
                            <span aria-hidden="true">下一页</span>
                          </a>
                      </li>
                      <li>
                          <a style="cursor:default">共{{pageTotal}}页</a>
                      </li>
                  </ul>
              </div>
          </div>
      </div>
      <Footer />
    </div>
</template>

<script>
    import Header from "../components/Header.vue";
    import Footer from "../components/Footer.vue";
    import RongziFenleiTag from "../components/RongziFenleiTag.vue"
    import {GetPagePost} from "@/apis/read.js";
    import {formatter} from "../utils/date.js";

    export default {
      name: "RongziInfoMore.vue",
      components: {
        Header,
        Footer,
        RongziFenleiTag
        },
      data() {
            return {
                formatter,
                url: this.$route.path,
                pageNo: 1, //当前页码
                pageTotal: 100, //总页数
                pageSize: 10, //每页条数

                items: {
                    rongziItems:[],
                },
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
                    this.items.rongziItems = resp.data.data
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
    }
}
</script>

<style scoped>
.container {
    width: 1250px;
}
.m-t {
    margin-top: 15px;
}
.row {
    margin-right: -15px;
    margin-left: 80px;
}
.col-md-12 {
    width: 100%;
}

.breadcrumb {
    padding-left: 10px;
    margin-bottom: 10px;
}

.breadcrumb {
    padding: 8px 15px;
    list-style: none;
    border-radius: 4px;
}
.breadcrumb > li {
    display: inline-block;
}

.page-col {
    position: relative;
    min-height: 1px;
    float: left;
    padding-left: 15px;
    padding-right: 7px;
    width: 936px;
    margin-left: 10px;
}

.list-group {
    border-radius: 2px;
}
.list-group {
    padding-left: 0;
    margin-bottom: 20px;
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
.primary-text {
    color: #3b3b3b;
    font-weight: bold;
}
.list-item .title {
    font-size: 16px;
    line-height: 19px;
    height: 30px;
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
    margin-bottom: 8px;
    margin-right: 15px;
}
.list-item .desc>.time {
    float: right;
}
.list-item .desc>span {
    margin-right: 10px;
    color: #999;
}

/*分页样式*/
    ul.pagination {
        display: inline-block;
        padding: 0;
    }

    ul.pagination li {
      display: inline;

    }

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

    ul.pagination li a:hover:not(.active) {
        background-color: #c6646d;
    }
    div.center {text-align: center;}
</style>
