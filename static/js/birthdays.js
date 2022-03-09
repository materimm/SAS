function getBirthdays() {
  // hide results divs
  $("#no_birthdays_div").hide();
  $("#table_div").hide();

  //get value of selected month
  month = $("#month").val();

  //make sure the user didnt jus select the default text
  if(month != 0) {
    //send api call
    $.ajax({
      type:"GET",
      dataType: "json",
      data:{'month': month},
      url: "/get_birthdays",
      success: function(data) {
        birthdays = data.birthdays;
        if(birthdays.length == 0) {
          //There were no birthdays in this month
          $("#no_birthdays_div").show();
        }
        else {
          //empty the last results from the table
          $("#tbodyid").empty();
          //loop over employee list and fill table
          birthdays.forEach(function(item, index) {
            $("#tbodyid").append('<tr><td>' + item.first_name + ' ' + item.last_name + '</td><td>' + item.birthday + '</td><td><a href="#"><img src="/static/email.png" height="40"></a></td></tr>');
          });
          //show the table
          $("#table_div").show();
        }
      }});
  }
}
