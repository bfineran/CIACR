
/*Small function wich create a sidebar(just to illustrate my point)*/
var sidebarOpen = false;
function toggleSidebar(matches) {
	if(sidebarOpen) {
		var el = document.getElementById('mySidebar');
		el.parentNode.removeChild(el);
		sidebarOpen = false;
	}
	else {
		var sidebar = document.createElement('div');
		sidebar.id = "mySidebar";
		
		if (matches && matches.length > 0){
			sidebar.innerHTML = '<ul><li>' + 
				matches.join('</li><li>') + '</li></ul>';
		}
		else{
			sidebar.innerHTML = "No Matches";
		}
		//sidebar.innerHTML = 'hello world'
		sidebar.style.cssText = "\
			position:fixed;\
			top:0px;\
			left:0px;\
			width:30%;\
			height:100%;\
			background:white;\
			box-shadow:inset 0 0 1em black;\
			z-index:999999;\
		";
		document.body.appendChild(sidebar);
		sidebarOpen = true;
	}
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
	console.log(request);
	console.log('received');
	if (request.callFunction == "toggleSidebar"){
		var linked = ['google.com','yahoo.com'];
		toggleSidebar(linked);
	}
});
