<template>
      <div class="filterItem mb10">
          <div class="filterTile fc6 mr14">分类标签</div>
          <span v-for="(item,i) in tagItems" :key="i" :class="item.url + '/fenlei' === url ? 'active':''">
            <a :href="item.url + '/fenlei'">
              <span>{{item.tag}}</span>
            </a>
          </span>
      </div>
</template>

<script>
export default {
    name: "RongziFenleiTag.vue",
    data() {
        return {
            url: this.$route.path,
            tagItems: [
              {'tag': '不限', 'url': '/all'},
              {'tag': 'IPO排队', 'url': '/ipo'},
              {'tag': '投资事件', 'url': '/tz'},
              {'tag': '人事变动', 'url': '/rs'},
              {'tag': '收购事件', 'url': '/sg'},
              {'tag': '上市事件', 'url': '/ss'},
              {'tag': '退出事件', 'url': '/tc'},
              {'tag': '坏消息', 'url': '/hx'},
              {'tag': '产品发布', 'url': '/cp'},
              {'tag': '退市事件', 'url': '/ts'},
              {'tag': '机构要闻', 'url': '/jg'},
              {'tag': '募资事件', 'url': '/mz'},
              {'tag': 'VC洞见', 'url': '/vc'},
              {'tag': '合并事件', 'url': '/hb'},
            ],
            tags: ['IPO排队', '投资事件', '人事变动', '收购事件', '上市事件', '退出事件', '坏消息', '产品发布', '退市事件',
              '机构要闻', '募资事件', 'VC洞见', '合并事件']

        }
    },
    created() {
            console.log("url = ", this.url);
        },
}

</script>

<style scoped>

.filterItem {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
}
.mb10 {
    margin-bottom: 20px;
}
.filterItem {
    font-size: 10px;
    height: 20px;
    line-height: 20px;
    min-width: 48px;
}
.fc6 {
    color: #666;
}
.mr14 {
    margin-right: 14px;
}

/*.tag {*/
/*    height: 20px;*/
/*    line-height: 20px;*/
/*    padding: 0 6px;*/
/*    margin-bottom: 5px;*/
/*    margin-right: 4px;*/
/*    cursor: pointer;*/
/*    font-size: 10px;*/
/*}*/
.mb10 >span{
    height: 20px;
    line-height: 20px;
    padding: 0 6px;
    margin-bottom: 5px;
    margin-right: 4px;
    cursor: pointer;
    font-size: 12px;
}
.mb10 >span> a{
    color: #0e0e0e;
}
.mb10 >span.active > a{
    background: #e76969;
    border-radius: 2px;
    color: #323232;
    text-align: center;
}
</style>
