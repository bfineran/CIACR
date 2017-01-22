console.log( 'Background.html starting!' );
	/*Put page action icon on all tabs*/
	chrome.tabs.onUpdated.addListener(function(tabId) {
		chrome.pageAction.show(tabId);
	});

	chrome.tabs.query({active : true}, function(tabs) {
		chrome.pageAction.show(tabs[0].id);
	});

	chrome.pageAction.onClicked.addListener(function(tab) {
		chrome.tabs.query({active : true, currentWindow : true}, function(tabs) {
			var page_url = tabs[0].url;	
			chrome.tabs.sendMessage(
				tabs[0].id,
				{callFunction : "toggleSidebar", url : page_url}, 
				function(response) {
					console.log(response);
				}
			);
		});
	});
	


console.log( 'Background.html done.' );