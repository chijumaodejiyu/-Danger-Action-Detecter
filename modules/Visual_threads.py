import cv2
import numpy as np
from copy import deepcopy
import threading
from PyCameraList.camera_device import list_video_devices

thread_lock = threading.Lock()  # 全局线程锁
thread_exit = False  # 定义全局变量thread_exit,标志主线程退出，初始化False


def get_cap_list():
    """
        调用PyCameraList获取可用摄像头的名称及id
        :param None
        :return: 以字典形式返回所有的摄像头信息（eg. {0: 'Intel(R) RealSense(TM) 3D Camera (Front F200) RGB', 1: 'NewTek NDI Video'}））
    """
    cameras = list_video_devices()
    camera_num = len(cameras)
    print('可用摄像头数量：' + str(camera_num) + "个\n")
    for i in range(0, camera_num, 1):
        print(str(i) + '----' + str(cameras[i]))
    return cameras


class Visual(threading.Thread):
    def __init__(self, camera_id, img_height, img_width):
        super(Visual, self).__init__()
        self.camera_id = camera_id
        self.img_height = img_height
        self.img_width = img_width
        self.frame = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    def get_frame(self):
        """
        获取视频推流的接口方法
        :return: self.frame的重置大小后的摄像头画面
        """
        return deepcopy(self.frame)

    def run(self):
        """
        打开cap获取画面
        :return: 向get_frame方法传参
        """
        global thread_exit
        cap = cv2.VideoCapture(int(self.camera_id))
        while not thread_exit:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (self.img_width, self.img_height))
                thread_lock.acquire()
                self.frame = frame
                thread_lock.release()
            else:
                thread_exit = True
                print("无法读取摄像头")
        cap.release()


"""
class CapWide(Visual):
    def __init__(self):
        super().__init__()
        pass
"""


#  暂时无用的cap子类


def test():
    """
    Visual类的测试方法
    :return: 测试画面显示窗口
    """
    global thread_exit
    img_height = 480
    img_width = 640
    cap_list = get_cap_list()
    print(cap_list)
    camera_id = int(input("输入测试对象摄像头ID："))
    thread = Visual(camera_id, img_height, img_width)
    thread.start()

    while not thread_exit:
        thread_lock.acquire()
        frame = thread.get_frame()
        thread_lock.release()
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            thread_exit = True
    thread.join()


if __name__ == "__main__":
    test()
