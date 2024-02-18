function loadContent(data, site ='add') {
	html = new XMLHttpRequest()
	html.onloadend = (e) => {
		if (site == 'del' || site == 'updatedb')	{
			document.querySelector('main').innerHTML = `<ul>${html.responseText}</ul>`
			startup()
		//console.log(html.responseText)
		}
		if (site == 'edit')	{
			document.querySelector('main').innerHTML = html.responseText
			startup()
		}
	}
	html.open("POST", `${location.origin}/${site}/${data}`)
	//html.open("POST", `./templates/pages/${nazwa}.html`)
	html.send()
}
function startup() {
	//window.onload = function() {
		btns = document.querySelectorAll('button')
		if (btns.length == 0)
			return
		btns.forEach((v) => {
			if (v.id == "edit"){
				v.onclick = (e) => { 
					e.stopPropagation()
					e.preventDefault()
					let name = document.querySelector('input[name=imie]').value
					let lastname = document.querySelector('input[name=nazwisko]').value
					loadContent(`edit=${v.dataset.id}&imie=${name}&nazwisko=${lastname}`, 'updatedb') 
			//console.log(v)
				}
			}
			else if (v.dataset.action === undefined) {
				v.onclick = (e) => { 
					e.stopPropagation()
					e.preventDefault()
					let name = document.querySelector('input[name=imie]').value
					let lastname = document.querySelector('input[name=nazwisko]').value
					loadContent(`imie=${name}&nazwisko=${lastname}`) 
				}
			}
			else if (v.dataset.action === "edit" || v.dataset.action === "del") {
				v.onclick = () => { 
					loadContent(`${v.dataset.id}`, v.dataset.action) 
					console.log(v.dataset.id)
				
				}
			}
		})
}

	/*if (btn === null || btn.id !== "")
		return
	btn.onclick = (e) => { 
		//e.stopPropagation()
		e.preventDefault()
		let name = document.querySelector('input[name=imie]').value
		let lastname = document.querySelector('input[name=nazwisko]').value
		loadContent(`imie=${name}&nazwisko=${lastname}`) 
	}*/
