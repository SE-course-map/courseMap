function check(){
    var userName = document.getElementById("userName").value;
    if(userName.length == 0){
        alert("User name field is empty");
        return false;
    }

    var rawPasssword = document.getElementById("rawPassword").value;
    if(rawPasssword.length == 0){
        alert("Password field is empty");
        return false;
    }

    return true;
}