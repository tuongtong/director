# 07 - FOLDER JOB, ASSET ID & ĐẦU RA (CANVA / FOLDER)
© 2026 Đạo diễn Tường Tống - Space Gray Production

## 1. Một job = một folder
```
~/Documents/SpaceGray_Treatments/
└── <YYMMDD>_<Khách>_<DựÁn>/              <- tạo 1 lần, dùng lại cho mọi bản
    ├── 00_project.md                     <- THẺ DỰ ÁN: thông tin, quyết định đã chốt, tiến độ, nhật ký version, feedback khách
    ├── 00_brief/                         <- brief gốc, 00_brief-breakdown.md, 00_cau-hoi-khach.txt, 00_concepts.md, 00_gop-y-kich-ban.md
    ├── 00_brand/                         <- logo (sáng/tối, nền trong), màu brand khách
    ├── Script_v01/                       <- kịch bản + cut-down
    ├── Proposal_v01/   Proposal_v02/
    └── PPM_v01/
```
Lệnh (`~/.claude/skills/director/scripts/make_project.py`):
- Tạo / mở job + tạo sản phẩm: `--client <Khách> --project <Dự án> --type Brief|Script|Proposal|PPM` (version tự tăng).
- Sửa theo feedback: thêm `--copy-prev` (chép bản trước sang version mới rồi sửa).
- Tìm job cũ: `--find`.
Tên tự bỏ dấu, viết liền (Sông Xanh → SongXanh). **Không tạo file `_v02` bên trong folder** - version là folder. File trung gian (JSON…) để trong `_work/`.

**Thẻ dự án `00_project.md`:** đọc đầu mỗi phiên; cập nhật ngay khi 3T chốt điều gì (spine, concept, palette, ★, font…), khi xong một bước (tiến độ), và khi có feedback khách (chép nguyên văn + ngày).

## 2. Folder sản phẩm
**Script_v##:** `00_README.txt` · `02_script.xlsx` (+ `.md`) · `02_script_<15s|30s>.xlsx` · `03_transition-map.md` · `_work/`

**Proposal_v## / PPM_v##:**
```
├── 00_README.txt          ← link Canva · GIẢ ĐỊNH - CHỜ XÁC NHẬN · THAY ĐỔI SO VỚI BẢN TRƯỚC
├── 01_slide-content.md    ← nội dung từng slide (theo tên slide, không theo số)
├── 02_script.xlsx         ← kịch bản (format 04)
├── 03_shotlist.xlsx       ← shot list
├── 03_transition-map.md   ← Transition Map + ★ (format 09)
├── 04_prompts/            ← image_prompts.md · video_prompts.md (theo Asset ID)
├── 05_assets/             ← file đặt tên theo Asset ID; refs/ character/ environment/
├── 06_palette/            ← film_palette.png · deck_palette.png · palette.txt
├── 07_music/huong-nhac.md ← Music & Sound
├── 99_asset-log.csv       ← asset_id · file · dùng ở slide · loại · nguồn/model · prompt · trạng thái · ghi chú
└── _work/
```

## 3. Asset ID (thay cho số slide - không bị lệch khi thêm/bớt slide)
| ID | Là gì |
|---|---|
| `KV_keyvisual` | keyvisual |
| `SB_<shot#>` | khung storyboard theo số shot trong kịch bản (vd `SB_03`, `SB_09b`) |
| `TR_T<#>_A` / `TR_T<#>_B` | khung A / B của chuyển cảnh T# (★ chữ ký: `TR_T1_A`…) |
| `CH_<tên>` · `ENV_<tên>` · `WD_<tên>` | character sheet · environment sheet · wardrobe |
| `REF_<cam|motion|color|mood|tr>_<##>` | reference đi mượn (ghi nguồn trong refs/nguon.txt) |
| `PAL_film` · `PAL_deck` | swatch màu |

File: `<AssetID>.png` (vd `SB_03.png`). Trong `01_slide-content.md` mỗi slide ghi `Asset: SB_03, SB_04`. Khi ráp mới quy đổi ra số trang.

## 4. Đầu ra
> **Đầu ra?** (A) Có - dựng tự động trên Canva · (B) Không - đóng gói vào folder để tự làm slide. Không trả lời → **(B)**.

### Nhánh A - Canva
1. Kiểm tra Canva MCP có trong phiên. Chưa có → báo 1 dòng + cách kết nối (README), hỏi: "Kết nối rồi chạy tiếp, hay chuyển sang (B)?" Không tự đổi nhánh.
2. Folder luôn dựng trước (bản gốc).
3. Báo số slide + số asset sẽ upload → chờ duyệt (gộp vào điểm dừng duyệt treatment chữ nếu được).
4. Công cụ Canva MCP thường có: `upload-asset-from-url`, `generate-design` / `generate-design-structured`, `create-design-from-brand-template` + `autofill-design` (khi có template Space Gray), `edit-design`, `export-design`. Dùng đúng tên công cụ đang có trong phiên. Ưu tiên **template Space Gray**; màu theo brand khách; font Montserrat; dấu "-".
5. Xuất link Canva (+ PDF nếu được) → ghi vào `00_README.txt`. Ghi rõ đây là bản nháp để QC & sửa trong editor Canva.
6. Lỗi giữa chừng → dừng, báo phần nào đã lên Canva, phần nào còn trong folder (theo Asset ID).

### Nhánh B - Folder
Dừng khi folder đủ file. Báo đường dẫn + số slide + asset đã tạo / chưa tạo.
