<template>
  <div class="box-shadow">

        <div id="nav-collapse" style="display: flex;">
          <div class="alsp">
            <p class="logo"><a href="/" style="color: #94000c;text-decoration: none">星空资讯</a></p>
            <em class="logo-text">Galaxy Info</em>
          </div>
          <div style="position: relative; left: 25vw;display: flex;">
            <div class="alsp1"><a href="/info_more/shangshi" style="color: #a0323a;text-decoration: none">上市信息</a></div>
            <div class="alsp1"><a href="/info_more/rongzi" style="color: #a0323a;text-decoration: none">创投资讯</a></div>
            <div class="alsp1"><a href="/info_more/hangye" style="color: #a0323a;text-decoration: none">行业分析</a></div>
            <div class="alsp1"><a href="/info_more/death" style="color: #a0323a;text-decoration: none">死亡公司</a></div>
            <div class="alsp1"><a href="/map/all" style="color: #a0323a;text-decoration: none">数据地图</a></div>
          </div>

          <div style="position: relative; left: 28vw; margin-top: 0.6vw;">
            <ul  class="navbar-nav">

                <div class="form-inline">
                  <label>
                    <input v-model="search.key" type="text" style="width:15vw;height: 2vw;border-radius: 1vw;" placeholder="请输入企业名称" class="form-control" >
                  </label>
                  <button @click="onSearch" type="submit" style="margin-left: 1vw;" class="btn">
                    <span>开始查询</span>
                  </button>
                </div>

            </ul>
          </div>

      </div>

    </div>
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

<style lang="scss" scoped>
.alsp {
    font-family: DFKai-SB,sans-serif;
    font-weight: bold;
    margin-top: 0.6vw;
    position: relative;
    left: 19vw;
}
.logo {
    font-family: DFKai-SB,sans-serif;
    margin-bottom: -0.6vw;
    font-size: 1.2vw;
}
.logo-text {
    font-size: 0.66vw;
    color: #9d6b6b;
}
.alsp1 {
    font-family: KaiTi,serif;
    font-weight: bold;
    margin-left: 2vw;
    // position: relative;
    // left: 2vw;
    font-size: 1.2vw;
    transform: translate(-50%, -50%);
    transition: color .5s;
    margin-top: 2vw;
}
.alsp1::before {
    content: "";
    position: absolute;
    left: 0;
    bottom: -0.3vw;
    width: 0;
    height: 0.4vw;
    background: #b30707;
    z-index: -1;
    transition: width .5s;
}
.alsp1:hover::before {
    width: 4.9vw;
}


.btn {
    background-color: #94000c;
    border-color: #b57f82;
    color: #ffffff;
    padding: 0.4vw 1vw;
    font-size: 0.5vw;
    border-radius: 0.8vw;
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
