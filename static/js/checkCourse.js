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

    return true;
}