// read sitemap.json
let sitemap = require('./sitemap.json');

// get all file paths from json
function injectMeta(sitemap, path) {
  let files = [];
  for (let i = 0; i < sitemap.length; i++) {
	if (sitemap[i].type === 'file' && sitemap[i].name.endsWith('.json')) {
		// find the file without .json
		for (let j = 0; j < sitemap.length; j++)
			if (sitemap[j].name + '.json' === sitemap[i].name)
				sitemap[j].meta = require(path + sitemap[i].name);
	} else if (sitemap[i].type === 'directory') {
	  injectMeta(sitemap[i].contents, path + sitemap[i].name + '/');
	}
  }
}

injectMeta(sitemap, '')

// store the result in sitemap.json
const fs = require('fs');
fs.writeFileSync('./sitemap.json', JSON.stringify(sitemap, null, 2));
