//Remove Item from list
$(".remove-item").click(function(){
    var id = $(this).attr("cid").toString();
    var eml = this;
    // console.log(id);
    $.ajax({
        type: "GET",
        url: "/removeitem",
        data: {
            course_id: id,
        },
        success: function(data){
            document.getElementById("amount").innerHTML = data.amount;
            document.getElementById("totalamount").innerHTML = data.totalamount;
            eml.parentNode.parentNode.parentNode.parentNode.remove();
        }
    });

});