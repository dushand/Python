#I have hostnames on following flie.
#
#----------http://example.host.com/abc.php-------------
#host1
#host2
#host3
#host4
#---------------------------------------------------------------------
#
#And on each host have following file locations.
#
#http://host1.example.com/pqr.php 
#http://host2.example.com/pqr.php 
#http://host3.example.com/pqr.php 
#http://host4.example.com/pqr.php 
#
#Please find attached code of one pqr.php
#
#I want to read every pqr.php file on each host and I want to print summery report in one page. 
#----------------------------------------------------------------------------------------------------
#<node-status>
#<fdispatch>
#<version value="123"/>
#<httpdconn calls-to-constructor="2" calls-to-destructor="0" select-operations="17552"/>
#<searchhandler active-count="0" instantiate-count="0"/>
#<datasets>
#<dataset id="0" partitions="1" first-partition="0" max-active-nodes="1" active-nodes="1" max-active-partitions="1" active-partitions="1" unit-selection-cost="1" total-selection-cost="0" up-time="123.456" total-search-time="1.367" total-searches="4" avg-sec-per-search="0.342" avg-searches-per-sec="0.000" avg-uncached-search-time="0.342" samples="4" timed-out="0" timed-out-percentage="0.000">
#<engine socket="node1.example.com:15714" state="up" type="search" partition="0" row="0" refcost="1" docstamp="32472487243" avg-search-time="0.329" samples="4"/>
#</dataset>
#</datasets>
#<httpd select-operations="23123723" waiting-connections="0" open-connections="1" connection-limit="1024"/>
#<filedesc-resource wait-queue-len="0" resource-usage="20" total-resource-count="1014"/>
#</fdispatch>
#</node-status>
#----------------------------------------------------------------------------------------------------

import xml.dom.minidom
 
# Get the page content.
content = '''\
<system-descriptor>
  <component type="search" name="column0/0" node="node1.example.com"/>
  <component type="indexer" name="indexer-0-0" node="node2.example.com"/>
</system-descriptor>
'''
  
# Parse it.
dom = xml.dom.minidom.parseString(content)   # or ...minidom.parse(filename)
 
# Extract and process the component elements with certain type.
for elem in dom.getElementsByTagName('component'):   # list of all component elements iterated
    if elem.getAttribute('type') == u'indexer':
        print elem.getAttribute('node')