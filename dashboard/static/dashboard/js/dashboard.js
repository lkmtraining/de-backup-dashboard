$( document ).ready(function() {
  $('#hosts-table').DataTable({
      responsive: true,
      pageLength: 20,
  });

  $(".hostlink").click(function() {
      var id = $(this).attr('hid');
      $.ajax({
        type: "GET",
        url: "/api/status/" + id,
        dataType: "text",
        success : function(data) {
          $('#details-modal').html(data);
        }
      });
  });
  // // Filter table
  // $("#filter-hosts").on("keyup", function() {
  //   var value = $(this).val().toLowerCase();
  //   $("#hosts-table tr").filter(function() {
  //     $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
  //   });
  // });


});
