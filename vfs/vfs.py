#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Frame Stacker
"""
import glob2
import argparse
import cv2
import os

def composevid(**kwargs):
    importfile = os.path.abspath(kwargs['video'])
    if isinstance(kwargs['e'],type(None)):
        exportfile = "".join(importfile.split('.')[:-1])+'.jpg'
    else: exportfile = os.path.abspath(kwargs['e'])
 
    video = cv2.VideoCapture(importfile) 

    compose=None
    lastframe=None
    while(True):
        ret,frame = video.read()
        if ret:
            if isinstance(compose,type(None)):
                compose = frame
            
            if not isinstance(lastframe,type(None)):
                # compute difference
                difference = cv2.subtract(lastframe, frame)
                ## color the mask red
                Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
                
                compose[mask != 255] = frame[mask != 255]  
            lastframe = frame
        else: break
    	
    video.release() 
    cv2.imwrite(exportfile, compose)
    
def dir_file(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid file")
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="video file to stack to image",type=dir_file, required=True)
    parser.add_argument("-e", help="exported image",default=None,type=str)
    
    args = parser.parse_args()
    
    # init object
    composevid(**vars(args))   

if __name__ == '__main__':
    main()