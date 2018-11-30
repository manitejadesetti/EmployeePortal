function validate(message,name,email,phno){
    var flag=true;
    if(name=="" || email=="" || phno=="")
    {
        alert("All fields are required");
        flag= false;
    }
    else if(name.length<6) {
        alert("name should contain atleast 6 characters");
        flag = false;
    }
    else if(email.indexOf('@')<6||email.lastIndexOf('.')<email.indexOf('@'))
    {
        alert("Enter the correct email");
        flag=false;
    }
    else if(phno.length!=10) {
        alert("Phone number invalid");
        flag=false;
    }
    else {
        flag=true;
    }
    if(flag==true && message=='.val1') {
       ajaxcalling(name,email,phno,"/EMP/");
    }
    else if(flag==true && message==".val2") {
       ajaxcalling(name,email,phno,"/EMP/updatedata/")
    }
    else {
        return false;
    }
}
function validate1(data){
    var name=data[0];
    var email=data[1];
    var phno=data[2];
    if(name=='')
                return false;
    else if(email.indexOf('@')<0 || email.indexOf('.')<0 || email.lastIndexOf('.')<email.indexOf('@') || email.lastIndexOf('.') >= (email.length-1))
                return false;
    else if(phno.length !=10 )
        return false;
    else {
        return true;
    }
    }
 function ajaxcalling(name,email,phno,post){
        var empdata={};
        empdata.uname=name;
        empdata.email=email;
        empdata.phonenum=phno;
        var posturl=post;
        $.ajax({
        url:posturl,
        type:"POST",
        data: empdata,
        traditional: true,
        dataType: 'html',
        success: function(){
        alert('success');
        },
        error: function(){
        alert('failure');
        }
});
}

