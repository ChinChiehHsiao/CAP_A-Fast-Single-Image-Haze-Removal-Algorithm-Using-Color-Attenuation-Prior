# (2015) CAP_A Fast Single Image Haze Removal Algorithm Using Color Attenuation Prior
![My Image](https://github.com/user-attachments/assets/8383ff97-e215-44ee-997b-36f740f1fb52)



References : ZHU, Qingsong; MAI, Jiaming; SHAO, Ling. A fast single image haze removal algorithm using color attenuation prior. IEEE transactions on image processing, 2015, 24.11: 3522-3533.<br><br>
顏色衰減先驗圖像去霧文章復現<br>
使用python<br><br>
- 原文PDF &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;：[點擊此連結](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7128396)
- 原文DOI &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;：[點擊此連結](https://doi.org/10.1109/TIP.2015.2446191)
- 原作者code &nbsp;：[點擊此連結](https://github.com/JiamingMai/Color-Attenuation-Prior-Dehazing)<br><br>


操作說明 
---
把圖片放進 `my dataset` 資料夾，打開 `my_CAP_main.py` 檔案執行即可<br>
結果圖將儲存在 `my result` 資料夾中。<br><br>


result檔案名稱說明
---
- 原圖名稱
- d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 深度圖
- local_min_d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 深度圖取local_min
- GF_d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 取 guide filter(引導圖=原圖, 輸入圖=local_min_d, r=15, eps=1e-3)
- t &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : GF_d 還原的 transmission, &beta; = 1
- clip_t &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 截斷(t, 0.1, 0.9)
- my_CAP beta=1.0 &nbsp; : 最終去霧結果圖<br><br>

---
關於
---

- 復現 : 蕭晉杰
- 時間 : 2024.08.27
