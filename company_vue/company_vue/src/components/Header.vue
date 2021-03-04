<template>
  <header class="box-shadow ">
    <div>
      <b-navbar toggleable="lg" type="light" variant="light">
<!--        <b-navbar-brand><img src="https://www.qcc.com/material/theme/chacha/cms/v2/images/logo4.png" alt="" height="50" width="80"></b-navbar-brand>-->
<!--        <b-navbar-brand class="container"></b-navbar-brand>-->

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-brand class="alsp" href="/">
            <p style="margin-bottom: -10px;">GalaxyInfor</p>
            <em style="font-size: 1px;color: #9d6b6b">More Than Data !</em>
          </b-navbar-brand>
          <b-navbar-brand class="alsp1" href="/info_more/shangshi">上市信息</b-navbar-brand>
          <b-navbar-brand class="alsp1" href="/info_more/rongzi">创投资讯</b-navbar-brand>
          <b-navbar-brand class="alsp1" href="/info_more/hangye">行业分析</b-navbar-brand>
          <b-navbar-brand class="alsp1" href="/info_more/death">死亡公司</b-navbar-brand>
          <ul  class="navbar-nav ml-auto container1">
            <li  class="form-inline">
              <div  class="form-inline" style="width:470px;">
                <label>
                  <input v-model="search.key" type="text" style="width:200px;height: 35px;border-radius: 15px;" placeholder="请输入企业名称" class="form-control headerKey active" >
                </label>
                <button @click="onSearch" type="submit" style="margin-left: 15px;" class="btn">
                  <span>开始查询</span>
                </button>
              </div>
            </li>
          </ul>
        </b-collapse>
      </b-navbar>
    </div>
    </header>
</template>

<script>
   import { stripscript } from "../apis/validate.js";

export default {
    name:"Header",
    data() {
        return {
            now_url: this.$route.path,
            headerData: {},
            search:{
                key:''
            }
        }
    },

    methods: {
       onSearch () {
          console.log("search.key = ", this.search.key);
          if(stripscript(this.search.key) === false || this.search.key === ''){
            alert("您输入的信息有误，请确认后重新输入");
          }else{
            this.$router.push({
              path: '/search',
              query:{
                q: this.search.key
              }
            });
          }
      }
    }
}
</script>

<style lang="scss" scoped> // lang告诉解释其css符合什么编译器的语法; scoped：当前vue文件生效，没有scoped则全局生效
.alsp {
    font-family: DFKai-SB,sans-serif;
    font-weight: bold;
    color: #94000c;
    margin-left: 11.98vw;
}
.alsp1 {
    font-family: KaiTi,serif;
    font-weight: bold;
    color: #a0323a;
    margin-left: 1.2vw;
    font-size: 1.2vw;
}
.btn {
    background-color: #bf5860;
    border-color: #b57f82;
    color: #ffffff;
    padding: 7px 10px;
    font-size: 12px;
    border-radius: 13px;
}
.container {
    padding-right: 200px;
    padding-left: 100px;
    margin-right: auto;
    margin-left: auto;
}
.container1 {
    //padding-right: 400px;
    padding-left: 1px;
    //margin-right: auto;
    //margin-left: auto;
}
//.navi-header {
//    //height: 2.92vw;
//    background: #ffffff;
//    position: relative;
//    z-index: 1000;
//    min-width: 65.1vw;
//}
.box-shadow {
    box-shadow: 0 2px 2px rgba(0,0,0,0.05), 0 1px 0 rgba(0,0,0,0.05);
}
input::-webkit-input-placeholder{
        color: #d0cece;
    }
    input::-moz-placeholder {
        /* Mozilla Firefox 19+ */
        color: #d0cece;
    }
    input:-moz-placeholder {
        /* Mozilla Firefox 4 to 18 */
        color: #d0cece;
    }
    input:-ms-input-placeholder {
        /* Internet Explorer 10-11 */
        color: #d0cece;
    }

</style>
