function deleteBlock(blockId, blockName){
    if(!confirm("Do you really want to delete " + blockName + " block?"))
        return false;

    $.ajax({
        url: "/admin/manageBlock/" + blockId,
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

function check(blockId){
    var name = document.getElementById("name" + blockId).value;

    if(name.length == 0){
        alert("Name cannot be empty!");
        return false;
    }

    return true;
}