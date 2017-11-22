#!/usr/bin/env python3
# -*-  coding: UTF-8 -*-

import urllib.request
from urllib.request import urlopen
import re
import os, sys
import socket
import io




print  ('\033[1;32;40m ####################################################################################################')
print  ('\033[1;32;40m #                                         +++ dv03 +++                                             #')
print  ('\033[1;32;40m #                                                                                                  #')
print  ('\033[1;32;40m #                                                                                                  #')
print  ('\033[1;32;40m #','\033[1;31;40m                                    Admin login Master-Finder       ','\033[1;32;40m                             #')
print  ('\033[1;32;40m #                                                                                                  #')
print  ('\033[1;32;40m #                                                                                                  #')
print  ('\033[1;32;40m #                                    be alone, and think different                                 #')
print  ('\033[1;32;40m #                                     we are pirates  by heredity                                  #')
print  ('\033[1;32;40m ####################################################################################################')
print ("\n")
print ("\n")
print ("\n")
print ('hello')
print ("\n")
print ("\n")
print ("\033[1;31;47m Please check !!!!! that your target url look like this https://www.exemple.com/")
print ("\n")
url= input("\033[1;32;00m plese enter your target website :")
print("good luck ")


#ths part of code for clean up  url to be worker for socket
r=''
for i in url:
    i = url[0:8]
    if i==str("https://"):
      r=url.replace(url[0:8],"")
      rs = r.replace(" ","")
    elif i==str("http://w"):
     r=url.replace(url[0:7],"")
     rs = r.replace(" ", "")
    else:
        r = url
c=rs.replace("/","")
print ("\n")
print ("\n")
if __name__ =='__main__':

    addr = socket.gethostbyname(c)
    print ("the adress ip of the target ",c," is ",addr)
print ("\n")
print ("please wait ")
print ("\n")

#this part of code for check the hadine link robots page
try:
    open_url = urllib.request.urlopen(url)
    r ="robots.txt"
    urlr = url+""+r
    d = urlr.replace(' ','')

    open_url = urllib.request.urlopen(d)
    with urllib.request.urlopen(d) as con:
        cont = con.read()
    print(" check in this resulats if the admin path url is present :",d)

    print("\n")

    data = io.TextIOWrapper(open_url)
    print(data.read())

except urllib.error.URLError as msg:
    print(url)
    print(d)
    print(msg)


#part of code combainde ip with open port check for cpanal
print ("\n")
print ("\033[1;31;00m\n")
print ("\033[1;31;00m _________________________________________________________________________________________________ ")
print ("\033[1;31;00m[_________________________________________________________________________________________________]")
print ("                                                                                                                ")
print ("\033[1;31;00m/\/\/\/\/\______/\_____available services and ports on this server__/\_______/\______/\/\/\/\/\/\/\n")
print ("\033[1;31;00m _________________________________________________________________________________________________ ")
print ("\033[1;31;00m[_________________________________________________________________________________________________]\n")
print ("\033[1;31;00m\n")
print ("\n")
def get_nmap(opt, ip):
    command = "nmap" + " " + opt + " " + ip
    proc = os.popen(command)
    reslt = str(proc.read())
    return reslt
print(get_nmap('-F -Pn', addr))

# part of code for brute forcing url admin cpnal


f = open('cpbrut.txt', 'r')
t = f.readlines()

e = url.replace(" ", '')

for item in t:

    n = e + item
    l = n.replace('\n', '')

    try:
        open = urllib.request.urlopen(l)
        print("\033[1;32;00m______________________________________________________________________________________ \n")
        print("\033[1;32;00m                                         Good result                                     ")
        print("\033[1;32;00m                                             ^_^                                         ")
        print("\033[1;32;00m______________________________________________________________________________________ \n")
        print('                                  ', n)

        print("\033[1;38;00m_______________________________________________________________________________________\n")



    except urllib.error.URLError as msg:
        print("\033[1;31;00m______________________________________________________________________________________ \n")
        print("\033[1;31;00m                                         Bad result                                      ")
        print("\033[1;31;00m______________________________________________________________________________________ \n")
        print('                         ', n)
        print("                                ",msg)
        print("\033[1;38;00m______________________________________________________________________________________ \n")

