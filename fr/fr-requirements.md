# AI Business Copilot (ABC) — Functional Requirements (trích lọc)
Nguồn: FA26_Capstone Register (FR theo role) + Report1 (Major Features FE-01→FE-16 + Limitations). Chỉ giữ phần liên quan build UI.

## Phạm vi & giới hạn (Limitations & Exclusions)
- LI-1: MVP chỉ phục vụ ngành quần áo & mỹ phẩm; loại trừ nhà hàng, quán cà phê, tạp hóa, sản xuất, dịch vụ.
- LI-2: Loại trừ mô hình tồn kho công thức/BOM (F&B).
- LI-3: Không thay thế phần mềm kế toán/khai thuế chính thức.
- LI-4: AI chỉ hỗ trợ ra quyết định, chủ shop vẫn phải xác nhận hành động.
- LI-5: Độ chính xác dự báo phụ thuộc chất lượng dữ liệu lịch sử.
- LI-6: Không đảm bảo tích hợp real-time với mọi POS/ngân hàng/sàn TMĐT/cổng thanh toán ngoài.
- LI-7: Không có tối ưu đa kho (multi-warehouse) hay lập kế hoạch sản xuất.
- LI-8: AI Agent chỉ dùng tool được duyệt sẵn, không bypass phân quyền ứng dụng.

## Major Features (FE-01 → FE-16) — bảng gốc từ Report1, dùng để đối chiếu khi 1 màn hình có vẻ thiếu chức năng
| ID | Feature | Nội dung |
|---|---|---|
| FE-01 | Authentication and Role-Based Access | Quản lý business profile, user/nhân viên, gán role/permission, access control theo user. |
| FE-02 | Business and Product Management | Quản lý business, category, product, **variant, SKU**, giá, thuộc tính cấu hình được; hỗ trợ **size/màu cho quần áo**, **dung tích cho mỹ phẩm**. |
| FE-03 | Inventory Management | Theo dõi tồn, ghi nhận nhập/xuất, điều chỉnh tồn, cấu hình ngưỡng tồn thấp, **theo dõi theo lô (batch)**, xem lịch sử tồn kho. |
| FE-04 | Batch and Expiration Management | Theo dõi lô từ NCC, quản lý lô tồn kho, **ghi số lượng theo lô**, **ghi hạn dùng**, xác định sản phẩm **sắp hết hạn**. |
| FE-05 | Supplier Management | Quản lý NCC, thông tin NCC, **liên kết sản phẩm ↔ NCC**, hỗ trợ phân tích mua hàng. |
| FE-06 | Sales and Order Management | Quản lý **khách hàng**, tạo/quản lý đơn, order item, **ghi nhận thanh toán** (không chỉ phương thức mà cả trạng thái/mã giao dịch), ghi giao dịch bán, lịch sử bán hàng. |
| FE-07 | Expense and Cash-Flow Recording | Ghi chi phí, phân loại chi phí, **theo dõi tiền vào/ra**, xem thông tin **dòng tiền cơ bản**. |
| FE-08 | Business Dashboard | Tổng quan doanh thu, xu hướng bán hàng, tình trạng tồn kho, hiệu suất sản phẩm, tổng hợp chi phí. |
| FE-09 | Demand Forecasting | Dự báo nhu cầu sản phẩm tương lai, xu hướng bán kỳ vọng, hỗ trợ lập kế hoạch tồn kho, dự báo thiếu hàng tiềm ẩn. |
| FE-10 | Inventory Intelligence | **Xác định hàng tồn thấp/bán chậm/cần nhập lại**, sản phẩm sụt giảm doanh số, **rủi ro hết hàng**, sản phẩm sắp hết hạn. |
| FE-11 | What-if Simulation | Mô phỏng quyết định: ngân sách, giá, nhu cầu bán kỳ vọng, chi phí vận hành, **số lượng tồn kho**. |
| FE-12 | AI Business Copilot | Hỏi bằng ngôn ngữ tự nhiên, trả lời có dữ liệu minh chứng. |
| FE-13 | AI Agent with Business Tools | Gọi tool có kiểm soát: sales history, inventory status, margin, forecast, supplier info, simulation. |
| FE-14 | AI Recommendations and Insights | Sinh khuyến nghị hành động kèm dữ liệu hỗ trợ + độ tin cậy. |
| FE-15 | Notifications | **Giao diện thông báo** cho sự kiện kinh doanh và insight được chọn. |
| FE-16 | Audit and AI Execution Logs | Ghi hành động hệ thống quan trọng + log thực thi tool AI. |

## 1. Business Owner
### 1.1 Business Management
Tạo/cập nhật thông tin doanh nghiệp; cấu hình đơn vị tiền tệ, quy tắc giá, ngưỡng tồn kho, tham số cảnh báo; xem hiệu suất kinh doanh; quản lý nhân viên và phân quyền. *(FE-01)*

### 1.2 Expense and Basic Financial Management
Tạo/sửa/xóa/phân loại chi phí; ghi nhận theo hạng mục-số tiền-thời gian; theo dõi tổng chi theo ngày/tháng/kỳ; tính doanh thu từ đơn hàng; tính lợi nhuận ước tính (doanh thu - giá vốn - chi phí); phân tích tỷ trọng/xu hướng chi phí. **Bổ sung (FE-07): ghi nhận tiền vào/ra (cash inflow/outflow), xem dòng tiền cơ bản** — trước đây MD chỉ có phần phân tích dòng tiền (1.7/1.8) mà thiếu nguồn dữ liệu đầu vào này.

### 1.3 Product and Pricing Management
Tạo/sửa/ẩn sản phẩm; tổ chức theo danh mục; cấu hình giá bán/giá vốn; cấu hình mức tồn kho tối thiểu; tính lợi nhuận gộp theo sản phẩm/danh mục; tính biên lợi nhuận gộp. **Bổ sung (FE-02): quản lý biến thể sản phẩm (product variant) + SKU riêng theo variant; thuộc tính size/màu cho quần áo, dung tích cho mỹ phẩm** — khớp entity `product_variants` trong ERD (attributes, sku, sellingPrice, costPrice riêng theo variant).

### 1.4 Inventory Management
Xem tồn kho hiện tại theo sản phẩm; theo dõi mức tồn tối thiểu; ghi nhận nhập/xuất kho; điều chỉnh tồn theo chênh lệch thực tế; xem lịch sử biến động tồn; ước tính tốc độ tiêu thụ; cảnh báo sắp hết hàng kèm giải thích dựa trên dữ liệu. **Bổ sung (FE-04): quản lý theo LÔ (batch) — số lượng theo lô, số lượng còn lại, giá vốn theo lô, ngày sản xuất, ngày nhận, hạn dùng; cảnh báo sản phẩm sắp hết hạn** — khớp entity `inventory_batches` (batchNumber, quantity, remainingQuantity, unitCost, manufactureDate, receivedAt, expiresAt).

### 1.4b Supplier Management (bổ sung mới — FE-05)
Quản lý danh sách nhà cung cấp; thông tin liên hệ NCC; **liên kết sản phẩm/lô hàng với nhà cung cấp**; hỗ trợ phân tích mua hàng. Khớp entity `suppliers` và field `supplierId` trong `inventory_batches`.

### 1.5 Order Management
Tạo đơn bán; chọn sản phẩm & số lượng; tự tính tổng tiền; áp dụng chiết khấu/khuyến mãi; ghi nhận phương thức thanh toán; cập nhật trạng thái đơn; hủy đơn kèm lý do; xem lịch sử đơn; cập nhật tồn kho theo đơn hoàn tất/hủy. **Bổ sung (FE-06): quản lý khách hàng (customer) gắn với đơn; ghi nhận thanh toán đầy đủ — không chỉ phương thức mà cả trạng thái thanh toán, mã giao dịch, thời điểm thanh toán** — khớp entity `customers` và `payments` (amount, method, status, transactionCode, paidAt).

### 1.6 Dashboard and KPI
Hiển thị hiệu suất theo ngày/tháng/kỳ; doanh thu, lợi nhuận, chi phí, tổng đơn, giá trị đơn trung bình, giá trị tồn kho; xu hướng doanh thu/lợi nhuận; phân tích bán hàng theo sản phẩm/danh mục; phân tích cơ cấu chi phí; phân tích tình trạng tồn kho; lọc theo tiêu chí. *(FE-08)*

### 1.7 AI Business Analytics
Phân tích doanh thu/chi phí/lợi nhuận/tồn kho/đơn hàng/dòng tiền; giải thích nguyên nhân tăng/giảm; cung cấp dữ liệu minh chứng; gợi ý bước điều tra/quyết định tiếp theo.

### 1.8 AI Anomaly Detection and Alerts
Phát hiện bất thường về doanh thu/chi phí/lợi nhuận/tồn kho/dòng tiền/đơn hàng/hiệu suất sản phẩm; cung cấp nguyên nhân khả dĩ + bằng chứng; cho phép xem dữ liệu gốc của cảnh báo.

### 1.9 AI Forecasting & Inventory Intelligence
Dự báo nhu cầu sản phẩm, mức tồn kho cần thiết, doanh thu tương lai; hiển thị kỳ dự báo + dữ liệu đầu vào; hiển thị giới hạn/độ tin cậy nếu mô hình hỗ trợ; dùng kết quả dự báo cho quyết định tồn kho & mô phỏng. **Bổ sung (FE-10 — Inventory Intelligence): phát hiện hàng bán chậm (slow-moving), hàng cần nhập lại (replenishment candidate), rủi ro hết hàng (stockout risk), sản phẩm sắp hết hạn** — đây là 1 khối UI/logic riêng, không chỉ là "dự báo" thuần túy.

### 1.10 Business Simulation
Tạo kịch bản mô phỏng từ dữ liệu hiện tại; thay đổi giá bán, giá vốn, chi phí, sản lượng bán, ngân sách marketing, chi phí nhân công; tính lại doanh thu/chi phí/lợi nhuận/KPI; so sánh với baseline; giải thích yếu tố chính ảnh hưởng; lưu kịch bản để xem lại. **Bổ sung (FE-11): biến mô phỏng còn bao gồm thay đổi SỐ LƯỢNG TỒN KHO** (inventory quantity), không chỉ giá/chi phí/sản lượng.

### 1.11 AI Business Advisor
Giao tiếp bằng ngôn ngữ tự nhiên; nhận diện ý định; chọn tool nghiệp vụ phù hợp; truy xuất dữ liệu được phân quyền; thực hiện tính toán/phân tích/mô phỏng khi cần; trả lời kèm bằng chứng; phân biệt rõ dữ liệu thật/tính toán/dự báo/giả định/khuyến nghị; yêu cầu xác nhận của chủ shop trước hành động quan trọng. *(FE-12, FE-13, FE-14)*

### 1.12 Notifications (bổ sung mới — FE-15)
Giao diện thông báo cho người dùng về các sự kiện kinh doanh và insight được chọn (vd cảnh báo tồn kho, anomaly, kết quả forecast quan trọng). Khớp entity `notifications` (type, title, message, isRead).

## 2. Store Employee
- 2.1 Sales Transaction: ghi nhận giao dịch bán, chọn SP & số lượng, tính tổng, ghi phương thức thanh toán được phép, cập nhật tồn kho sau giao dịch hợp lệ.
- 2.2 Inventory Operations: ghi số lượng tồn thực tế, cập nhật chênh lệch trong phạm vi cho phép, ghi lý do điều chỉnh khi cần, ghi nhận nhập kho.
- 2.3 Product Viewing: xem sản phẩm được phân quyền (tên, danh mục, giá bán), không được sửa thông tin quan trọng.
- 2.4 Access Restrictions: KHÔNG được xem lợi nhuận nhạy cảm, đổi cấu hình cấp doanh nghiệp, quản lý tài khoản, sửa cấu hình AI, ra quyết định thay chủ shop, sửa thông tin tài chính ngoài quyền.

## 3. System Administrator
- 3.1 Account & Role: xem tài khoản, kích hoạt/vô hiệu hóa, quản lý role/permission.
- 3.2 Business Management: xem doanh nghiệp đã đăng ký, quản lý trạng thái tài khoản doanh nghiệp.
- 3.3 System Configuration: quản lý cấu hình hệ thống dùng chung, ngưỡng/giới hạn hệ thống.
- 3.4 Audit Log: ghi actor/timestamp/action/object; theo dõi thay đổi quyền, cấu hình, dữ liệu nhạy cảm, thao tác AI quan trọng; tìm kiếm/lọc log. *(FE-16)*

## Non-Functional Requirements
- Performance: thao tác thường dùng phản hồi trong thời gian chấp nhận được; dashboard truy xuất hiệu quả; AI phản hồi thực tế cho web app tương tác.
- Scalability: hỗ trợ nhiều doanh nghiệp cùng lúc; multi-tenant data isolation.
- Security: xác thực + phân quyền theo role; Business Owner chỉ truy cập dữ liệu của mình; Store Employee giới hạn theo quyền; log thao tác nhạy cảm; AI tool tôn trọng phân quyền.
- Reliability: giao dịch phải nhất quán; thay đổi tồn kho theo đúng business rule; kết quả AI phải nêu rõ khi dựa trên dự báo/giả định.
- Explainability & Traceability: insight AI quan trọng phải có bằng chứng; phân biệt fact/calculation/forecast/recommendation; log thao tác AI quan trọng.
- Privacy: bảo vệ dữ liệu doanh nghiệp; AI chỉ nhận tối thiểu dữ liệu cần cho tác vụ.
