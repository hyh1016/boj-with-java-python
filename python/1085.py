x, y, w, h = list(map(int, input().split(' ')))
close_w = w - x if x > (w / 2) else x
close_h = h - y if y > (h / 2) else y
print(min(close_w, close_h))
