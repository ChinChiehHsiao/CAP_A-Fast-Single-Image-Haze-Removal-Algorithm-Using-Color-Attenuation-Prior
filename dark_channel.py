import numpy as np

def dark_channel(image) : 
    # 3通道使用
    H, W, _ = image.shape
    patch_size = 15
    pad_size = patch_size // 2
    #創建 H*W 全零矩陣
    dc = np.zeros((H, W), dtype=np.float32)
    #填充邊界
    #用無限大的值填充的用意是取local min才不會影響到取值
    imJ = np.pad(image ,((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='constant', constant_values=np.inf)   
    #計算暗通道
    for j in range(H):
        for i in range(W):
            #遍例3通道, 所有patch為15
            patch = imJ[j:(j+patch_size), i:(i+patch_size),:]
            #將patch中抓到的local min存到dc(j, i)裡
            dc[j, i] = np.min(patch)
            
    return dc