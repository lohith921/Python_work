import urllib3

url = "http://www.math.ku.edu/~xu/16s-Math782w/HW"
name = input("Enter the number of the file")
#while ( not name == "0")
urla = url + name + "a.pdf"
urlb = url + name + "b.pdf"
file_namea = urla.split('/')[-1]
print(file_namea)
file_nameb = urlb.split('/')[-1]
print(file_nameb)
extnsn = "F://Education//Spring 2016//EECS 782//Xu HW//"
file_namea = extnsn + file_namea
file_nameb = extnsn + file_nameb
fa = open(file_namea, 'wb')
fb = open(file_nameb, 'wb')
http = urllib3.PoolManager()
r1 = http.request('GET', urla)
r2 = http.request('GET', urlb)
out1 = open(file_namea, 'wb')
out2 = open(file_nameb, 'wb')
out1.write(r1.data)
out1.close()
out2.write(r2.data)
out2.close()
#name = input("Enter another file ")
r1.release_conn()
r2.release_conn()
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

