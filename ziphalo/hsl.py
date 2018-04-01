import math

def hsl2rgb(h,s,l):
    h = (h - math.floor(h)) * 6
    c = (1 - abs(2 * l - 1)) * s * 255
    m =  l * 255 - c/2
    x = c * (1 - abs(h%2 - 1))
    if h < 1:
        return int(c + m), int(x + m), int(m)
    elif h < 2:
        return int(x + m), int(c + m), int(m)
    elif h < 3:
        return int(m), int(c + m), int(x + m)
    elif h < 4:
        return int(m), int(x + m), int(c + m)
    elif h < 5:
        return int(x + m), int(m), int(c + m)
    else:
        return int(c + m), int(m), int(x + m)


def hsv2rgb(h,s,v):
    h = (h - math.floor(h)) * 6
    m = (v - s*v)*255 
    c = s * v * 255 
    x = c * (1 - abs(h%2 - 1)) 
    if h < 1:
        return int(c+m),int(x+m),int(m)
    elif h < 2:
        return int(x+m),int(c+m),int(m)
    elif h < 3:
        return int(m),int(c+m),int(x+m)
    elif h < 4:
        return int(m),int(x+m),int(c+m)
    elif h < 5:
        return int(x+m),int(m),int(c+m)
    else:
        return int(c+m),int(m),int(x+m)

