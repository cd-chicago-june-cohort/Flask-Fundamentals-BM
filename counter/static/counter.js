$(document).ready(function() {
console.log('NOW READY')
 
$('#button').click(function(){
    window.location.assign('/twice')
})

$('#reset').click(function(){
    window.location.assign('/reset')
})

});