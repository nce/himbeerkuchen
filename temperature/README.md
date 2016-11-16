RRD Tools
---------

```
$ sudo apt install rrdtool python-rrdtool
$ rrdtool create temperature.rrd --step 2 DS:temp0:GAUGE:6:15:45 DS:temp1:GAUGE:6:15:45 RRA:AVERAGE:0.5:1m:5400 RRA:AVERAGE:0.5:1m:5400
$ rrdtool graph /var/www/html/30min.png -w 800 -h 200 -a PNG -u 45 -l 15 -r --slope-mode --vertical-label 'Grad in Celsius' -s 'now - 90 minute' -e 'now' DEF:temp0=temperature.rrd:temp0:AVERAGE   LINE2:temp0#00FF00:TEMP1   DEF:temp1=temperature.rrd:temp1:AVERAGE   LINE2:temp1#0000FF:TEMP2 
```
