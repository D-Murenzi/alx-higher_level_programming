#!/usr/bin/node

const fs = require('fs');
let filepath = process.argv[2];
fs.readFile(filepath, 'utf8', function(err, data) {
    if(err){
	console.log(err);
    }else{
	console.log(data);
    };
});
