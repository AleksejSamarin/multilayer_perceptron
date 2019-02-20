import cv2
import numpy as np

class Graphics:

    def __init__(self, path, output_path, size, count, pos_x, pos_y, padding):
        self.codes = []
        img = cv2.imread(path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, bin_img = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite(output_path + 'main_bin.png', bin_img)
        # cv2.imshow('Image', bin_img)
        # cv2.waitKey(0)

        for i in range(count):  # 11, 11, 25
            part = bin_img[pos_y:pos_y + size, pos_x:pos_x + size]
            cv2.imwrite(output_path + str(i + 1) + '_part.png', part)
            pos_x += size + padding
            part[part > 0] = 1
            self.codes.append(np.asarray(part).reshape(-1)) # one-row array


    def get_codes(self):
        return np.array(self.codes)
