#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DIRECTOR - ghi kịch bản / shot list ra .xlsx (hoặc .csv nếu thiếu openpyxl).
© 2026 Đạo diễn Tường Tống - Space Gray Production. All rights reserved.

Dùng:
  python3 write_table.py --kind tvc --json _work/script.json --out 02_script.xlsx
  python3 write_table.py --kind shotlist --json _work/shotlist.json --out 03_shotlist.xlsx
  python3 write_table.py --kind tvc --empty --out 02_script.xlsx   (chỉ tạo khung)

--kind:
  corporate  STT · Phần · Thời lượng (giây) · VO · TEXT · Key visual · Source · Mô tả · Ref / Ảnh
  scene      SCENE · SECTION · DESCRIPTION · DURATION · VO · TEXT · Source
  tvc        STT · Giây · Hình · Âm thanh (VO / SFX / nhạc) · TEXT · Source
  shotlist   (xem SHOTLIST_COLS)

JSON:
  {
    "header": {"Tên": "...", "Thời lượng": "60s", "Concept": "...", "Tone & Mood": "...",
               "Ý nghĩa hình tượng": "...", "Phương án sản xuất": "..."},
    "rows": [
      {"_purpose": "Mục đích: mở bằng giác quan ..."},      <- dòng Mục đích (gộp ô, in nghiêng)
      {"STT": 1, "Giây": 6, "Hình": "...", "Source": "Shooting"},
      ...
    ]
  }
  "rows" có thể là list object (key = tên cột) hoặc list list (theo thứ tự cột).
  Xuống dòng trong ô: dùng \n.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys

COLS = {
    "corporate": ["STT", "Phần", "Thời lượng (giây)", "VO", "TEXT", "Key visual",
                  "Source", "Mô tả", "Ref / Ảnh"],
    "scene": ["SCENE", "SECTION", "DESCRIPTION", "DURATION", "VO", "TEXT", "Source"],
    "tvc": ["STT", "Giây", "Hình", "Âm thanh (VO / SFX / nhạc)", "TEXT", "Source"],
    "shotlist": ["Shot #", "Phần", "Timecode", "Thời lượng", "Source",
                 "Cỡ cảnh & góc máy", "Cú máy", "Ánh sáng", "Màu sắc", "Bối cảnh",
                 "Nhân vật / talent", "Props", "Nội dung", "VO", "TEXT on screen", "SFX",
                 "Chuyển cảnh", "Ref", "Asset ID", "Prompt ảnh", "Prompt video"],
}
DURATION_COL = {"corporate": "Thời lượng (giây)", "scene": "DURATION", "tvc": "Giây",
                "shotlist": "Thời lượng"}
WIDE = {"VO", "Mô tả", "DESCRIPTION", "Hình", "Âm thanh (VO / SFX / nhạc)", "Nội dung",
        "Prompt ảnh", "Prompt video", "Cú máy", "Ánh sáng"}
SOURCE_VALUES = ["Shooting", "Stock", "AI generation", "Graphic", "3D", "Tư liệu",
                 "Shooting kết hợp AI generation"]


def copyright_line():
    return f"© {dt.date.today().year} Space Gray Production - Director Tường Tống. All rights reserved."


def _num(v):
    try:
        return float(str(v).replace("s", "").replace(",", ".").strip())
    except (ValueError, AttributeError):
        return None


def normalise(rows, cols):
    out = []
    for r in rows:
        if isinstance(r, dict) and "_purpose" in r:
            out.append(("purpose", r["_purpose"]))
        elif isinstance(r, dict):
            out.append(("row", [r.get(c, "") for c in cols]))
        else:
            out.append(("row", list(r) + [""] * (len(cols) - len(r))))
    return out


def write(kind, data, out_path):
    cols = COLS[kind]
    header = data.get("header", {}) if isinstance(data, dict) else {}
    rows = normalise(data.get("rows", []) if isinstance(data, dict) else data, cols)
    dcol = DURATION_COL.get(kind)
    total = None
    if dcol:
        idx = cols.index(dcol)
        nums = [_num(r[idx]) for t, r in rows if t == "row"]
        nums = [n for n in nums if n is not None]
        total = sum(nums) if nums else None

    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font, PatternFill
        from openpyxl.worksheet.datavalidation import DataValidation
    except ImportError:
        out_path = os.path.splitext(out_path)[0] + ".csv"
        with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            for k, v in header.items():
                w.writerow([k, v])
            if header:
                w.writerow([])
            w.writerow(cols)
            for t, r in rows:
                w.writerow([r] if t == "purpose" else r)
            if total is not None:
                w.writerow(["TỔNG", f"{total:g}s"])
            w.writerow([copyright_line()])
        return out_path

    wb = Workbook()
    ws = wb.active
    ws.title = {"shotlist": "Shot list"}.get(kind, "Kịch bản")
    r0 = 1
    for k, v in header.items():
        ws.cell(row=r0, column=1, value=k).font = Font(bold=True)
        ws.cell(row=r0, column=2, value=v)
        ws.merge_cells(start_row=r0, start_column=2, end_row=r0, end_column=len(cols))
        r0 += 1
    if header:
        r0 += 1
    head_row = r0
    fill = PatternFill("solid", fgColor="1F1F1F")
    for i, c in enumerate(cols, start=1):
        cell = ws.cell(row=head_row, column=i, value=c)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = fill
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[cell.column_letter].width = 48 if c in WIDE else 16
    r = head_row + 1
    for t, vals in rows:
        if t == "purpose":
            cell = ws.cell(row=r, column=1, value=vals)
            cell.font = Font(italic=True, color="555555")
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(cols))
        else:
            for i, v in enumerate(vals, start=1):
                c = ws.cell(row=r, column=i, value=v)
                c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    if total is not None:
        ws.cell(row=r, column=1, value="TỔNG").font = Font(bold=True)
        ws.cell(row=r, column=cols.index(dcol) + 1, value=f"{total:g}s").font = Font(bold=True)
        r += 1
    if "Source" in cols:
        letter = ws.cell(row=head_row, column=cols.index("Source") + 1).column_letter
        dv = DataValidation(type="list", formula1='"' + ",".join(SOURCE_VALUES) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{letter}{head_row + 1}:{letter}{max(r, head_row + 300)}")
    ws.freeze_panes = ws.cell(row=head_row + 1, column=1)
    ws.cell(row=r + 1, column=1, value=copyright_line()).font = Font(italic=True, color="888888", size=8)
    wb.save(out_path)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", required=True, choices=list(COLS))
    ap.add_argument("--json")
    ap.add_argument("--empty", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.empty:
        data = {"rows": []}
    elif a.json:
        with open(a.json, encoding="utf-8") as f:
            data = json.load(f)
    else:
        sys.exit("Cần --json hoặc --empty")
    p = write(a.kind, data, os.path.expanduser(a.out))
    print(p)


if __name__ == "__main__":
    main()
