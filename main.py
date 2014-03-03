import os


FPS_IN = 10
FPS_OUT = 24
FORMAT = '%1d'

os.system(
    "avconv -r %(FPS_IN)s -i img/image%(FORMAT)s.jpg -r %(FPS_OUT)s -vcodec"
    " libx264 -crf 20 -g 15 -vf crop=640:480,scale=320:240"
    " timelapse.mp4" %
    {
        'FPS_IN': FPS_IN,
        'FPS_OUT': FPS_OUT,
        'FORMAT': FORMAT,
    }
)
