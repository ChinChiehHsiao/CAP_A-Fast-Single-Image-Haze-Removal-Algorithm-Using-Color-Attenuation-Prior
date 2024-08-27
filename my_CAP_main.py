import numpy as np
import os
import cv2

import dark_channel
import recover
import local_minimum
import atmospheric_light



def CAP_main_dehaze(image_name, beta):

    image = (cv2.imread(image_name).astype(np.float32))/255.0

    dc = dark_channel.dark_channel(image)
    A = atmospheric_light.atmospheric_light(image, dc)

    image_bgr2hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _, s, v = cv2.split(image_bgr2hsv)

    H, W, _ = image.shape
    sigma = 0.041337
    sigmaMat = np.random.normal(0, sigma, (H, W)).astype(np.float32)
    d = 0.121779 + 0.959710*v - 0.780245*s + sigmaMat
    local_min_d = local_minimum.local_minimum(d)
    GF_d = cv2.ximgproc.guidedFilter(guide=image, src=local_min_d, radius=15, eps=1e-3)

    result_dehaze, t, clip_t = recover.recover(image, A, GF_d, beta)

    return image, dc, sigmaMat, d, local_min_d, GF_d, t, clip_t, result_dehaze



input_folder  = "my dataset"
output_folder = "my result"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_count = 0

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        image_count += 1
        image_path = os.path.join(input_folder, filename)
        file_base_name = os.path.splitext(filename)[0]
        print(file_base_name)

        individual_output_folder = os.path.join(output_folder, f"{file_base_name}")
        if not os.path.exists(individual_output_folder):
            os.makedirs(individual_output_folder)

        image, dc, sigmaMat, d, local_min_d, GF_d, t, clip_t, CAP_beta_10 = CAP_main_dehaze(image_path, beta = 1.0)

        output_path_ori = os.path.join(individual_output_folder, f"{file_base_name}.png")
        cv2.imwrite(output_path_ori, (image * 255).astype(np.uint8))

        output_path_d = os.path.join(individual_output_folder, f"d ({file_base_name}).png")
        cv2.imwrite(output_path_d, (np.clip(d, 0, 1) * 255).astype(np.uint8))
        output_path_local_min_d = os.path.join(individual_output_folder, f"local_min_d ({file_base_name}).png")
        cv2.imwrite(output_path_local_min_d, (np.clip(local_min_d, 0, 1) * 255).astype(np.uint8))
        output_path_GF_d = os.path.join(individual_output_folder, f"GF_d ({file_base_name}).png")
        cv2.imwrite(output_path_GF_d, (np.clip(GF_d, 0, 1) * 255).astype(np.uint8))

        output_path_t = os.path.join(individual_output_folder, f"t ({file_base_name}).png")
        cv2.imwrite(output_path_t, (np.clip(t, 0, 1) * 255).astype(np.uint8))
        output_path_clip_t = os.path.join(individual_output_folder, f"clip_t ({file_base_name}).png")
        cv2.imwrite(output_path_clip_t, (clip_t * 255).astype(np.uint8))

        output_path_CAP10 = os.path.join(individual_output_folder, f"my_CAP beta=1.0 ({file_base_name}).png")
        cv2.imwrite(output_path_CAP10, (CAP_beta_10 * 255).astype(np.uint8))

print("===========================================================")
# print("\n")
print(f"總共讀入了 {image_count} 張圖片")
