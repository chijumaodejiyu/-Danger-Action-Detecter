from modules.base import init, get_image
from modules.detect import simple_detect, part_detect
from modules.action import action


def main():
    init_dict = init()
    capture_dict = init_dict['capture']
    image = get_image(capture_dict['finder'])
    simple_judgment, part_image = simple_detect(image)
    if simple_judgment:
        vector = part_detect(part_image)
        loc = locals()  # 把所有变量变为字典形式
        action(loc)
    else:
        pass