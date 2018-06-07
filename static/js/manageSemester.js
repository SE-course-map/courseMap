function check(semesterId){
    var name = document.getElementById('semester' + semesterId).value;

    if(name.length == 0){
        alert("Name field cannot be empty!");
        return false;
    }

    return true;
}
