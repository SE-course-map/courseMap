function deleteUser(userName, userId){
    if(!confirm("Do you really want to delete " + userName + "?"))
        return false;

    $.ajax({
        url: "/admin/users/" + userId,
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