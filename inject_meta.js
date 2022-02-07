// read sitemap.json
let sitemap = require('./sitemap.json')[0].contents;

// get all file paths from json
function injectMeta(sitemap, path) {
  for (let i = sitemap.length - 1; i >= 0; i--) {
	sitemap[i].path = path + sitemap[i].name;	
	if (sitemap[i].type === 'file' && sitemap[i].name.endsWith('.json')) {
		// find the file without .json
		for (let j = sitemap.length - 1; j >= 0; j--)
			if (sitemap[j].name + '.json' === sitemap[i].name) {
				sitemap[j].meta = require('./' + path + sitemap[i].name);
			}
		sitemap.splice(i, 1);
	} else if (sitemap[i].type === 'directory') {
	  injectMeta(sitemap[i].contents, path + sitemap[i].name + '/');
	}
  }
}

injectMeta(sitemap, '')

// store the result in sitemap.json
const fs = require('fs');
fs.writeFileSync('./sitemap.json', JSON.stringify(sitemap, null, 2));
