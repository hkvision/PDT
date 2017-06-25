$("#submit").click(function() {
  $('#closeForm').submit(function(e){
    e.preventDefault();
    var url=$(this).closest('form').attr('action'),
        data=$(this).closest('form').serialize();
    $.ajax({
        url:url,
        type:'post',
        data:data,
        });
    });
});
