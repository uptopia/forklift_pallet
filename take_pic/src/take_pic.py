#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import rospy
from sensor_msgs.msg import Image
import cv2
import sys
if sys.version > '3': #ROS自帶的cv_bridge只支持python2，想要使用Python3需要自行編譯cv_bridge包
    sys.path.insert(0, '/opt/installer/open_cv/cv_bridge/lib/python3/dist-packages/')
from cv_bridge import CvBridge, CvBridgeError

cnt = 0

def img_rgb_callback(msg):
    global cnt

    bridge = CvBridge()
    try: 
        rgb_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow('rgb_image', rgb_image)
        k = cv2.waitKey(1)

        if k%256 == 32: #press SPACE
            img_name = './test_img/altek_img_{}.jpg'.format(cnt)
            cv2.imwrite(img_name, rgb_image)
            print('{} saved'.format(img_name))
            cnt+=1
    except CvBridgeError as e:
        print(e)

def listener():
    rospy.init_node('altek_take_pic')
    rospy.Subscriber('/camera/color/image_raw', Image, img_rgb_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()