import numpy as np

def atmospheric_light(image, dark_channel):
	#在暗通道中找最亮的像素，並在原3通道彩圖中找到對應的位置，來計算大氣光的顏色

	H, W, _ = image.shape
	imsize = H * W													#計算圖像總像素數量
	numpx = np.floor(imsize / 1000).astype(int)						#計算要選擇的像素數量，選前0.1%，並向下取整
	dark_channel_Vec = dark_channel.ravel()							#將dark_channel展平成 imsize *1 的列向量
	ImVec = image.reshape(imsize, 3)								#將原始影像image展平成 imsize * 3 的矩陣
	indices = np.argsort(dark_channel_Vec)							#對暗通道進行升序排序，indices=索引值
	indices = indices[-numpx:]										#選擇排序後最亮的0.1%，計算從哪裡開始提取索引的起點，並到end
	atmSum = np.zeros(3, dtype=np.float32)							#計算大氣光的顏色，創建 1 * 3 全0矩陣，用來儲存最亮像素的顏色值累加和

	#遍例所有選中的像素
	for ind in range(numpx):
		atmSum += ImVec[indices[ind]]								#將每個選中像素的RGB顏色值累加到atmSum

	A = atmSum / numpx												#將atmSum取平均，即為大氣光的顏色

	return A
