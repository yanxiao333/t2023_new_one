//稀牛数据逆向2
var _keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=', _p = 'W5D80NFZHAYB8EUI2T649RT2MNRMVE2O'
function d1(e) {
    var t, n, r, o, i, a, c = "", u = 0;
    for (e = e.replace(/[^A-Za-z0-9\+\/\=]/g, ""); u < e.length;)
        t = _keyStr.indexOf(e.charAt(u++)) << 2 | (o = _keyStr.indexOf(e.charAt(u++))) >> 4,
            n = (15 & o) << 4 | (i = _keyStr.indexOf(e.charAt(u++))) >> 2,
            r = (3 & i) << 6 | (a = _keyStr.indexOf(e.charAt(u++))),
            c += String.fromCharCode(t),
            64 != i && (c += String.fromCharCode(n)),
            64 != a && (c += String.fromCharCode(r));
    return c
}
function d2(e) {
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t = _u_d(t)
}
function _u_d(e) {
    for (var t = "", n = 0, r = 0, o = 0, i = 0; n < e.length;)
        (r = e.charCodeAt(n)) < 128 ? (t += String.fromCharCode(r),
            n++) : r > 191 && r < 224 ? (o = e.charCodeAt(n + 1),
                t += String.fromCharCode((31 & r) << 6 | 63 & o),
                n += 2) : (o = e.charCodeAt(n + 1),
                    i = e.charCodeAt(n + 2),
                    t += String.fromCharCode((15 & r) << 12 | (63 & o) << 6 | 63 & i),
                    n += 3);
    return t
}

function main456(text) {
    var d = d1(text)
        , v = d2(d)
        , y = JSON.parse(v);
    return y
}