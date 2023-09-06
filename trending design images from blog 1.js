const cherio = require('cherio');
const request = require('request');
const fs = require('fs');

var WriteStream  = fs.createWriteStream("ImagesLink.txt", "UTF-8");

request('https://www.tashiara.com/2023/08/trousers-for-women.html', (err, resp, html)=>{

    if(!err && resp.statusCode == 200){
        console.log("Request was success ");
        
        const $ = cherio.load(html);

        $("img").each((index, image)=>{

            var img = $(image).attr('src');
            WriteStream.write(img);
            WriteStream.write("\n");
            console.log(img);
        });

    }else{
        console.log("Request Failed ");
    }

});