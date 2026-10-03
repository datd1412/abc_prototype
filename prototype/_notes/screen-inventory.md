# Checklist Tiến Độ Màn Hình (Screen Inventory)

File này là **nguồn sự thật kiểm soát tiến độ build** của toàn bộ 50+ màn hình/component từ `stitch_ai_business_copilot_platform/`.

## 1. Danh sách Màn hình chính có Prefix (bo_XX, se_XX, sa_XX)

| Đã build | Slug chính thức | Folder Desktop (Giữ) | Folder Bỏ (Mobile / Sub-form) | Portal | Ghi chú & Delta |
|:---:|---|---|---|---|---|
| ☑ | `bo-quan-ly-doanh-nghiep` | `bo_01_qu_n_l_doanh_nghi_p_c_u_h_nh_v_n_h_nh` | *(Không có)* | Business Owner (`bo-`) | Quản lý doanh nghiệp & cấu hình vận hành |
| ☑ | `bo-chi-phi` | `bo_02_qu_n_l_chi_ph_t_i_ch_nh_c_b_n` | `bo_02_ghi_nh_n_chi_ph_nhanh_qu_n_l_ng_n_s_ch_opex_mobile` | Business Owner (`bo-`) | Bản mobile bổ sung nút OCR Camera chụp hóa đơn. |
| ☑ | `bo-san-pham-danh-sach` | *(Chỉ có mobile)* | `bo_03_qu_n_l_s_n_ph_m_b_ng_gi` | Business Owner (`bo-`) | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |
| ☑ | `bo-kho-ton-kho` | `bo_04_qu_n_l_t_n_kho_ki_m_so_t_xu_t_nh_p` | `bo_04_ki_m_tra_t_n_kho_nhanh_qu_t_m_fefo_mobile` | Business Owner (`bo-`) | Bản mobile bổ sung nút quét Barcode/QR Camera. |
| ☑ | `bo-tong-quan` | `bo_05_b_o_c_o_t_ng_quan_dashboard_kpi_doanh_nghi_p` | `bo_05_b_o_c_o_dashboard_kpi_doanh_nghi_p_mobile` | Business Owner (`bo-`) | Tương đồng nội dung, tối ưu layout Desktop. |
| ☑ | `bo-don-hang` | `bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh` | `bo_06_form_t_o_n_h_ng_m_i_xu_t_kho_a_k_nh`, `bo_06_qu_n_l_n_h_ng_v_n_h_nh_a_k_nh_mobile` | Business Owner (`bo-`) | Sub-form/Detail `bo_06_form_t_o_n_h_ng_m_i_xu_t_kho_a_k_nh` được tích hợp vào Form Drawer. |
| ☑ | `bo-ai-phan-tich` | `bo_07_ai_business_analytics_ph_n_t_ch_hi_u_su_t_a_chi_u` | *(Không có)* | Business Owner (`bo-`) | AI Business Analytics phân tích hiệu suất |
| ☑ | `bo-ai-canh-bao` | *(Chỉ có mobile)* | `bo_08_ai_anomaly_detection_trung_t_m_c_nh_b_o_r_i_ro_th_i_gian_th_c` | Business Owner (`bo-`) | Màn hình thiết kế mobile-first. Cần dựng bản Desktop theo Component Contract. |
| ☑ | `bo-ai-du-bao` |  | `bo_09_ai_demand_forecasting_replenishment_planning`, `bo_09_ai_demand_forecasting_replenishment_planning_mobile_summary` | Business Owner (`bo-`) | Tương đồng nội dung, tối ưu layout Desktop. |
| ☑ | `bo-ai-mo-phong` | `bo_10_m_ph_ng_k_ch_b_n_kinh_doanh_what_if_scenario_lab` | *(Không có)* | Business Owner (`bo-`) | Phòng thí nghiệm kịch bản kinh doanh What-If |
| ☑ | `bo-ai-copilot` | `bo_11_ai_business_advisor_tr_l_chi_n_l_c_c_level` | `bo_11_ai_business_advisor_tr_l_chi_n_l_c_c_level_mobile` | Business Owner (`bo-`) | Bản Desktop có thêm panel bằng chứng bên phải. |
| ☑ | `sa-cau-hinh-he-thong` | `sa_01_qu_n_tr_h_th_ng_c_u_h_nh_n_n_t_ng_system_administrator_master_console` | *(Không)* | System Admin (`sa-`) | Tương đồng nội dung, tối ưu layout Desktop. |
| ☑ | `sa-quan-ly-doanh-nghiep` | `sa_02_qu_n_l_doanh_nghi_p_multi_tenant_governance_console` | *(Không có)* | System Admin (`sa-`) | Quản lý doanh nghiệp Multi-tenant Governance |
| ☑ | `sa-an-ninh-he-thong` | `sa_03_qu_n_l_c_u_h_nh_h_th_ng_ng_ng_an_ninh_v_n_h_nh` | *(Không có)* | System Admin (`sa-`) | Quản lý cấu hình động & an ninh hệ thống |
| ☑ | `sa-audit-log` | `sa_04_nh_t_k_audit_trail_ki_m_to_n_b_o_m_t_truy_v_t_s_c` | *(Không có)* | System Admin (`sa-`) | Audit Trail nhật ký kiểm toán & truy vết |
| ☑ | `se-ban-hang` | `se_01_ghi_nh_n_giao_d_ch_b_n_h_ng_pos_store_employee_pos_terminal` | *(Không có)* | Store Employee (`se-`) | Ghi nhận giao dịch bán hàng POS Terminal |
| ☑ | `se-kiem-ke-ton-kho` | `se_02_ki_m_k_t_n_kho_qu_y_qu_n_l_l_h_n_d_ng_fefo` | *(Không có)* | Store Employee (`se-`) | Kiểm kê tồn kho quầy & hạn dùng FEFO |
| ☑ | `se-nhap-kho` | `se_03_ghi_nh_n_h_ng_nh_p_kho_qu_y_store_inward_goods_receiving_inventory_intake` | *(Không)* | Store Employee (`se-`) | Ghi nhận hàng nhập kho quầy & tiếp nhận lô hàng |
| ☑ | `se-tra-cuu-san-pham` | `se_04_tra_c_u_xem_th_ng_tin_s_n_ph_m_b_n_h_ng_product_directory_sales_reference` | *(Không)* | Store Employee (`se-`) | Tra cứu thông tin sản phẩm & bảng giá bán lẻ |
| ☑ | `se-giao-ca` | `se_03_giao_ca_k_t_s_b_n_h_ng_cashier_shift_handover_drawer_settlement` | *(Không)* | Store Employee (`se-`) | Giao ca kết sổ bán hàng cashier shift handover |
| ☑ | `se-doi-tra-hang` | `se_04_x_l_i_tr_h_ng_ho_n_ti_n_b_o_h_nh_t_i_qu_y_pos` | *(Không)* | Store Employee (`se-`) | Xử lý đổi trả hàng & hoàn tiền tại quầy POS |

## 2. Danh sách Sub-screens, Modals & Component không có Prefix

| Đã build | Slug đề xuất | Folder Stitch gốc | Portal | Mô tả nội dung |
|:---:|---|---|---|---|
| ☑ | `bo-ai-copilot-tro-ly` | `ai_copilot_tr_l_quy_t_nh` | Business Owner (`bo-`) | AI Copilot trợ lý ra quyết định |
| ☑ | `bo-ai-canh-bao-realtime` | `ai_insights_ph_t_hi_n_b_t_th_ng_th_i_gian_th_c` | Business Owner (`bo-`) | AI Insights phát hiện bất thường real-time |
| ☑ | `bo-dong-tien-detail` | `b_o_c_o_l_i_l_p_l_chi_ti_t_accrual_vs_cashflow` | Business Owner (`bo-`) | Báo cáo P&L dồn tích vs Dòng tiền thực tế |
| ☑ | `bo-tong-quan-cua-hang` | `b_o_c_o_t_ng_quan_ch_c_a_h_ng` | Business Owner (`bo-`) | Báo cáo tổng quan chủ cửa hàng |
| ☑ | `bo-quan-ly-nhan-vien` | `c_i_t_ph_n_quy_n_qu_n_l_nh_n_vi_n` | Business Owner (`bo-`) | Quản lý nhân viên & Ma trận phân quyền RBAC |
| ☑ | `sa-master-console` | `c_ng_qu_n_tr_h_th_ng_to_n_n_ng_system_administrator_sa_console` | System Admin (`sa-`) | Console quản trị hệ thống toàn năng SA |
| ☑ | `bo-ai-du-bao-goi-y-nhap` | `d_b_o_c_u_g_i_nh_p_h_ng_ai` | Business Owner (`bo-`) | Dự báo cầu & Gợi ý nhập hàng AI |
| ☑ | `bo-thanh-toan-doi-soat-san` | `i_so_t_chi_ti_t_v_s_n_shopee_tiktok_shop` | Business Owner (`bo-`) | Đối soát chi tiết ví sàn TMĐT Shopee/TikTok |
| ☑ | `bo-ai-mo-phong-whatif` | `m_ph_ng_k_ch_b_n_kinh_doanh_what_if` | Business Owner (`bo-`) | Mô phỏng kịch bản kinh doanh What-If |
| ☑ | `bo-ai-mo-phong-dong-tien` | `m_ph_ng_k_ch_b_n_what_if_d_ng_ti_n_p_l_c_thanh_kho_n` | Business Owner (`bo-`) | Mô phỏng kịch bản What-If dòng tiền & thanh khoản |
| ☑ | `bo-modal-po-draft-preview-1` | `modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_1` | Business Owner / Modal | Modal xem trước & phê duyệt PO Draft |
| ☑ | `bo-modal-po-draft-preview-2` | `modal_chi_ti_t_xem_tr_c_n_t_h_ng_po_draft_preview_2` | Business Owner / Modal | Modal dự báo & gợi ý nhập hàng PO Mega 11.11 |
| ☑ | `bo-modal-phieu-chi-vietqr` | `modal_l_p_phi_u_chi_ti_n_qu_t_vietqr_b2b_cashflow_p_l` | Business Owner / Modal | Modal lập phiếu chi tiền & VietQR B2B |
| ☑ | `bo-modal-phieu-thu-ban-si` | `modal_l_p_phi_u_thu_ti_n_b_n_s_i_t_c_i_l_cashflow_p_l` | Business Owner / Modal | Modal lập phiếu thu tiền bán sỉ / đại lý |
| ☑ | `bo-modal-nhap-kho-po-1` | `modal_nh_p_kho_kh_i_t_o_l_date_po_1` | Business Owner / Modal | Modal khởi tạo lô date & phiếu nhập kho PO 1 |
| ☑ | `bo-modal-nhap-kho-po-2` | `modal_nh_p_kho_kh_i_t_o_l_date_po_2` | Business Owner / Modal | Modal khởi tạo lô date & phiếu nhập kho PO 2 |
| ☑ | `bo-modal-nhap-kho-po-3` | `modal_nh_p_kho_kh_i_t_o_l_date_po_3` | Business Owner / Modal | Modal khởi tạo lô date & phiếu nhập kho PO 3 |
| ☑ | `bo-modal-them-nhan-vien-rbac` | `modal_th_m_nh_n_vi_n_m_i_g_n_ph_n_quy_n_rbac` | Business Owner / Modal | Modal thêm nhân viên mới & gán quyền RBAC |
| ☑ | `bo-modal-thanh-toan-cong-no-vietqr` | `modal_thanh_to_n_c_ng_n_qu_t_vietqr_b2b_h_ng_lo_t` | Business Owner / Modal | Modal thanh toán công nợ hàng loạt VietQR B2B |
| ☑ | `bo-don-hang-pos-da-kenh` | `qu_n_l_n_h_ng_pos_b_n_l_a_k_nh` | Business Owner (`bo-`) | Hub quản lý đơn hàng & POS bán lẻ đa kênh |
| ☑ | `bo-nha-cung-cap-cong-no` | `qu_n_l_nh_cung_c_p_c_ng_n_n_h_ng` | Business Owner (`bo-`) | Quản lý nhà cung cấp & công nợ đơn hàng |
| ☑ | `bo-san-pham-bien-the-kho` | `qu_n_l_s_n_ph_m_bi_n_th_kho_l_m_ph_m` | Business Owner (`bo-`) | Quản lý sản phẩm, biến thể & kho lô mỹ phẩm |
| ☑ | `bo-ai-retail-pulse` | `retail_intelligence_pulse` | Business Owner (`bo-`) | Báo cáo Retail Intelligence Pulse |
| ☑ | `bo-chi-phi-so-thu-chi` | `s_thu_chi_d_ng_ti_n_th_c_t_cashflow_p_l` | Business Owner (`bo-`) | Sổ thu chi & quản trị dòng tiền thực tế |