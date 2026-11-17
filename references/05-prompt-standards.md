# 05 — CHUẨN PROMPT AI CỦA 3T
© 2026 Đạo diễn Tường Tống — Space Gray Production

Nếu máy có skill `image-prompt-3t` hoặc `seedance-video-prompt`, ưu tiên đọc skill đó. File này là bản rút gọn để director tự chạy được.

## Quy tắc đầu ra (bắt buộc)
- Trong `04_prompts/`, mỗi prompt đứng dưới tiêu đề **Asset ID** (`### SB_03`, `### TR_T1_A`) + 1 dòng: model đề xuất · tỉ lệ · ảnh tham chiếu cần đính kèm.
- Prompt tiếng Anh trong **một khối** từ đầu đến cuối → ngay sau là **bản dịch tiếng Việt** (một khối).
- Negative/loại trừ **gộp vào cuối chính khối prompt** (dòng "Avoid: …" hoặc khóa khẳng định), không tách ô riêng.
- Ảnh tham chiếu gọi bằng `@image1, @image2…`; video nguồn `@video1`. Gán vai trò rõ cho từng ref.
- Không dùng tham số có dấu "--". Model, tỉ lệ, độ phân giải ghi **ngoài** khối prompt ("Thiết lập khuyến nghị").
- **Không ghi lens/tiêu cự bằng số.** Tả cảm giác quang học bằng chữ: wide establishing view, telephoto compression, shallow depth of field, soft background separation.
- Sửa prompt → gửi lại **toàn bộ** prompt + bản dịch.
- Casting: ghi rõ "Vietnamese" cho người trong khung (trừ khi brief khác).

## Chọn model ảnh
| Model | Dùng khi | Cú pháp |
|---|---|---|
| Nano Banana Pro | người photoreal, da/vải, backlight, macro texture, khóa nhận diện từ ảnh mặt, character/expression sheet | văn xuôi liền mạch |
| GPT Image 2 (high) | chữ/nhãn chính xác, product có typography, bảng màu hex, wardrobe sheet có label, edit ảnh | khối có nhãn: Subject / Layout / Setting / Lighting / Camera / Style / Avoid |
| Seedream 5 Pro | keyvisual/poster có chữ (kể cả tiếng Việt), layout nhiều vùng, ghép nhiều ref | thứ tự SPACE: Subject → Palette & style → Arrangement → Camera & light → Extra detail; chữ trong nháy kép |
| Seedream 4.5 | character sheet siêu thực theo ref trang phục | văn xuôi, nhấn chất liệu |

## Khung storyboard (ảnh tĩnh, 16:9)
```
[Storyboard frame - <Asset ID>] <chủ thể + hành động>, <bối cảnh>.
Framing: <cỡ cảnh, góc máy, vị trí chủ thể trong khung>.
Light: <hướng, chất sáng, thời điểm, hiệu ứng>.
Color: <palette phim bằng chữ + hex nếu cần>, <hướng grading>.
Mood: <tính từ Mood & Tone>.
Style: <cinematic photoreal | motion graphic/UI | 3D render | documentary> theo Source.
Composition: <chừa khoảng trống cho chữ nếu shot có TEXT>.
Avoid: watermark, on-image text, extra people, <thứ dễ bám từ ref>.
```
Nhất quán nhân vật/bối cảnh: dùng character sheet / wardrobe sheet / environment sheet làm `@image` thay vì chỉ lặp mô tả.

## Film look của 3T (khi cần "chất phim")
fine-grain film, warm amber halation quanh vùng sáng, lifted blacks, soft rolled-off highlights; teal-cool shadows tách với warm highlights; volumetric light / haze vừa phải.

## Video — Seedance 2.5 (mặc định cố định)
- Camera luôn có: `180-degree shutter angle, natural motion blur.`
- Audio luôn **chỉ SFX**: 3–5 tiếng động cụ thể, kết bằng `SFX only. No music, no score, no bgm, no dialogue, no voiceover.`
- Ràng buộc viết dạng khẳng định/đếm, đặt cuối (POSITIVE LOCKS).
- Không tên hãng máy/ống kính; không tỉ lệ/độ phân giải/fps/tên model trong prompt.
- Dạng khối cho việc khách hàng: SCENE CONTEXT → ACTIVE REFERENCES → LOCATION MAP → FIRST FRAME / BLOCKING → FORMAT MODE → CAMERA → ACTION (beat có mốc giây) → PERFORMANCE → PHYSICS → LIGHTING → COLOR GRADE → AUDIO → STYLE → OUTPUT SETTINGS → POSITIVE LOCKS.
- Số shot theo thời lượng: 5s = 1 · 10–15s = 2–4 · 20–30s = 4–8.
- Kling 3.0: không có ô negative → mọi ràng buộc viết khẳng định trong prompt.

## Kỷ luật sản xuất
- Chốt ảnh tĩnh sạch trước khi gen video.
- Test video 480p trước, đổi 1 biến mỗi lần.
- Sau mỗi prompt: 1–3 ghi chú rủi ro, mỗi ghi chú nói rõ đổi câu nào thành gì.
