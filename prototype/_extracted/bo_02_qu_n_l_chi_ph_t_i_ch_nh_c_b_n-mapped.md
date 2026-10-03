# BO-02: Quản lý Chi phí & Tài chính Cơ bản — đã đối chiếu ERD/FR & Content Density

Nguồn: `abc-prototype/prototype/_extracted/bo_02_qu_n_l_chi_ph_t_i_ch_nh_c_b_n.md`

## 1. Field GIỮ (Phân loại theo Content Density Rule)

### Primary Fields (Hiển thị trực tiếp trên List View — Cột bảng nhóm chi phí):
- `expense_categories.name` → Nhóm chi phí (Tên danh mục chi phí)
- `expense_categories.description` → Mô tả nhóm chi phí
- `expenses.amount` → Số tiền chi thực tế
- `expense_categories.status` → Trạng thái nhóm chi phí

### Secondary Fields (CHỈ hiển thị trong Form Panel / Slide-Over Drawer khi click xem/sửa khoản chi):
- `expenses.title` → Tiêu đề khoản chi chi tiết
- `expenses.expenseDate` → Ngày ghi nhận chi
- `expenses.description` → Diễn giải nội dung khoản chi
- `expenses.createdBy` → Người ghi nhận khoản chi
- `expenses.metadata` → Dữ liệu bổ trợ JSON

---

## 2. Field LOẠI
- `OCR scan hóa đơn tự động`: LOẠI — Không có entity/field OCR hóa đơn trong ERD `SEP490_entities_fields.txt`.
- `Nhà cung cấp gắn trực tiếp vào Expense`: LOẠI — Không có quan hệ trực tiếp giữa entity `expenses` và `suppliers`.

---

## 3. Navigation Placement
- Vị trí IA: Menu **Tài chính** ▾ → Item: **Chi phí** (Portal Business Owner: `bo-chi-phi`).
