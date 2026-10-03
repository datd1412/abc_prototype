# Bảng Ánh Xạ Field ↔ Label Tiếng Việt

| Field (ERD, camelCase) | Label tiếng Việt dùng trên UI | Màn hình dùng đầu tiên |
|---|---|---|
| products.name | Tên sản phẩm | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.name | Tên biến thể | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.sku | Mã SKU | BO-03 Quản lý Sản phẩm & Bảng giá |
| categories.name | Danh mục sản phẩm | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.sellingPrice | Giá bán | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.costPrice | Giá vốn | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory.quantity | Số lượng tồn kho | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory.reservedQty | Số lượng tạm giữ | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory.lowStockThreshold | Ngưỡng tồn thấp | BO-03 Quản lý Sản phẩm & Bảng giá |
| products.status | Trạng thái | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.status | Trạng thái biến thể | BO-03 Quản lý Sản phẩm & Bảng giá |
| products.productType | Loại sản phẩm | BO-03 Quản lý Sản phẩm & Bảng giá |
| products.description | Mô tả sản phẩm | BO-03 Quản lý Sản phẩm & Bảng giá |
| product_variants.attributes | Thuộc tính biến thể | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory_batches.batchNumber | Số lô nhập | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory_batches.expiresAt | Hạn sử dụng lô | BO-03 Quản lý Sản phẩm & Bảng giá |
| inventory_batches.manufactureDate | Ngày sản xuất | BO-04 Quản lý Tồn kho |
| inventory_batches.unitCost | Đơn giá vốn lô | BO-04 Quản lý Tồn kho |
| inventory_transactions.type | Loại giao dịch kho | BO-04 Quản lý Tồn kho |
| inventory_transactions.reason | Lý do xuất nhập kho | BO-04 Quản lý Tồn kho |
| orders.orderNumber | Mã đơn hàng | BO-06 Quản lý Đơn hàng |
| orders.status | Trạng thái đơn hàng | BO-06 Quản lý Đơn hàng |
| orders.total | Tổng tiền thanh toán | BO-06 Quản lý Đơn hàng |
| payments.method | Phương thức thanh toán | BO-06 Quản lý Đơn hàng |
| ai_insights.severity | Mức độ cảnh báo | BO-08 AI Anomaly Detection |
| ai_insights.title | Tiêu đề cảnh báo | BO-08 AI Anomaly Detection |
| ai_insights.summary | Tóm tắt sự cố | BO-08 AI Anomaly Detection |
| ai_insights.evidence | Dữ liệu bằng chứng | BO-08 AI Anomaly Detection |
| ai_insights.recommendation | Gợi ý xử lý AI | BO-08 AI Anomaly Detection |
| ai_insights.confidence | Độ tin cậy AI Sentinel | BO-08 AI Anomaly Detection |
| forecast_runs.forecastType | Loại dự báo nhu cầu | BO-09 AI Demand Forecasting |
| forecast_runs.horizonDays | Chu kỳ dự báo | BO-09 AI Demand Forecasting |
| forecast_results.predictedValue | Nhu cầu dự báo | BO-09 AI Demand Forecasting |
| forecast_results.confidence | Độ tin cậy WAPE | BO-09 AI Demand Forecasting |
| simulations.name | Tên kịch bản mô phỏng | BO-10 AI Scenario Lab |
| simulations.type | Loại kịch bản mô phỏng | BO-10 AI Scenario Lab |
| simulation_results.metricName | Chỉ số mô phỏng dự kiến | BO-10 AI Scenario Lab |
| simulation_results.projectedValue | Giá trị dự phóng | BO-10 AI Scenario Lab |
| ai_conversations.title | Tiêu đề phiên tham vấn | BO-11 AI Business Advisor |
| ai_messages.role | Vai trò gửi tin AI | BO-11 AI Business Advisor |
| ai_messages.content | Nội dung tham vấn AI | BO-11 AI Business Advisor |
| ai_messages.metadata | Bằng chứng minh bạch | BO-11 AI Business Advisor |
| business_settings.timezone | Múi giờ hệ thống | SA-01 Cấu Hình Hệ Thống |
| business_settings.lowStockDefault | Ngưỡng tồn kho mặc định | SA-01 Cấu Hình Hệ Thống |
| business_settings.aiEnabled | Kích hoạt AI Copilot toàn cục | SA-01 Cấu Hình Hệ Thống |
| business_settings.settings | Master Feature Flags JSON | SA-01 Cấu Hình Hệ Thống |
| businesses.id | Mã doanh nghiệp / Tenant ID | SA-02 Quản Lý Doanh Nghiệp |
| businesses.name | Tên doanh nghiệp | SA-02 Quản Lý Doanh Nghiệp |
| businesses.businessType | Gói dịch vụ / Loại DN | SA-02 Quản Lý Doanh Nghiệp |
| businesses.taxCode | Mã số thuế | SA-02 Quản Lý Doanh Nghiệp |
| businesses.status | Trạng thái doanh nghiệp | SA-02 Quản Lý Doanh Nghiệp |
| audit_logs.action | Thao tác an ninh | SA-03 An Ninh Hệ Thống |
| audit_logs.metadata | Mã băm SHA-256 Commit | SA-03 An Ninh Hệ Thống |
| audit_logs.id | Mã nhật ký / Trace ID | SA-04 Audit Log |
| audit_logs.userId | ID người thực hiện | SA-04 Audit Log |
| audit_logs.businessId | ID doanh nghiệp tác động | SA-04 Audit Log |
| audit_logs.entityType | Loại đối tượng tác động | SA-04 Audit Log |
| audit_logs.createdAt | Thời điểm thực hiện NTP | SA-04 Audit Log |
| order_items.productNameSnapshot | Tên sản phẩm giỏ POS | SE-01 POS Terminal Bán Hàng |
| order_items.skuSnapshot | Mã SKU giỏ POS | SE-01 POS Terminal Bán Hàng |
| order_items.quantity | Số lượng bán POS | SE-01 POS Terminal Bán Hàng |
| order_items.unitPrice | Đơn giá bán POS | SE-01 POS Terminal Bán Hàng |
| payments.method | Phương thức thanh toán POS | SE-01 POS Terminal Bán Hàng |
| inventory_transactions.beforeQuantity | Tồn trước kiểm (Tồn sổ sách) | SE-02 Kiểm Kê Tồn Kho Quầy |
| inventory_transactions.afterQuantity | Tồn sau kiểm (Thực đếm) | SE-02 Kiểm Kê Tồn Kho Quầy |
| inventory_transactions.quantity | Số lượng chênh lệch | SE-02 Kiểm Kê Tồn Kho Quầy |
| inventory_batches.remainingQuantity | Tồn lô | SE-02 Kiểm Kê Tồn Kho Quầy |
| inventory_batches.receivedAt | Thời điểm nhận hàng vào kho | SE-03 Ghi Nhận Nhập Kho Quầy |
| inventory_transactions.referenceId | Mã chứng từ GRN / Phiếu xuất nhập | SE-03 Ghi Nhận Nhập Kho Quầy |













