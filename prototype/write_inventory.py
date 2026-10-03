import os
import json
import re

with open(r"d:\prototype\abc-prototype\prototype\stitch_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

base_dir = r"d:\prototype\stitch_ai_business_copilot_platform"

groups = {}
non_prefixed = []

for item in data:
    name = item["folder"]
    match = re.match(r'^(bo_\d+|se_\d+|sa_\d+)', name)
    if match:
        prefix = match.group(1)
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append(item)
    else:
        non_prefixed.append(item)

# Mapping slug & portal for prefixed screens
prefix_slug_map = {
    "bo_01": ("bo-tong-quan-vanchanh", "Business Owner (`bo-`)", "Quản lý doanh nghiệp & cấu hình vận hành"),
    "bo_02": ("bo-chi-phi", "Business Owner (`bo-`)", "Quản lý chi phí & ngân sách OPEX"),
    "bo_03": ("bo-san-pham-danh-sach", "Business Owner (`bo-`)", "Quản lý sản phẩm & bảng giá"),
    "bo_04": ("bo-kho-ton-kho", "Business Owner (`bo-`)", "Quản lý tồn kho & kiểm soát xuất nhập FEFO"),
    "bo_05": ("bo-tong-quan", "Business Owner (`bo-`)", "Dashboard tổng quan KPI doanh nghiệp"),
    "bo_06": ("bo-don-hang", "Business Owner (`bo-`)", "Quản lý đơn hàng vận hành đa kênh"),
    "bo_07": ("bo-ai-phan-tich", "Business Owner (`bo-`)", "AI Business Analytics phân tích hiệu suất"),
    "bo_08": ("bo-ai-canh-bao", "Business Owner (`bo-`)", "AI Anomaly Detection trung tâm cảnh báo rủi ro"),
    "bo_09": ("bo-ai-du-bao", "Business Owner (`bo-`)", "AI Demand Forecasting & Replenishment"),
    "bo_10": ("bo-ai-mo-phong", "Business Owner (`bo-`)", "Phòng thí nghiệm kịch bản kinh doanh What-If"),
    "bo_11": ("bo-ai-copilot", "Business Owner (`bo-`)", "AI Business Advisor trợ lý chiến lược C-Level"),
    "sa_01": ("sa-cau-hinh-he-thong", "System Admin (`sa-`)", "Quản trị hệ thống & IAM RBAC Console"),
    "sa_02": ("sa-quan-ly-doanh-nghiep", "System Admin (`sa-`)", "Quản lý doanh nghiệp Multi-tenant Governance"),
    "sa_03": ("sa-an-ninh-he-thong", "System Admin (`sa-`)", "Quản lý cấu hình động & an ninh hệ thống"),
    "sa_04": ("sa-audit-log", "System Admin (`sa-`)", "Audit Trail nhật ký kiểm toán & truy vết"),
    "se_01": ("se-ban-hang", "Store Employee (`se-`)", "Ghi nhận giao dịch bán hàng POS Terminal"),
    "se_02": ("se-kiem-ke-ton-kho", "Store Employee (`se-`)", "Kiểm kê tồn kho quầy & hạn dùng FEFO"),
    "se_03": ("se-nhap-kho", "Store Employee (`se-`)", "Ghi nhận hàng nhập kho quầy & Giao ca thu ngân"),
    "se_04": ("se-tra-cuu-san-pham", "Store Employee (`se-`)", "Tra cứu sản phẩm & Xử lý đổi trả hàng POS")
}

non_prefixed_map = {
    "ai_copilot_tr_l_quy_t_nh": ("bo-ai-copilot-tro-ly", "Business Owner (`bo-`)", "AI Copilot trợ lý ra quyết định"),
    "ai_insights_ph_t_hi_n_b_t_th_ng_th_i_gian_th_c": ("bo-ai-canh-bao-realtime", "Business Owner (`bo-`)", "AI Insights phát hiện bất thường real-time"),
    "b_o_c_o_l_i_l_p_l_chi_ti_t_accrual_vs_cashflow": ("bo-dong-tien-detail", "Business Owner (`bo-`)", "Báo cáo P&L dồn tích vs Dòng tiền thực tế"),
    "b_o_c_o_t_ng_quan_ch_c_a_h_ng": ("bo-tong-quan-cua-hang", "Business Owner (`bo-`)", "Báo cáo tổng quan chủ cửa hàng"),
    "c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n": ("bo-quan-ly-nhan-vien", "Business Owner (`bo-`)", "Quản lý nhân viên & Ma trận phân quyền RBAC"),
    "c_ng_qu_n_tr_h_th_ng_to_n_n_ng_system_administrator_sa_console": ("sa-master-console", "System Admin (`sa-`)", "Console quản trị hệ thống toàn năng SA"),
    "d_b_o_c_u_g_i_nh_p_h_ng_ai": ("bo-ai-du-bao-goi-y-nhap", "Business Owner (`bo-`)", "Dự báo cầu & Gợi ý nhập hàng AI"),
    "i_so_t_chi_ti_t_v_s_n_shopee_tiktok_shop": ("bo-thanh-toan-doi-soat-san", "Business Owner (`bo-`)", "Đối soát chi tiết ví sàn TMĐT Shopee/TikTok"),
    "m_ph_ng_k_ch_b_n_kinh_doanh_what_if": ("bo-ai-mo-phong-whatif", "Business Owner (`bo-`)", "Mô phỏng kịch bản kinh doanh What-If"),
    "m_ph_ng_k_ch_b_n_what_if_d_ng_ti_n_p_l_c_thanh_kho_n": ("bo-ai-mo-phong-dong-tien", "Business Owner (`bo-`)", "Mô phỏng kịch bản What-If dòng tiền & thanh khoản"),
    "modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_1": ("bo-modal-po-draft-preview-1", "Business Owner / Modal", "Modal xem trước & phê duyệt PO Draft"),
    "modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_2": ("bo-modal-po-draft-preview-2", "Business Owner / Modal", "Modal dự báo & gợi ý nhập hàng PO Mega 11.11"),
    "modal_l_p_phi_u_chi_ti_n_qu_t_vietqr_b2b_cashflow_p_l": ("bo-modal-phieu-chi-vietqr", "Business Owner / Modal", "Modal lập phiếu chi tiền & VietQR B2B"),
    "modal_l_p_phi_u_thu_ti_n_b_n_s_i_t_c_i_l_cashflow_p_l": ("bo-modal-phieu-thu-ban-si", "Business Owner / Modal", "Modal lập phiếu thu tiền bán sỉ / đại lý"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_1": ("bo-modal-nhap-kho-po-1", "Business Owner / Modal", "Modal khởi tạo lô date & phiếu nhập kho PO 1"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_2": ("bo-modal-nhap-kho-po-2", "Business Owner / Modal", "Modal khởi tạo lô date & phiếu nhập kho PO 2"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_3": ("bo-modal-nhap-kho-po-3", "Business Owner / Modal", "Modal khởi tạo lô date & phiếu nhập kho PO 3"),
    "modal_th_m_nh_n_vi_n_m_i_g_n_ph_n_quy_n_rbac": ("bo-modal-them-nhan-vien-rbac", "Business Owner / Modal", "Modal thêm nhân viên mới & gán quyền RBAC"),
    "modal_thanh_to_n_c_ng_n_qu_t_vietqr_b2b_h_ng_lo_t": ("bo-modal-thanh-toan-cong-no-vietqr", "Business Owner / Modal", "Modal thanh toán công nợ hàng loạt VietQR B2B"),
    "qu_n_l_n_h_ng_pos_b_n_l_a_k_nh": ("bo-don-hang-pos-da-kenh", "Business Owner (`bo-`)", "Hub quản lý đơn hàng & POS bán lẻ đa kênh"),
    "qu_n_l_nh_cung_c_p_c_ng_n_n_h_ng": ("bo-nha-cung-cap-cong-no", "Business Owner (`bo-`)", "Quản lý nhà cung cấp & công nợ đơn hàng"),
    "qu_n_l_s_n_ph_m_bi_n_th_kho_l_m_ph_m": ("bo-san-pham-bien-the-kho", "Business Owner (`bo-`)", "Quản lý sản phẩm, biến thể & kho lô mỹ phẩm"),
    "retail_intelligence_pulse": ("bo-ai-retail-pulse", "Business Owner (`bo-`)", "Báo cáo Retail Intelligence Pulse"),
    "s_thu_chi_d_ng_ti_n_th_c_t_cashflow_p_l": ("bo-chi-phi-so-thu-chi", "Business Owner (`bo-`)", "Sổ thu chi & quản trị dòng tiền thực tế")
}

lines = []
lines.append("# Checklist Tiến Độ Màn Hình (Screen Inventory)")
lines.append("\nFile này là **nguồn sự thật kiểm soát tiến độ build** của toàn bộ 50+ màn hình/component từ `stitch_ai_business_copilot_platform/`.\n")

lines.append("## 1. Danh sách Màn hình chính có Prefix (bo_XX, se_XX, sa_XX)\n")
lines.append("| Đã build | Slug chính thức | Folder Desktop (Giữ) | Folder Bỏ (Mobile / Sub-form) | Portal | Ghi chú & Delta |")
lines.append("|:---:|---|---|---|---|---|")

for prefix, items in sorted(groups.items()):
    slug, portal, desc = prefix_slug_map.get(prefix, (f"{prefix.replace('_', '-')}-screen", "Business Owner (`bo-`)", "Màn hình nghiệp vụ"))
    
    # Check if built
    is_built = "☑" if slug == "bo-san-pham-danh-sach" else "☐"
    
    desktops = [it for it in items if not it["is_mobile"]]
    mobiles = [it for it in items if it["is_mobile"]]
    
    if len(items) == 1:
        it = items[0]
        f = it["folder"]
        if it["is_mobile"]:
            lines.append(f"| {is_built} | `{slug}` | *(Chỉ có mobile)* | `{f}` | {portal} | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |")
        else:
            lines.append(f"| {is_built} | `{slug}` | `{f}` | *(Không có)* | {portal} | {desc} |")
    else:
        keep_folder = ""
        discard_folders = []
        delta_info = []
        
        for it in items:
            f = it["folder"]
            if it["is_mobile"] or "mobile" in f.lower():
                discard_folders.append(f"`{f}`")
                if "bo_02" in f:
                    delta_info.append("Bản mobile bổ sung nút OCR Camera chụp hóa đơn.")
                elif "bo_04" in f:
                    delta_info.append("Bản mobile bổ sung nút quét Barcode/QR Camera.")
                elif "bo_11" in f:
                    delta_info.append("Bản Desktop có thêm panel bằng chứng bên phải.")
            elif "form" in f.lower() or "chi_tiet" in f.lower():
                discard_folders.append(f"`{f}`")
                delta_info.append(f"Sub-form/Detail `{f}` được tích hợp vào Form Drawer.")
            else:
                keep_folder = f"`{f}`"
                
        if not keep_folder and desktops:
            keep_folder = f"`{desktops[0]['folder']}`"
            discard_folders = [f"`{it['folder']}`" for it in items if it != desktops[0]]
            
        delta_str = " ".join(delta_info) if delta_info else "Tương đồng nội dung, tối ưu layout Desktop."
        discard_str = ", ".join(discard_folders) if discard_folders else "*(Không)*"
        
        lines.append(f"| {is_built} | `{slug}` | {keep_folder} | {discard_str} | {portal} | {delta_str} |")

lines.append("\n## 2. Danh sách Sub-screens, Modals & Component không có Prefix\n")
lines.append("| Đã build | Slug đề xuất | Folder Stitch gốc | Portal | Mô tả nội dung |")
lines.append("|:---:|---|---|---|---|")

for it in non_prefixed:
    f = it["folder"]
    slug, portal, desc = non_prefixed_map.get(f, (f"bo-{f.replace('_', '-')}", "Business Owner (`bo-`)", "Component bổ trợ"))
    is_built = "☑" if slug == "bo-san-pham-danh-sach" else "☐"
    lines.append(f"| {is_built} | `{slug}` | `{f}` | {portal} | {desc} |")

content = "\n".join(lines)
with open(r"d:\prototype\abc-prototype\prototype\_notes\screen-inventory.md", "w", encoding="utf-8") as out:
    out.write(content)

print("Screen inventory created successfully.")
