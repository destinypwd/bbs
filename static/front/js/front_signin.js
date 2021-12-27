$(function (){
    $('#submit-btn').click(function (event){
        event.preventDefault();
        var email_input = $("input[name='telephone']");
        var password_input = $("input[name='password']");
        var remember_input = $("input[name='remember']")

        var email = email_input.val();
        var password = password_input.val();
        var remember = remember_input.checked?1:0;

        zlajax.post({
            "url":"/login/",
            "data":{
                "email":email,
                "password":password,
                "remember":remember
            },
            "success":function (data){
                if (data['code']==200){
                    var return_to = $("#return-to-span").text();
                    if (return_to != 'http://127.0.0.1:5000/signup/'){
                        window.location = return_to;
                    }else {
                        window.location = '/'
                    }
                }else{
                    zlalert.alertInfoToast(data['message']);
                }
            }

        })

    });
});