from PIL import ImageGrab
import os
import time

def screenGrab():
	x = 84
	y = 90

	vmy = 177

	im = ImageGrab.grab((x, vmy, x+900, vmy+1286))
	im.save(os.getcwd() + "\\full_snap_" + str(int(time.time())) + ".png", "PNG")
	return im

if __name__ == '__main__':
	screenGrab()