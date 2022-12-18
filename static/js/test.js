$("#anyalang").on("click", function(){
    const sel = $("#anyasel").val();
	$.ajax({	
		url:"/api/" + sel,
		type:"GET",
		dataType:"json",
		timespan:3000,
		async: false,
		}).done(function(jsonval,textStatus,jqXHR) {
				$("#anyaid").text(jsonval["COLUM1"]);
				$("#anyamsg").text(jsonval["COLUM2"]);

		}).fail(function(jqXHR, textStatus, errorThrown ) {
            $("#anyaid").text("ERROR : (" + jqXHR.status + ")" + textStatus);
            $("#anyamsg").text(errorThrown);
	});
});