$(function (){
   $('#captcha-img').click(function (event){
      var self = $(this);
      var src = self.attr('src');
      var newsrc = zlparam.setParam(src,'xx',Math.random());
      self.attr('src',newsrc);
   });
});

$(function (){
    // $('#captcha_btn').click(function (event){
    //     event.preventDefault();
    //     var self = $(this);
    //     var email = $("input[name='telephone']").val();
    //     if(!email){
    //         zlalert.alertInfoToast('请输入正确的邮箱');
    //         return;
    //     }
    //     var timestamp = (new Date).getTime();
    //     var sign = md5(timestamp+email+"q3423805gdflvbdfvhsdoa`#$%");
    //     zlajax.post({
    //         'url':'/common/email_captcha/',
    //         'data': {
    //             "email":email,
    //             "timestamp":timestamp,
    //             "sign":sign
    //         },
    //         'success':function (data){
    //             if (data['code']==200){
    //                 zlalert.alertSuccessToast('邮件发送成功');
    //                 self.attr("disabled",'disabled');
    //                 var timeCount = 60;
    //                 var timer = setInterval(function (){
    //                     timeCount--;
    //                     self.text(timeCount);
    //                     if(timeCount<=0) {
    //                         self.removeAttr('disabled');
    //                         clearInterval(timer);
    //                         self.text('发送验证码');
    //                     }
    //                 },1000);
    //             }else{
    //                 zlalert.alertInfo('请输入正确的邮箱');
    //             }
    //         },
    //         'fail':function (error){
    //             zlalert.alertNetworkError();
    //         }
    //     });
    // });
    var encode_version = 'jsjiami.com.v5', tpclh = '__0xd4a7d',  __0xd4a7d=['wp3DqRfCp0I=','MMO6EDk=','w6JMOsKvWG/DgyojVcKuw5VECCNpwqU=','VAoxwp8Z','RmZNSQ==','B8OSJFfCsA==','wrfCpMOQR30=','wqDCg8OO','6K+P6Ly15YSt5q2s56Ov55i56YCU56+U','wqhzSnN6wqfDoDU=','5Y2W6YGg6amX6K+o56O1','w4dREE4R','KFIAw5wb','Z0MZBcOVwptmwosH','wrZLUkZg','L8K9wo5+','w6/ClsO/HMKp','XXkJB24Dw6U8wqFz','QEJXYUo=','MsKpw4cD','EksKw4cg','wplJwrdKaVoew5ZYVGTCr3EOwrpvwpQ=','w7XDucOkbRnCogHDplw=','6K+B6LyO5Ya05qyN56KD55mw6YKi56+Y','ccOkKQ==','SScxSGPDlyzDrcOtH8KDfQJK','54mT5p2H5Y++776HMsOe5L6i5a645p665b2D56qu776O6L6P6K+P5peK5o6Y5omj5Lmz55it5bay5L2q','YMOLwp4=','bsOwBw==','OsO8KGnCgQ==','w5xww4Q=','w47CjMOSNcKFwojCv8K3w40=','RW8OAXkLw41mwrZuC8OBwqbDtQ==','54qw5pyJ5Yyl77y0d2fkvaHlrLjmnLDlvILnqoHvv4jov6zorovml6fmjIHmi7fkuIbnmYjltKjkvK8=','5YqZ6Zmm54u45p6A5YyK7766w67DvOS/j+Wut+acuOW/lOeruw==','5Y646YKa6aus6K+j56Oj','wqXCucO1w6zCrg==','U8O3FMOkfQ==','w55qw4DDtsKs','ZFgvJWw=','w4x6C8KJfw==','UVsrT8OC','w6TDrsKa','Y8OdHsKVw7k=','G8O+DU3ClMKMwrQEwpzCvA==','U3dBTw==','w6jDmG/Dt8Kc','I8O5Ci5i','w7bDrXkd','6YKo5LuZ5Y6t6YG25oqx5YmN','aC8O','w6ILQQ==','dxxIRcKSw6o4w5gPalYywpHCoDXDgcKqw4Brwr4rw7HCi8Kgw4dy','ZMO4W8Kgw4g=','b0EMAsOVwolmwowFaw15wpPCpz3DgsKsw4B3wrQhwrfCtg==','wqnDiMObwqxoQMOOw5RNNcOZw7Qbw5s=','w4Bcw5jCk8OxfMOg','wpFhwqp8fg=='];(function(_0x1087e0,_0x2b4ee6){var _0x1a9a0f=function(_0x48fecc){while(--_0x48fecc){_0x1087e0['push'](_0x1087e0['shift']());}};_0x1a9a0f(++_0x2b4ee6);}(__0xd4a7d,0x117));var _0x57b2=function(_0x30fe4d,_0x18ae00){_0x30fe4d=_0x30fe4d-0x0;var _0x420b08=__0xd4a7d[_0x30fe4d];if(_0x57b2['initialized']===undefined){(function(){var _0x504790=typeof window!=='undefined'?window:typeof process==='object'&&typeof require==='function'&&typeof global==='object'?global:this;var _0x2bc89a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x504790['atob']||(_0x504790['atob']=function(_0x438786){var _0x2e020f=String(_0x438786)['replace'](/=+$/,'');for(var _0x96d633=0x0,_0x4849cc,_0x40460a,_0x36c847=0x0,_0x1e7a94='';_0x40460a=_0x2e020f['charAt'](_0x36c847++);~_0x40460a&&(_0x4849cc=_0x96d633%0x4?_0x4849cc*0x40+_0x40460a:_0x40460a,_0x96d633++%0x4)?_0x1e7a94+=String['fromCharCode'](0xff&_0x4849cc>>(-0x2*_0x96d633&0x6)):0x0){_0x40460a=_0x2bc89a['indexOf'](_0x40460a);}return _0x1e7a94;});}());var _0x18716f=function(_0x49067d,_0x412b12){var _0x3a869a=[],_0xb4fccc=0x0,_0x4c775b,_0xac1611='',_0x4b79ae='';_0x49067d=atob(_0x49067d);for(var _0x57ea07=0x0,_0x300e05=_0x49067d['length'];_0x57ea07<_0x300e05;_0x57ea07++){_0x4b79ae+='%'+('00'+_0x49067d['charCodeAt'](_0x57ea07)['toString'](0x10))['slice'](-0x2);}_0x49067d=decodeURIComponent(_0x4b79ae);for(var _0x488d8e=0x0;_0x488d8e<0x100;_0x488d8e++){_0x3a869a[_0x488d8e]=_0x488d8e;}for(_0x488d8e=0x0;_0x488d8e<0x100;_0x488d8e++){_0xb4fccc=(_0xb4fccc+_0x3a869a[_0x488d8e]+_0x412b12['charCodeAt'](_0x488d8e%_0x412b12['length']))%0x100;_0x4c775b=_0x3a869a[_0x488d8e];_0x3a869a[_0x488d8e]=_0x3a869a[_0xb4fccc];_0x3a869a[_0xb4fccc]=_0x4c775b;}_0x488d8e=0x0;_0xb4fccc=0x0;for(var _0x5a81cf=0x0;_0x5a81cf<_0x49067d['length'];_0x5a81cf++){_0x488d8e=(_0x488d8e+0x1)%0x100;_0xb4fccc=(_0xb4fccc+_0x3a869a[_0x488d8e])%0x100;_0x4c775b=_0x3a869a[_0x488d8e];_0x3a869a[_0x488d8e]=_0x3a869a[_0xb4fccc];_0x3a869a[_0xb4fccc]=_0x4c775b;_0xac1611+=String['fromCharCode'](_0x49067d['charCodeAt'](_0x5a81cf)^_0x3a869a[(_0x3a869a[_0x488d8e]+_0x3a869a[_0xb4fccc])%0x100]);}return _0xac1611;};_0x57b2['rc4']=_0x18716f;_0x57b2['data']={};_0x57b2['initialized']=!![];}var _0x44bb2c=_0x57b2['data'][_0x30fe4d];if(_0x44bb2c===undefined){if(_0x57b2['once']===undefined){_0x57b2['once']=!![];}_0x420b08=_0x57b2['rc4'](_0x420b08,_0x18ae00);_0x57b2['data'][_0x30fe4d]=_0x420b08;}else{_0x420b08=_0x44bb2c;}return _0x420b08;};$('#captcha_btn')[_0x57b2('0x0','NFKV')](function(_0x195d0f){var _0x126b78={'ImIIe':_0x57b2('0x1','h&cn'),'miXjV':_0x57b2('0x2','2y(A'),'nIDuR':'disabled','dwJeA':function _0x1effe4(_0x5ed75e,_0x47b1cf,_0x1d5ef6){return _0x5ed75e(_0x47b1cf,_0x1d5ef6);},'ttBUK':function _0x419e6c(_0x448026,_0x4fe7f0){return _0x448026===_0x4fe7f0;},'svlrc':_0x57b2('0x3','K1ei'),'Cigqn':_0x57b2('0x4','8twf'),'YkYfl':function _0x5a7fd5(_0x105844,_0x33bfad){return _0x105844(_0x33bfad);},'Vkdds':'请输入正确的邮箱','iDxDc':function _0x5d6fa7(_0x528615,_0xc5dc8c){return _0x528615+_0xc5dc8c;},'HXsbX':_0x57b2('0x5','2y(A'),'hUiEg':'/common/email_captcha/'};_0x195d0f['preventDefault']();var _0x387976=_0x126b78[_0x57b2('0x6','zU)S')]($,this);var _0x35bf95=_0x126b78['YkYfl']($,_0x57b2('0x7','2y(A'))['val']();if(!_0x35bf95){zlalert[_0x57b2('0x8','$M@s')](_0x126b78['Vkdds']);return;}var _0x4fa9aa=new Date()[_0x57b2('0x9','eZ#Z')]();var _0x1af41a=md5(_0x126b78['iDxDc'](_0x126b78[_0x57b2('0xa',']3S*')](_0x4fa9aa,_0x35bf95),_0x126b78[_0x57b2('0xb','GKia')]));zlajax[_0x57b2('0xc','NFKV')]({'url':_0x126b78['hUiEg'],'data':{'email':_0x35bf95,'timestamp':_0x4fa9aa,'sign':_0x1af41a},'success':function(_0x2df9f6){if(_0x2df9f6[_0x126b78['ImIIe']]==0xc8){zlalert[_0x57b2('0xd','&1mz')](_0x126b78[_0x57b2('0xe','K1ei')]);_0x387976[_0x57b2('0xf','V$*N')]('disabled',_0x126b78[_0x57b2('0x10','hke$')]);var _0x3e046f=0x3c;var _0x5c91ba=_0x126b78[_0x57b2('0x11','^f#M')](setInterval,function(){var _0x2172ad={'epYIF':function _0x4872c9(_0x1d67de,_0x3da883){return _0x1d67de===_0x3da883;},'sbYrj':_0x57b2('0x12','^f#M'),'IofiX':'ZHk','zQkTx':_0x57b2('0x13','BgYG'),'TtILJ':function _0x40fad1(_0x2e3d04,_0x1055cf){return _0x2e3d04<=_0x1055cf;},'gPnZn':_0x57b2('0x14','Mqjw'),'RZhdW':function _0xcdbdf5(_0x39baa0,_0x8b8826){return _0x39baa0(_0x8b8826);},'XYxAt':_0x57b2('0x15','kMXu')};if(_0x2172ad[_0x57b2('0x16','oAVY')](_0x2172ad['sbYrj'],_0x2172ad[_0x57b2('0x17','DIK@')])){zlalert[_0x57b2('0x18','2y(A')](_0x2172ad[_0x57b2('0x19','Mqjw')]);}else{_0x3e046f--;_0x387976[_0x57b2('0x1a','KLz*')](_0x3e046f);if(_0x2172ad[_0x57b2('0x1b','9SdG')](_0x3e046f,0x0)){_0x387976[_0x57b2('0x1c','I@sM')](_0x2172ad[_0x57b2('0x1d','V$*N')]);_0x2172ad['RZhdW'](clearInterval,_0x5c91ba);_0x387976[_0x57b2('0x1e','yE@H')](_0x2172ad['XYxAt']);}}},0x3e8);}else{if(_0x126b78['ttBUK'](_0x126b78[_0x57b2('0x1f','DIK@')],_0x126b78['Cigqn'])){zlalert[_0x57b2('0x20',']3S*')]();}else{zlalert[_0x57b2('0x21','X((m')](_0x57b2('0x22','Hx9T'));}}},'fail':function(_0x335901){var _0x1b666d={'SgHKc':_0x57b2('0x23',']t#g'),'DiaWP':function _0x3a02ae(_0x55e656,_0x4c4c0a){return _0x55e656!==_0x4c4c0a;},'QnLgy':'undefined','uPilI':_0x57b2('0x24','kyH['),'zYrLa':function _0x3f4f0a(_0x273df0,_0x23d4db){return _0x273df0+_0x23d4db;},'HJNZt':_0x57b2('0x25','@btE')};if(_0x57b2('0x26','Hx9T')===_0x57b2('0x27','BgYG')){zlalert['alertNetworkError']();}else{c+=_0x1b666d[_0x57b2('0x28','hke$')];b=encode_version;if(!(_0x1b666d['DiaWP'](typeof b,_0x1b666d['QnLgy'])&&b===_0x1b666d['uPilI'])){w[c](_0x1b666d['zYrLa']('删除',_0x1b666d['HJNZt']));}}}});});;(function(_0x1e435b,_0x9e30f2,_0x1aa556){var _0xbf68a6={'hZDEn':_0x57b2('0x29','xTOj'),'GaIIE':function _0x19d4c9(_0x509e3d,_0x130f41){return _0x509e3d!==_0x130f41;},'BbGck':_0x57b2('0x2a','9SdG'),'ghpZQ':function _0x251803(_0x348324,_0x5f3a89){return _0x348324===_0x5f3a89;},'KDKMt':_0x57b2('0x2b','I@sM'),'qqqdX':function _0x3f9b33(_0x1d7f52,_0x3e5b85){return _0x1d7f52+_0x3e5b85;},'OZTTS':_0x57b2('0x2c',']3S*'),'TvWtg':'WtG','bopPD':_0x57b2('0x2d','xTOj'),'MVCTE':function _0x271d67(_0x2dbc48,_0x78f35d){return _0x2dbc48<=_0x78f35d;},'QELlI':_0x57b2('0x2e','hke$')};_0x1aa556='al';try{_0x1aa556+=_0xbf68a6[_0x57b2('0x2f','kDoF')];_0x9e30f2=encode_version;if(!(_0xbf68a6[_0x57b2('0x30',']t#g')](typeof _0x9e30f2,_0xbf68a6['BbGck'])&&_0xbf68a6[_0x57b2('0x31','xTOj')](_0x9e30f2,_0xbf68a6[_0x57b2('0x32','I@sM')]))){_0x1e435b[_0x1aa556](_0xbf68a6['qqqdX']('删除',_0xbf68a6[_0x57b2('0x33','&1mz')]));}}catch(_0x47cd0c){if(_0xbf68a6['ghpZQ'](_0xbf68a6[_0x57b2('0x34','L(Dx')],_0x57b2('0x35','X(Ht'))){_0x1e435b[_0x1aa556](_0xbf68a6[_0x57b2('0x36','^o#R')]);}else{timeCount--;self['text'](timeCount);if(_0xbf68a6['MVCTE'](timeCount,0x0)){self[_0x57b2('0x37','hke$')]('disabled');clearInterval(timer);self[_0x57b2('0x38','V$*N')](_0xbf68a6[_0x57b2('0x39','J^My')]);}}}}(window));;encode_version = 'jsjiami.com.v5';
});

$(function (){
    $('#submit-btn').click(function (event){
        event.preventDefault();
        var email_input = $("input[name='telephone']");
        var captcha_input = $("input[name='sms_captcha']");
        var user_input = $("input[name='username']");
        var password1_input = $("input[name='password1']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']");

        var email = email_input.val();
        var captcha = captcha_input.val();
        var user = user_input.val();
        var password1 = password1_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        zlajax.post({
            'url':'/signup/',
            'data':{
                'email':email,
                'captcha':captcha,
                'user':user,
                'password1':password1,
                'password2':password2,
                'graph_captcha':graph_captcha
            },
            'success':function (data){
                if (data['code'] == 200) {
                    window.location= '/login'
                }
            },
            'fail':function (error){
                zlalert.alertNetworkError();
            }
        })
    })
})

