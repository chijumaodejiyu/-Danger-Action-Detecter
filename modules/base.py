import numpy as np
import mediapipe as mp


def init(loc: dict) -> dict:
    """
    利用loc初始化并以字典形式返回的所需变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的所需变量（包含：'servo', 'capture' 等）
    """
    # detect
    detect = init_detect(loc)

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
    """
    mpPose = mp.solutions.pose  # 姿态检测模块
    pose = mpPose.Pose()  # 检测模块
    mpDraw = mp.solutions.drawing_utils  # 绘画模块
    connections = mpPose.POSE_CONNECTIONS  # 连接点

    output = locals()
    return output


def init_simple_detect(loc: dict) -> dict:
    """
    初始化simple_detect的相关变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的simple_detect的相关变量
    """
    pass


def get_image(capture) -> np.ndarray:
    """
    从指定摄像头中获取图片并返回
    :param capture: 指定的摄像头
    :return: 从摄像头中获取的图片
    """
    pass
