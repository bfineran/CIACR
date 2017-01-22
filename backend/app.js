var express = require('express')
var spawn = require('child_process').spawn
var featuredict = require('./featuredict.json')

var app = express()

app.get('/', function (req, res) {
  var process = spawn('python',["./test.py"])
  process.stdout.on('data', function(data) {
    res.send(featuredict)
  })

})

app.post('/getdocs', function (req, res) {
  var process = spawn('python',["./test.py", req.body.url])
  process.stdout.on('data', function(data) {
    var keywords = JSON.parse(data)
    var matches = []
    for (keyword in keywords) {
      if (keyword in featuredict) {
        for (pdf in featuredict[keyword]) {
          matches.push(pdf)
        }
      }
    }
  })
})

app.listen(8080, function() {
  console.log('Server listening on port 8080')
})
