from modules.base import init, get_image
from modules.detect import simple_detect, part_detect
from modules.action import action


def main():

    loc = locals()  # 把所有变量变为字典形式
    init_dict = init(loc)  # 初始化所需变量
    capture_dict = init_dict['capture']  # 解出 'capture'
    image = get_image(capture_dict['finder'])  # 获取 'finder' 的图片
    simple_judgment, part_image = simple_detect(image)  # 初步检测
    if simple_judgment:
        vector = part_detect(part_image)  # 精准检测
        loc = locals()  # 把所有变量变为字典形式
        action(loc)  # 执行特定行为
    else:
        pass
