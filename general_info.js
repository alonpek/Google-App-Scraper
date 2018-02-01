var gplay = require('google-play-scraper');

// My code
gplay.search({
    term: process.argv[2],
    num: 25,
    throttle: 5, //To avoid hitting throttling limit
    fullDetail:True
}).then(console.log);

