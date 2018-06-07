function check(){
    if(
        !document.getElementById('forCS').checked &&
        !document.getElementById('forBA').checked
    ){
        alert("Course should be either for CS or BA");
        return false;
    }

    name = document.getElementById('name').value;
    description = document.getElementById('description').value;
    outcomes = document.getElementById('outcomes').value;
    teacher = document.getElementById('teacher').value;

    if(name.length == 0){
        alert("Name field cannot be empty!");
        return false;
    }
    if(description.length == 0){
        alert("Description field cannot be empty!");
        return false;
    }
    if(outcomes.length == 0){
        alert("Outcomes field cannot be empty!");
        return false;
    }
    if(teacher.length == 0){
        alert("Teacher field cannot be empty!");
        return false;
    }

    return true;
}