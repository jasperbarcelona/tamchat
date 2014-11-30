function send(){
var message = $('#text').val();
$.post('/send',{message:message},
function(data){
$('.convo').html(data);
});
document.getElementById('text').value = "";
}

