# director

Skill Claude Code đạo diễn chính của Đạo diễn Tường Tống (3T) - Space Gray Production. Làm kịch bản, proposal, PPM deck, treatment, shot list, prompt ảnh/video AI, và nhớ tiến độ từng job để làm tiếp hoặc sửa theo feedback.

> © 2026 Đạo diễn Tường Tống - Space Gray Production. All rights reserved. Skill nội bộ, không phân phối lại khi chưa được cho phép.

## Làm được gì
- **SCRIPT** - kịch bản dạng bảng (+ cut-down), xuất .xlsx.
- **PROPOSAL** - deck đi pitch (xuất Canva hoặc folder).
- **PPM DECK** - họp tiền kỳ.
- Spine, cảnh đáng nhớ nhất, chuyển cảnh đặc trưng + Transition Map, phần DP (ánh sáng, màu sắc, cú máy), music và sound, wardrobe, props, shot list, prompt ảnh/video AI.
- 3 chế độ: **MỚI**, **TIẾP TỤC** (làm tiếp job cũ), **SỬA** (theo feedback khách).

## Cấu trúc
```
SKILL.md                          điểm vào: quy trình, luật cứng
references/
  01-dna-3t.md                    gu đạo diễn, spine, kênh và định dạng
  02-proposal-ppm-structure.md    cấu trúc Proposal / PPM
  03-dp-anh-sang-mau-cu-may.md    phần DP
  04-script-shotlist-format.md    format kịch bản, cut-down, shot list
  05-prompt-standards.md          chuẩn prompt ảnh/video AI
  06-asset-engine.md              tạo ảnh/video, reference, music
  07-output-canva-folder.md       folder job, Asset ID, ráp Canva
  08-qc-checklist.md              kiểm tra trước khi giao
  09-transition-treatment.md      chuyển cảnh và Transition Map
  10-concept-statement.md         concept statement, tagline
  11-cach-viet-dung-chu.md        cách viết, cách dùng chữ (từ phổ thông, nói thẳng)
scripts/
  make_project.py                 tìm / tạo folder job, tự tăng version
  write_table.py                  ghi kịch bản / shot list ra .xlsx
```

## Cài trên máy mới
Yêu cầu: máy có Claude Code, Python 3. Để ghi file .xlsx cần thêm `openpyxl` (không có thì script tự ghi .csv).

**1. Đăng nhập GitHub** (repo private, chỉ tài khoản tuongtong mở được). Nếu máy chưa có `gh`:
```bash
brew install gh
```
```bash
gh auth login
```
Chọn GitHub.com, giao thức HTTPS, đăng nhập bằng trình duyệt.

**2. Tải skill về thư mục skill của Claude Code:**
```bash
git clone https://github.com/tuongtong/director.git ~/.claude/skills/director
```

**3. (Tùy chọn) Cài thư viện ghi .xlsx:**
```bash
python3 -m venv ~/.claude/skills/director/.venv && ~/.claude/skills/director/.venv/bin/pip install openpyxl
```
Nếu không cài, `write_table.py` vẫn chạy nhưng xuất .csv thay vì .xlsx.

**4. Mở lại Claude Code**, gõ `/director` để kiểm tra skill đã nhận.

Nên cài kèm các skill đi cùng: `brief` (phân tích brief khách, chuyển giao sang director), `director-storytelling` (dựng câu chuyện trước khi viết kịch bản), `image-prompt-3t` và `seedance-video-prompt` (viết prompt ảnh/video AI).

## Cập nhật bản mới
Trên máy đã cài:
```bash
git -C ~/.claude/skills/director pull
```

## Dùng
Gõ `/director`, hoặc nói: "viết kịch bản", "làm cut-down", "làm proposal", "làm PPM", "tiếp tục dự án ...", "sửa theo feedback khách".

Dữ liệu từng job lưu trong folder `261116_TenKhach_TenPhim/` (tạo bằng `make_project.py`), gồm thẻ dự án `00_project.md` ghi các quyết định đã chốt để làm tiếp lần sau.

## Ghi chú cho người sửa skill
- Mọi chữ giao khách hoặc ekip đọc phải theo `references/11-cach-viet-dung-chu.md`.
- Sửa xong, tăng `version` trong `SKILL.md`, commit và push.
