from PIL import Image
from PIL import ImageDraw
import os


def pict_redact(dir, px_color_orig, px_color_ch):
    with Image.open(dir) as im:
        w, h = im.size[0], im.size[1]
        px = im.load()
        for x in range(w):
            for y in range(h):
                current_color = px[x, y]
                if current_color[0] == px_color_orig[0] and current_color[1] == px_color_orig[1] and current_color[2] == px_color_orig[2]:
                    px[x, y] = px_color_ch
        im.save(r"C:\Users\semen\OneDrive\Изображения\Cyberpunk 2077\hz.png")


pict_redact(r"1660473843583.jpg", (255, 255, 255), (0, 0, 0, 255))
