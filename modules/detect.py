import cv2
import numpy as np
import mediapipe as mp


def simple_detect(image: np.ndarray, loc: dict) -> (bool, np.ndarray):
    """
    从指定图片中准确检测危险行为并返回危险行为的方向向量
    :param image: 指定检测的图片
    :return: (判断结果, 大致发生的区域图片)
    """
    pass


def part_detect(image: np.ndarray, loc: dict) -> (np.float64, np.float64, np.float64):
    """
    从指定图片中简单的检测危险行为并返回判断结果和大致发生的区域图片
    :param image: 指定检测的图片
    :return: 危险行为的方向向量
    """
    # 初始化数据
    imageBGR = loc['imageBGR']
    image = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)
    simple = loc['detect']['simple']
    mpPose = simple['mpPose']
    pose = simple['pose']
    mpDraw = simple['mpDraw']

    result = pose.process(image)
    if result.pose_landmarks:
        for id_, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = image.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
