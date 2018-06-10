function checkCourse(id=null){
    args = ['name', 'description', 'prerequisites', 'outcomes', 'teacher'];

    if(!checkEmpty(args, id))
        return false;

    checkBoxes = ['forCS', 'forBA'];
    if(id != null)
        for(var i = 0; i < checkBoxes.length; ++i)
            checkBoxes[i] = checkBoxes[i] + id;

    var checkedNum = 0;
    for(var i = 0; i < checkBoxes.length; ++i)
        if(document.getElementById(checkBoxes[i]).checked)
            ++checkedNum;

    if(checkedNum == 0){
        alert("Course should be either for CS or BA");
        return false;
    }

    var semesterId = null;
    if(id == null)
        semesterId = document.getElementById('semesterId');
    else
        semesterId = document.getElementById('semesterId' + id);
    var options = semesterId && semesterId.options;
    console.log(options);
    if(options == null){
        alert("Course should have at least one semester");
        return false;
    }
    else{
        var selectedNum = 0;
        for(var i = 0; i < options.length; ++i)
            if(options[i].selected)
                ++selectedNum;

        if(selectedNum == 0){
            alert("Course should have at least one semester");
            return false;
        }
    }

    return true;
}