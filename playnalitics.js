$(document).ready(function() {  
  //richiesta php on_load
  function call_load() {
    $.ajax({
      type: "GET",
      url: "on_load.php",
      success: function () {
        // $('#content').load("plot_.html");
        // location.reload();
        // showDataOfJsonDescriptions()
      }
    })
  };

  call_load()

  $.getJSON("playlist_list.json", 
      function (data) 
      {
        var tableToShow = '';
        for (var k0 in data["items"])
        {
            var playlist = data["items"][k0]
            var name = playlist["name"]
            var id = playlist["id"]
            tableToShow += '<tr onclick=call_plotter("'+id+'")>';
            tableToShow += '<td>' + name + '</td>';
            tableToShow += '<td>' + id + '</td>';
            tableToShow += '</tr>';
          }
          $('#table').append(tableToShow);
      });      
    });
    
function call_plotter(id) {

  $.ajax({
    type: "GET",
    url: "on_playlist.php",
    data: id,
    success: function () {
      //location.reload();
      //showDataOfJsonDescriptions()
    }
  });

  $('#content').load("plot"+id+".html");
}
