import numpy as np
import mediapipe as mp
import threading
from Visual_threads import get_cap_list, Visual


def init(loc: dict) -> dict:
    """
    利用loc初始化并以字典形式返回的所需变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的所需变量
    {
        'detect' : detect的相关变量,
        'threads' : threads的相关变量
    }
    """
    # detect
    detect = init_detect(loc)  # detect的相关变量
    # threads
    threads = init_threads(loc)   # threads的相关变量

    output = locals()
    return output


def init_detect(loc: dict) -> dict:
    """
    初始化detect的相关变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的detect的相关变量
    """
    simple = init_simple_detect(loc)
    part = init_part_detect(loc)
    detect = locals()
    return detect


def init_part_detect(loc: dict) -> dict:
    """
    初始化part_detect的相关变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的part_detect的相关变量
    {
        'mpPose' : 姿态检测模块,
        'pose' : 检测模块,
        'mpDraw' : 绘画模块,
        'connections' : 连接点对
    }
    """
    mpPose = mp.solutions.pose  # 姿态检测模块
    pose = mpPose.Pose()  # 检测模块
    mpDraw = mp.solutions.drawing_utils  # 绘画模块
    connections = mpPose.POSE_CONNECTIONS  # 连接点对

    output = locals()
    return output


def init_simple_detect(loc: dict) -> dict:
    """
    初始化simple_detect的相关变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的simple_detect的相关变量
    """
    pass


def init_threads(loc: dict) -> dict:
    """
    初始化visual_threads的相关变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的visual_threads的相关变量
    {
        'lock' : 全局线程锁,
        'exit' : 定义全局变量thread_exit，标志主线程退出，默认为False
    }
    """
    lock = threading.Lock()  # 全局线程锁
    exit = False  # 定义全局变量thread_exit，标志主线程退出，初始化False

    output = locals()
    return output


def get_image(capture) -> np.ndarray:
    """
    从指定摄像头中获取图片并返回
    :param capture: 指定的摄像头
    :return: 从摄像头中获取的图片
    """
    init_threads(l)
    img_height = 480
    img_width = 640
    camera_id = capture
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

