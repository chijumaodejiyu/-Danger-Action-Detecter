import numpy as np
import cv2


def init(data: dict) -> dict:
    """
    利用data初始化并以字典形式返回的所需变量
    :param data: 以字典形式储存的所需数据
    :return: 以字典形式返回的所需变量（包含：'servo', 'capture' 等）
    """
    output = {}
    cap_finder = cv2.VideoCapture(0)
    capture = {}
    capture['finder'] = cap_finder
    output['capture'] = capture
    return output


def get_image(capture) -> np.ndarray:
    """
    从指定摄像头中获取图片并返回
    :param capture: 指定的摄像头
    :return: 从摄像头中获取的图片
    """
    pass


if __name__ == '__main__':
    data = {}
    capture_channel = {'finder': 0, 'tracker': 1}
    data['capture_channel'] = capture_channel
