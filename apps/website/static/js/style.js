$(document).ready(function() {
  $("#about-link").click(function(){
    $('html, body').animate({
      scrollTop: $("#about").offset().top
    },200000);
  });
  $("#portfolio-link").click(function(){
    $('html, body').animate({
      scrollTop: $("#portfolio").offset().top
    },2000);
  });
  $("#contacts-link").click(function(){
    $('html, body').animate({
      scrollTop: $("#contacts").offset().top
    },2000);
  });
})
