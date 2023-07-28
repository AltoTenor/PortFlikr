

//Start and sequence of animations
var animationtime_first_left=500;
var animationtime_bounce=100;
var bouncedist=((1).toString()+'%');


if (sessionStorage.getItem("animationshown")!=='1'){
    $(window).on('load', function () {
        $('#loading').hide();
        $('.Nav').hide();
        $('.heading').hide();
        $('.tabs').hide();
        $('[class^="forms-"]').hide();
        $('.make').hide();
    
    
        //Screen Bouncing
        $('.left').animate({
            'width':'0'
        },animationtime_first_left,'swing');
        $('.left').animate({
            'width':bouncedist
        },animationtime_bounce);
        $('.left').animate({
            'width':'0'
        },animationtime_bounce,'easeOutBounce',hidingandshowing);
    }) 
    
}
else{
    $('#loading').hide();
    $('.Nav').hide();
    $('.heading').hide();
    $('.tabs').hide();
    $('[class^="forms-"]').hide();
    $('.make').hide();
    hidingandshowing();
}

//Transition Animations
function hidingandshowing(){
    $('.animation-container').hide();
    $('.main').fadeIn(300,showlogo);
}




//Sequence of Fading Divs
var div_fade_time=300;

function showlogo(){
    $('.Nav').fadeIn(div_fade_time,showheader);
}

function showheader(){
    $('.heading').fadeIn(div_fade_time,showtabs);
}

function showtabs(){
    $('.tabs').fadeIn(div_fade_time);
    $('.forms-first').fadeIn(div_fade_time,showcreate);
    let required_tabid=`#tab--profile--1 a`;
    $(required_tabid).css("background-color", "#9FD6FD")
}

function showcreate(){
    $('.make').fadeIn(div_fade_time);
    // console.log("hello");
}

//Animation Cancel
$('[class^="btn--"]').on('click',()=>{
    sessionStorage.setItem("animationshown",1);
})



//Tab Selection

//Make as Reusable as possible

function hideall(){
    //Hiding all forms
    $('[class^="forms-"]').hide();
    //Setting BG color of add to black
    $("#tab--projects-new a").css("background-image","url(../static/pfapp/img/add-black.png)")
    $("#tab--works-new a").css("background-image","url(../static/pfapp/img/add-black.png)")
    //Setting BG color of all other tab links to white
    $('.tabs a').css("background-color", "#fcfcf2");
}


//CASE: Profile is clicked
$('[class^="tab--profile"] a').on('click',(e)=>{
    let pid=e.target.className;
    hideall();
    //For Profile 1 hardcoded
    if (pid==-1) {
        $(".forms-first").show();
        let required_tabid=`#tab--profile--1 a`;
        $(required_tabid).css("background-color", "#9FD6FD")
    }
    return false;
})



//CASE: Projects is clicked
$('[class^="tab--projects"] a').click((e)=>{
    let pid=e.target.className;
    hideall();
    let required_formclass=`.forms-proj-${pid}`
    console.log(required_formclass+" clicked");
    //Showing Required form
    $(required_formclass).show();

    let required_tabid=`#tab--projects-${pid} a`;

    //CSS Change 
    //If new project is clicked
    if (pid==="new"){
        $(required_tabid).css("background-image","url(../static/pfapp/img/add-blue.png)")
    }
    //If old project is clicked
    else
        $(required_tabid).css("background-color", "#9FD6FD")
    return false;
})

//CASE: Works is clicked
$('[class^="tab--works"] a').click((e)=>{
    let wid=e.target.className;
    hideall();
    let required_formclass=`.forms-works-${wid}`
    console.log(required_formclass+" clicked");
    //Showing Required form
    $(required_formclass).show();

    let required_tabid=`#tab--works-${wid} a`;

    //CSS Change 
    //If new work is clicked
    if (wid==="new"){
        $(required_tabid).css("background-image","url(../static/pfapp/img/add-blue.png)")
    }
    //If old work is clicked
    else
        $(required_tabid).css("background-color", "#9FD6FD")
    return false;
})



//Drop Down 
$("[class^='tab--drop']").on('click',e=>{
    animate_tab_drop_down(e.target.className);
})

var mode=0;

function animate_tab_drop_down(class_var){
    console.log();
    if (mode===0){
        $('.'+class_var).css("transform", "rotate(90deg)");
        $('.tab--'+class_var.slice(10)+'-list').slideUp(200);
    }
    else{ 
        $('.'+class_var).css("transform", "rotate(0deg)");
        $('.tab--'+class_var.slice(10)+'-list').slideDown(200);
    }

    mode=1-mode
    
}