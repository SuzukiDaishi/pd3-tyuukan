import cv2, glob


for p in glob.glob('sp_code_x2/*.png'):
    img = cv2.imread(p)
    cv2.imwrite(p, img[:, 240:-470])