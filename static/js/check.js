function checkEmpty(data, id=null){
    for(var i = 0; i < data.length; i++){
        var key = data[i];

        if(id != null)
            key += id;

        var val = document.getElementById(key).value;
        if(val.length == 0){
            alert("Field " + (data[i].charAt(0).toUpperCase() + data[i].slice(1)) + " cannot be empty!");
            return false;
        }
    }

    return true;
}