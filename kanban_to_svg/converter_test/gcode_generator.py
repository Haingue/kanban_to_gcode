from ttgLib.TextToGcode import ttg

ON = "M02 S500"
OFF = "M05 S0"
FAST = "G0"
SLOW = "G1"

def generate_title (title):
  gcode = ttg(title,1,0,"return",1).toGcode(ON, OFF, FAST, SLOW)
  gcode[3] = ' X2 Y10'
  return gcode

def exemple_text():
  title = "Hello"
  gcode = generate_title(title)
  for line in gcode:
    print(line)