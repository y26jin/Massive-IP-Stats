import os
import glob
import operator

if __name__=="__main__":
    file_addr = "./massiveIP.log"
    # divide files into 1000 smaller files
    fp = open(file_addr, 'r')
    splitLen = 1000000
    count = 0
    at = 0
    dest = None
    for line in fp:
        if count % splitLen == 0:
            if dest:
                dest.close()
            dest = open("./massiveIP-"+str(at)+".log", 'w')
            at = at+1
        dest.write(line)
        count = count + 1

    # for each file, compute frequency of each ip
    Result = {}
    for file_id in range(at):
        temp_result = {}
        path = "./massiveIP-" + str(file_id) + ".log"
        fp = open(path, 'r')
        lines = fp.readlines()
        fp.close()
        for l in lines:
            if l in temp_result:
                temp_result[l] = temp_result[l] + 1
            else:
                temp_result[l] = 1
        # sort the temp result
        temp_result = sorted(temp_result.iteritems(), key=operator.itemgetter(1))
        max_value = temp_result[-1][1]
        print 'File: '+path+':'
        print '    max frequency = '+str(max_value)

        temp_tuple = temp_result.pop()
        while temp_tuple[1] == max_value:
            if temp_tuple[0] in Result:
                Result[temp_tuple[0]] = Result[temp_tuple[0]]+1
            else:
                Result[temp_tuple[0]] = temp_tuple[1]
            temp_tuple = temp_result.pop()
    print sorted(Result.iteritems(), key=operator.itemgetter(1))

        
        
            
    
