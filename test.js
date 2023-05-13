var model = "human"  // change the text inside the quotes to be your desired model

var xhttp = XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		var response = JSON.parse(xhttp.responseText);

		console.log(response);
    }
}

xhttp.open("GET", "http://llm-study-env.eba-59vqgjye.us-west-1.elasticbeanstalk.com?model=" + model);
xhttp.send();
