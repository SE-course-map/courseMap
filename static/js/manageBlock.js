function check(blockId){
    var name = document.getElementById("name" + blockId).value;

    if(name.length == 0){
        alert("Name cannot be empty!");
        return false;
    }

    return true;
}