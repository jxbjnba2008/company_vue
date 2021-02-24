<template>
    <div style="background-color: #f6f6f6;">
    <Header />
    <div class="container c-t-cd">
        <Left />
        <div class="company-box">
            <div class="new-box new-box-p">
                <div class="titlebar">
                    <h2 class="title-info"> 工商信息 </h2>
                </div>
                <section class="section-box">
                    <div class="tcaption">
                        <span class="title">{{url.replace('/company_detail/', '')}} -> </span>
                        <span class="">基本信息</span>
                        <table class="newtable">
                            <tbody>
                                <tr>
                                  <td width="16%" class="tb">法定代表人</td>
                                  <td class="ta">{{items.baseInfo['representative']}}</td>
                                  <td width="14%" class="tb">登记状态</td>
                                  <td width="21%" class="ta">{{items.baseInfo['company_status']}}</td>
                                  <td width="5%" class="tb">成立日期</td>
                                  <td width="32%" class="ta">{{items.baseInfo['establishment_date']}}</td>
                                </tr>
                                <tr>
                                  <td class="tb"> 注册资本 </td>
                                  <td class="ta">{{items.baseInfo['registered_capital']}}</td>
                                  <td class="tb"> 实缴资本 </td>
                                  <td class="ta">{{items.baseInfo['paid_in_capital']}}</td>
                                  <td class="tb">核准日期</td>
                                  <td class="ta">{{items.baseInfo['approval_date']}}</td>
                                </tr>
                                <tr>
                                  <td class="tb">统一社会信用代码</td>
                                  <td class="ta">{{items.baseInfo['social_credit_code']}}</td>
                                  <td class="tb">组织机构代码</td>
                                  <td class="ta">{{items.baseInfo['registration_number_organization_code']}}</td>
                                  <td class="tb">工商注册号</td>
                                  <td class="ta">{{items.baseInfo['registration_number']}}</td>
                                </tr>
                                <tr>
                                  <td class="tb">纳税人识别号</td>
                                  <td class="ta">{{items.baseInfo['taxpayer_identification_number']}}</td>
                                  <td class="tb">进出口企业代码</td>
                                  <td class="ta">{{items.baseInfo['import_export_enterprise_code']}}</td>
                                  <td class="tb">所属行业</td>
                                  <td class="ta">{{items.baseInfo['industry']}}</td>
                                </tr>
                                <tr>
                                  <td width="13%" class="tb">企业类型</td>
                                  <td width="20%" class="ta">{{items.baseInfo['enterprise_type']}}</td>
                                  <td class="tb">营业期限</td>
                                  <td class="ta">{{items.baseInfo['business_term']}}</td>
                                  <td width="13%" class="tb">登记机关</td>
                                  <td width="20%" class="ta">{{items.baseInfo['registration_authority']}}</td>
                                </tr>
                                <tr>
                                  <td class="tb">人员规模</td>
                                  <td class="ta">{{items.baseInfo['staff_size']}}</td>
                                  <td class="tb">参保人数</td>
                                  <td class="ta">{{items.baseInfo['num_insured']}}</td>
                                  <td class="tb">所属地区</td>
                                  <td class="ta">{{items.baseInfo['area']}}</td>
                                </tr>
                                <tr> <td class="tb">曾用名</td>
                                  <td class="ta"> <span>{{items.baseInfo['history_name']}}</span> <br> </td>
                                  <td class="tb">英文名</td>
                                  <td class="ta" colspan="3">{{items.baseInfo['english_name']}}</td>
                                </tr>
                                <tr>
                                  <td class="tb">企业地址</td>
                                  <td colspan="6">
                                    {{items.baseInfo['source_address']}}
                                  </td>
                                </tr>
                                <tr>
                                  <td class="tb">经营范围</td>
                                  <td class="" colspan="6">
                                  {{items.baseInfo['business_scope']}}
                                  </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
                <section class="section-box">
                    <div class="tcaption">
                        <span class="title">{{url.replace('/company_detail/', '')}} -> </span>
                        <span class="">股东信息</span>
                        <table class="newtable">
                            <tbody>
                                <tr>
                                  <th class="tx">序号</th>
                                  <th width="220">股东名称</th>
                                  <th width="85">持股比例</th>
                                  <th width="115">认缴出资额(万元)</th>
                                  <th width="100">认缴出资日期</th>
                                  <th width="115">实缴出资额(万元)</th>
                                  <th width="95">实缴出资日期</th>
                                </tr>
                                <tr v-for="(item,index) in items.partnerInfo" :key="index">
                                  <td class="tx">{{index+1}}</td>
                                  <td class="tx" style="padding: 0px 1px 0px 1px;">{{item.partner_name}}</td>
                                  <td class="tx">{{item.stock_percent}}</td>
                                  <td class="tx">{{item.should_capi}}</td>
                                  <td class="tx">{{item.shoud_date}}</td>
                                  <td class="tx">{{item.real_capi}}</td>
                                  <td class="tx">{{item.capi_date}}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
                <section class="section-box">
                    <div class="tcaption">
                        <span class="title">{{url.replace('/company_detail/', '')}} -> </span>
                        <span class="">变更信息</span>
                        <table class="newtable">
                            <tbody>
                                <tr>
                                  <th width="10">序号</th>
                                  <th width="150">变更项目</th>
                                  <th width="60">变更日期</th>
                                  <th width="190">变更前</th>
                                  <th width="190">变更后</th>

                                </tr>
                                <tr v-for="(item,index) in items.changeInfo" :key="index">
                                  <td class="tx">{{index+1}}</td>
                                  <td class="tx" style="padding: 10px 10px 10px 10px;">{{item.change_name}}</td>
                                  <td class="tx">{{item.change_date}}</td>
                                  <td class="tx">
                                    <div style="padding: 0 10px 1px 10px;">
                                      {{item.change_befor.replaceAll(':', '：').replaceAll(';', '；').replaceAll(',', '，')}}
                                    </div>
                                  </td>
                                  <td class="tx">
                                    <div style="padding: 0 10px 1px 10px; color: #9f1717">
                                      {{item.change_after.replaceAll(':', '：').replaceAll(';', '；').replaceAll(',', '，')}}
                                    </div>
                                  </td>

                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
            </div>
        </div>
    </div>
  <Footer />

  </div>
</template>

<script>
    import Header from "../components/Header.vue";
    import Footer from "../components/Footer.vue";
    import Left from "../components/Left.vue";
    import { GetInfoPost } from "@/apis/read.js";

    export default {
      name: "CompanyDetaiil.vue",
      components: {
        Left,
        Header,
        Footer
      },
      data() {
        return {
          'url': this.$route.path,
          baseParams: {
              url: this.$route.path,
              key: 'base'
            },
          changeParams:{
              url: this.$route.path,
              key: 'change'
            },
          partnerParams:{
              url: this.$route.path,
              key: 'partner'
            },
          items: {
              baseInfo: {},
              changeInfo: [],
              partnerInfo: []
          }
        }
      },
      created () {
        console.log('url: ', this.$route.path)
        GetInfoPost(this.baseParams).then(resp =>{
            console.log("In baseInfo resp.data = ", resp.data.data);
            this.items.baseInfo = resp.data.data;
        });

        GetInfoPost(this.changeParams).then(resp =>{
            console.log("In changeInfo resp.data = ", resp.data.data);
            this.items.changeInfo = resp.data.data
        });

        GetInfoPost(this.partnerParams).then(resp =>{
            console.log("In partnerInfo resp.data = ", resp.data.data);
            this.items.partnerInfo = resp.data.data
        });
    }

    }
</script>

<style scoped>
    .container {
        width: 1250px;
    }

    .c-t-cd {
        margin-top: 20px;
    }

    .company-box {
        margin-left: 266px;
    }
    .new-box-p {
        padding: 20px;
        width: 930px;
    }
    .new-box {
        background: #ffffff;
        border-radius: 10px;
        /*-webkit-box-shadow: 0 0 6px 0 rgba(93,82,77,.08);*/
        box-shadow: 0 0 6px 0 rgba(93,82,77,.08);
        margin-bottom: 10px;
        /*padding-top: 20px;*/
        /*padding-bottom: 20px;*/
        overflow: hidden;
    }
    .new-box-p .titlebar {
        padding-left: 0;
    }
    .titlebar .title-info {
        font-size: 18px;
        font-weight: 700;
        display: inline-block;
    }
    h1, h2, h3, h4, h5, h6 {
        margin: 0;
    }

    .section-box {
        border-radius: 0;
        margin-bottom: 20px;
        background-color: #ffffff;
    }
    .tcaption {
        margin-bottom: 10px;
        padding: 15px 0 0;

    }
    .tcaption .title {
        font-size: 16px;
        color: #c64f4f;
        font-weight: 550;
        /*margin-left: 20px;*/
        display: inline;
        line-height: 1.8;
    }
    .newtable {
        width: 100%;
        margin: 0 auto 20px;
    }

    .newtable .tb {
        background: #faeded;
        text-align: center;
    }
    .newtable .ta {
        text-align: center;
    }
    .newtable td {
        padding: 10px 10px 11px 10px;
        border: #fbdbdb 1px solid;
        word-break: break-all;
        font-size: 14px;
        line-height: 1.6;
        color: #222;
        word-wrap: break-word;
    }
    .newtable .tx {
        text-align: center;
        width: 35px;
        padding-left: 0px;
        padding-right: 0px;
    }
    .newtable th {
        text-align: center;
        background: #faeded;
        border: #fbdbdb 1px solid;
        border-collapse: collapse;
        padding: 12px 12px 12px 12px;
        font-weight: normal;
        font-size: 14px;
        color: #444;
        line-height: 10px;
    }
</style>
