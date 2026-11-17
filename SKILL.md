---
name: director
description: >-
  Skill đạo diễn chính của Đạo diễn Tường Tống (Space Gray Production). Ưu tiên dùng skill này thay cho director-treatment (ColorMedia). Làm 3 loại sản phẩm: SCRIPT (kịch bản bảng + cut-down), PROPOSAL (deck đi pitch), PPM DECK (họp tiền kỳ). Có spine & khoảnh khắc nhớ mãi, chuyển cảnh chữ ký + Transition Map, phần DP (ánh sáng · màu sắc · cú máy), music & sound, wardrobe, props, shot list, prompt + ảnh/video AI, xuất Canva hoặc folder; nhớ tiến độ từng job để làm tiếp và sửa theo feedback. Dùng khi người dùng nói "viết kịch bản", "làm cut-down", "làm proposal", "làm treatment", "làm PPM", "dựng deck đạo diễn", "storyboard", "shot list", "tiếp tục dự án …", "sửa theo feedback khách", hoặc được skill brief chuyển giao.
license: "© 2026 Đạo diễn Tường Tống - Space Gray Production. All rights reserved."
metadata:
  author: "Đạo diễn Tường Tống (3T)"
  studio: "Space Gray Production"
  version: "1.5.0"
---

# DIRECTOR - Hồ sơ đạo diễn Space Gray

> Bản quyền © 2026 **Đạo diễn Tường Tống** - Space Gray Production. Skill nội bộ, không phân phối lại khi chưa được cho phép.

> **Câu chốt:** Khách không mua kịch bản. Khách mua niềm tin rằng phim sẽ ra đúng như họ hình dung. Hồ sơ bán niềm tin đó bằng cái khách **thấy, nghe và cảm**.

## Đọc file nào, khi nào (chỉ đọc file cần cho bước đang làm)

| File (`references/`) | Đọc khi |
|---|---|
| `01-dna-3t.md` | **Luôn đọc** - gu đạo diễn, spine, kênh & định dạng, thói quen viết |
| `09-transition-treatment.md` | **Luôn đọc** khi viết kịch bản/storyline |
| `11-cach-viet-dung-chu.md` | **Luôn đọc** trước khi viết bất kỳ chữ nào khách / ekip sẽ đọc (kịch bản, treatment, Transition Map, shot list, câu hỏi phỏng vấn, slide) |
| `04-script-shotlist-format.md` | Viết kịch bản, cut-down, shot list |
| `02-proposal-ppm-structure.md` | Dựng Proposal / PPM |
| `03-dp-anh-sang-mau-cu-may.md` | Viết phần DP, storyline, shot list |
| `05-prompt-standards.md` | Viết prompt ảnh/video AI |
| `06-asset-engine.md` | Tạo ảnh/video, reference, music options |
| `07-output-canva-folder.md` | Folder job, Asset ID, ráp Canva / folder |
| `08-qc-checklist.md` | Trước khi giao |
| `10-concept-statement.md` | Viết / viết lại concept statement, tagline, tuyên ngôn gửi khách (nhất là doanh nghiệp nhiều mảng, hồ sơ đấu thầu) |

**Skill đi kèm `director-storytelling`** (`~/.claude/skills/director-storytelling/`): lo phần "phim kể bằng cách nào" (câu căng, khung kể, motif, cài trước - trả lời, lộ sản phẩm, đường cong nhịp, giọng kể, kết) và giải phẫu video ref. Có `00_brief/00_story-blueprint.md` trong job → đọc trước bước 2 và dùng làm gốc, không hỏi lại.

Script (`~/.claude/skills/director/scripts/`):
- `make_project.py` - tìm / tạo folder job, tự tăng version, `--copy-prev` khi sửa.
- `write_table.py` - ghi kịch bản / shot list từ JSON ra .xlsx (có tổng thời lượng, cột Source chọn sẵn).

## 3 chế độ - nhận ra từ câu lệnh

| Chế độ | Nhận ra khi | Làm gì đầu tiên |
|---|---|---|
| **MỚI** | job mới, có kịch bản / concept / brief đã phân tích | `make_project.py --type …` |
| **TIẾP TỤC** | "tiếp tục dự án X", "làm tiếp", nhắc tên job cũ | `make_project.py --find` → đọc `00_project.md` → báo 3 dòng: đã chốt gì · đang ở bước nào · bước tiếp theo |
| **SỬA** | "khách góp ý…", "sửa slide/cảnh…", dán feedback | đọc `00_project.md` → ghi feedback nguyên văn vào thẻ → `--copy-prev` tạo version mới → **chỉ sửa phần feedback chạm tới** → ghi "THAY ĐỔI SO VỚI BẢN TRƯỚC" trong README. Sửa nội bộ trước khi gửi khách thì sửa tại chỗ, không tăng version. |

## Khởi tạo - hỏi tối đa 3 câu, còn lại dùng mặc định

Hỏi (bỏ câu đã có câu trả lời, kể cả từ brief / `00_project.md`):
1. **Sản phẩm:** Script · Proposal · PPM?
2. **Đầu vào:** kịch bản đã chốt hay concept đã chọn? Chưa có gì → chuyển sang skill `brief` (dừng chọn concept). **Không tự sáng tác concept khi 3T chưa chọn.**
3. **Đầu ra** (Proposal/PPM): (A) Canva · (B) folder.

Rồi in **1 dòng mặc định** để 3T sửa nếu muốn:
> Mặc định: kênh <suy từ brief> · cut-down <nếu brief có> · ảnh AI = 1 keyvisual + 1 cặp khung chuyển cảnh chữ ký + 4-6 khung then chốt · video AI tắt · font Montserrat · màu deck theo brand khách.

## Quy trình (text trước → duyệt → asset → ráp)

1. **Job:** `make_project.py` (MỚI) hoặc `--find` (TIẾP TỤC/SỬA). Mọi quyết định đã chốt ghi vào `00_project.md`.
2. **Neo phim** (`01`): viết **Spine** (phim thực sự nói về điều gì, 1 câu) + **khoảnh khắc nhớ mãi** + chọn **2-3 chữ ký DNA** hợp brief, mỗi chữ ký 1 dòng lý do. Đọc **kênh & định dạng** để chỉnh nhịp mở phim. Có Story Blueprint → lấy spine, khung kể, cài trước - trả lời, đường cong nhịp từ đó. Chưa có mà phim cần một cách kể rõ (iTVC, brand film, BĐS hạng sang) → đề xuất chạy `director-storytelling` chế độ DỰNG trước.
3. **Kịch bản / storyline** (`04`): beat theo timecode, mỗi cảnh có Mục đích, Source, Hình (ánh sáng · màu · cú máy), Âm thanh, TEXT. Kịch bản khách → giữ nguyên chữ, chỉ thêm phần hình. Cut-down: viết riêng, không cắt máy móc (`04` mục cut-down).
4. **Transition Map** (`09`): 1 chuyển cảnh chữ ký ★ lặp 2-3 lần + map mọi ranh giới PHẦN/beat.
5. **Lớp ý đồ** (Proposal/PPM): Director's Vision · Mood & Tone · Color Palette phim · DP · Acting · Music & Sound · Wardrobe · Props/Art direction · VFX/3D.
6. **⏸ DỪNG - DUYỆT TREATMENT CHỮ.** Trình 1 trang: Spine · khoảnh khắc nhớ mãi · chữ ký DNA đã chọn · mood & palette · danh sách beat (1 dòng/beat) · chuyển cảnh chữ ký ★ + Transition Map rút gọn · scope asset + credit ước tính. **Chưa tạo ảnh/video, chưa dựng slide khi 3T chưa duyệt.**
   - Sản phẩm = **Script**: giao kịch bản (+ cut-down) ở bước này, ghi xlsx bằng `write_table.py`, rồi dừng.
7. **Shot list** + **prompt** (`04`, `05`) → `04_prompts/`, đặt theo **Asset ID**.
8. **Asset** (`06`) trong scope đã duyệt → tên file = Asset ID (`07`), ghi `99_asset-log.csv`.
9. **Ráp** (`07`): `01_slide-content.md` → A Canva / B dừng ở folder.
10. **QC** (`08`) → báo cáo cuối: link/đường dẫn · asset đã/chưa tạo · giả định chờ xác nhận · câu hỏi còn mở. Cập nhật tiến độ trong `00_project.md`.

## Luật cứng
- **Cách viết (đọc `11`):** không phải nhà văn - viết để khách hình dung được sẽ quay gì, thể hiện ra sao, cấu trúc thế nào. Từ phổ thông kiểu miền Nam (không "ráng chiều", "mặt nước đồng", "gió rạp"); mô tả hình nói thẳng thấy gì, không ví von; không số giây và thuật ngữ quay/dựng trong ô hình; không khóa vào thời tiết, hướng gió; Mục đích, tên phần, "Để làm gì" của chuyển cảnh nói thẳng nội dung.
- **Không bịa** insight, số liệu, credentials, giải thưởng, thông tin dự án. Câu do agent tự viết (Vision, VO đề xuất) **không chứa con số hay ước lượng** ("hàng triệu lần", "20 năm") nếu khách chưa cung cấp. Đã ghi "đã bỏ" thì chữ trên slide phải thật sự đã bỏ.
- **Concept statement (đọc `10`):** hiểu trước khi viết - lập bảng [mảng | giá trị cốt lõi] cho 3T xác nhận; giọng khẳng định của thương hiệu (không câu hỏi); hình ảnh thuộc thế giới của khách; không khoe nghĩa vụ tối thiểu ("giao đủ", "đúng hẹn", "kiểm kỹ"); không tự thêm claim; số liệu để trang chứng minh, không đặt ở concept.
- **DP chỉ gồm ánh sáng · màu sắc · cú máy.** Không ghi lens, tiêu cự, thông số máy. Ngoại lệ: dòng "180-degree shutter angle" trong prompt Seedance.
- **Chuyển cảnh là chữ ký của 3T:** mọi sản phẩm có Transition Map + 1 chuyển cảnh chữ ký ★ (Proposal/PPM trình bằng cặp khung A → B).
- **DNA là gu, không phải công thức:** không ép đủ mọi chữ ký vào mọi phim.
- **Asset AI** dán nhãn *"AI-generated - chờ QC"*; reference ghi **nguồn + nhãn REFERENCE**; stock ghi link.
- **Deck:** màu theo brand khách; font mặc định **Montserrat**; dấu gạch dùng **"-"** thường (không dùng — hoặc –); Space Gray chỉ ở footer + Thank you; cover ghi "Director: Tường Tống".
- **Prompt AI:** tiếng Anh 1 khối + bản dịch tiếng Việt; negative gộp chung; `@image1, @image2…`; không "--"; Seedance luôn có "180-degree shutter angle" và audio chỉ SFX. Sửa prompt → gửi lại **toàn bộ**.
- Trả lời tiếng Việt, ngắn gọn. Không recap từng bước khi xong.
