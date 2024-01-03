import numpy as np
# main.py -->ltdxsy


def main():

    loc = locals()
    init_dict = init(loc)
    servo_dict = init_dict['servo']
    capture_dict = init_dict['capture']
    image = get_image(capture_dict['finder'])
    simple_judgment, part_image = simple_detect(image)
    if simple_judgment:
        angel = part_detect(part_image)
        loc = locals()  # 把所有变量变为字典形式
        action(loc)
    else:
        pass


# modules/base.py -->cjmdjy


def init(loc: dict) -> dict:
    """
    利用loc初始化并以字典形式返回的所需变量
    :param loc: 以字典形式储存的所需数据
    :return: 以字典形式返回的所需变量（包含：'servo', 'capture' 等）
    """
    pass


def get_image(capture) -> np.ndarray:
    """
    从指定摄像头中获取图片并返回
    :param capture: 指定的摄像头
    :return: 从摄像头中获取的图片
    """
    pass



# modules/visual_threads.py -->cjmdjy
def


# modules/detect.py -->cjmdjy


def simple_detect(image: np.ndarray) -> (bool, np.ndarray):
    """
    从指定图片中简单的检测危险行为并返回判断结果和大致发生的区域图片
    :param image: 指定检测的图片
    :return: (判断结果, 大致发生的区域图片)
    """
    pass


def part_detect(image: np.ndarray) -> (np.float64, np.float64, np.float64):
    """
    从指定图片中准确检测危险行为并返回危险行为的方向向量
    :param image: 指定检测的图片
    :return: 危险行为的方向向量
    """
    pass


# modules/action.py -->cjmdjy, ltdxsy


def action(loc: dict):
    """
    利用已知变量执行特定行为
    :param loc: 以字典形式储存的已知变量
    :return: None
    """
    pass

