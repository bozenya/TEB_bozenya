function loadContent(nazwa) {
	html = new XMLHttpRequest()
	html.onloadend = (e) => {
		document.querySelector('main').innerHTML = html.responseText
		//console.log(html.responseText)
	}
	html.open("POST", `${location.origin}/ajax/${nazwa}`)
	//html.open("POST", `./templates/pages/${nazwa}.html`)
	html.send()
}

window.onload = function() {
	document.querySelectorAll('.przycisk').forEach( (v) => {
		v.onclick = () => { loadContent(v.dataset.odnosnik) }
	})
}