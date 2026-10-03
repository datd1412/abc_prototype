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

# Report generation
report_lines = []
report_lines.append("# Báo cáo Tổng hợp & Phân loại Folder Stitch Gốc\n")

report_lines.append("## 1. Màn hình có Prefix (bo_XX, se_XX, sa_XX)\n")
report_lines.append("| Số hiệu | Bản giữ (Desktop) | Bản bỏ (Mobile / Form / Duplicate) | Chênh lệch nội dung (Delta) nếu có |")
report_lines.append("|---|---|---|---|")

for prefix, items in sorted(groups.items()):
    desktops = [it for it in items if not it["is_mobile"]]
    mobiles = [it for it in items if it["is_mobile"]]
    
    # If no desktop or multiple desktops, analyze carefully
    if len(items) == 1:
        it = items[0]
        f = it["folder"]
        if it["is_mobile"]:
            report_lines.append(f"| **{prefix}** | *(Chỉ có bản mobile)* | `{f}` | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |")
        else:
            report_lines.append(f"| **{prefix}** | `{f}` | *(Không có)* | Bản Desktop duy nhất. |")
    else:
        # Multiple folders in group
        keep_folder = ""
        discard_folders = []
        delta_info = []
        
        # Check specific duplicates
        desktop_item = None
        for it in items:
            f = it["folder"]
            if it["is_mobile"] or "mobile" in f.lower():
                discard_folders.append(f"`{f}`")
            elif "form" in f.lower() or "chi_tiet" in f.lower():
                discard_folders.append(f"`{f}` (Sub-form/Detail view)")
                delta_info.append(f"Folder `{f}` chứa form/detail view riêng (sẽ đưa vào Form Drawer).")
            else:
                keep_folder = f"`{f}`"
                desktop_item = it
        
        if not keep_folder and desktops:
            keep_folder = f"`{desktops[0]['folder']}`"
            desktop_item = desktops[0]
            discard_folders = [f"`{it['folder']}`" for it in items if it != desktops[0]]
            
        # Detail delta extraction
        for it in items:
            f = it["folder"]
            if "mobile" in f.lower():
                delta_info.append(f"Bản mobile `{f}` tối ưu layout hẹp; nội dung field tương đồng.")
        
        delta_str = "<br>".join(delta_info) if delta_info else "Nội dung tương đồng, khác biệt về layout mobile/desktop."
        discard_str = ", ".join(discard_folders) if discard_folders else "*(Không)*"
        
        report_lines.append(f"| **{prefix}** | {keep_folder} | {discard_str} | {delta_str} |")

report_lines.append("\n## 2. Folder KHÔNG có Prefix (bo_/se_/sa_)\n")
report_lines.append("| Tên Folder | Tóm tắt Nội dung Màn hình | Đề xuất Portal (FR Alignment) |")
report_lines.append("|---|---|---|")

portal_proposals = {
    "ai_copilot_tr_l_quy_t_nh": ("Màn hình AI Copilot hỏi đáp trợ lý ra quyết định", "Business Owner (`bo-ai-copilot`)"),
    "ai_insights_ph_t_hi_n_b_t_th_ng_th_i_gian_th_c": ("Trung tâm phát hiện bất thường & cảnh báo rủi ro real-time", "Business Owner (`bo-ai-canh-bao`)"),
    "b_o_c_o_l_i_l_p_l_chi_ti_t_accrual_vs_cashflow": ("Báo cáo chi tiết P&L dồn tích vs Dòng tiền thực tế", "Business Owner (`bo-dong-tien`)"),
    "b_o_c_o_t_ng_quan_ch_c_a_h_ng": ("Dashboard tổng quan hiệu suất cửa hàng", "Business Owner (`bo-tong-quan`)"),
    "c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n": ("Quản lý nhân viên & Ma trận phân quyền RBAC", "Business Owner (`bo-quan-ly-nhan-vien`)"),
    "c_ng_qu_n_tr_h_th_ng_to_n_n_ng_system_administrator_sa_console": ("Console quản trị toàn năng System Administrator", "System Admin (`sa-cau-hinh-he-thong`)"),
    "d_b_o_c_u_g_i_nh_p_h_ng_ai": ("Trung tâm dự báo cầu & gợi ý nhập hàng tự động AI", "Business Owner (`bo-ai-du-bao`)"),
    "i_so_t_chi_ti_t_v_s_n_shopee_tiktok_shop": ("Đối soát chi tiết ví sàn TMĐT (Shopee, TikTok Shop)", "Business Owner (`bo-thanh-toan`)"),
    "m_ph_ng_k_ch_b_n_kinh_doanh_what_if": ("Phòng thí nghiệm kịch bản kinh doanh What-If", "Business Owner (`bo-ai-mo-phong`)"),
    "m_ph_ng_k_ch_b_n_what_if_d_ng_ti_n_p_l_c_thanh_kho_n": ("Mô phỏng áp lực dòng tiền & tối ưu thanh khoản", "Business Owner (`bo-ai-mo-phong`)"),
    "modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_1": ("Modal xem trước & phê duyệt đơn đặt hàng PO Draft", "Business Owner / Component Modal"),
    "modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_2": ("Modal dự báo & gợi ý nhập hàng PO Mega 11.11", "Business Owner / Component Modal"),
    "modal_l_p_phi_u_chi_ti_n_qu_t_vietqr_b2b_cashflow_p_l": ("Modal lập phiếu chi tiền & VietQR B2B", "Business Owner (`bo-chi-phi`) / Modal"),
    "modal_l_p_phi_u_thu_ti_n_b_n_s_i_t_c_i_l_cashflow_p_l": ("Modal lập phiếu thu tiền bán sỉ / đại lý", "Business Owner (`bo-thanh-toan`) / Modal"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_1": ("Modal khởi tạo lô date & phiếu nhập kho PO (1)", "Business Owner (`bo-kho-lo-hang`) / Modal"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_2": ("Modal khởi tạo lô date & phiếu nhập kho PO (2)", "Business Owner (`bo-kho-lo-hang`) / Modal"),
    "modal_nh_p_kho_kh_i_t_o_l_date_po_3": ("Modal khởi tạo lô date & phiếu nhập kho PO (3)", "Business Owner (`bo-kho-lo-hang`) / Modal"),
    "modal_th_m_nh_n_vi_n_m_i_g_n_ph_n_quy_n_rbac": ("Modal thêm nhân viên mới & gán quyền RBAC", "Business Owner (`bo-quan-ly-nhan-vien`) / Modal"),
    "modal_thanh_to_n_c_ng_n_qu_t_vietqr_b2b_h_ng_lo_t": ("Modal thanh toán công nợ hàng loạt VietQR B2B", "Business Owner (`bo-thanh-toan`) / Modal"),
    "qu_n_l_n_h_ng_pos_b_n_l_a_k_nh": ("Hub quản lý đơn hàng & POS đa kênh", "Business Owner (`bo-don-hang`) hoặc Store Employee (`se-ban-hang`)"),
    "qu_n_l_nh_cung_c_p_c_ng_n_n_h_ng": ("Quản lý nhà cung cấp & công nợ đơn hàng", "Business Owner (`bo-nha-cung-cap`)"),
    "qu_n_l_s_n_ph_m_bi_n_th_kho_l_m_ph_m": ("Quản lý sản phẩm, biến thể & kho lô mỹ phẩm FEFO", "Business Owner (`bo-san-pham-danh-sach`)"),
    "retail_intelligence_pulse": ("Báo cáo Retail Intelligence Pulse & xu hướng bán", "Business Owner (`bo-ai-phan-tich`)"),
    "s_thu_chi_d_ng_ti_n_th_c_t_cashflow_p_l": ("Sổ thu chi & quản trị dòng tiền thực tế", "Business Owner (`bo-chi-phi` / `bo-dong-tien`)")
}

for it in non_prefixed:
    f = it["folder"]
    summary, proposal = portal_proposals.get(f, ("Màn hình chức năng bổ trợ", "Cần xác định theo nội dung"))
    report_lines.append(f"| `{f}` | {summary} | {proposal} |")

report_content = "\n".join(report_lines)
with open(r"d:\prototype\abc-prototype\prototype\stitch_inventory_report.md", "w", encoding="utf-8") as out:
    out.write(report_content)

print("Report generated successfully: stitch_inventory_report.md")
