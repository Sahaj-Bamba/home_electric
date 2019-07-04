
$(document).ready(function () {

    $('.well')
        .hover(
        function(){
          $(this).css('background', '#ff00ff');
        },
        function(){
          $(this).css('background', '');
        }
        )
        .css('cursor', 'pointer')
        .click(function () {
        room_no = $(this).parent().children('.room_no').text();
        console.log(room_no);
        $(this).parent().children(".form").submit();
    });

})