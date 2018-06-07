function check(semesterId){
    var name = document.getElementById('semester' + semesterId).value;

    if(name.length == 0){
        alert("Name field cannot be empty!");
        return false;
    }

    return true;
}

function deleteSemester(semesterId, semesterName){
    if(!confirm("Do you really want to delete " + semesterName + " ?"))
        return false;

    $.ajax({
        url: "/admin/manageSemester/" + semesterId,
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