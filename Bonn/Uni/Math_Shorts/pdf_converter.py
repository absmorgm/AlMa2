#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:26:07 2021

@author: alex
Export HIC to PDF
"""

import os
import pyheif
from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image


#directory1= "/Users/alex/Downloads"
#output = r'/Users/alex/Downloads/Output/'
dirc = "/Users/alex/Downloads/Ana Abgabe"
outnames = "Ana Blatt "

def convert_HEIC_to_pdf(directory, outputdir, ):
    directory2 = os.fsencode(directory)
    counter = 0
    for file in os.listdir(directory2):
        
        filename = os.fsdecode(file)
        if filename.endswith(".HEIC"): 
            counter = counter + 1
            heif_file = pyheif.read(directory + "/" + filename)
            image = Image.frombytes(
               heif_file.mode, 
               heif_file.size, 
               heif_file.data,
               "raw",
               heif_file.mode,
               heif_file.stride,
               )
            outname = outnames + str(counter)
            image.save(outputdir + outname + '.pdf')
    
            continue
        else:
            continue
    
 
# Call the PdfFileMerger
def mergePdfs(directory, outputname):
    directory2 = os.fsencode(directory)
    mergedObject = PdfFileMerger()
    for file in os.listdir(directory2):
        
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"): 
            mergedObject.append(PdfFileReader(directory + "/" + filename, 'rb'))
    
            continue
        else:
            continue
     
    # Write all the files into a file which is named as shown below
    mergedObject.write(outputname)
    
    
mergePdfs(dirc, dirc + "/Abgabe.pdf")
    
    