const cherio = require('cherio');
const request = require('request');
const fs = require('fs');

// var WriteStream  = fs.createWriteStream("ImagesLink.txt", "UTF-8");

request('https://www.fibre2fashion.com/industry-article/9076/36-best-current-fashion-trends', (err, resp, html)=>{

    if(!err && resp.statusCode == 200){
        console.log("Request was success ");
        
        const $ = cherio.load(html);

        $("#divArticleFile").each((index, image)=>{

            var img = $(image).find('span > b > span').text();
            
            console.log(img, ' ');
            // WriteStream.write(img);
            // WriteStream.write("\n");
            // console.log(img);
        });
        

    }else{
        console.log("Request Failed ");
    }

});