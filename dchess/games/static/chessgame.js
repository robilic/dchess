
addPiece = function(e) {
	// calls back to the website to move a piece
	var div = document.getElementById('pieces');
	div.innerHTML += e;
	var game_id = document.getElementById('game-id');
	if (div.innerHTML.length == 4) {
		console.log("Sending " + div.innerHTML + " to the server as a move");
		window.location.href = "http://localhost:8000/games/" + game_id.innerHTML + "/move/" + div.innerHTML;
	}
};

