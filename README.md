# crawler-solarmonitor

To crawler solarmonitor.org images and data


## How to use

Create a virtual env with python2 e.g:

    virualenv .env -p /usr/bin/python2


Activate this environment:

    source .venv/bin/activate

Install requirements:

    pip install -r requirements.txt

Run Crawler:

    scrapy crawl solarmonitor -o <some_name>.json -a final_date=<some_final_date>

    scrapy crawl solarmonitor -o data.json -a final_date=20150822
