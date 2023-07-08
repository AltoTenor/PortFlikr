

//Start and sequence of animations
var animationtime_first_left=500;
var animationtime_bounce=100;
var bouncedist=((1).toString()+'%');

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
}

function showcreate(){
    $('.make').fadeIn(div_fade_time);
    console.log("hello");
}






//Tab Selection

