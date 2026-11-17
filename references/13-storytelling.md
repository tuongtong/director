# 13 - CÁCH KỂ CHUYỆN (phim thương hiệu, phim quảng cáo)
© 2026 Đạo diễn Tường Tống - Space Gray Production

> Phần này lo chuyện "phim kể bằng cách nào", làm trước bước 2 (Neo phim). Đọc khi:
> - phim cần một cách kể rõ: phim quảng cáo trên mạng, phim thương hiệu, BĐS cao cấp
> - 3T nói "dựng câu chuyện", "khung kể", "story blueprint"
> - 3T nhờ soát một kịch bản hoặc bản dựng: "soát câu chuyện", "phim này có xương chưa"
>
> Không cần video tham khảo để chạy. Đây là cách nghĩ, không phải cách mổ phim tham khảo (việc đó của skill `ref-dissect`).
> Mọi luật cứng trong `SKILL.md` vẫn áp dụng: cách viết theo `11`, DP chỉ ánh sáng · màu · cú máy, không bịa, prompt theo `05`, dấu gạch "-".
> 6 file chi tiết nằm ở `references/storytelling/`.
> Job đã có `00_brief/00_story-blueprint.md` thì bước 2 và bước 3-4 lấy từ đó, không hỏi lại.

## 7 bước nghĩ

1. **Câu căng:** người xem đang tin ___ → phim cho thấy ___. Chưa viết được câu này thì chưa đi tiếp.
2. **Khung kể:** chọn một kiểu cấu trúc gọi tên được. Thử bằng câu: "Phim là ___ mà ___".
3. **Biến ý thành vật:** đổi ý trừu tượng thành 3-5 món đồ, hành động hoặc kiểu ánh sáng quay được, có thật trong thế giới của khách. Chọn một hình lặp lại suốt phim.
4. **Gài trước, trả sau:** lúc lộ ra quan trọng nhất của phim phải được gài sẵn từ sớm bằng một câu hoặc một hình.
5. **Lúc lộ sản phẩm:** tùy ngành mà giấu tới cuối, cho thấy sớm qua bối cảnh, hoặc cho thấy sớm rồi lặp lại có lý do. Lộ theo 3 lớp.
6. **Nhịp phim:** có một đoạn lắng ngay trước lúc mạnh nhất. Cảnh giữ lâu nhất phải là cảnh quan trọng nhất. Màu, cách đặt máy, chất hình đều phục vụ điều phim muốn nói.
7. **Kết 3 nhịp:** cảm xúc → sản phẩm trong khung hình có người → logo (thêm một câu hoặc hình chốt nếu cần).

## Đọc file nào, khi nào

| File (`references/storytelling/`) | Đọc khi |
|---|---|
| `01-khung-ke.md` | **Luôn đọc** khi DỰNG: câu căng, 9 khung kể, chọn khung theo ngành, mẫu thẻ khung kể |
| `06-nguyen-tac.md` | **Luôn đọc**: 8 quy luật nền và 24 luật KHI → LÀM → ĐỂ |
| `02-hinh-hoa-va-motif.md` | Bước 3-4: biến ý thành vật, hình lặp lại, gài trước trả sau, màu thương hiệu, hình thức đi theo điều muốn nói |
| `03-nhip-giong-ke-am-thanh.md` | Bước 6: nhịp phim, chia phần, 5 giọng kể, âm thanh |
| `04-lo-san-pham-va-ket.md` | Bước 5 và 7: lúc lộ sản phẩm, đổi thế giới, kết phim, câu kêu gọi |
| `07-phep-thu-cau-chuyen.md` | Khi SOÁT, và tự soát Story Blueprint trước khi giao |

## Hai chế độ

| Chế độ | Nhận ra khi | Làm gì trước |
|---|---|---|
| **DỰNG** | Có brief hoặc concept, muốn "dựng câu chuyện", "cách kể", "khung kể", hoặc bước 2 của director cần | Mở hoặc tạo job (`make_project.py --find` hoặc `--type Brief`), đọc `00_project.md` và brief |
| **SOÁT** | Gửi kịch bản hoặc bản dựng, hỏi "có xương chưa", "soát câu chuyện" | Đọc hết bản gửi, giữ nguyên chữ |

---

## CHẾ ĐỘ 1 - DỰNG CÂU CHUYỆN

1. **Đầu vào.** Đã có brief phân tích xong hoặc concept đã chọn chưa? Chưa có brief thì chạy skill `brief` Hướng 1 trước.
2. **Câu căng** (`01` mục A). Chỗ nào tự suy ra thì ghi "suy luận".
3. **Khung kể** (`01` mục B-C):
   - **Chưa chọn concept** → đưa **2-3 thẻ khung kể** (`01` mục D), mỗi thẻ một khung khác nhau, đánh dấu 1 thẻ ĐỀ XUẤT. **⏸ DỪNG cho 3T chọn.** Không chọn thay, không viết tiếp.
   - **Đã có concept** (từ `brief` hoặc `00_project.md`) → gọi tên khung của concept đó. Concept chưa rõ khung thì đề xuất 1 khung, kèm lý do, hỏi 1 câu xác nhận.
4. **Viết Story Blueprint** theo mẫu bên dưới và 7 bước nghĩ, dùng `02`, `03`, `04`, `06`. Mỗi lựa chọn có 1 dòng lý do.
5. **Tự soát** bằng `07` mục A và phép thử spine ở `08`. Sửa xong mới giao.
6. **Giao và ghi vào job:** lưu `00_brief/00_story-blueprint.md`. Ghi vào `00_project.md`: câu căng · spine · khung kể · gài trước trả sau · chuyển cảnh chữ ký ★ · cảnh đáng nhớ nhất. **⏸ DỪNG cho 3T duyệt.**
7. **Đi tiếp:** 3T duyệt xong thì làm tiếp quy trình director trong cùng job. Bước 2 (Neo phim) và bước 3-4 (kịch bản, Transition Map) lấy từ Blueprint, không hỏi lại.

### Mẫu STORY BLUEPRINT (1 trang)
```
STORY BLUEPRINT - <Khách> - <Phim> - <thời lượng> - <kênh>

1. Câu căng:          Người xem tin ___ → phim cho thấy ___
2. Spine:             <1 câu, theo 01>
3. Khung kể:          <tên khung> - "Phim là ___ mà ___"
4. Biến ý thành vật:  từ khóa <___> → <3-5 món đồ / hành động / kiểu ánh sáng>
   Hình lặp lại:      <vật gì> · xuất hiện ở <đoạn nào> · lặp kiểu gì <đổi người cầm / lặp bố cục / lớn dần / thành thói quen> · khép lại ở <đoạn nào>
5. Gài trước, trả sau: gài ở <timecode> bằng <câu/hình> → trả ở <timecode> bằng <câu/hình>
6. Lộ sản phẩm:       lớp 1 <không gian / trải nghiệm, timecode, %> · lớp 2 <tên, timecode> · lớp 3 <logo + slogan, timecode>
7. Nhịp phim:
   | Timecode | Đoạn | Đoạn này để làm gì | Người xem cảm thấy gì | Độ mạnh 1-5 | Cắt nhanh / chậm |
   Đoạn lắng: <timecode, bằng gì> · Cảnh giữ lâu nhất: <timecode, cảnh gì>
8. Giọng kể:          <câu hỏi lặp lại / nhân vật tự nói / danh sách chữ / không lời, chỉ bài hát / VO kể song song> + họ VO · ngôi kể · điệp khúc · từ khóa riêng (theo `14`) + cặp câu mở - câu kết + 2-3 câu VO mẫu [mẫu - chờ duyệt]
9. Luật hình (3-5 luật, mỗi luật 1 lý do): màu · cú máy · ánh sáng · chất hình
10. Chuyển cảnh:      ★ chữ ký <nối bằng gì · khớp ở đâu · để làm gì> (theo 09) · lúc đổi thế giới <nối bằng gì, timecode>
11. Kết:              cảm xúc <___> → sản phẩm trong khung có người <___> → logo + slogan → câu hoặc hình chốt <có/không, là gì>
12. Cảnh đáng nhớ nhất: <1 cảnh cụ thể>
13. Rủi ro và giả định: <cái gì đang chờ xác nhận>
```
Bản trình khách: đổi tên mục theo `07` mục C, viết theo `11`.

---

## CHẾ ĐỘ 2 - SOÁT CÂU CHUYỆN

1. Đọc hết bản gửi. Gọi tên khung kể đang có, hoặc ghi "chưa có khung".
2. Chạy 10 phép thử ở `07` mục A, rồi 4 phép thử ở `08` mục A.
3. Góp ý theo mẫu `07` mục B: ở đâu · phép thử nào · vấn đề gì · 1 gợi ý sửa. **Giữ nguyên chữ người viết.** Góp ý để ở file riêng `00_brief/00_gop-y-cau-chuyen.md`.
4. Kết bằng 3 dòng: điểm mạnh nhất cần giữ · lỗi gốc lớn nhất · việc sửa đầu tiên.

---

## Thêm luật mới
Phần này lớn lên bằng luật, không bằng phim tham khảo. Luật mới đến từ 2 nguồn: 3T tự học từ phim hay (dùng skill `ref-dissect`), hoặc bài học sau một job. Chỉ thêm khi 3T duyệt. Viết thành luật chung vào `storytelling/06-nguyen-tac.md`, ví dụ để trong ngoặc. Trùng với luật cũ thì gộp lại.

## Luật cứng của phần kể chuyện
- **Có khung kể rồi mới tới cảnh quay.** Chưa có khung kể 3T chọn thì không viết shot list, không viết prompt.
- **Không tự sáng tác concept khi 3T chưa chọn.** Thẻ khung kể là phương án để chọn, không phải quyết định.
- **Không bịa** insight, số liệu, thông tin dự án. Tự suy ra thì ghi "suy luận". Giả định thì ghi "giả định - chờ xác nhận".
- **Luật là gu, không phải công thức.** Mỗi phim chọn 3-5 luật hợp với spine, không ép đủ (giống luật chữ ký DNA ở `01`).
- **Không chép phim có thật.** Không làm lại cảnh, nhân vật, logo, slogan của quảng cáo khác. Ví dụ trong file chỉ để hiểu luật.
- **Chữ giao khách theo `11`.** Các tên gọi nội bộ (khung kể, hình lặp lại, gài trước trả sau, câu chốt) không đưa thẳng cho khách. Giao khách thì đổi tên theo `07` mục C.
- **DP giao khách chỉ ghi ánh sáng · màu · cú máy.**
- **Prompt AI** theo `05`.
- Dấu gạch "-" thường. Trả lời tiếng Việt, ngắn gọn.
