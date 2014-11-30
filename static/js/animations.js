$(document).ready(function(){
	
var height = $(window).height()-120;
$(".convo").css("height",height);

	
var myTxtArea = document.getElementById('text');
myTxtArea.value = myTxtArea.value.replace(/^\s*|\s*$/g,'');

$(window).resize(function(){
	var height = $(window).height()-120;
	$(".convo").css("height",height);
});

});
