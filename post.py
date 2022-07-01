import os
import sys

#script to create a template post for this github pages application 
#format for posts in jekyll is let's say for this post here 
'''
FORMAT = year-month-day-title-goes-here.md
INPUT : 
    Date : 5-20-2002
    Title : This is my first post 

OUTPUT: ( could automatically find the date as well )
    2002-5-20-This-is-my-first-post
'''

'''
TODO: 
    [] - create a test file 
    '''
DATE = 'date "+%Y-%m-%d"'
