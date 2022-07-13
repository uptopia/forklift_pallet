# forklift_pallet

cd ~/Altek_ws
git clone --recursive https://github.com/uptopia/forklift_pallet.git src

. devel/setup.bash
roslaunch realsense2_camera rs_camera.launch

cd ~/Altek_forklift_pallet
. devel/setup.bash
rosrun take_pic take_pic.py