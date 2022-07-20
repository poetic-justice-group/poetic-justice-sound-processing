# Poetic Justice Sound Processing 

This repository will be a collection of functions for common sound-processing operations that we will need throughout different projects. In general, the approach is to give the functions a common interface despite using different third party libraries under the hood. 

## Currently Supported Operations

* File I/O - reading and writing sound files
* Converting format (.mp3 -> .wav, etc.)
* Changing the sample rate (22 kHz -> 10 kHz, etc.)
* Low pass filter
* Noise reduction

## In progress

* Vocal activity detector (via WebRTC: https://github.com/wiseman/py-webrtcvad)