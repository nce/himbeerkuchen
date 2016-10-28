RRD Tools
---------

```
$ rrdtool create temperature.rrd --step 2 DS:temp0:GAUGE:2:15:35 DS:temp1:GAUGE:2:15:35 RRA:AVERAGE:0.5:1:1920 RRA:AVERAGE:0.5:1:1920
$ rrdtool graph 30min.png -s 'now - 30 minute' -e 'now' DEF:temp0=temperature.rrd:temp0:AVERAGE   LINE2:temp0#00FF00:TEMP1   DEF:temp1=temperature.rrd:temp1:AVERAGE   LINE2:temp1#0000FF:TEMP2
```
