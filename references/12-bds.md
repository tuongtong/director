# 12 - PHIM BẤT ĐỘNG SẢN
© 2026 Đạo diễn Tường Tống - Space Gray Production

> Đọc thêm file này khi brief là phim bất động sản: phim quảng cáo dự án (TV hoặc mạng), phim ra mắt phân khu, phim đi một vòng dự án, phim chiếu ở nhà mẫu, phim thương hiệu chủ đầu tư.
> Các luật ở đây rút ra từ 11 phim tham khảo: Sola, Masteri West Heights, Masteri - Nâng tầm, The Valley (Emaar), Charmora City, Văn Phú, Vinhomes Ocean Park, Vịnh Tiên, Wonder City, COLORBOND, một phim thời trang Ả Rập (KAEC). Tên phim và timecode trong ngoặc là chỗ để mở ra xem lại.
> **Khi xung đột, luật cứng trong `SKILL.md` thắng:** không ghi ống kính, cách viết theo `11`, prompt theo `05`, bảng theo `04`. Các con số giây trong file này là chuẩn nhịp nội bộ để tự kiểm. Không chép số giây vào ô hình gửi khách.

## Dùng ở bước nào

- **Bước 2 (Neo phim):** xác định loại phim, kênh chiếu, dự án đang ở giai đoạn nào (chưa xây thì dùng CGI, đã có người ở thì quay thật). Đưa ra 2-3 khung kịch bản ở bảng dưới, mỗi khung một dòng lý do, **chờ 3T chọn**. Spine viết 1 câu. Thêm slogan (tối đa 3 vế) và một hình lặp lại ít nhất 3 lần trong phim.
- **Bước 3 (Kịch bản):** theo bảng "Nhịp chuẩn" và các luật bên dưới. Có cột Nguồn (Quay thật / CGI / AI / Stock / Đồ họa), cuối bảng ghi tỷ lệ % mỗi nguồn.
- **Số liệu dự án:** không bịa. Thiếu thì ghi `[cần số liệu]`.
- **Bước 7-8:** cảnh nào AI làm khó (xem bảng "Cảnh nào AI làm được") thì chuyển sang quay thật hoặc dựng 3D. Kiến trúc dự án thật luôn lấy phối cảnh hoặc mặt bằng chính thức của chủ đầu tư làm `@image1`, và thêm câu `Do not redesign the architecture.` vào prompt.
- **Bước 10 (QC):** chạy danh sách tự rà ở cuối file, cùng với `08`.
- Phim dài hơn 2 phút chiếu trên mạng: luôn đề xuất thêm 1 bản ngắn 30-60 giây và các clip từng phần 15-30 giây.

## Loại phim

| Loại phim | Dài | Người xem cần gì sau khi xem | Lúc thấy dự án lần đầu | Lượng VO |
|---|---|---|---|---|
| Phim quảng cáo cảm xúc (TV hoặc mạng) | 30-90 giây | Muốn về đó sống | Sau 30-50% phim | Ít, mỗi câu dưới 5 giây |
| Phim ra mắt phân khu | 1-3 phút | Hiểu phân khu chia ra sao, muốn mua | Trong 5 giây đầu | Vừa, có số liệu |
| Phim đi một vòng dự án | 2-3 phút | Biết đủ các tiện ích | Trong 3 giây đầu | Nhiều, mỗi cảnh đi với một câu VO |
| Phim chiếu ở nhà mẫu | 3-5 phút | Có đủ ý để nhân viên tư vấn | Ngay giây đầu | Nhiều, bắt buộc chia phần |
| Phim thương hiệu chủ đầu tư | 1-2 phút | Tin vào cách làm của chủ đầu tư | Sau 25-35% phim, hoặc chỉ ở cuối | Ít, có một câu nói lên quan điểm |
| Phim vật liệu, hạ tầng | 30-60 giây | Tin vào công nghệ | Thấy sớm, gọi tên muộn | Đọc liền, giọng trầm |

## 10 khung kịch bản

| Mã | Tên | Phim đi theo thứ tự | Hợp với | Phim mẫu |
|---|---|---|---|---|
| A1 | Mượn một hình ảnh | Mở bằng hình ảnh của tên dự án → hình đó lặp lại qua 3 chất liệu khác nhau → giữa phim nối sang dự án → gia đình → lộ dự án | Dự án có tên trừu tượng (phản chiếu, lan tỏa, ánh sáng) | Sola |
| A2 | Gài trước, trả sau | Giới thiệu chủ nhà → gài sớm một chuyện phụ (đứa con, sở thích) → đi qua tiện ích → chuyện phụ có kết quả → ghép nhân vật vào cảnh toàn dự án | Phim cao cấp 90-160 giây | Masteri West Heights |
| A3 | Có vấn đề, có lời giải | Mở bằng một cảnh khổ ở thành phố → nhân vật bị kẹt → hình tối, mờ → bùng nắng, hiện logo → một ngày ở dự án | Căn hộ trong thành phố, khách 30-40 tuổi có con | Masteri - Nâng tầm |
| A4 | "Nếu tôi chọn…" theo đời người | Mở bằng điểm mạnh nhất ngay giây đầu → các mốc đời (đi làm, sinh con, con lớn, sở thích, sum họp) → mỗi mốc một tiện ích và một lúc thành công → lộ dự án ban đêm | Khu đô thị lớn đã có người ở | Ocean Park |
| A5 | Không đo bằng thước cũ | Mở bằng câu hỏi, bác bỏ cách đo quen (diện tích, chiều cao, vị trí) → một hình ảnh văn hóa ai cũng biết để chốt quan điểm → các giá trị lặp cùng một kiểu câu → đội ngũ làm dự án → các dự án đã làm | Phim thương hiệu chủ đầu tư | Văn Phú |
| A6 | Mỗi cảnh một tiện ích | Chào, cổng vào → flycam quay thật toàn khu, số liệu đổi ra thứ dễ hình dung → tiện ích theo từng nhóm → một câu nối "Và còn…" → nhóm thứ hai → biệt thự, câu kêu gọi → lặp slogan | Phim đi một vòng dự án, khách nước ngoài | The Valley |
| A7 | Bản đồ làm mục lục | Tên và định vị → flycam toàn khu → bản đồ phân khu có ghi tên → đi từng phân khu theo đúng thứ tự trên bản đồ → cảnh đẹp nhất của dự án | Ra mắt phân khu, khu có nhiều đảo hoặc phân khu | Charmora, Wonder City |
| A8 | Từ cổ tích sang tính toán | Mở bằng hình ảnh cổ tích (cuốn sách, người đi trên mặt nước) → định vị, quy mô → tiện ích → một đoạn đổi hẳn chất liệu → chủ nhà → lý do đầu tư (đường đi, dòng tiền) ở 15% cuối | Nghỉ dưỡng, nhà thứ hai, khách đầu tư | Vịnh Tiên |
| A9 | Người già đi, sản phẩm vẫn vậy | Người thay đổi theo năm tháng, sản phẩm vẫn như cũ → sản phẩm không tên bên cạnh bị hư → cận vào bên trong để thấy công nghệ → để lại cho đời sau | Vật liệu, hạ tầng, nhà xưởng | COLORBOND |
| A10 | Chân dung người ở trẻ | 6-7 nhân vật, mỗi người một màu áo và một món đồ → nhiều giọng VO, mỗi người tự kể → từng người nhìn vào máy → cả nhóm đi tới máy | Dự án nhắm khách trẻ, nhà phố thương mại | Phim thời trang KAEC |

## Nhịp chuẩn (nội bộ, để tự kiểm)

| Hạng mục | Chuẩn | Ghi chú |
|---|---|---|
| Hình mở đầu | Ngay giây 0-1 | Phim chiếu mạng không để logo hay tên phim đứng trước hình mở đầu (Sola để logo 4 giây, West Heights 9 giây, Wonder City 8 giây là lỗi) |
| Độ dài trung bình một cảnh, phim cảm xúc | 1,7-2,4 giây | Ocean Park 1,7 · Masteri 2,0 · West Heights 2,4 |
| Độ dài trung bình một cảnh, phim đi một vòng / nhà mẫu | 2,6-3,2 giây | Cảnh để đọc chữ hoặc bản đồ tối đa 6 giây. Dài hơn thì cho máy đi hoặc cắt làm hai |
| Chuỗi cắt nhanh trước khi lộ dự án | 4-7 cảnh, mỗi cảnh 0,3-0,8 giây | Sau đó cảnh dự án giữ ít nhất 2,5 giây |
| Cảnh cảm xúc mạnh nhất | Giữ 8-10 giây, không VO | Trước nó là chuỗi cắt nhanh xen màn đen |
| Đoạn không VO | Ít nhất 3-5 giây trong phim dài hơn 75 giây | |
| Đoạn đổi chất liệu | 1,5-2 giây, ở khoảng 60% phim | Bắt buộc với phim dài hơn 2 phút |
| Chữ số liệu trên màn hình | Giữ ít nhất 2,5 giây, số lớn, chữ đi kèm tối đa 6 chữ | |
| Màn kết phim chiếu mạng | Tối đa 5 giây, có câu kêu gọi hoặc chỗ bấm xem tiếp | Màn đen 11-12 giây là phí |
| Câu VO | Mỗi câu dưới 5 giây, nghỉ 1-2 giây. Cả phim dùng chung một kiểu câu lặp lại | |

## Luật đạo diễn

Viết theo dạng KHI → LÀM → ĐỂ. Dùng luật nào khớp với phim, không ép đủ.

### Mở phim và nhịp cắt

1. KHI mở phim chiếu mạng → LÀM cảnh đầu là một tình huống hiểu được trong 1 giây (kẹt xe quay thẳng từ trên xuống, một câu hỏi bác bỏ, điểm mạnh ai cũng biết) → ĐỂ người xem không lướt qua trong 3 giây đầu. (Masteri 00:00, Văn Phú 00:00, Ocean Park 00:00)
2. KHI chuyển từ vấn đề sang lời giải → LÀM hình tối, mờ chừng 1,5-2 giây, rồi bùng nắng chiếu ngược vào máy, logo hiện đúng cảnh có nắng → ĐỂ thương hiệu đi liền với cảm giác nhẹ người. (Masteri 00:09-00:13)
3. KHI sắp lộ dự án → LÀM 4-7 cảnh cắt rất nhanh, rồi cảnh dự án giữ ít nhất 2,5 giây → ĐỂ người xem thấy như vừa "tới nơi". (Sola 00:42-00:47)
4. KHI cần cảnh cảm xúc mạnh nhất → LÀM chuỗi cắt nhanh xen màn đen, rồi giữ cận mặt nhân vật thật lâu, bỏ VO → ĐỂ cảm xúc có chỗ lắng. (West Heights 01:58-02:13)
5. KHI phim dài hơn 2 phút → LÀM ở khoảng 60% phim một đoạn đổi hẳn chất liệu (cắt dán ảnh, hoạt hình) → ĐỂ kéo người xem quay lại. (Vịnh Tiên 01:56)
6. KHI có cảnh chơi thể thao → LÀM 3 cảnh đi theo quả bóng (đánh → bay → vào) ở 3 góc khác hẳn nhau (ngang, từ dưới nhìn lên, từ trên xuống) → ĐỂ kéo dài lúc hồi hộp. (Ocean Park 00:32-00:38)
7. KHI cần cho thấy nhiều trải nghiệm → LÀM xen kẽ hai người (người đánh đàn và người múa), cắt theo nốt nhạc → ĐỂ đoạn liệt kê có nhịp. (Wonder City 00:18-00:22)

### Con người và cảm xúc

8. KHI phim dài hơn 75 giây → LÀM một gia đình hoặc một nhân vật đi suốt phim, gài một chuyện phụ ở nửa đầu, chuyện đó có kết quả ngay trước khi lộ logo → ĐỂ tiện ích có người dẫn đi. (West Heights 00:40 → 02:02)
9. KHI quay một tiện ích → LÀM một lúc nhân vật làm được việc gì đó, có kết quả, có người xung quanh phản ứng → ĐỂ tiện ích thành một cảm xúc. (Ocean Park 00:16, 00:38-00:42)
10. KHI phải kể nhiều tiện ích → LÀM xếp theo các mốc đời người → ĐỂ danh sách thành một câu chuyện. (Ocean Park)
11. KHI muốn nói chủ nhà có vị thế → LÀM người khác vỗ tay cho nhân vật (bữa tiệc, khán phòng), không để nhân vật tự khoe → ĐỂ vị thế do người khác công nhận. (West Heights 00:17, 02:16)
12. KHI muốn người xem tự đặt mình vào vai người mua → LÀM VO ngôi thứ nhất của người quyết định mua, kèm một cảnh khá dài nhìn từ mắt nhân vật sang người thân → ĐỂ người xem ở trong lúc đó. (Masteri 00:27-00:36)
13. KHI ý tưởng trừu tượng → LÀM một hình lặp lại ít nhất 3 lần bằng các chất liệu khác nhau, hoặc một hình ảnh văn hóa ai cũng biết, đặt đúng câu VO chốt → ĐỂ VO không phải giải thích. (Sola: nước, khung đôi, bàn tay. Văn Phú: hình người Vitruvius 00:13)
14. KHI khách là gia đình nhiều thế hệ → LÀM chuỗi cận bàn tay nắm nhau của 3 lứa tuổi, nắng chiếu ngược → ĐỂ chốt cảm xúc rất nhanh. (Sola 01:13-01:16)
15. KHI kể "một ngày ở dự án" → LÀM ánh sáng đi từ ban ngày → hoàng hôn → ban đêm. Ban đêm thấy nhiều cửa sổ căn hộ sáng đèn → ĐỂ thấy một ngày đủ đầy và khu đông người ở. (Masteri)
16. KHI nhắm khách trẻ → LÀM mỗi nhân vật một màu áo và một món đồ, mỗi người 2-3 cảnh (toàn - chi tiết - mặt), rồi từng người nhìn vào máy, mỗi người chừng 1 giây → ĐỂ người xem nhớ ai là ai. (KAEC 00:09-00:16, 00:39-00:46)

### Không gian và kiến trúc

17. KHI nối cảnh quay thật với cảnh CGI → LÀM cầu nối bằng thứ có ở cả hai bên (mặt nước, mây, hơi nước) hoặc một chuyến đi (xe chạy về nhà, flycam bay nhanh ban đêm) → ĐỂ người xem không thấy chỗ đổi. (Sola 00:46-00:47, West Heights 00:50-01:01, Charmora 00:04 và 00:39)
18. KHI cảnh CGI có người → LÀM máy đặt ngang tầm mắt, đi tới thật chậm, người ở phía trước và giữa khung → ĐỂ hình CGI nhìn như mình đang đứng ở đó. (The Valley 01:13-02:02)
19. KHI dự án có nhiều phân khu → LÀM bản đồ có ghi tên trước, rồi đi từng phân khu đúng thứ tự trên bản đồ → ĐỂ người xem có mục lục. (Charmora 00:21, Wonder City 01:55)
20. KHI có số liệu quy mô → LÀM đổi ra thứ dễ hình dung (bao nhiêu sân bóng, bao nhiêu km đường chạy), đặt chữ lên cảnh flycam quay thật từ trên xuống → ĐỂ con số có hình và đáng tin. (The Valley 00:08-00:24)
21. KHI có nhiều mẫu nhà → LÀM mỗi mẫu một cảnh ngang tầm mắt, ghi tên phong cách và một chữ nói cảm giác → ĐỂ khách chọn theo cảm giác. (Wonder City 01:18-01:29)
22. KHI phải nói "có rất nhiều tiện ích" → LÀM chia màn hình 4 ô, kèm một con số tổng → ĐỂ gói 4 cảnh vào 4 giây. (The Valley 00:25)
23. KHI có chữ đặt trong cảnh → LÀM tối đa 4 chữ, chữ đứng yên trong cảnh khi máy di chuyển, màu thương hiệu. Nói về thứ gây hại thì chữ làm bằng chính thứ đó (rỉ sét) → ĐỂ chữ vừa là thông tin vừa là hình. (Charmora, COLORBOND)
24. KHI thương hiệu có màu nổi → LÀM lặp màu đó trong ánh sáng của cảnh (sông phát sáng, pháo hoa, chữ tên và chức danh) → ĐỂ thương hiệu có mặt cả khi không có logo. (Charmora, Vịnh Tiên)
25. KHI phải trộn nhiều nguồn hình (stock, CGI, AI) → LÀM một khung trình bày chung (chia màn hình trên nền màu thương hiệu, khung tranh treo tường, cuốn sách lật trang) → ĐỂ hình nhiều nguồn nhìn như một phong cách. (Sola 00:19, Vịnh Tiên 00:47 và 02:16)
26. KHI kết phim → LÀM ghép nhân vật vào cảnh toàn dự án, hoặc lặp lại đúng câu mở đầu → ĐỂ cảnh lộ dự án mang theo cảm xúc của cả phim và người xem nhớ slogan. (West Heights 02:20, The Valley 00:00 và 02:18)
27. KHI phim nhắm khách đầu tư → LÀM phần tính toán (đường đi, dòng tiền) ở 15% cuối, minh họa bằng xe, tàu, máy bay → ĐỂ lý do mua đến sau khi người xem đã muốn. (Vịnh Tiên 02:33-02:50)

## Lỗi hay gặp

- Phim chiếu mạng để logo hoặc tên phim từ 4 giây trở lên trước hình mở đầu.
- Tiện ích không có người, hoặc chỉ có người CGI nhỏ xíu, không có lúc nào có người thật.
- VO đọc liền hơn 60 giây không nghỉ.
- Kể tiện ích mà không có kiểu câu hoặc kiểu hình lặp lại.
- Cảnh giữ 10-18 giây chỉ để đọc chữ hoặc bản đồ.
- Dùng lại cảnh của dự án khác cùng chủ đầu tư mà không chỉnh màu lại hoặc không đổi cách dùng.
- Màn kết phim chiếu mạng đứng yên quá 5 giây mà không có câu kêu gọi.
- Phim dài hơn 75 giây mà mỗi cảnh một người, không có ai đi suốt.
- Màn cuối nhồi quá 4 thứ (chân dung, công trình, slogan, huy hiệu, logo) → tách làm 2 màn.

## Hình ảnh tra nhanh

| Hạng mục | Mặc định cho BĐS cao cấp | Khi cần khác |
|---|---|---|
| Ánh sáng ngoài trời | Hoàng hôn, nắng chiếu ngược vào máy, có lóe sáng nhẹ | Sáng sớm cho "bắt đầu". Ban đêm có đèn nhà, đèn đường cho "đông vui" |
| Ánh sáng trong nhà | Nắng mềm qua cửa sổ, rèm trắng | Phòng tối, chỉ có đèn trong cảnh, cho bữa tiệc, cho vị thế |
| Cú máy với người | Cận, phía sau mờ | Đặt máy thấp nhìn lên cho trẻ em, thể thao, nhân vật đi tới máy |
| Cú máy với không gian | Ngang tầm mắt. Flycam góc rộng | Đặt máy sát đất nhìn lên cho cảnh siêu thực |
| Máy đi thế nào | Máy đi chậm, đi tới gần, flycam | Flycam bay nhanh để đổi địa điểm. Quay thẳng từ trên xuống cho điểm mạnh và chuyển phần |
| Màu phim | Không quá tương phản, vùng sáng sáng rõ | Xanh lạnh và cam ấm cho "vị thế". Đèn màu theo màu thương hiệu cho "lễ hội" |
| Màu nhân vật | Một màu riêng lặp lại (vàng mù tạt, vàng chanh) | Mỗi nhân vật một màu khi có nhiều nhân vật |
| Chuyển cảnh chữ ký | Nối bằng mặt nước. Nối bàn chân sang bàn chân, bàn tay sang bàn tay | Bay xuyên mây, hơi nước. Khung trong khung. Máy lia rất nhanh |
| Nhạc | Dàn nhạc hoặc piano lên dần, 100-125 nhịp/phút, nhạc bùng đúng lúc lộ logo | Nhạc pop có lời xưng "tôi". Nhạc điện tử trên 130 nhịp/phút cho khách trẻ |

## Cảnh nào AI làm được (prompt viết theo `05`)

| AI làm tốt | AI làm khó → quay thật hoặc dựng 3D |
|---|---|
| Flycam lấy không khí, hình mờ có đốm sáng, mặt nước, ánh sáng, chân dung đứng yên | Cận bàn tay đang làm việc, tay chạm tay, ngón tay trên phím đàn |
| Một cảnh siêu thực (bông hoa khổng lồ, người đi trên mặt nước) | Mặt bằng, bản đồ, chữ ghi tên, số liệu (dính pháp lý) |
| Chuyển cảnh bay xuyên mây, hơi nước | Chuỗi cảnh nối nhau cần cùng một nhân vật qua nhiều cảnh |
| Một lúc ngắn của trẻ em, dưới 3 giây | Biểu cảm trẻ em kéo dài, đám đông xe máy, bóng bay đúng vật lý |
| | Chữ tiếng Việt có dấu trong cảnh, logo thương hiệu thật |

## Tự rà trước khi giao

- [ ] Hình mở đầu ở giây 0-1. Phim chiếu mạng không để logo đứng trước.
- [ ] Dự án hiện ra đúng lúc theo bảng "Loại phim".
- [ ] Độ dài trung bình mỗi cảnh nằm trong chuẩn. Có chuỗi cắt nhanh trước khi lộ dự án.
- [ ] Có một hình lặp lại ít nhất 3 lần.
- [ ] Tiện ích nào cũng có người đang làm gì đó, không để trống.
- [ ] Phim dài hơn 75 giây: có nhân vật đi suốt, chuyện gài trước có kết quả. Có ít nhất 3 giây không VO.
- [ ] Phim dài hơn 2 phút: có đoạn đổi chất liệu ở khoảng 60%. Mỗi phần mở bằng bản đồ hoặc tên phần.
- [ ] Chữ số liệu giữ ít nhất 2,5 giây. Không cảnh nào giữ quá 6 giây chỉ để đọc chữ.
- [ ] Chỗ nối cảnh quay thật với CGI có cầu nối rõ.
- [ ] Màn kết tối đa 5 giây, có câu kêu gọi hoặc chỗ bấm xem tiếp.
- [ ] Cột Nguồn đủ. Cảnh AI làm khó đã chuyển sang quay thật hoặc 3D.
- [ ] Không có số liệu bịa. Chỗ thiếu ghi `[cần số liệu]`.
- [ ] Có đề xuất bản ngắn cho mạng.

Mục nào chưa đạt thì sửa rồi mới giao. Mục cố ý bỏ qua thì ghi lý do một dòng.
