const cherio = require('cherio');
const request = require('request');
const fs = require('fs');

var WriteStream  = fs.createWriteStream("Names.txt", "UTF-8");
const arr = [];

request('https://www.tashiara.com/2023/08/trousers-for-women.html', (err, resp, html)=>{

    if(!err && resp.statusCode == 200){
        console.log("Request was success ");
        const $ = cherio.load(html);

        $("div.blog-posts.hfeed > div > div > div > article").each((i, element)=>{

            var text = $(element).find(`b`).text();
            
            console.log(text, ' ');
            WriteStream.write(text);
            WriteStream.write("\n");
        });

    }else{
        console.log("Request Failed ");
    }
});