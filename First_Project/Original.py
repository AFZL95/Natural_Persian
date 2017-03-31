#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs

dict = {'ش':'sh' , 'ا':'A' ,'آ':'~' , 'ب':'b' , 'پ':'p' , 'ت':'t' , 'ث':'C' , 'ج':'j' , 'چ':'c' ,'ح':'H' ,'خ':'x' , 'د':'d' ,'ذ':'D', 'ر':'r' , 'ز':'z' ,'ژ':'j' ,'س':'s' ,'ش':'$' ,'ص':'S' ,'ض':'X' ,'ط':'T' ,'ظ':'Z' ,'ع':'E' ,'غ':'G' ,'ف':'f' ,'ق':'q' ,'ک':'k' ,'گ':'g' ,'ل':'l' ,'م':'m' ,'ن':'n' ,'ه':'h' ,'و':'O' ,'ی':'y' }
def converttoe (worD , dicT) :
    for key in dicT:
        worD = worD.replace(key, dicT[key])
    return  worD



adds =  input("Please Enter The full address of source File  : ")
addd =  input("Please Enter The full address of destination File :")
f = open(addd, "w")
with codecs.open(adds) as fp:
    for line in fp:
        for word in line.split():
            f.write( converttoe(word,dict) + "\n")


