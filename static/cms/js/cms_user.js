$(function() {
   $(".btn").click(function (event){
       var self = $(this);
       var tr = self.parent().parent();
       var user_id = tr.attr("data-id") ;
       zlalert.alertConfirm({
          "msg":"您确定要删除这个用户账号吗？",
          'confirmCallback':function (){
              zlajax.post({
                  'url':'/cms/dcusers/',
                  'data':{
                      'user_id':user_id,
                  },
                  'success':function (data){
                      if (data['code'] == 200){
                            window.location.reload();
                  }else {
                          zlalert.alertInfo(data['message']);
                      }
                  }
              })
          }
       })
   });
});
