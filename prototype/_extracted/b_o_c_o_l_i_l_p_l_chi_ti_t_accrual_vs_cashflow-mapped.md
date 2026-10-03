# BO: Báo Cáo Kết Quả Kinh Doanh & Dòng Tiền Thực Tế — đã đối chiếu ERD/FR

## Field GIỮ
- `orders.totalAmount` / `orders.finalAmount` → Tổng doanh thu hóa đơn bán hàng (Accrual)
- `orders.paymentMethod` → Phân tách doanh thu theo phương thức (Tiền mặt, Chuyển khoản, Công nợ)
- `orders.paymentStatus` → Phân biệt doanh thu đã thu tiền (Cash In) và chưa thu (Công nợ phải thu)
- `orders.createdAt` → Kỳ ghi nhận doanh thu
- `expenses.amount` → Chi phí hoạt động kinh doanh (OPEX) và chi phí Marketing
- `expenses.category` → Phân loại chi phí (marketing, operational, salary, rent)
- `expenses.paymentMethod` → Hình thức chi tiền
- `expenses.status` → Trạng thái duyệt chi
- `purchase_orders.totalAmount` → Tiền mua hàng trả nhà cung cấp (Cash Out)
- `purchase_orders.status` → Trạng thái thanh toán đơn mua hàng
- `product_variants.costPrice` → Cơ sở tính Giá vốn hàng bán COGS

## Field LOẠI
- `chi nhánh Q.1`: Không có entity multi-branch trong ERD.
- `EBITDA / thuế TNDN dồn tích`: ERD không có phân hệ kế toán thuế chuyên sâu; quản lý tài chính dựa trên doanh thu đơn hàng (`orders`), chi phí vận hành (`expenses`) và nhập hàng (`purchase_orders`).

## Field THIẾU - CẦN BỔ SUNG
- `expenses.category`: Phân loại rõ để bóc tách OPEX và chi phí Marketing trên bảng P&L.
- `orders.paymentStatus`: Đóng vai trò quyết định chênh lệch giữa Dồn tích (mọi đơn đã tạo) và Dòng tiền thực tế (chỉ đơn có `paymentStatus = 'paid'`).
