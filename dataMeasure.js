// use JavaScript to use PhantomJS API. 
// .create() is PhantomJS specific; opens webpage
// require('webpage') is a function that returns an object
// .create() is a property of require('webpage'); .create is a method, until called
var page = require('webpage').create();
var system = require('system');

// //Shows total bodySize values
var bodySizeArray = []
page.onResourceReceived = function(response) {
  //response is an object. I want the bodySize property
  bodySizeArray.push(response.bodySize)
};

function addSizesAndQuit(status) {
  var bodySizeTotal = 0
  for (var i=0; i < bodySizeArray.length; i++) {
    if (bodySizeArray[i] === undefined) {
    //if undefined, continue to else statement
    } else {
      bodySizeTotal += bodySizeArray[i];
      //add up all values from bodySize
    }
  };
  data_result = {'program': "complete", 'total': bodySizeTotal}
  data_result_json = JSON.stringify(data_result)
  console.log(data_result_json);

  // shuts program down
  phantom.exit();
};

function addSizesSetTimeout(status) {
  var bodySizeTotal = 0
  for (var i=0; i < bodySizeArray.length; i++) {
    if (bodySizeArray[i] === undefined) {
    //if undefined, continue to else statement
    } else {
      bodySizeTotal += bodySizeArray[i];
      //add up all values from bodySize
    }
  };
  data_result = {'program': "setTimeout", 'total': bodySizeTotal}
  data_result_json = JSON.stringify(data_result)
  console.log(data_result_json);

  // shuts program down
  phantom.exit();
};

// setting up computation
page.onLoadFinished = addSizesAndQuit

// run addSizesSetTimeout after 10 seconds
setTimeout(addSizesSetTimeout, 9500);

// program doesn't start until page.open() is called
page.open(system.args[1]);


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
