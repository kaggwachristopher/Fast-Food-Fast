function tabbed_menu(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
    }
function validate(){
    var confirm=document.getElementById("confirm");
    var password=document.getElementById("password");
    if (password.value!=confirm.value){
        alert("passwords dont match");
        return false;
    }else{
        return true;
    }
}
function button_status(current_button){
    if (current_button.value=="Add to menu" ){
        current_button.value = "Remove from menu";
    }
    else if(current_button.value=="Remove from menu" ){
        current_button.value = "Add to menu";
    }
    
    if (current_button.value==="Accept" ){
        current_button.value = "Complete";
    }
    else if(current_button.value==="Complete" ){
        current_button.value = "Completed";    
    }
    else if(current_button.value==="Accepted" ){
        current_button.value = "Completed";
    }
    else if(current_button.value==="Decline" ){
        current_button.value = "Declined";
        current_button.style.bgcolor = "red";
    }
}

function order(){
    order=document.getElementsByClassName("order_button");
    alert("Your order has been recieved and is pending acceptance, Thank you again");
}
var table=document.getElementById("orders")
var item=document.getElementById("ordered_item");
var x=1;
while(x<10){
table.innerHTML+= item.innerHTML;
x++;
}