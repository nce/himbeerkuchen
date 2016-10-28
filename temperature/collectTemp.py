#!/usr/bin/python

import re, os, rrdtool, time

def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e
  return value

pathes = (
  "/sys/bus/w1/devices/28-0416354bbaff/w1_slave",
  "/sys/bus/w1/devices/28-041635684cff/w1_slave"
)

data = 'N'
t_end = time.time() + 60 * 30

while time.time() < t_end:
        data = 'N'

        for path in pathes:
            data += ':' + read_sensor(path)

        print data
        rrdtool.update("%s/temperature.rrd" % (os.path.dirname(os.path.abspath(__file__))), data)

        time.sleep(2)


