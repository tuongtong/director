#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DIRECTOR - tạo / mở folder dự án chuẩn Space Gray.
© 2026 Đạo diễn Tường Tống - Space Gray Production. All rights reserved.

Cấu trúc: MỘT JOB = MỘT FOLDER, bên trong mỗi sản phẩm giao là một folder version.

  ~/Documents/SpaceGray_Treatments/
  └── 261020_Amai_15thAnniversary/          <- folder job (tạo 1 lần, dùng lại)
      ├── 00_project.md                     <- thẻ dự án: thông tin, quyết định đã chốt, tiến độ
      ├── 00_brief/                         <- brief gốc + breakdown + câu hỏi khách
      ├── 00_brand/                         <- logo, màu brand khách
      ├── Script_v01/                       <- kịch bản (+ cut-down)
      ├── Proposal_v01/  Proposal_v02/
      └── PPM_v01/

Dùng:
  python3 make_project.py --client Amai --project "15th Anniversary" --type Brief
  python3 make_project.py --client Amai --project "15th Anniversary" --type Proposal
  python3 make_project.py --client Amai --project "15th Anniversary" --type Proposal --copy-prev
  python3 make_project.py --client Amai --project "15th Anniversary" --find
  Tùy chọn: --date YYMMDD · --root <thư mục gốc>

--type tự tăng version (v01 → v02 …). --copy-prev chép nội dung bản trước sang bản mới
(dùng khi sửa theo feedback). In ra đường dẫn folder job và folder sản phẩm.
"""
import argparse
import csv
import datetime as dt
import os
import re
import shutil
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from write_table import write as write_table, copyright_line  # noqa: E402

DEFAULT_ROOT = os.path.expanduser("~/Documents/SpaceGray_Treatments")
TYPES = {"brief": "Brief", "script": "Script", "proposal": "Proposal", "ppm": "PPM"}
ASSET_LOG_COLS = ["asset_id", "file", "dùng ở slide", "loại", "nguồn/model",
                  "prompt hoặc truy vấn", "trạng thái", "ghi chú"]


def slug(s: str) -> str:
    s = s.replace("Đ", "D").replace("đ", "d")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    parts = re.split(r"[^A-Za-z0-9]+", s)
    return "".join(p[:1].upper() + p[1:] for p in parts if p) or "Untitled"


def find_job(root, client, project):
    pat = re.compile(rf"^\d{{6}}_{re.escape(client)}_{re.escape(project)}$")
    if not os.path.isdir(root):
        return None
    hits = sorted(d for d in os.listdir(root) if pat.match(d) and os.path.isdir(os.path.join(root, d)))
    return os.path.join(root, hits[-1]) if hits else None


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


PROJECT_CARD = """# THẺ DỰ ÁN - {client} · {project}
> File này là "bộ nhớ" của job. Skill đọc file này đầu mỗi phiên và cập nhật sau mỗi quyết định.

## Thông tin
- Khách: {client}
- Dự án / tên phim: {project}
- Loại phim:
- Thời lượng + cut-down:
- Kênh phát hành:
- Người xem:
- Deadline:

## Đã chốt (sáng tạo)
- Spine (phim này thực sự nói về điều gì, 1 câu):
- Khoảnh khắc nhớ mãi:
- Concept:
- Mood & tone:
- Color palette phim:
- Chuyển cảnh chữ ký ★:
- Chữ ký DNA dùng cho phim này (2-3, kèm lý do):

## Thiết lập
- Đầu ra: A Canva / B Folder
- Scope asset AI:
- Font / dấu gạch: Montserrat · dùng "-" thường

## Tiến độ
- [ ] Brief breakdown
- [ ] Concept đã chọn
- [ ] Kịch bản
- [ ] Treatment chữ đã duyệt
- [ ] Asset
- [ ] Ráp (Canva / folder)
- [ ] QC

## Nhật ký phiên bản
- {date}: tạo job

## Feedback khách (ghi nguyên văn + ngày)
"""


def ensure_job(root, client, project, date):
    job = find_job(root, client, project)
    created = False
    if not job:
        job = os.path.join(root, f"{date}_{client}_{project}")
        os.makedirs(job)
        created = True
    for sub in ("00_brief", "00_brand"):
        os.makedirs(os.path.join(job, sub), exist_ok=True)
    card = os.path.join(job, "00_project.md")
    if not os.path.exists(card):
        write(card, PROJECT_CARD.format(client=client, project=project,
                                        date=dt.date.today().strftime("%d/%m/%Y")))
    return job, created


def next_version(job, kind):
    pat = re.compile(rf"^{kind}_v(\d+)$")
    vs = [int(m.group(1)) for d in os.listdir(job) if (m := pat.match(d))]
    prev = max(vs) if vs else 0
    return prev, prev + 1


def skeleton(path, kind, client, project):
    os.makedirs(os.path.join(path, "_work"), exist_ok=True)
    readme = (f"{os.path.basename(path)} - {client} · {project}\n\n"
              "LINK CANVA: (nếu có)\n\n"
              "GIẢ ĐỊNH - CHỜ XÁC NHẬN:\n- \n\n"
              "THAY ĐỔI SO VỚI BẢN TRƯỚC:\n- \n\n"
              f"{copyright_line()}\n")
    write(os.path.join(path, "00_README.txt"), readme)
    write_table("tvc", {"rows": []}, os.path.join(path, "02_script.xlsx"))
    write(os.path.join(path, "03_transition-map.md"),
          "# Transition Map\n\nChuyển cảnh chữ ký ★: <kiểu> - lặp ở: <T#, T#, T#>\n\n"
          "| # | Từ cảnh → Đến cảnh | Kiểu | Điểm khớp | Ý nghĩa | Làm bằng | Ghi chú quay/dựng | Ref |\n"
          "|---|---|---|---|---|---|---|---|\n| T1 |  |  |  |  |  |  |  |\n")
    if kind == "Script":
        return
    for sub in ("04_prompts", "05_assets/refs", "05_assets/character",
                "05_assets/environment", "06_palette", "07_music"):
        os.makedirs(os.path.join(path, sub), exist_ok=True)
    write(os.path.join(path, "01_slide-content.md"),
          f"# {client} - {project} · {kind}\n\n"
          "<!-- Mỗi slide:\n## Slide: COVER\nLoại:\nTiêu đề:\nNội dung:\nAsset: KV_keyvisual\nGhi chú trình bày:\n-->\n")
    write_table("shotlist", {"rows": []}, os.path.join(path, "03_shotlist.xlsx"))
    write(os.path.join(path, "04_prompts/image_prompts.md"), "# Image prompts (EN + VN) - theo Asset ID\n")
    write(os.path.join(path, "04_prompts/video_prompts.md"), "# Video prompts (EN + VN) - theo Asset ID\n")
    write(os.path.join(path, "05_assets/refs/nguon.txt"), "# asset_id | nguồn (URL) | lấy gì từ ref này\n")
    write(os.path.join(path, "06_palette/palette.txt"),
          "# PALETTE PHIM: hex | tên cảm xúc | vai trò\n\n# PALETTE DECK (brand khách): hex | vai trò\n")
    write(os.path.join(path, "07_music/huong-nhac.md"),
          "# Music & Sound\nThể loại (3 tính từ):\n\nOptions (link) - đánh dấu RECOMMEND:\n1.\n\n"
          "Sound treatment (ambient / SFX chữ ký / điểm lặng):\n")
    with open(os.path.join(path, "99_asset-log.csv"), "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow(ASSET_LOG_COLS)


def log_version(card, line):
    """Chèn dòng nhật ký vào cuối mục 'Nhật ký phiên bản' (trước mục kế tiếp)."""
    with open(card, encoding="utf-8") as f:
        lines = f.read().split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("## Nhật ký phiên bản"))
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        while end > start + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, line)
    except StopIteration:
        lines.append(line)
    write(card, "\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description="Tạo / mở folder dự án Space Gray")
    ap.add_argument("--client", required=True)
    ap.add_argument("--project", required=True)
    ap.add_argument("--type", choices=list(TYPES) + list(TYPES.values()))
    ap.add_argument("--find", action="store_true", help="chỉ tìm folder job, không tạo")
    ap.add_argument("--copy-prev", action="store_true")
    ap.add_argument("--date", help="YYMMDD, mặc định hôm nay")
    ap.add_argument("--root", default=DEFAULT_ROOT)
    a = ap.parse_args()

    root = os.path.expanduser(a.root)
    client, project = slug(a.client), slug(a.project)

    if a.find:
        job = find_job(root, client, project)
        if not job:
            sys.exit(f"KHÔNG THẤY job {client}_{project} trong {root}")
        print(job)
        for d in sorted(os.listdir(job)):
            print("  -", d)
        return

    if not a.type:
        sys.exit("Cần --type Brief|Script|Proposal|PPM (hoặc --find)")
    kind = TYPES.get(a.type.lower(), a.type)
    os.makedirs(root, exist_ok=True)
    job, created = ensure_job(root, client, project, a.date or dt.date.today().strftime("%y%m%d"))
    print(("TẠO JOB: " if created else "JOB: ") + job)

    if kind == "Brief":
        print("BRIEF: " + os.path.join(job, "00_brief"))
        return

    prev, ver = next_version(job, kind)
    path = os.path.join(job, f"{kind}_v{ver:02d}")
    if a.copy_prev and prev:
        src = os.path.join(job, f"{kind}_v{prev:02d}")
        shutil.copytree(src, path)
        with open(os.path.join(path, "00_README.txt"), "a", encoding="utf-8") as f:
            f.write(f"\n--- Tạo từ {kind}_v{prev:02d} ngày {dt.date.today():%d/%m/%Y}. "
                    "Ghi thay đổi ở mục THAY ĐỔI SO VỚI BẢN TRƯỚC. ---\n")
    else:
        os.makedirs(path)
        skeleton(path, kind, a.client, a.project)
    log_version(os.path.join(job, "00_project.md"),
                f"- {dt.date.today():%d/%m/%Y}: tạo {kind}_v{ver:02d}"
                + (f" (chép từ v{prev:02d})" if a.copy_prev and prev else ""))
    print(f"{kind.upper()}: {path}")


if __name__ == "__main__":
    main()
