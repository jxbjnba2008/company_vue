<template>
<span>
    <span v-if="data.length<maxLen">
        <span class="tj">{{data}}</span>
    </span>
    <span v-else>
        <span class="tj">{{showBtn?sliceStr:data}}
            <span class="btnWord" @click="showBtn=!showBtn">{{showBtn?"查看更多":"收起"}}</span>
        </span>
    </span>
</span>
</template>

<script>
export default {
    name: "unfold",
    data() {
        return {
            showBtn: true,
        }
    },
    props: {
        // 数据
        data: {
            type: String,
            default: ''
        },
        // 最大长度
        maxLen: {
            type: Number,
            default: 150
        },
    },
    computed: {
        sliceStr() {
            if (this.data != null) {
                return this.data.substring(0, this.maxLen) + "...";
            }
            return '';
        }
    },
}
</script>

<style scoped>
.tj {
    text-align: justify;
}

.btnWord {
    color: cornflowerblue;
    cursor: pointer;
    word-break: keep-all;
}
</style>
