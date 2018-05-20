function check(){
    var userName = document.getElementById("userName").value;

    if(userName.length == 0){
        alert("empty user name");
        return false;
    }

    var rawPassword = document.getElementById("rawPassword").value;

    if(rawPassword.length == 0){
        alert("empty password");
        return false;
    }

    var rawPasswordConfirmation = document.getElementById("rawPasswordConfirmation").value;

    if(rawPassword != rawPasswordConfirmation){
        alert("passwords do not match");
        return false;
    }

    return true;
}