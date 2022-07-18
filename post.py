#!/usr/bin/env python3 
#Ryan "buhfur" McVicker

import os 
import time
import tempfile 
#get the title of the file
title = input("Enter the title of the file : ")
title = title.replace(' ', '-')

EDITOR = os.environ.get('EDITOR', 'vim') # set the editor to vim 

#get the date format( in this case it would be +%F-[title-seperated-by-dashes]

dt = time.strftime("%F")
filename = f'_posts/{dt}-{title}.md'
#Template string to automatically be put in the file 
TEMPLATE=f'''
---
layout: post
title: {filename}
---

'''
#print the file out in yyyy-mm-dd-title
print(f'{filename} was created\n\n')


#open the file and input the template text 
try:

    with open(filename, 'w') as file : 
        file.write(TEMPLATE)

    #open the file in vim 
    print('text was appeneded to file ')


except Exception as e: 
    print(e) 

