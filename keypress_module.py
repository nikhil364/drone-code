#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 01:37:26 2022

@author: nikhilsaini
"""

import pygame 

def init():
    pygame.init()
    
    win = pygame.display.set_mode((400, 400))
    

def getKey(keyName):
    
    # what ever key we want to have , if the key is pressed it will return Turn and if not pressed it will return false 
    ans = False 
    for eve in pygame.event.get(): pass 
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()    
    
    
    
    
    return ans 
    
def main():
    if getKey("LEFT"):
        print('left key pressed')
    if getKey("RIGHT"):
        print('right key pressed')
        
    
if __name__ == '__main__':
     init()
     while True:
         main()
    





    