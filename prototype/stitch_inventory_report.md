# Báo cáo Tổng hợp & Phân loại Folder Stitch Gốc

## 1. Màn hình có Prefix (bo_XX, se_XX, sa_XX)

| Số hiệu | Bản giữ (Desktop) | Bản bỏ (Mobile / Form / Duplicate) | Chênh lệch nội dung (Delta) nếu có |
|---|---|---|---|
| **bo_01** | `bo_01_qu_n_l_doanh_nghi_p_c_u_h_nh_v_n_h_nh` | *(Không có)* | Bản Desktop duy nhất. |
| **bo_02** | `bo_02_qu_n_l_chi_ph_t_i_ch_nh_c_b_n` | `bo_02_ghi_nh_n_chi_ph_nhanh_qu_n_l_ng_n_s_ch_opex_mobile` | Bản mobile `bo_02_ghi_nh_n_chi_ph_nhanh_qu_n_l_ng_n_s_ch_opex_mobile` tối ưu layout hẹp; nội dung field tương đồng. |
| **bo_03** | *(Chỉ có bản mobile)* | `bo_03_qu_n_l_s_n_ph_m_b_ng_gi` | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |
| **bo_04** | `bo_04_qu_n_l_t_n_kho_ki_m_so_t_xu_t_nh_p` | `bo_04_ki_m_tra_t_n_kho_nhanh_qu_t_m_fefo_mobile` | Bản mobile `bo_04_ki_m_tra_t_n_kho_nhanh_qu_t_m_fefo_mobile` tối ưu layout hẹp; nội dung field tương đồng. |
| **bo_05** | `bo_05_b_o_c_o_t_ng_quan_dashboard_kpi_doanh_nghi_p` | `bo_05_b_o_c_o_dashboard_kpi_doanh_nghi_p_mobile` | Bản mobile `bo_05_b_o_c_o_dashboard_kpi_doanh_nghi_p_mobile` tối ưu layout hẹp; nội dung field tương đồng. |
| **bo_06** | `bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh` | `bo_06_form_t_o_n_h_ng_m_i_xu_t_kho_a_k_nh` (Sub-form/Detail view), `bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh_mobile` | Folder `bo_06_form_t_o_n_h_ng_m_i_xu_t_kho_a_k_nh` chứa form/detail view riêng (sẽ đưa vào Form Drawer).<br>Bản mobile `bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh_mobile` tối ưu layout hẹp; nội dung field tương đồng. |
| **bo_07** | `bo_07_ai_business_analytics_ph_n_t_ch_hi_u_su_t_a_chi_u` | *(Không có)* | Bản Desktop duy nhất. |
| **bo_08** | *(Chỉ có bản mobile)* | `bo_08_ai_anomaly_detection_trung_t_m_c_nh_b_o_r_i_ro_th_i_gian_th_c` | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |
| **bo_09** |  | `bo_09_ai_demand_forecasting_replenishment_planning`, `bo_09_ai_demand_forecasting_replenishment_planning_mobile_summary` | Bản mobile `bo_09_ai_demand_forecasting_replenishment_planning_mobile_summary` tối ưu layout hẹp; nội dung field tương đồng. |
| **bo_10** | `bo_10_m_ph_ng_k_ch_b_n_kinh_doanh_what_if_scenario_lab` | *(Không có)* | Bản Desktop duy nhất. |
| **bo_11** | `bo_11_ai_business_advisor_tr_l_chi_n_l_c_c_level` | `bo_11_ai_business_advisor_tr_l_chi_n_l_c_c_level_mobile` | Bản mobile `bo_11_ai_business_advisor_tr_l_chi_n_l_c_c_level_mobile` tối ưu layout hẹp; nội dung field tương đồng. |
| **sa_01** | `sa_01_qu_n_tr_h_th_ng_c_u_h_nh_n_n_t_ng_system_administrator_master_console` | *(Không)* | Nội dung tương đồng, khác biệt về layout mobile/desktop. |
| **sa_02** | `sa_02_qu_n_l_doanh_nghi_p_multi_tenant_governance_console` | *(Không có)* | Bản Desktop duy nhất. |
| **sa_03** | `sa_03_qu_n_l_c_u_h_nh_h_th_ng_ng_ng_an_ninh_v_n_h_nh` | *(Không có)* | Bản Desktop duy nhất. |
| **sa_04** | `sa_04_nh_t_k_audit_trail_ki_m_to_n_b_o_m_t_truy_v_t_s_c` | *(Không có)* | Bản Desktop duy nhất. |
| **se_01** | `se_01_ghi_nh_n_giao_d_ch_b_n_h_ng_pos_store_employee_pos_terminal` | *(Không có)* | Bản Desktop duy nhất. |
| **se_02** | `se_02_ki_m_k_t_n_kho_qu_y_qu_n_l_l_h_n_d_ng_fefo` | *(Không có)* | Bản Desktop duy nhất. |
| **se_03** | `se_03_giao_ca_k_t_s_b_n_h_ng_cashier_shift_handover_drawer_settlement` | *(Không)* | Nội dung tương đồng, khác biệt về layout mobile/desktop. |
| **se_04** | `se_04_x_l_i_tr_h_ng_ho_n_ti_n_b_o_h_nh_t_i_qu_y_pos` | *(Không)* | Nội dung tương đồng, khác biệt về layout mobile/desktop. |

## 2. Folder KHÔNG có Prefix (bo_/se_/sa_)

| Tên Folder | Tóm tắt Nội dung Màn hình | Đề xuất Portal (FR Alignment) |
|---|---|---|
| `ai_copilot_tr_l_quy_t_nh` | Màn hình AI Copilot hỏi đáp trợ lý ra quyết định | Business Owner (`bo-ai-copilot`) |
| `ai_insights_ph_t_hi_n_b_t_th_ng_th_i_gian_th_c` | Trung tâm phát hiện bất thường & cảnh báo rủi ro real-time | Business Owner (`bo-ai-canh-bao`) |
| `b_o_c_o_l_i_l_p_l_chi_ti_t_accrual_vs_cashflow` | Báo cáo chi tiết P&L dồn tích vs Dòng tiền thực tế | Business Owner (`bo-dong-tien`) |
| `b_o_c_o_t_ng_quan_ch_c_a_h_ng` | Dashboard tổng quan hiệu suất cửa hàng | Business Owner (`bo-tong-quan`) |
| `c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n` | Quản lý nhân viên & Ma trận phân quyền RBAC | Business Owner (`bo-quan-ly-nhan-vien`) |
| `c_ng_qu_n_tr_h_th_ng_to_n_n_ng_system_administrator_sa_console` | Console quản trị toàn năng System Administrator | System Admin (`sa-cau-hinh-he-thong`) |
| `d_b_o_c_u_g_i_nh_p_h_ng_ai` | Trung tâm dự báo cầu & gợi ý nhập hàng tự động AI | Business Owner (`bo-ai-du-bao`) |
| `i_so_t_chi_ti_t_v_s_n_shopee_tiktok_shop` | Đối soát chi tiết ví sàn TMĐT (Shopee, TikTok Shop) | Business Owner (`bo-thanh-toan`) |
| `m_ph_ng_k_ch_b_n_kinh_doanh_what_if` | Phòng thí nghiệm kịch bản kinh doanh What-If | Business Owner (`bo-ai-mo-phong`) |
| `m_ph_ng_k_ch_b_n_what_if_d_ng_ti_n_p_l_c_thanh_kho_n` | Mô phỏng áp lực dòng tiền & tối ưu thanh khoản | Business Owner (`bo-ai-mo-phong`) |
| `modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_1` | Modal xem trước & phê duyệt đơn đặt hàng PO Draft | Business Owner / Component Modal |
| `modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_2` | Modal dự báo & gợi ý nhập hàng PO Mega 11.11 | Business Owner / Component Modal |
| `modal_l_p_phi_u_chi_ti_n_qu_t_vietqr_b2b_cashflow_p_l` | Modal lập phiếu chi tiền & VietQR B2B | Business Owner (`bo-chi-phi`) / Modal |
| `modal_l_p_phi_u_thu_ti_n_b_n_s_i_t_c_i_l_cashflow_p_l` | Modal lập phiếu thu tiền bán sỉ / đại lý | Business Owner (`bo-thanh-toan`) / Modal |
| `modal_nh_p_kho_kh_i_t_o_l_date_po_1` | Modal khởi tạo lô date & phiếu nhập kho PO (1) | Business Owner (`bo-kho-lo-hang`) / Modal |
| `modal_nh_p_kho_kh_i_t_o_l_date_po_2` | Modal khởi tạo lô date & phiếu nhập kho PO (2) | Business Owner (`bo-kho-lo-hang`) / Modal |
| `modal_nh_p_kho_kh_i_t_o_l_date_po_3` | Modal khởi tạo lô date & phiếu nhập kho PO (3) | Business Owner (`bo-kho-lo-hang`) / Modal |
| `modal_th_m_nh_n_vi_n_m_i_g_n_ph_n_quy_n_rbac` | Modal thêm nhân viên mới & gán quyền RBAC | Business Owner (`bo-quan-ly-nhan-vien`) / Modal |
| `modal_thanh_to_n_c_ng_n_qu_t_vietqr_b2b_h_ng_lo_t` | Modal thanh toán công nợ hàng loạt VietQR B2B | Business Owner (`bo-thanh-toan`) / Modal |
| `qu_n_l_n_h_ng_pos_b_n_l_a_k_nh` | Hub quản lý đơn hàng & POS đa kênh | Business Owner (`bo-don-hang`) hoặc Store Employee (`se-ban-hang`) |
| `qu_n_l_nh_cung_c_p_c_ng_n_n_h_ng` | Quản lý nhà cung cấp & công nợ đơn hàng | Business Owner (`bo-nha-cung-cap`) |
| `qu_n_l_s_n_ph_m_bi_n_th_kho_l_m_ph_m` | Quản lý sản phẩm, biến thể & kho lô mỹ phẩm FEFO | Business Owner (`bo-san-pham-danh-sach`) |
| `retail_intelligence_pulse` | Báo cáo Retail Intelligence Pulse & xu hướng bán | Business Owner (`bo-ai-phan-tich`) |
| `s_thu_chi_d_ng_ti_n_th_c_t_cashflow_p_l` | Sổ thu chi & quản trị dòng tiền thực tế | Business Owner (`bo-chi-phi` / `bo-dong-tien`) |