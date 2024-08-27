# (2015) CAP_A Fast Single Image Haze Removal Algorithm Using Color Attenuation Prior

顏色衰減先驗圖像去霧文章復現<br>
使用python<br><br>



操作說明 
---

打開 my_CAP_main.py 檔案，把圖片放進 my dataset 資料夾，執行即可。<br>
結果圖將儲存在 my result 資料夾中。<br><br>


result檔案名稱說明
---
- 原圖名稱
- d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 深度圖
- local_min_d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 深度圖取local_min
- GF_d &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 取 guide filter(引導圖=原圖, 輸入圖=local_min_d, r=15, eps=1e-3)
- t &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : GF_d 還原的 transmission, &beta; = 1
- clip_t &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : 截斷(t, 0.1, 0.9)
- my_CAP beta=1.0 : 最終去霧結果圖



|                  |                                 |
|------------------|---------------------------------|
| 原圖名稱         | : 深度圖                        |
| d                | : 深度圖                        |
| local_min_d      | : 深度圖取local_min             |
| GF_d             | : 取 guide filter(引導圖=原圖, 輸入圖=local_min_d, r=15, eps=1e-3) |
| t                | : GF_d 還原的 transmission, β = 1 |
| clip_t           | : 截斷(t, 0.1, 0.9)             |
| my_CAP beta=1.0  | : 最終去霧結果圖                |
