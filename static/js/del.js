function del(textRepresentation, url){
    if(!confirm("Do you really want to delete " + textRepresentation + "?"))
        return false;

    $.ajax({
        url: url,
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