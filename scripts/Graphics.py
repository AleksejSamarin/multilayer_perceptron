import cv2
import numpy as np

class Graphics:

    def __init__(self, path, output_path, size, count, pos_x, pos_y, padding):
        self.codes = []
        self.output_path = output_path
        self.size = size
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


    def get_image_code(self, number, noise):
        print(f"Image number: {number}, noise: {noise}")
        code = np.copy(self.codes[number - 1])
        if noise:
            code[np.random.rand(*code.shape) < 0.2] ^= 1
        self.show_image(code * 255)
        return code


    def show_image(self, code):
        image = np.reshape(code, (self.size, self.size))
        rescaled = cv2.resize(image, (0, 0), fx=10, fy=10)
        cv2.imshow('Image', rescaled)