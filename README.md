# Homework 1: Option 1.2 Write a Web Crawler of your own
Maria Shapiro CS 4675


There are 4 different crawlers with various rules available to use. All crawlers follow the same stop protocal: stop recursing at 1,200 pages (usually finishes the queue at ~1,600 pages) or run out of pages to crawl. All spiders abide by Robots.txt. 

1. No rules, no keywords, start at 'https://www.gatech.edu'. This spider's name is **sip**
2. Only add links that contain the keyword "gatech" to the queue. This spider's name is **gatech**
3. Only add links that contain the keywords "gatech" and "computing". This spider's name is **computing**
4. Only add links that contain the keywords "AI", "ML", and "research". This spider's name is **research**


<h2>How to run</h2>  
You need to run the spiders in a virtual enviorment. 
  
Create a virtual env: `python3 -m venv venv`  
Activate your env: `venv/scripts/activate`  
Install Scrapy with pip: `pip install scrapy`   
Go to the crawling directory: `cd .\projectname\` (I didn't realize I could change the project name at the time I created it)  
Start your crawler: `scrapy crawl [name of spider]`. For example: `scrapy crawl sip`
