//const Crypto = require('crypto')
var _p = 'W5D80NFZHAYB8EUI2T649RT2MNRMVE2O', _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    md55 = '4DA6328ED82E464C7C1A9735C490F9E0'

function sig123(e) {
    return md55.toUpperCase()
}

//function md5(text) {
//  return crypto.createHash(algorithms.md5).update(text).digest('hex');
//};
function e1(e) {
    if (null == e)
        return null;
    for (var t, n, r, o, i, a, c, u = "", s = 0; s < e.length;)
        o = (t = e.charCodeAt(s++)) >> 2,
            i = (3 & t) << 4 | (n = e.charCodeAt(s++)) >> 4,
            a = (15 & n) << 2 | (r = e.charCodeAt(s++)) >> 6,
            c = 63 & r,
            isNaN(n) ? a = c = 64 : isNaN(r) && (c = 64),
            u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(c);
    return u
}
function _u_e(e) {
    if (null == e)
        return null;
    e = e.replace(/\r\n/g, "\n");
    for (var t = "", n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
            t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
                t += String.fromCharCode(r >> 6 & 63 | 128),
                t += String.fromCharCode(63 & r | 128))
    }
    return t
}

//Object(c.d)函数
function e2(e) {
    if (null == (e = _u_e(e)))
        return null;
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t
}
function main123() {
    h = {}
    //分页参数
    pay123 = {
        'limit': 20,
        'sort': 1,
        'start': 40
    }
    h['playload'] = e1(e2(JSON.stringify(pay123)))
    h['sig'] = sig123(h['playload'])
    return h
}
//console.log(main123({}))