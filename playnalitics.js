$(document).ready(function(){

    var playlist_list = "<ul>"
    $.getJSON("playlist_list.json", function(json) {
        obj = JSON.parse(json)
        obj.items.forEach(element => {
            playlist_list += "<li>" + element.name + " - " + element.id+ "</li>"
        });
    })
    playlist_list += "</ul>"
    $('#list').append(playlist_list)

    $.getJSON( "playlist_list.json", function( data ) {
        var items = [];
        $.each( data["items"], function( key, val ) {
          items.push( "<li id='" + key + "'>" + val + "</li>" );
        });
       
        $( "<ul/>", {
          "class": "my-new-list",
          html: items.join( "" )
        }).appendTo( "body" );
      });
   
    $('#plot_div').load("plot.html");

 
 });
