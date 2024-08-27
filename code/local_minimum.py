import numpy as np

def local_minimum(image):
    # 單通道使用
    H, W = image.shape
    patch_size = 15
    pad_size = patch_size // 2
    #創建 H*W 全零矩陣
    local_min = np.zeros((H, W), dtype=np.float32)
    #填充邊界
    #用無限大的值填充的用意是取local min才不會影響到取值
    imJ = np.pad(image ,((pad_size, pad_size), (pad_size, pad_size)), mode='constant', constant_values=np.inf)   
    #計算local min
    for j in range(H):
        for i in range(W):
            patch = imJ[j:(j+patch_size), i:(i+patch_size)]
            local_min[j, i] = np.min(patch)
            
    return local_min
