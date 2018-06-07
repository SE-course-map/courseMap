function check(){
    var name = document.getElementById("name").value;

    if(name.length == 0){
        alert("Name cannot be empty!");
        return false;
    }

    return true;
}