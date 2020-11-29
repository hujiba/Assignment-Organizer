function sub()
{
 var an = document.getElementById('AssignmentName').value;
 var dd = document.getElementById('DueDate').value;
 var al = document.getElementById('AssignmentLink').value;
 var ac = document.getElementById('AssignmentClass').value;
 var td = document.getElementById('dropdown').value;

if (an.length == 0){
  alert("Assignment Name is required")
}
else {

if (al.length > 0){
  linkHtml = "<a href=" + al + " target=\"_blank\">"
}
else {
  linkHtml = ""
}

if (dd != "" && ac != ""){
  hoverText = dd + " - " + ac
}
else {
  hoverText = dd + ac
}
var table = document.getElementById("table");
var rows = table.rows.length;
var row = table.insertRow(rows);

if (td == "To Do") {
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell1.innerHTML = "<div ondblclick=\"del()\" class=\"myDIV\">" + linkHtml + an + "</a></div> <div class=\"hide\">" + hoverText + "</div>";
}
else if (td == "Doing") {
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell2.innerHTML = "<div ondblclick=\"del()\" class=\"myDIV\">" + linkHtml + an + "</a></div> <div class=\"hide\">" + hoverText + "</div>";
}
else {
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell3.innerHTML = "<div ondblclick=\"del()\" class=\"myDIV\">" + linkHtml + an + "</a></div> <div class=\"hide\">" + hoverText + "</div>";
}
}
}
function del() {

$("table tr").not("thead tr").unbind().dblclick(function(){
    clickedRow = this.rowIndex
    if (clickedRow == 0) {
      null
    }
    else {
    table.deleteRow(clickedRow);
    }
});
}
