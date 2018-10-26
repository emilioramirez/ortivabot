#!/usr/bin/env python3
import numpy as np
import sounddevice as sd


DURATION = 60 #in seconds
SECOND = 1000


def audio_callback(indata, frames, time, status):
   volume_norm = np.linalg.norm(indata) * 10
   print("|" * int(volume_norm))


def function():
    stream = sd.InputStream(callback=audio_callback)
    with stream:
        sd.sleep(DURATION * SECOND)


def function1():

    def callback(indata, outdata, frames, time, status):
        print("input", indata)
        print("outdata", outdata)
        print("frames", frames)
        print("time", time)
        print("status", status)
        # if status:
        #     print(status)
        # outdata[:] = indata

    with sd.Stream(channels=2, callback=callback):
        sd.sleep(int(DURATION * SECOND))


if __name__ == "__main__":
    function()
    # function1()