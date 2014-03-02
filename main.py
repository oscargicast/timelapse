import os


FPS_IN = 10
FPS_OUT = 24
os.system("avconv -r %s -i image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=500:500,scale=720:720 timelapse.mp4" % (FPS_IN, '%1d', FPS_OUT))
