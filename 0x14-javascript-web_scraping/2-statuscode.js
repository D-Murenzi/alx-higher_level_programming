#!/usr/bin/node

const request = require('request');
let urlgiven = process.argv[2];
let newrequest = request({url: urlgiven, method:'GET'}, function(err, response, body){
    console.log('code: '+response.statusCode);
});
