/**
 * This script generates a new words_dictionary.json from words_alpha.txt
 * 
 * You must have nodejs installed to run this script.
 * 
 * To use it, run this from the command line in the project folder:
 * node dictmaker.js
 * 
 */

var FS = require('fs');

var SOURCE_PATH = './words_alpha.txt';
var OUTPUT_PATH = './words_dictionary.json';


console.log('reading file ' + SOURCE_PATH);

FS.readFile(SOURCE_PATH, 'utf8', function(err, content) {
	if(err) {
		throw err;
	}
	
	console.log('processing word list...');
	
	var words = content.split('\n');
	
	var dictionary = content
	.split('\n')
	.reduce(function(dct, line, i) {
		var word = String(line).trim();
		dct[word] = 1;
		return dct;
	}, {});
	
	console.log('writing dictionary to ' + OUTPUT_PATH + ' ...');
	
	FS.writeFile(OUTPUT_PATH, JSON.stringify(dictionary), 'utf8', function(err) {
		console.log('done!');
	});
});
