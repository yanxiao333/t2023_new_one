//作业：进行js测试跑通，在使用Python执行execjs操作
//url='https://ggzyfw.fj.gov.cn/business/list'



s.n = function (t) {
    var e = t && t.__esModule ? function () {
        return t["default"]
    }
        : function () {
            return t
        }
        ;
    return s.d(e, "a", e),
        e
}
function b(t) {
    var e = h.a.enc.Utf8.parse(r["c"])
        , n = h.a.enc.Utf8.parse(r["b"])
        , a = h.a.AES.decrypt(t, e, {
            iv: n,
            mode: h.a.mode.CBC,
            padding: h.a.pad.Pkcs7
        });
    return a.toString(h.a.enc.Utf8)
}

console.log(b())



