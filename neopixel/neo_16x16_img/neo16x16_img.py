from microbit import *
from neopixel import NeoPixel

class neo16x16_img:
    def __init__(self,pin):
        self.np=NeoPixel(pin,256)

    def clear(self):
        self.np.clear()

    def show(self,dat,pos=0):
        for x in range(16):
            for y in range(8):
                if ((x+pos)*8)>=len(dat):
                    self.np[x*16+y*2]=(0,0,0)
                    self.np[x*16+y*2+1]=(0,0,0)
                else:
                    t=dat[(x+pos)*8+y]
                    r=t%16
                    g=(t>>4)%16
                    b=(t>>8)%16
                    if pos%2:
                        self.np[x*16+y*2]=(r,g,b) 
                    else:
                        self.np[x*16+15-y*2]=(r,g,b)
                    r=(t>>12)%16
                    g=(t>>16)%16
                    b=(t>>20)%16
                    if pos%2:
                        self.np[x*16+y*2+1]=(r,g,b) 
                    else:
                        self.np[x*16+14-y*2]=(r,g,b)
        self.np.show()

def _delay(t):
    while t>0:
        t=t-1

npdat=[
0x000000, 0x000000, 0x000000, 0x000000, 
0x121145, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x169156, 
0x000000, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x234000, 
0x15818B, 0x000217, 0x000000, 0x000000, 
0x000000, 0x000000, 0x129000, 0x0AE17B, 
0x000169, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x19C301, 
0x24709C, 0x00013A, 0x000000, 0x000000, 
0x000000, 0x000000, 0x116000, 0x169237, 
0x24718B, 0x245169, 0x000000, 0x000000, 
0x000000, 0x235000, 0x0CF09D, 0x1590AE, 
0x159159, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x17C149, 
0x09D18C, 0x0BF0BE, 0x23519C, 0x000234, 
0x000000, 0x17B000, 0x16B15C, 0x14817C, 
0x000024, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x002013, 
0x012000, 0x11A126, 0x000116, 0x000000, 
0x000000, 0x000000, 0x000000, 0x048012, 
0x16B149, 0x12716A, 0x000000, 0x000000, 
0x000000, 0x12811B, 0x147247, 0x09E16A, 
0x15B09D, 0x00010A, 0x000000, 0x000000, 
0x000000, 0x000000, 0x16C127, 0x0BE08D, 
0x17A0BF, 0x18B09C, 0x13A17A, 0x000227, 
0x214000, 0x0AE17A, 0x1680AE, 0x0AD235, 
0x0BE0BF, 0x00009C, 0x000000, 0x000000, 
0x000000, 0x000000, 0x236235, 0x158246, 
0x000245, 0x246312, 0x18B168, 0x200145, 
0x122000, 0x000123, 0x000000, 0x000000, 
0x000000, 0x235000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0xEEE000, 0xFC9FC9, 
0xFC9FC9, 0x000000, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9000, 0xFC9FC9, 
0xFC9FC9, 0xEEEFC9, 0x000000, 0x000000, 
0x000000, 0xAAA000, 0x555FC9, 0x000000, 
0x333000, 0xEEEFC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9FC9, 0x000000, 
0x000F90, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0xF99000, 
0x000000, 0xFC9FC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9FC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9FC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xFC9000, 0x000FC9, 0xF99000, 
0x000000, 0xFC9FC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9FC9, 0x000000, 
0x000F90, 0xFC9000, 0x000FC9, 0x000000, 
0x000000, 0xBBB000, 0x333FC9, 0x000000, 
0x111000, 0xEEEFC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9000, 0xFC9FC9, 
0xFC9FC9, 0xFC9FC9, 0x000000, 0x000000, 
0x000000, 0x000000, 0xFC9000, 0xFC9FC9, 
0xFC9FC9, 0x000000, 0x000000, 0x000000, 
]

ne = neo16x16_img(pin1)
n = 0
while True:
    ne.show(npdat, n)
    n = (n+16)%32
    _delay(15000)
