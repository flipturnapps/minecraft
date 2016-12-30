open('text.txt', 'a')
f = open('text.txt','r+')
print f
f.write('testtst\n')
f.close();
f = open('text.txt','r+')
print f.read()
