
$(function(){
  $("#tryItButton").click(function(){
    // disable UI
    $( "#tryItForm textarea" ).prop( "disabled", true );
    $( "#tryItForm button" ).prop( "disabled", true );
    // submit request
    var fields = $( "#tryItForm" ).serialize();
    $.ajax({
      url:'/process',
      data: { 'text': $('#tryItText').val() },
      type: "POST",
      dataType : "json",
      success: function( content ) {
        $('#cliffResults').html(JSON.stringify(content,null,"  "));
      },
      error: function( xhr, status, errorThrown ) {
        $('#cliffResults').html(status+": "+errorThrown);
      },
      // code to run regardless of success or failure
      complete: function( xhr, status ) {
        // update UI
        $( "#tryItForm textarea" ).prop( "disabled", false );
        $( "#tryItForm button" ).prop( "disabled", false );
      }
    });
  });
});