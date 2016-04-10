import urllib3

url = "http://www.math.ku.edu/~xu/16s-Math782w/Lec16-"
name = input("Enter the number of the file")
#while ( not name == "0")
url = url + name + ".pdf"
file_name = url.split('/')[-1]
print(file_name)
extnsn = "F://Education//Spring 2016//EECS 782//Xu Notes//"
file_name = extnsn + file_name
f = open(file_name, 'wb')
http = urllib3.PoolManager()
r = http.request('GET', url)
out = open(file_name, 'wb')
out.write(r.data)
out.close()
#name = input("Enter another file ")
r.release_conn()
print("Done downloading")
#u = urllib3.urlopen(url)
#with open(file_name, 'wb') as out:
 #   while True:
  #      data = r.read(block_sz)
   #     if data is None:
    #        break
     #   out.write(data)
	#print("Read a chunk")
#meta = u.info()
#file_size = int(meta.getheaders("Content-Length")[0])
# print "Downloading: %s Bytes: %s" + (file_name, file_size)

# file_size_dl = 0

#while True:
 #   buffer = u.read(block_sz)
  #  if not buffer:
   #    break
    #file_size_dl += len(buffer)
    #f.write(buffer)
    #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    #status = status + chr(8)*(len(status)+1)
    #print status,
#f.close()

