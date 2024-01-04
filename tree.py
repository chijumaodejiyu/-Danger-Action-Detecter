import numpy as np
# main.py  -> ltdxsy


def main():

    loc = locals()  # 把所有变量变为字典形式
    init_dict = init(loc)  # 初始化所需变量
    capture_dict = init_dict['capture']  # 解出 'capture'
    image = get_image(capture_dict['finder'])  # 获取 'finder' 的图片
    simple_judgment, item_bbox = simple_detect(image)  # 初步检测
    if simple_judgment:
        part_image = get_part_image(image, item_bbox)  # 获取疑似危险行为相关的区域图片
        judgment = part_detect(part_image)  # 精准检测
        # 数据整合为字典
        loc = locals()
        del loc['init_dict']
        loc = loc | init_dict
        action(loc)  # 执行特定行为
    else:
        pass


# modules/base.py  -> cjmdjy


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


def get_part_image(image, item_bbox) -> np.ndarray:
    """
    利用指定item_bbox在image中截取部分区域图片并返回
    :param image: 原图片
    :param item_bbox: 以(x1, y1, x2, y2, '', id)形式储存的数据
    :return: 在image中截取部分区域图片并返回
    """


# modules/detect.py  -> ltdxsy, cjmdjy


def simple_detect(image: np.ndarray) -> (bool, np.ndarray):  # -> ltdxsy
    """
    从指定图片中简单的检测危险行为并返回判断结果和其item_bbox
    :param image: 指定检测的图片
    :return: (判断结果, 其item_bbox)
    """
    pass


def part_detect(image: np.ndarray) -> np.float64:
    """
    从指定图片中准确检测危险行为并返回置信度
    :param image: 指定检测的图片
    :return: 危险行为的置信度
    """
    pass


# modules/action.py  -> ltdxsy, cjmdjy


def action(loc: dict):
    """
    利用已知变量执行特定行为
    :param loc: 以字典形式储存的已知变量
    :return: None
    """
    pass


def track(loc: dict) -> bool:
    """
    利用loc['servo']['track']的舵机控制模块旋转至指定向量
    :param loc: 变量库
    :return: 执行结果
    """
    pass


def draw(loc: dict) -> bool:
    """
    在loc['screen']['picture']的基础上进行额外绘制行为并重写入loc['screen']['picture']
    :param loc: 变量库
    :return: 执行结果
    """
    pass


def show(loc: dict) -> bool:
    """
    利用loc['screen']显示界面
    :param loc: 变量库
    :return: 执行结果
    """
    pass
