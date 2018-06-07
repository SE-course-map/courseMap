function check(courseId){
    if(
        !document.getElementById('forCS' + courseId).checked &&
        !document.getElementById('forBA' + courseId).checked
    ){
        alert("Course should be either for CS or BA");
        return false;
    }

    name = document.getElementById('name' + courseId).value;
    description = document.getElementById('description' + courseId).value;
    outcomes = document.getElementById('outcomes' + courseId).value;
    teacher = document.getElementById('teacher' + courseId).value;

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

function deleteCourse(courseId, courseName){
    if(!confirm("Do you really want to delete " + courseName + " ?"))
        return false;

    $.ajax({
        url: "/admin/manageCourse/" + courseId,
        type: 'DELETE',
        statusCode: {
            201: function(result) {
              location.reload();
            },
            500: function(result) {
              location.reload();
            }
        }
    });
}