<template>
  <header class="box-shadow">
    <div>
      <b-navbar toggleable="lg" type="light" variant="light">
<!--        <b-navbar-brand><img src="https://www.qcc.com/material/theme/chacha/cms/v2/images/logo4.png" alt="" height="50" width="80"></b-navbar-brand>-->
<!--        <b-navbar-brand class="container"></b-navbar-brand>-->

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-brand class="alsp" href="/">
            <p style="margin-bottom: -10px;">GalaxyInfor</p>
            <em style="font-size: 1px;color: #9d6b6b">More Than Data !</em>
          </b-navbar-brand>
          <div style="margin-left: 6.5%">
            <b-navbar-brand class="alsp1" href="/info_more/shangshi">上市信息</b-navbar-brand>
            <b-navbar-brand class="alsp1" href="/info_more/rongzi">创投资讯</b-navbar-brand>
            <b-navbar-brand class="alsp1" href="/info_more/hangye">行业分析</b-navbar-brand>
            <b-navbar-brand class="alsp1" href="/info_more/death">死亡公司</b-navbar-brand>
            <b-navbar-brand class="alsp1" href="/map/all">数据地图</b-navbar-brand>
          </div>
<!--          <b-navbar-brand class="move"></b-navbar-brand>-->
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
    name: "Header",
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
    margin-left: 16%;
}
.alsp1 {
    font-family: KaiTi,serif;
    font-weight: bold;
    color: #a0323a;
    margin-left: 1.2vw;
    font-size: 1.2vw;
    transform: translate(-50%, -50%);
    transition: color .5s;
    margin-top: 33px;
}
.alsp1::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0;
    height: 0.4vw;
    background: #b30707;
    z-index: -1;
    transition: width .5s;
}
.alsp1:hover::before {
    width: 4.9vw;
}
.move{
    width: 81px;
    border-top: 5px solid #a0323a;/*只需要将上边显示出来*/
    border-radius: 3px;

    position: absolute;
    left: 356px;
    top: 60px;
    transition: left .1s ease-in-out 0.1s;/*包含四个过度属性：执行变换属性、执行时间、速率、延迟*/
    -webkit-transition: left .2s ease-in-out 0.1s;/*chrome和safari*/
    -moz-transition: left .2s ease-in-out 0.1s;/*firefox*/
    -o-transition: left .2s ease-in-out 0.1s;/*opera*/
}
.alsp1:nth-child(1):hover~ .move{    /*li元素的父元素的第一个子元素，当鼠标停留其上时，move元素的left属性改变*/
    left: 0px;
}
.alsp1:nth-child(2):hover~ .move{
    left: 356px;
}
.alsp1:nth-child(3):hover~ .move{
    left: 465px;
}
.alsp1:nth-child(4):hover~ .move{
    left: 596px;
}
.alsp1:nth-child(5):hover~ .move{
    left: 725px;
}
.alsp1:nth-child(6):hover~ .move{
    left: 853px;
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
    padding-left: 1px;

}

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
