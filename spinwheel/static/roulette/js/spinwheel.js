console.log("spinwheel.js");

$.ajax({
	url: '/api/round/get_current_round',
	method: 'GET',
	dataType: 'json',
	success: function(result){
		console.log(result);
    $("#round-number").text(`Round #${result.id}`);
	},
  error: function(error) {
    console.log(error);
  }
});