
function addEmpl(){
    var myForm = document.getElementById('addEmployeeForm');
    formData = new FormData(myForm);
    var name=formData.get('name');
    var email=formData.get('email');
    var phno=formData.get('phno');
    var message='.val1';
    $('.val1').show();
    //console.log(storedData);
    if(validate(message,name,email,phno)) { 

        alert("Successfull");

        }
     else {
        alert("email already exists");
     }

        myForm.reset();

    
    return false;
}
function updateData(){
    var count=0;
    var myForm = document.getElementById('updateEmployeeForm');
    formData = new FormData(myForm);
    var name=formData.get('name1');
    var email=formData.get('email1');
    var phno=formData.get('phno1');
    var message='.val2';
    $('.val2').show(); 
   
   if(validate(message,name,email,phno)) {
            myForm.reset();
            alert("Successfull");
    }

    return false;
}


    
   
