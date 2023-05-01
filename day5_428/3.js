/*
 * @Author: yanxiao333 yanxiao_333@126.com
 * @Date: 2023-04-30 16:19:28
 * @LastEditors: yanxiao333 yanxiao_333@126.com
 * @LastEditTime: 2023-04-30 21:35:12
 * @FilePath: \t2023_new_one\day5_428\3.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */


function o(n) {

    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65'].forEach(function (n) {
            t += this["unescape"]("%u00" + n)
        });
    var t, e = t;
    return (n);
}
function v(t) {
    Y1 = "0x"
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o(Y1 + t)
    });
    try {
        return z[Q1](t)
    } catch (n) {
        return this["Buffer"]['from'](t)["toString"]("base64")
    }
}
a = ['all', '36', 'iphone', 'cn', '2023-04-30', 2]
/*复制a函数*/
function url(e) {
    a = (0,
        v)(a)
    return a
}

e = "/rank/indexPlus/brand_id/0"

// console.log(url(e))