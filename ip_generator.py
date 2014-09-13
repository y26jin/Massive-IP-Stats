import os
import glob
import random

if __name__=="__main__":
    file_addr = "./massiveIP.log"
    fp = open(file_addr, 'a+')
    for i in range(100000000):
        temp_ip = '10.127.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'\n'
        fp.write(temp_ip)
    fp.close()
    
