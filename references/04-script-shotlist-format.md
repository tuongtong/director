# 04 - FORMAT KỊCH BẢN, CUT-DOWN & SHOT LIST
© 2026 Đạo diễn Tường Tống - Space Gray Production

Ghi ra Excel bằng: `python3 ~/.claude/skills/director/scripts/write_table.py --kind <tvc|scene|corporate|shotlist> --json _work/<file>.json --out <file>.xlsx`
(JSON có "header" + "rows"; dòng Mục đích viết `{"_purpose": "Mục đích: …"}`. File JSON để trong `_work/`.) Song song luôn có bản `.md` dễ đọc trong chat.

## 1. Header kịch bản
```
KỊCH BẢN
<TÊN KHÁCH> - <TÊN PHIM>
Thời lượng: <x phút / x giây> (+ cut-down …)
Concept: <TÊN CONCEPT>
Spine: <1 câu>
Tone & Mood: <4 tính từ>
Ý nghĩa hình tượng: <2-4 câu>
Phương án sản xuất: <cảnh nào dùng AI / 3D / stock; "hình ảnh minh họa" cho công trình chưa xây>
```

## 2. Chọn bảng theo loại phim

**`tvc` - TVC / iTVC / phim ngắn ≤ 90s (mẫu Lumière)**
| STT | Giây | Hình | Âm thanh (VO / SFX / nhạc) | TEXT | Source |
- Ô **Hình** viết liền 1 đoạn: hành động → ánh sáng → màu → cú máy (+ lý do), rồi `=>` ghi chú đạo diễn.
- Chuyển cảnh chữ ký ghi ngay trong ô Hình: `★ Chuyển cảnh chữ ký lần 1: … Điểm khớp: …`.
- Dòng **Mục đích** (gộp ô, in nghiêng) đứng trước mỗi nhóm cảnh.

**`scene` - Corporate quy trình / brand / testimonial (mẫu Amai)**
| SCENE | SECTION | DESCRIPTION | DURATION | VO | TEXT | Source |

**`corporate` - Corporate dài / BĐS nhiều phần (mẫu TTC Land)**
| STT | Phần | Thời lượng (giây) | VO | TEXT | Key visual | Source | Mô tả | Ref / Ảnh |

Quy ước ô DESCRIPTION / Mô tả:
```
Mục đích:
<cảnh này để làm gì - 1-2 câu>

- <shot 1>
- <shot 2>
=> <ghi chú đạo diễn: nhịp, cảm giác, diễn xuất>
```

TEXT song ngữ: `<tiêu đề EN chữ thường>` + xuống dòng `sub: <tiếng Việt>`.
Testimonial: ô VO ghi câu hỏi + `sub:` EN + "(lấy phần trả lời làm VO)"; ô mô tả liệt kê B-roll chạy trên lời.
Shot con: `2a/b/c` cho chuỗi jump cut / sliding cut.

## 3. Giá trị cột Source (dùng đúng chữ)
`Shooting` · `Stock` · `AI generation` · `Graphic` · `3D` · `Tư liệu` · `Shooting kết hợp AI generation`

## 4. Kiểm tra thời lượng & VO
- VO tiếng Việt khoảng 3-4 âm tiết/giây (ước tính). Phần VO dài hơn số giây → cờ.
- Tổng các dòng = thời lượng phim (write_table tự cộng dòng TỔNG).
- TVC ≤ 30s: VO tối đa khoảng 2/3 thời lượng, chừa chỗ cho hình và điểm lặng.

## 5. Cut-down
Mỗi bản cut-down là **một phim riêng**, viết bảng riêng (`02_script_15s.xlsx`, `02_script_30s.xlsx` trong cùng folder version).
1. Giữ: **spine**, **chuyển cảnh chữ ký ★** (ít nhất 1 lần), **brand reveal + slogan**, CTA nếu brief bắt buộc.
2. Bỏ trước: cảnh giải thích, cảnh lặp ý, testimonial dài.
3. Mở phim theo kênh (`01` Kênh & định dạng): 15s/6s social → hook ngay giây đầu.
4. Gợi ý độ dài: 60s → 30s: giữ 3 beat chính. 15s: mở + 1 beat + ★ + logo. 6s bumper: 1 hình mạnh nhất + logo/slogan.
5. Ghi ở đầu bảng: "Lấy từ bản dài: cảnh #… · cảnh mới: #…".

## 6. Shot list (`03_shotlist.xlsx`, `--kind shotlist`)
| Cột | Ghi gì |
|---|---|
| Shot # | 1, 2a, 2b… |
| Phần | tên PHẦN / beat |
| Timecode | 00:00 - 00:04 |
| Thời lượng | giây |
| Source | theo mục 3 |
| Cỡ cảnh & góc máy | xem `03` |
| Cú máy | chuyển động + lý do; slow-mo/timelapse nếu có |
| Ánh sáng | hướng · chất · thời điểm · hiệu ứng |
| Màu sắc | tông cảnh, khớp palette phim |
| Bối cảnh · Nhân vật / talent · Props | |
| Nội dung | hành động trong shot |
| VO · TEXT on screen · SFX | |
| Chuyển cảnh | `T#: <kiểu> → shot <x> · khớp <điểm khớp>`; ★ nếu là chuyển cảnh chữ ký |
| Ref | file/link |
| Asset ID | vd `SB_03`, `TR_T1_A` (xem `07`) |
| Prompt ảnh · Prompt video | tham chiếu tới mục cùng Asset ID trong `04_prompts/` |

Không có cột lens / tiêu cự / fps.
