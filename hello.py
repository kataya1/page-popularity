#!/bin/python3
import cgi
import re

print("Content-Type: text/html")
print()

f = open('hello.html', 'r')
print(f.read())
f.close()
# print('im here')

Regex_Pattern = r'^cgi-bin/hello\.py$'
y = open('access.log', 'r')

# print('im hhere 2')
counter = 0
time = 0
sites = {}
for x in y:
    arr = x.split()
    # if time != 1:
    #     print(arr)
    #     times = 1
    # print(arr[6])
    if arr[6] not in sites:
        sites[arr[6]] = 1 
    else:
        sites[arr[6]] += 1
        

    line = str(bool(re.search(Regex_Pattern, x))).lower()
    if line:
        counter+=1
y.close()
# print('im here 3')

listitems = []
for key,value in sites.items():
    listitems.append(f'this <span class="url">{key}</span> was visited <h3>{value}</h3> time/s')
# listitems.append('</ul>')

ol = '</li><li>'.join(listitems)
ol = f'<ol><li>{ol}</li></ol>'
print(ol)
print(f'<div><span>number of visits for this page <h2>{counter}</h2></span></div>')
print('</body></html>')
