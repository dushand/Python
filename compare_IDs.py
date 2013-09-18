#Compare two files which will have following Ids(fileds).
#
#----------file01--------
#6100100013
#6110010003
#6120010001
#6120010002
#-------------------------
#
#----------file02---------
#6120120001
#6130040001
#6130070001
#6130070005
#-------------------------
#
#
#Two outputs requires
#01.) file01 Ids, which are not in file02.
#01.) file02 Ids, which are not in file01.


# filecompare.py
in1 = file('file01.txt')
in2 = file('file02.txt')
out1 = file('in01notin02.txt','w')
out2 = file('in02notin01.txt','w')
f1_line = in1.readline().strip()
f2_line = in2.readline().strip()
while f1_line or f2_line:
  if f1_line==f2_line: 
    f1_line = in1.readline().strip()
    f2_line = in2.readline().strip()
  while f1_line and f1_line < f2_line:
    out1.write(f1_line+"\n")
    f1_line = in1.readline().strip()
  while f2_line and f1_line > f2_line:
    out2.write(f2_line+"\n")
    f2_line = in2.readline().strip()
  while f1_line and not f2_line:
    out1.write(f1_line+"\n")
    f1_line = in1.readline().strip()
  while f2_line and not f1_line:
    out2.write(f2_line+"\n")
    f2_line = in2.readline().strip()
in1.close()
in2.close()
out1.close()
out2.close()