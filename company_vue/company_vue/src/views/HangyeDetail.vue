<template>
    <div style="background-color: #f6f6f6;">
    <Header />
    <div class="container m-t">
        <h1>{{items.baseInfo.title}}</h1>
        <div class="contant">
            <div class="post-top-bar eo-flex">
                <span class="type">
                  <a>
                    <em>{{items.baseInfo.type}}</em>
                  </a>
                </span>
                <span><em>作者：{{items.baseInfo.author}}</em></span>
              <span><em>{{items.baseInfo.time}}</em></span>
            </div>
        <div v-html="items.baseInfo.html_content"></div>
        <div style="height:1px; margin-top:-1px;clear: both;overflow:hidden;"></div>
        </div>
    </div>

  <Footer />

  </div>
</template>

<script>
    import Header from "../components/Header.vue";
    import Footer from "../components/Footer.vue";
    import { GetHangyeDetail } from "../apis/read.js";

    export default {
      name: "HangyeDetail.vue",
      components: {
        Header,
        Footer
      },
      data() {
        return {
          'url': this.$route.path,

          items: {
              baseInfo: {},
          }
        }
      },
      created () {
        console.log('url: ', this.$route.path)
        GetHangyeDetail(this.url).then(resp =>{
            console.log("In baseInfo resp.data = ", resp.data.data);
            this.items.baseInfo = resp.data.data;
            document.title = this.items.baseInfo.title
        });
      }
    }
</script>

<style scoped>
.container {
    width: 960px;
}
.m-t {
    margin-top: 15px;
    margin-left: auto;

}
h1 {
    font-size: 36px;
    color: #333;
    line-height: 50px;
    margin-bottom: 32px;
}
.post-top-bar {
    padding-bottom: 8px;
    margin-bottom: 16px;
    border-bottom: 1px dotted rgba(51,51,51,.2);
    flex-wrap: wrap;
}
.eo-flex {
    display: flex;
}
.post-top-bar span {
    font-size: 14px;
    color: #333;
    padding: 0 16px;
    border-right: 1px dashed rgba(51,51,51,.2);
    vertical-align: middle;
    position: relative;
    left: -16px;
    margin-bottom: 8px;
}
img {
  height: auto;
  max-width: 100%;
}
</style>
