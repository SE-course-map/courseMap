function deleteYear(yearId, yearPosition){
    if(!confirm("Do you really want to delete year " + yearPosition + " ?"))
        return false;

    $.ajax({
        url: "/admin/manageYear/" + yearId,
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