#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import zipfile


#########################################################
#    PYTHON - ZipFileRead ( Z.F.R. )- GH0ST S0FTWARE    #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################	

def print_bilgi(archive_name):
    konum = zipfile.ZipFile(archive_name)
    for bilgi in konum.infolist():
        print bilgi.filename
        print '\tAçıklama :\t', bilgi.comment
        print '\tDeğiştirilme Zamanı :\t', datetime.datetime(*bilgi.date_time)
        print '\tİşletim Sistemi :\t\t', bilgi.create_system, '(0 = Windows, 3 = Unix)'
        print '\tZIP Dosya Versiyonu :\t', bilgi.create_version
        print '\tSıkıştırılmış Dosya Boyut :\t', bilgi.compress_size, 'bytes'
        print '\tSıkıştırılmamış Dosya Boyutu :\t', bilgi.file_size, 'bytes'
        print

if __name__ == '__main__':
    print_bilgi('zip_dosya_ismi.zip') # --> zip_dosya_ismi.zip yazılacak.  
