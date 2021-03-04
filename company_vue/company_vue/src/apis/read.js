import service from "../utils/request.js";
//import { rsaEncrypt } from "../utils/rsa.js";

export function GetHangyeDetail(url){
    return service.request({
        method: "get",
        url: url
    });
}

export function GetInfoPost(postParams){
    return service.request({
        method: "post",
        url: postParams.url,
        data:{
            key: postParams.key,
        }
    });
}

export function GetPagePost(url, pageNo, pageSize){
    return service.request({
        method: "post",
        url: url + '/page',
        data:{
            pageNo: pageNo,
            pageSize: pageSize,
        }

    });
}
