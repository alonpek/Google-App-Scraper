var gplay = require('google-play-scraper');

// My code
gplay.search({
    term: process.argv[2],
    num: 25,
    throttle: 10, //To avoid hitting throttling limit
    fullDetail:true
}).then(console.log);

