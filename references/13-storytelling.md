# Module kể chuyện - brand film / TVC / iTVC (gộp từ director-storytelling)

> Đây là "não kể chuyện" của director, đứng trước bước 2 (Neo phim). Đọc khi: phim cần một cách kể rõ (iTVC, brand film, BĐS hạng sang), khi 3T nói "dựng câu chuyện", "khung kể", "story blueprint", hoặc khi **soát** một kịch bản / bản dựng ("soát câu chuyện", "phim này có xương chưa"). Không cần video ref để chạy.
> Là cách nghĩ, không phải quy trình phân tích ref (việc đó của skill `ref-dissect`). Mọi luật cứng của `SKILL.md` (cách viết `11`, DP chỉ ánh sáng · màu · cú máy, không bịa, prompt AI, dấu gạch "-") vẫn áp dụng. Bản gốc `references/` của module nằm ở `references/storytelling/`.
> Có `00_brief/00_story-blueprint.md` trong job thì bước 2 và bước 3-4 của director lấy từ đó, không hỏi lại.

## Chuỗi tư duy 7 bước (cốt lõi)
1. **Câu căng:** người xem đang tin ___ → phim cho thấy ___. Không viết được thì chưa đi tiếp.
2. **Khung kể:** chọn một cấu trúc gọi tên được. Phép thử: nói được "Phim là ___ mà ___".
3. **Vật thể hóa:** biến ý trừu tượng thành 3-5 vật / hành động / ánh sáng quay được, thuộc thế giới của khách. Chọn một motif chạy xuyên phim.
4. **Cài trước - trả lời:** cú reveal quan trọng nhất phải được cài bằng một câu hoặc một hình từ sớm.
5. **Lộ sản phẩm:** theo ngành (giấu / sớm qua bối cảnh / sớm và lặp có lý do), lộ theo 3 lớp.
6. **Đường cong nhịp:** một khoảng lặng trước cú lớn nhất; shot giữ lâu nhất là shot quan trọng nhất; hình thức (màu, máy, chất ảnh) phục vụ thông điệp.
7. **Kết 3 nhịp:** cảm xúc → sản phẩm trong khung có người → logo (+ cú chốt).

## Đọc file nào, khi nào

| File (`references/storytelling/`) | Đọc khi |
|---|---|
| `01-khung-ke.md` | **Luôn đọc** khi DỰNG - câu căng, 9 khung kể, chọn khung theo ngành, thẻ khung kể |
| `06-nguyen-tac.md` | **Luôn đọc** - 8 quy luật nền + 24 nguyên tắc KHI → LÀM → ĐỂ |
| `02-hinh-hoa-va-motif.md` | Bước 3-4 - vật thể hóa, motif, cài trước - trả lời, màu brand, hình thức = thông điệp |
| `03-nhip-giong-ke-am-thanh.md` | Bước 6 - đường cong nhịp, chương, 5 giọng kể, âm thanh |
| `04-lo-san-pham-va-ket.md` | Bước 5, 7 - lộ sản phẩm, chuyển thế giới, kết + cú chốt, CTA |
| `07-phep-thu-cau-chuyen.md` | SOÁT, và tự soát Story Blueprint trước khi giao |


## Chế độ - nhận ra từ câu lệnh

| Chế độ | Nhận ra khi | Làm gì đầu tiên |
|---|---|---|
| **DỰNG** | có brief / concept, muốn "dựng câu chuyện", "cách kể", "khung kể"; hoặc `director` chuyển sang | mở/tạo job (`make_project.py --find` hoặc `--type Brief`), đọc `00_project.md` + brief |
| **SOÁT** | gửi kịch bản / bản dựng, hỏi "có xương chưa", "soát câu chuyện" | đọc toàn bộ bản gửi, giữ nguyên chữ |

---

## CHẾ ĐỘ 1 - DỰNG CÂU CHUYỆN

1. **Đầu vào.** Có brief đã phân tích hoặc concept đã chọn? Chưa có brief → chạy skill `brief` Hướng 1 trước.
2. **Câu căng** (`01` mục A). Suy luận thì ghi nhãn.
3. **Khung kể** (`01` mục B-C):
   - **Chưa có concept đã chọn** → trình **2-3 thẻ khung kể** (`01` mục D), mỗi thẻ một khung khác nhau, 1 thẻ ĐỀ XUẤT. **⏸ DỪNG cho 3T chọn.** Không tự chọn thay, không viết tiếp.
   - **Đã có concept** (từ `brief` / `00_project.md`) → gọi tên khung của concept đó; concept chưa có khung rõ thì đề xuất 1 khung + lý do và hỏi 1 câu xác nhận.
4. **Viết Story Blueprint** (mẫu bên dưới) theo chuỗi 7 bước, dùng `02`, `03`, `04`, `06`. Mỗi lựa chọn có 1 dòng lý do.
5. **Tự soát** bằng `07` mục A + phép thử spine `director/08`. Sửa trước khi giao.
6. **Giao + ghi job:** lưu `00_brief/00_story-blueprint.md`; ghi vào `00_project.md`: câu căng · spine · khung kể · cài trước - trả lời · ★ · cảnh đáng nhớ nhất. **⏸ DỪNG cho 3T duyệt.**
7. **Tiếp tục:** 3T duyệt → đi tiếp quy trình director ngay trong cùng job. Dùng Blueprint cho bước 2 (Neo phim) và bước 3-4 (kịch bản, Transition Map), không hỏi lại.

### Mẫu STORY BLUEPRINT (1 trang)
```
STORY BLUEPRINT - <Khách> - <Phim> - <thời lượng> - <kênh>

1. Câu căng:     Người xem tin ___ → phim cho thấy ___
2. Spine:        <1 câu - theo director/01>
3. Khung kể:     <tên khung> - "Phim là ___ mà ___"
4. Vật thể hóa:  từ khóa <___> → <3-5 vật / hành động / ánh sáng>
   Motif:        <vật lặp> · lặp ở <beat> · cách lặp <đổi chủ / lặp bố cục / tăng cấp / nghi thức> · khép lại ở <beat>
5. Cài trước - trả lời:  cài ở <TC> bằng <câu/hình> → trả ở <TC> bằng <câu/hình>
6. Lộ sản phẩm:  lớp 1 <không gian/trải nghiệm, TC, %> · lớp 2 <tên, TC> · lớp 3 <logo + slogan, TC>
7. Đường cong nhịp:
   | TC | Beat | Chức năng | Cảm xúc người xem | Năng lượng 1-5 | Nhịp cắt |
   Khoảng lặng: <TC, bằng gì> · Shot giữ lâu nhất: <TC, cảnh gì>
8. Giọng kể:     <câu hỏi lặp / nhân vật nói / danh sách từ / không lời + bài hát / VO song hành> + 2-3 câu VO mồi [mồi - chờ duyệt]
9. Luật hình (3-5 luật, mỗi luật 1 lý do): màu · cú máy · ánh sáng · chất ảnh
10. Chuyển cảnh: ★ chữ ký <kiểu · điểm khớp · để làm gì> (director/09) · cú đổi thế giới <kiểu · TC>
11. Kết:         cảm xúc <___> → sản phẩm trong khung có người <___> → logo + slogan → cú chốt <có/không, là gì>
12. Cảnh đáng nhớ nhất: <1 cảnh cụ thể>
13. Rủi ro & giả định: <cái gì chờ xác nhận>
```
Bản trình khách: đổi tên mục theo `07` mục C, viết theo `director/11`.

---

## CHẾ ĐỘ 2 - SOÁT CÂU CHUYỆN

1. Đọc hết bản gửi. Gọi tên khung kể đang có (hoặc ghi "chưa có khung").
2. Chạy 10 phép thử `07` mục A, sau 4 phép thử `director/08` mục A.
3. Góp ý theo mẫu `07` mục B: vị trí · phép thử · vấn đề · 1 gợi ý sửa. **Giữ nguyên chữ người viết**, góp ý để ở file riêng (`00_brief/00_gop-y-cau-chuyen.md`).
4. Kết bằng 3 dòng: điểm mạnh nhất cần giữ · lỗi gốc lớn nhất · bước sửa đầu tiên.

---

## Bổ sung nguyên tắc
Skill lớn lên bằng nguyên tắc, không bằng ref. Nguồn bổ sung: 3T tự học từ phim hay (công cụ riêng `ref-dissect`), hoặc bài học sau một job. Chỉ thêm khi 3T duyệt; viết thành nguyên tắc chung vào `06-nguyen-tac.md`, ví dụ để trong ngoặc; gộp nếu trùng.

## Luật cứng (module kể chuyện)
- **Khung trước, shot sau.** Không viết shot list / prompt khi chưa có khung kể được 3T chọn.
- **Không tự sáng tác concept khi 3T chưa chọn** (luật `director`): thẻ khung kể là phương án để chọn, không phải quyết định.
- **Không bịa:** insight, số liệu, thông tin dự án. Suy luận ghi "suy luận"; giả định ghi "giả định - chờ xác nhận".
- **Nguyên tắc là gu, không phải công thức:** chọn 3-5 nguyên tắc hợp spine cho mỗi phim, không ép đủ (giống luật DNA của `director/01`).
- **Không chép phim có thật:** không tái tạo shot, nhân vật, logo, slogan của quảng cáo khác. Ví dụ trong skill chỉ để hiểu nguyên tắc.
- **Chữ giao khách theo `director/11`.** Thuật ngữ trong skill này (khung kể, motif, cài trước - trả lời, cú chốt) chỉ dùng nội bộ; giao khách thì đổi theo `07` mục C.
- **DP giao khách chỉ ánh sáng · màu · cú máy** (luật `director`).
- **Prompt AI:** chuẩn `director/05`.
- Dấu gạch "-" thường. Trả lời tiếng Việt, ngắn gọn.
