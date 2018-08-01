$(window).on("load", function () {
    var selector = $("select[name=overnight_rate_1]")
    selector.on("change", function(){
        var value = $("select[name=overnight_rate_1]").val();
        if (value) {
            $("#compute_monthly").html(String(parseInt(value) * 30) + " €");
        }
        else{
            $("#compute_monthly").html('');
        }
    });
    selector.change();
    if ($("div[role=alert]")){
        $("div[role=alert]").alert("close");
    }

});

function render_child(){
    console.log("hola");
}