$(function() {
    $('#btnSignUp').click(function() {
        $.ajax({
            url: '/signup',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert(response);
            },
            error: function(error) {
                alert(error);
            }
        });
    });
});