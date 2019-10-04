#!/bin/bash
PATH=$PATH:/usr/local/bin
export PATH
cd /home/sampo/projekti/auto/auto/spiders

scrapy runspider KaikkiAutot.py
