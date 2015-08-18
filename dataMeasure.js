var page = require('webpage').create();
var system = require('system');

page.onResourceRequested = function(request) {
  //request is an object
  // console.log('Request ' + JSON.stringify(request, undefined, 4));
};

// //Show contentType and bodySize
// var contentTypeArray = []
// var bodySizeArray = []
// page.onResourceReceived = function(response) {
//  contentTypeArray.push(response.contentType)
//  bodySizeArray.push(response.bodySize)
// };

// page.onLoadFinished = function(status) {
//  for (var i=0; i < contentTypeArray.length; i++) {
//    console.log(contentTypeArray[i], bodySizeArray[i]);
//  };
//  console.log(contentTypeArray.length)
//  //shows how many files(requests) there are

//  phantom.exit();
// };

// //Shows total bodySize values
var bodySizeArray = []
page.onResourceReceived = function(response) {
  //response is an object. I want the bodySize property
  bodySizeArray.push(response.bodySize)
};

page.onLoadFinished = function(status) {
  var bodySizeTotal = 0
  for (var i=0; i < bodySizeArray.length; i++) {
    if (bodySizeArray[i] === undefined) {
    //if undefined, continue to else statement
    } else {
      bodySizeTotal += bodySizeArray[i];
      //add up all values from bodySize
    }
  };
  console.log(bodySizeTotal);

  phantom.exit();
};

page.open(system.args[1]);
