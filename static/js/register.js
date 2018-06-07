function checkRegister(){
    var args = ['userName', 'rawPassword', 'rawPasswordConfirmation'];

    if(!checkEmpty(args))
        return false;

    var rawPassword = document.getElementById("rawPassword").value;
    var rawPasswordConfirmation = document.getElementById("rawPasswordConfirmation").value;

    if(rawPassword != rawPasswordConfirmation){
        alert("passwords do not match");
        return false;
    }

    return true;
}