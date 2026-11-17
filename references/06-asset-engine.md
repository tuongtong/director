# 06 — TẠO ASSET: ẢNH / VIDEO AI · REFERENCE · NHẠC
© 2026 Đạo diễn Tường Tống — Space Gray Production

Triết lý: text trước, asset sau. **Không tạo ảnh/video khi chưa chốt Mood & Tone + Color Palette phim.**

## 0. Kiểm tra công cụ & chi phí
| Asset | Công cụ | Nếu không có |
|---|---|---|
| Ảnh AI | theo thứ tự ưu tiên ở mục 0b | ghi prompt vào `04_prompts/` + placeholder; báo "3T tự gen" |
| Video AI | **Higgsfield MCP** (generate_video) — mặc định TẮT | chỉ ghi prompt |
| Reference camera / màu / mood | WebSearch + WebFetch | để ô link trống |
| Nhạc | WebSearch (Artlist ưu tiên) — chỉ đưa link option | mô tả hướng nhạc |

- Trước khi gen: kiểm tra số dư credit (công cụ balance nếu có), báo **số ảnh/video + credit ước tính**, chờ 3T duyệt.
- Kết nối Higgsfield cho Claude Code (nếu chưa có): xem README của bộ skill.

## 0b. Thứ tự engine ảnh (dùng cái đầu tiên đang có trong phiên)
1. **Higgsfield MCP** - ổn định nhất, tải file trực tiếp, chọn được model (Nano Banana Pro / GPT Image 2 / Seedream).
2. **ChatGPT Image qua trình duyệt** (Claude in Chrome) - dùng khi không có Higgsfield. Lưu ý đã gặp ở job Amai: Chrome **chặn tải nhiều file liên tiếp**. Cách làm:
   - Tải **ngay sau mỗi ảnh**, không gen hết rồi mới tải.
   - Tải hỏng → ghi link cuộc chat + Asset ID vào `00_README.txt` mục "CHỜ TẢI TAY", đi tiếp.
   - Báo 3T bật "cho phép tải nhiều file" cho chatgpt.com trong cài đặt Chrome nếu bị chặn.
3. **Không có engine** → chỉ ghi prompt, placeholder theo Asset ID.

## 1. Ảnh AI
Scope mặc định (đã duyệt ở điểm dừng treatment chữ): 1 keyvisual + 1 cặp khung A → B cho chuyển cảnh chữ ký (cùng bố cục, cùng vị trí chủ thể — xem `09` mục 5) + 4–6 khung storyboard then chốt (mở phim, cao trào, brand reveal, cảnh khách dễ hiểu lầm). Cảnh còn lại chỉ ghi prompt.

Thứ tự khi có nhân vật/bối cảnh lặp lại:
1. Character sheet / wardrobe sheet / environment sheet (khóa nhất quán).
2. Keyvisual.
3. Khung storyboard dùng các sheet làm `@image`.

Mỗi ảnh: tải về `05_assets/` với tên **`<AssetID>.png`** (vd `KV_keyvisual.png`, `SB_03.png`, `TR_T1_A.png` - xem `07` mục 3), ghi vào `99_asset-log.csv`. Lỗi 1 ảnh → ghi log, đi tiếp, không dừng cả lô. Lệch nhân vật → gen lại shot đó.

## 2. Video AI (chỉ khi 3T bật)
Từ khung storyboard đã duyệt → Seedance 2.5 / Kling 3.0, test 480p. Dùng cho stillomatic/animatic hoặc demo cú máy khó hình dung. Ghi trên slide: *"Bản dựng chỉ mang tính hình dung không khí và tiết tấu, chưa phải hình quay thực tế."*

## 3. Reference
Nhãn: CAM REF (góc máy) · CAM MOTION REF (chuyển động) · TRANSITION REF · COLOR REF · MOOD REF · FPV/DRONE REF.
- Tìm theo từ khóa điện ảnh + mood dự án.
- Lưu thumbnail vào `05_assets/refs/` tên `REF_<loại>_<##>` + **ghi nguồn** (URL + tên) trong `refs/nguon.txt` + 1 dòng "lấy gì từ ref này".
- Clip → thumbnail + link (không nhúng video).
- Stock footage dự kiến dùng → ghi link (Shutterstock…) ngay trên slide storyline, nhãn "Stock Footages".

## 4. Music & Sound (theo cách 3T)
- 3 tính từ thể loại (vd "Classical – Cinematic – Luxury").
- 4–6 option có link (ưu tiên Artlist), 1 option **RECOMMEND** + lý do.
- Ghi rõ: *"Agent chưa nghe được nhạc — 3T nghe & chốt."*
- Cấu trúc nhạc khớp nhịp phim: mở (ambient/SFX) → vào nhạc → điểm lặng → cao trào → kết nhỏ.
- **Sound treatment:** ambient/ASMR mở phim · SFX chữ ký (vd tiếng chạm gỗ, tiếng chén đặt xuống) · SFX cho chuyển cảnh ★ · điểm lặng ở đâu.

## 5. Bảng truy vết `99_asset-log.csv`
`asset_id, file, dùng ở slide, loại (ai-image|ai-video|ref|stock|music), nguồn/model, prompt hoặc truy vấn, trạng thái (đã chèn|chờ QC|chưa gen|chờ tải tay), ghi chú`
