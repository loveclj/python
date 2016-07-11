#!/usr/bin/env python
# encoding: utf-8

import Image
import os


def make_post_thumb(path, sizes=[(1200,550), (750,230), (365,230)]):
    """
    sizes 参数传递要生成的尺寸，可以生成多种尺寸
    """
    base, ext = os.path.splitext(path)
    print path
    try:
        im = Image.open(path)
    except IOError:
        print ' in  IOError'
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            im.load()
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255,255,255), None, bgmask)
        else:
            im = im.convert('RGB')

    width, height = im.size
    
    for size in sizes:
        filename = base + str(size[0]) + ".jpg"
        if float(width) / float(height) == float(str(size[0])) / float(str(size[1])):
            im_1200 = im
            im_1200.save(filename, quality=100)
        if float(width) / float(height) < float(size[0]) / float(size[1]):
            im_1200 = im.resize((int(size[0]), int(float(height)/(float(width)/float(size[0])))), Image.ANTIALIAS) #先把大图缩小到size宽
            im_1200_width, im_1200_height = im_1200.size
            delta = (im_1200_height - int(size[1]))/2
            box = (0, delta, int(size[0]), delta+int(size[1]))
            region = im_1200.crop(box)
            region.save(filename, quality=100)
        if float(width) / float(height) > float(size[0]) / float(size[1]):
            im_1200 = im.resize((int(float(width)/(float(height)/float(size[1]))), int(size[1])), Image.ANTIALIAS) #先把大图缩小到size高
            im_1200_width, im_1200_height = im_1200.size
            delta = (im_1200_width - int(size[0]))/2
            box = (delta, 0, delta+int(size[0]), int(size[1]))
            region = im_1200.crop(box)
            region.save(filename, quality=100)

if __name__ == "__main__":
    make_post_thumb("/home/lizhifeng/dog.jpg", [(100, 500)])