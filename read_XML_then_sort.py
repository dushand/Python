#
#
# To read following xml file.
# To filter/print  <eid> values of  <status>failed</status> type tags.


#<documents>
#  <doc>
#    <eid>766877_765765765_load</eid>
#    <reporter>dushan</reporter>
#    <trans-type>add</trans-type>
#    <status>failed</status>
#    <time-req-received>1287660397</time-req-received>
#    <time-process-start>2009-07-22T19:48:34+00:00</time-process-start>
#    <time-process-complete>2007-05-22T20:00:00+00:00</time-process-complete>
#    <load-unit-id></load-unit-id>
#    <item-transaction-id></item-transaction-id>
#    <status-detail>processing failure</status-detail>
#  </doc>
#  <doc>
#    <eid>123456789</eid>
#    <reporter>dushan</reporter>
#    <trans-type>add</trans-type>
#    <status>success</status>
#    <time-req-received>987654321</time-req-received>
#    <time-process-start>2009-07-16T03:01:26+00:00</time-process-start>
#    <time-process-complete>2009-07-16T06:00:00+00:00</time-process-complete>
#    <load-unit-id></load-unit-id>
#    <item-transaction-id></item-transaction-id>
#    <status-detail></status-detail>
#  </doc>
#  <doc>
#    <eid>6789123455</eid>
#    <reporter>dushan</reporter>
#    <trans-type>add</trans-type>
#    <status>success</status>
#    <time-req-received>5543219876</time-req-received>
#    <time-process-start>2009-07-16T03:01:50+00:00</time-process-start>
#    <time-process-complete>2009-07-16T06:00:00+00:00</time-process-complete>
#    <load-unit-id></load-unit-id>
#    <item-transaction-id></item-transaction-id>
#    <status-detail></status-detail>
#  </doc>
#</documents>


#------------------------------------------------------------
import glob
import os
import sets
import sys
import xml.dom.minidom
 
def dictOfFailed(fname):
 
    # Parse the existing file
    #
    assert os.path.isfile(fname)
    dom = xml.dom.minidom.parse(fname)
     
    # Initialize the resulting dictionary for the eids
    # of the failed documents and then parse the file
    # and collect the info.
    #
    result = {}
    for doc in dom.getElementsByTagName('doc'):    # through all doc elements
        lst = doc.getElementsByTagName('status')   
        assert len(lst) == 1                       # a doc should contain a single status element
        status = lst[0].firstChild.data            # the text of the status element
     
        if status == u'failed':                    # pay attention to unicode
            lst = doc.getElementsByTagName('eid')  
            assert len(lst) == 1                   # the doc should contain a single eid element
            eid = lst[0].firstChild.data           # the eid value as text 
            
            lst = doc.getElementsByTagName('time-process-complete')  
            assert len(lst) == 1
            tpc = lst[0].firstChild.data
            
            if tpc not in result:
                result[tpc] = sets.Set()    # init -- create the empty set of eids
 
            # Add the eid to the set of eids related to the same time.
            result[tpc].add(eid)    
        else:
            continue
            
    # Return the collected information.
    return result
            
            
if __name__ == '__main__':
    myPath = '.'               # default path
    if len(sys.argv) > 1:
        myPath = sys.argv[1]   # explicit path to your xml files
        
    # Get all XML file names from the path and process them.
    # Union all results to the result dictionary where time is the key.
    resultDic = {}
    for fname in glob.glob(os.path.join(myPath, '*.xml')):
        d = dictOfFailed(fname)   # get the dictionary of failed eids
        
        # Loop through the collected times and union the related sets of eids.
        for tpc in d:
            if tpc not in resultDic:
                resultDic[tpc] = sets.Set()  # init
            resultDic[tpc].update(d[tpc])    # union of the sets of eids
                
    # Sort the keys of the result dic and present the info from inside.
    lst = resultDic.keys()
    lst.sort()
    for tpc in lst:
        print '%s (%d eids): %s' % (tpc, len(resultDic[tpc]), 
                                    repr(list(resultDic[tpc])))