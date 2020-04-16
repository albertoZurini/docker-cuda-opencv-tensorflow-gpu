# Docker CUDA OpenCV Tensorflow GPU

## Installation

Run `build/download_opencv.sh` to download OpenCV zips.
Run `docker_build.sh` and wait for OpenCV compilation. The build will be optimized for CUDA and will use all the cores available, so expect the host computer to be slowed down.

## Run

Before running `docker_run.sh` edit the volume passtrough.
To check if `tf` and `cv2` are working fine, try running `opencv.py` and `tensorflow.py` into the test folder.

## TODOs and known issues
- OpenCV build works with python 3.6 only

## Credits
- https://github.com/loitho/docker-opencv-cuda