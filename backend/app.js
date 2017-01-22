var express = require('express')
var spawn = require('child_process').spawn
var featurewords = require('./featuredict.json')
var featuredict = JSON.parse(featurewords)
var bodyParser = require('body-parser')

var app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))

app.get('/', function (req, res) {
  var base = 'https://en.wikipedia.org/wiki/Barack_Obama'
  var printable = 'https://en.wikipedia.org/w/index.php?title='
  printable += base.split('wiki/')[1]
  printable += '&action=raw'
  var process = spawn('python',["./wiki_raker.py", printable])
  console.log("spawned")
  process.stdout.on('data', function(data) {
    console.log('returned')
    var str = data.toString(), lines = str.split(/(\r?\n)/g);

    res.send(str.split(', '))
  })

})

app.post('/getdocs', function (req, res) {
  console.log('HERE')
  var printable = 'https://en.wikipedia.org/w/index.php?title='
  //console.log(JSON.stringify(req))
  //console.log(JSON.stringify(req.body))
  //console.log(req)
  //for (val in req.body) {
  //  console.log('Val ' + val)
  //}
  printable += req.body.url.split('wiki/')[1]
  printable += '&action=raw'
  var process = spawn('python',["./wiki_raker.py", printable])

  process.stdout.on('data', function(data) {
    console.log('FINISHED')
    var rawdata = data.toString()
    var keywords = rawdata.split(', ')
    var matches = []
    for (var i = 0; i < keywords.length; i++) {
      var keyword = keywords[i]
      if (keyword in featuredict) {
        for (var j = 0; j < featuredict[keyword].length; j++) {
          matches.push(featuredict[keyword][j])
          if (matches.length >= 3) {
            res.send(matches)
            return
          }
        }
      }
    }
    console.log(JSON.stringify(featuredict['attorney gen  eral']))
    res.send(matches)
  })
})

app.listen(8080, function() {
  console.log('Server listening on port 8080')
})
