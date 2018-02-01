var gplay = require('google-play-scraper');

// My code

gplay.reviews({
  appId: process.argv[2], //Pass appId through command line
  page: 0,
  sort: gplay.sort.HELPFULNESS,
    throttle:10
}).then(console.log, console.log);
