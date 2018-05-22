$( document ).ready(function() {
    alert('hello i am loaded')
});

function test(){
    $.ajax({
        url: '/test/',
        type: 'POST',
        data: {message: 'hello'},
        statusCode: {
            500: function(result) {
                alert('fail');
            },
            201: function(result) {
                $("#pRat").text(result.message);
            }
        }
    });
}