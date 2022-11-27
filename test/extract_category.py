#########################################################################
# -*- coding: utf-8 -*-
#Created Time: 2014-11-25 15:10:18
#File Name: extract_category.py
#Description: 
#########################################################################
import re

f = open("498.html",'r')
all_lines = f.readlines()

file_result = open("result.txt","w")

for line in all_lines:

    title = re.findall("entry-title\">(.*)</h1>",line,flag)
    if(flag):
        print title
#result = str(title[0]) + str(tags[0])
    #print >>file_result,result
