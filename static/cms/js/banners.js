$(function (){
    $("#save-banner-btn").click(function (event){
        event.preventDefault();
        var self = $(this);
        var dialog = $("#banner-dialog");
        var nameInput = $("input[name='name']");
        var imageInput = $("input[name='image_url']");
        var linkInput = $("input[name='link_url']");
        var priorityInput = $("input[name='priority']");

        var name = nameInput.val();
        var image_url = imageInput.val();
        var link_url = linkInput.val();
        var priority = priorityInput.val();
        var submitType = self.attr('data-type');
        var bannerId = self.attr("data-id");

        if (!name || !image_url || !link_url || !priority){
            zlalert.alertInfoToast('请输入完整的轮播图设置');
            return;
        }
        if (submitType == 'update'){
            url = '/cms/ubanners/';
        }else {
            url = '/cms/abanners/';
        }
        zlajax.post({
           "url":url,
           "data":{
               'banner_id':bannerId,
               'name':name,
               'image_url':image_url,
               'link_url':link_url,
               'priority':priority
           } ,
           "success":function (data){
               if(data['code'] == 200){
                   //重新加载页面
                   window.location.reload()
                   dialog.modal("hide");
               }else {
                   zlalert.alertInfo(data['message']);
               }
           },
           "fail":function (){
               zlalert.alertNetworkError()
           }
        });

    });
});

$(function (){
    $(".edit-banner-btn").click(function (event){
        var self = $(this);
        event.preventDefault();
        var dialog = $("#banner-dialog");
        dialog.modal('show');

        var tr = self.parent().parent();
        var name = tr.attr("data-name");
        var image_url = tr.attr("data-image");
        var link_url = tr.attr("data-link");
        var priority = tr.attr("data-priority");

        var nameInput = dialog.find("input[name='name']");
        var imageInput = dialog.find("input[name='image_url']");
        var linkInput = dialog.find("input[name='link_url']");
        var priorityInput = dialog.find("input[name='priority']");
        var saveBtn = dialog.find("#save-banner-btn")

        nameInput.val(name);
        imageInput.val(image_url);
        linkInput.val(link_url);
        priorityInput.val(priority);
        saveBtn.attr("data-type",'update');
        saveBtn.attr("data-id",tr.attr('data-id'))
    })
})

$(function (){
    $(".delete-banner-btn").click(function (event){
        var self = $(this);
        var tr = self.parent().parent();
        var banner_id = tr.attr('data-id')
        zlalert.alertConfirm({
            "msg":"您确定要删除这个轮播图吗？",
            'confirmCallback':function (){
                zlajax.post({
                    'url':'/cms/dbanners/',
                    'data':{
                        'banner_id':banner_id
                    },
                    'success':function (data){
                        if(data['code']==200){
                            window.location.reload();
                        }else{
                            zlalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        })
    })
})

$(function (){
    $("#add-btn").click(function (event){
        event.preventDefault();
        var upload = $("#upload");
        upload.click();
    })
})

function checkFile(o){
    var fileobj = o.files[0]
    if (typeof(fileobj)=='undefined'){   //js提供了typeof运算符，用来检测一个变量的类型
        alert('请选择要上传的文件');
        return false;
    }
    else {
        var fileType = fileobj.type;
        var fileName = fileobj.name;
        var fileSize = fileSize / 1024 / 1024;   //MB
        var maxSize = 2048;

        var allowType = /^(image\/jpeg|image\/png|image\/jpg)$/i;  //检查图片的格式，/^开始的位置，$/结束的位置，i不区分大小写
        if (!allowType.test(fileType)){
            alert("图片格式必须为jpeg或png或jpg");
            return false
        }
        if (fileobj.name.indexOf("'")>-1){
            alert("名字不能包含以下字符：\\\\ / : * ? \\' \\ < > | ")
        }
        else if (fileSize > maxSize) {
                    alert("请选择" + maxSize + "MB以内的文件上传。您当前文件大小为：" + fileSize.toFixed(2) + "MB");
                    return false;
                }
        var formData = new FormData();
        formData.append('file',o.files[0]);
        zlajax.post({
            'url':'/cms/file_uploads/',
            'data':formData,
            'processData' : false,
			'contentType' : false,
            'success':function (data){
                if (data['code']==200){
                    document.getElementById('image_input').value='http://127.0.0.1:5000/static/picture/'+o.files[0].name;
                }else{
                    zlalert.alertInfo(data['message']);
                 }
            }
        })

    }
}

// document.getElementById('image_input').value=this.files[0].name