// https://stackoverflow.com/questions/19786525/how-to-list-loaded-resources-with-selenium-phantomjs

// getResources.js
// Usage:
// ./phantomjs --ssl-protocol=any --web-security=false getResources.js your_url
// the ssl-protocol and web-security flags are added to dismiss SSL errors

var page = require('webpage').create();
var system = require('system');

var error = function (str) {
  system.stderr.write(String(str) + '\n');
};

var stats = {
  size  : 0,
  files : 0,
};

// Listen for all requests made by the webpage,
// (like the 'Network' tab of Chrome developper tools)
// and add them to an array
page.onResourceRequested = function(request, networkRequest) {
  stats.files++
};

page.onResourceReceived = function(response) {
  if (response.redirectURL && response.stage == 'start') {
    error('Redirect: ' + response.redirectURL)
  }
  if (response.bodySize) {
    stats.size += response.bodySize
  }
};

// When all requests are made, output the array to the console
page.onLoadFinished = function(status) {
  console.log(JSON.stringify(stats)); //turn stats(dict) into a string via JSON
  //console.log() writes to standardOut(stdout)
  phantom.exit(0);
};

page.onResourceError = function(e){
  error('ResourceError: ' + e.errorString + JSON.stringify(e))
  return false;
}
page.onError = function(e){
  return false;
}

// Open the web page
page.open(system.args[1]);
