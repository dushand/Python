#------------------------------------file01.txt---------------------------
#00650260048_c,,,The Pink Sheet
#05040390072,,,The Tan Sheet
#020108d4,,,Health News Daily
#02260160016_b,,,The Rose Sheet
#00630360023,relatedDocs,00630220023,The Pink Sheet
#--------------------------------------------------------------------------
#
#------------------------------------file02.txt----------------------------
#000105d2,,,Health News Daily
#00650260048_c,,,The Pink Sheet
#000105d5,,,Health News Daily
#05040390072,,,The Tan Sheet
#000106d1,,,Health News Daily
#000106d3,,,Health News Daily
#000106d4,,,Health News Daily
#000106d6,,,Health News Daily
#--------------------------------------------------------------------------
#
#-------------------------both.txt----------------------------------------
#00650260048_c
#05040390072
#020108d4
#02260160016_b
#00630360023
#000105d2
#00650260048_c
#000105d5
#05040390072
#000106d1
#000106d3
#000106d4
#000106d6
#--------------------------------------------------------------------------
#1.) Load file01.txt into a dictionary, with the key being id (the first value before the comma) and the value being the entire line of the file.  
#2.) Load file02.txt into a dictionary, with the key being the id (the first value before the comma) and the value being the entire line of the file.
#3.) For all of the ids in both.txt, determine which ids(keys) have different values between file01.txt and file02.txt.

#----------------Solution 01----------------------------------------------------------

import csv, sys, os.path
 
def csvToDict( filename ):
  result = {};
  if os.path.exists( filename ) :
    try :
      handle = open( filename );
      for line in csv.reader( handle, delimiter=',' ) :
        inx = line[ 0 ];
        data = ','.join( line );
        result[ inx ] = data
      handle.close();
    except :
      ( kind, val ) = sys.exc_info()[ :2 ];
      ( kind, val ) = str( kind ), str( val );
      print 'Error: ' + kind + '\nValue: ' + val;
  return result;
 
def CSVcompare( file1, file2 ):
  print 'file1: "%s"\nfile2: "%s"' % ( file1, file2 )
  d1 = csvToDict( file1 );
  d2 = csvToDict( file2 );
  n1 = d1.keys();
  n1.sort();
  for n in n1[ : ] :
    if d2.has_key( n ) :
      if d1[ n ] == d2[ n ] :
        del( d1[ n ] );
        del( d2[ n ] );
      else :
        print d1[ n ];
    else :
      print d1[ n ];
  print '-' * 50
  n2 = d2.keys();
  n2.sort();
  for n in n2[ : ] :
    if d1.has_key( n ) :
      if d1[ n ] != d2[ n ] :
        print d2[ n ];
    else :
      print d2[ n ];
 
 
def Usage( cmd = 'CSVcompare' ):
  print 'Uage: %s.py file1.csv file2.csv'
  sys.exit()
 
if __name__ == '__main__' or __name__ == 'main' :
  if len( sys.argv ) == 3 :
    CSVcompare( sys.argv[ 1 ], sys.argv[ 2 ] );
  else :
    Usage();
else :
  Usage( __name__ );
  
#----------------------------Solution02------------------------------------------
import csv
import sys
 
f1 = open(sys.argv[1], 'rt')
f2 = open(sys.argv[2], 'rt')
f3 = open(sys.argv[3], 'rt')
#f1 = csv.reader(open(sys.argv[1]),delimiter=',')
h={}
try:
    reader1 = csv.reader(f1, delimiter=',')
    reader2 = csv.reader(f2, delimiter=',')
    reader3 = csv.reader(f3, delimiter=',')
    for row1 in reader1:
#       print row1[0]
#       print ','.join(row1[1:])
#       h[row1[0]]=','.join(row1[1:])
#       print h
            print row1[1:]
#       if row1[0]!= "":
            for row2 in reader2:
#               if row2[0]!= "":
                    if row2[0] in row1[0]:
#                       if row2[1:] in row1[1:]:
                           print row2[0]
#           print row2[1:]
 
finally:
    f1.close()
    f2.close()
    f3.close()