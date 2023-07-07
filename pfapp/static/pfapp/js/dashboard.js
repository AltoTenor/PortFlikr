var root=document.getElementById("root");
root.innerText+="Helo";

let x=10000;
while(x--){
    console.log(x);
}

$(window).on('load', function () {
    $('#loading').hide();
}) 