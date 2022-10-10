/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */


function CreateOrderRow(id,name,description,price,weight,quantity){
  console.log(window.location.hostname+window.location.pathname.replace(/[^\\\/]*$/, ''));
  // Find a <table> element with id="myTable":
    var table = document.getElementById("order-table");

  //check if row for this item exists then add qty to existing row
    for (var i = 0, row; row = table.rows[i]; i++) {
      var indicator=false;
      var tmp_price = 0;
      var tmp_weight = 0;

       //iterate through rows
       //rows would be accessed using the "row" variable assigned in the for loop
       for (var j = 0, col; col = row.cells[j]; j++) {
         if(row.cells[j].id == "row_id" && row.cells[j].innerHTML == id){
           indicator = true;
         }

         if(indicator == true && row.cells[j].id == "qty"){
            var str = row.cells[j].innerText;
            var res = str.replace(/\D/g, "");
            var num = parseInt(res);
            row.cells[j].innerHTML = '<font size=2><a href="#" id="btn-plus"  class="qty_btn"> + </a></font> <label id="qty">'+ (num=num+1) +' </label><font size=2><a href="#" id="btn-minus" class="qty_btn"> - </a></font>';//parseInt(res)+1;
          }

          if(indicator == true && row.cells[j].id == "price")
            tmp_price = row.cells[j].innerText;

          if(indicator == true && row.cells[j].id == "weight")
            tmp_weight = row.cells[j].innerText;

          if(indicator == true && row.cells[j].id == "total_price")
            row.cells[j].innerText = parseFloat(num * tmp_price).toFixed(2);

          if(indicator == true && row.cells[j].id == "total_weight")
            row.cells[j].innerText = parseFloat(num * tmp_weight).toFixed(2);
       }

       if(indicator==true)
        return;
    }

    // Create an empty <tr> element and add it to the 1st position of the table:
    var row = table.insertRow(1);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6);
    var cell8 = row.insertCell(7);
    var cell9 = row.insertCell(8);

    // Add some tex9t to the new cells:
    cell1.innerHTML = id;
    cell1.id="row_id";
    cell2.innerHTML = name;
    cell2.id="name";
    cell3.innerHTML = description;
    cell3.id="description";
    cell4.innerHTML = price;
    cell4.id="price";
    cell5.innerHTML = weight;
    cell5.id="weight";
    cell6.innerHTML = '<font size=2><a href="#" id="btn-plus"  class="qty_btn"> + </a></font> <label id="qty">'+ quantity +' </label><font size=2><a href="#" id="btn-minus" class="qty_btn"> - </a></font>';
    cell6.id="qty";
    cell7.innerHTML = price;
    cell7.id = "total_price";
    cell8.innerHTML = weight;
    cell8.id = "total_weight";
    cell9.innerHTML = '<a href="#" id="btn-trash" class="trash_btn"><span class="glyphicon glyphicon-trash"></span> Delete</a>';
}

$(document).ready(function(){
  $("table").on('click',".qty_btn",function(){
    var x = $(this).closest("td").find("#qty").text();
    if ($.isNumeric(x)){
      if($(this).attr("id") == "btn-plus")
        x++;
      else if($(this).attr("id") == "btn-minus" && x>1)
        x--;
      $(this).closest("td").find("#qty").text(x);

      r_qty = $(this).closest("td").find("#qty").text();
      r_price = $(this).closest("tr").find("#price").text();
      r_weight = $(this).closest("tr").find("#weight").text();

      $(this).closest("tr").find("#total_price").text(parseFloat(r_price * r_qty).toFixed(2));
      $(this).closest("tr").find("#total_weight").text(parseFloat(r_weight * r_qty).toFixed(2));
    }
  });

  $("table").on('click',"#btn-trash",function(){
    var x = $(this).closest("td").find("#qty").text();
    if ($.isNumeric(x)){
      if($(this).attr("id") == "btn-plus")
        x++;
      else if($(this).attr("id") == "btn-minus" && x>1)
        x--;
      $(this).closest("td").find("#qty").text(x);
    }
  });

  $("table").on('click',"#btn-trash",function(){
    // var x = $(this).closest("td").find("#qty").text();
    $(this).closest("tr").remove();
  });

//set total order prices and weight
  $("table").on('click',"#btn-trash, .qty_btn, #order_item",function(){
    console.log("total has changed")
    var total_price=0, total_weight=0;
    $("tr #total_price").each(function() {
        total_price = parseFloat(total_price) + parseFloat($(this).text());
    });
    $("tr #total_weight").each(function() {
        total_weight = parseFloat(total_weight) + parseFloat($(this).text());
    });
    $("#total_order_price").text(total_price);
    $("#total_order_weight").text(total_weight);
  });
});
