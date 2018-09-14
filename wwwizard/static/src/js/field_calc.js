$(window).on("load", function () {
    var selector = $("select[name=overnight_rate_1]")
    selector.on("change", function(){
        var value = $("select[name=overnight_rate_1]").val();
        if (value) {
            $("#compute_monthly").html(String(parseInt(value) * 6) + " €");
        }
        else{
            $("#compute_monthly").html('');
        }
    });
    selector.change();

});

function render_child(){
    console.log("Not yet");
}

function check_agreement(path){
    var checked = document.getElementById('document_agreement');

    if(checked.checked){
        path = '/sign/'+path;
        window.location.href=path;
    }
    else{
        checked.focus();
        alert("You have to check the agreements");
    }
}