
$(function(){
  $("#tryItButton").click(function(){
    // disable UI
    $( "#tryItForm textarea" ).prop( "disabled", true );
    $( "#tryItForm button" ).prop( "disabled", true );
    // submit request
    $.ajax({
      url:'/process',
      data: { 'text': $('#tryItText').val() },
      type: "POST",
      dataType : "json",
      // print out JSON results nicely
      success: function( content ) {
        $('#cliffResults').html(JSON.stringify(content,null,"  "));
      },
      // print out error nicely
      error: function( xhr, status, errorThrown ) {
        $('#cliffResults').html(status+": "+errorThrown);
      },
      // update UI
      complete: function( xhr, status ) {
        $( "#tryItForm textarea" ).prop( "disabled", false );
        $( "#tryItForm button" ).prop( "disabled", false );
      }
    });
  });
});