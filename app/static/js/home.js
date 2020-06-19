var profile = document.querySelector(".profile");
var menu = document.querySelector(".menu");

profile.addEventListener("click" , function(){
  menu.style.display = 'block';
});

$(document).click(function(event) {
if ( event.target == profile || event.target == menu) {
} else {
  menu.style.display = 'none';
}
});

$(".like").hover(function(){
  $(this).css({"cursor" : "pointer"});
})
function addbio() {
  $(".name-and-bio form").css({"display":"block"});
  $("#addbio").css({"display":"none"});
}
function nobio() {
  $(".name-and-bio form").css({"display":"none"});
  $("#addbio").css({"display":"block"});
}
$("#cover_pic").change(function(){
  document.getElementById("cover_pic_form").submit();
 });
 $("#profile_img").change(function(){
   document.getElementById("profile_pic_form").submit();
  });
