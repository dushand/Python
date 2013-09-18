#send an email with table(using HTMLTags

#!/bin/sh
if awk 'BEGIN  {
  FS = ","; x=1; y=1};
        NR > 1 {if ($4!=$3) {
                    if (y%2==0){
                    print "<tr style=!background: #ADABB3!><td>" $1 "</td><td>" $2 "</td><td>" $3 "</td><td>" $4 "</td><td style=!background: #F1595A!>" $4-$3 "</td></tr>";}
                    else {
                    print "<tr style=!background: #EAEAEA!><td>" $1 "</td><td>" $2 "</td><td>" $3 "</td><td>" $4 "</td><td style=!background: #F1595A!>" $4-$3 "</td></tr>";}
y=y+1;
}
};
        END    {exit(x)}' |tr @! \"\' > tmpfile
then
(echo 'To: abc@abc.com
Subject: Discrepancies between 'ICS' & 'Native Products' Indexes
Content-Type: text/html; charset="us-ascii"

<html>
<table border="1" bordercolor="#000000"" width="100%" cellpadding="0"  cellspacing="0">
  <tr style="background-color:#7B7881">
    <th>Cluster</th>
    <th>Query</th>
    <th>Data Results</th>
    <th>Product Results</th>
    <th>Results &#916; </th>
  </tr>'
cat tmpfile
echo '</table>
</html>') > tmpfile2 && echo "Sending mail" && /usr/sbin/sendmail prr@pqr.com,klm@pqr.com,prd@pqr < tmpfile2
fi