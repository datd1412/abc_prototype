/**
 * Navigation JS for Business Owner Portal (bo-*)
 * Injects topnav header dynamically into <header id="app-topnav"></header>
 */
(function initOwnerNav() {
  const currentSlug = document.body.getAttribute('data-screen') || '';

  const navConfig = [
    {
      title: "Tổng quan ▾",
      children: [
        { label: "Dashboard Doanh nghiệp", slug: "bo-tong-quan" },
        { label: "Vận hành Cửa hàng", slug: "bo-tong-quan-cua-hang" }
      ]
    },
    {
      title: "Sản phẩm ▾",
      children: [
        { label: "Danh sách sản phẩm", slug: "bo-san-pham-danh-sach" },
        { label: "Sản phẩm & Kho lô FEFO", slug: "bo-san-pham-bien-the-kho" },
        { label: "Danh mục sản phẩm", slug: "bo-san-pham-danh-muc" },
        { label: "Nhà cung cấp & Công nợ", slug: "bo-nha-cung-cap-cong-no" }
      ]
    },
    {
      title: "Kho ▾",
      children: [
        { label: "Tồn kho", slug: "bo-kho-ton-kho" },
        { label: "Lô hàng & hạn dùng", slug: "bo-kho-lo-hang" },
        { label: "Điều chỉnh tồn kho", slug: "bo-kho-dieu-chinh" }
      ]
    },
    {
      title: "Bán hàng ▾",
      children: [
        { label: "Đơn hàng", slug: "bo-don-hang" },
        { label: "Hub Đơn hàng Đa kênh", slug: "bo-don-hang-pos-da-kenh" },
        { label: "Khách hàng", slug: "bo-khach-hang" },
        { label: "Thanh toán", slug: "bo-thanh-toan" }
      ]
    },
    {
      title: "Tài chính ▾",
      children: [
        { label: "Chi phí", slug: "bo-chi-phi" },
        { label: "Sổ thu chi & Cashflow", slug: "bo-chi-phi-so-thu-chi" },
        { label: "Báo cáo P&L & Dòng tiền", slug: "bo-dong-tien-detail" },
        { label: "Đối soát ví sàn TMĐT", slug: "bo-thanh-toan-doi-soat-san" }
      ]
    },
    {
      title: "AI Insights ▾",
      children: [
        { label: "AI Copilot", slug: "bo-ai-copilot" },
        { label: "AI Trợ lý ra quyết định", slug: "bo-ai-copilot-tro-ly" },
        { label: "AI Retail Intelligence Pulse", slug: "bo-ai-retail-pulse" },
        { label: "AI Phân tích kinh doanh", slug: "bo-ai-phan-tich" },
        { label: "AI Cảnh báo bất thường", slug: "bo-ai-canh-bao" },
        { label: "AI Cảnh báo Real-time", slug: "bo-ai-canh-bao-realtime" },
        { label: "AI Dự báo nhu cầu", slug: "bo-ai-du-bao" },
        { label: "AI Gợi ý nhập hàng & ROP", slug: "bo-ai-du-bao-goi-y-nhap" },
        { label: "AI Inventory Intelligence", slug: "bo-ai-ton-kho-thong-minh" },
        { label: "AI Mô phỏng What-if", slug: "bo-ai-mo-phong" },
        { label: "AI Thử nghiệm Kịch bản What-If", slug: "bo-ai-mo-phong-whatif" },
        { label: "AI Mô phỏng Dòng tiền & Thanh khoản", slug: "bo-ai-mo-phong-dong-tien" }
      ]
    },
    {
      title: "Quản lý ▾",
      children: [
        { label: "Cấu hình doanh nghiệp", slug: "bo-quan-ly-doanh-nghiep" },
        { label: "Nhân viên & phân quyền", slug: "bo-quan-ly-nhan-vien" }
      ]
    }
  ];

  function renderNav() {
    const headerEl = document.getElementById('app-topnav');
    if (!headerEl) return;

    headerEl.className = 'top-header';

    let menuHtml = '<ul class="top-menu">';
    navConfig.forEach(item => {
      if (item.children) {
        const isChildActive = item.children.some(c => c.slug === currentSlug);
        menuHtml += `<li class="menu-item ${isChildActive ? 'active' : ''}">
          <a href="#" class="menu-link">${item.title}</a>
          <div class="dropdown-menu">`;
        item.children.forEach(c => {
          const isActive = c.slug === currentSlug;
          menuHtml += `<a href="${c.slug}.html" class="dropdown-item ${isActive ? 'active' : ''}">${c.label}</a>`;
        });
        menuHtml += `</div></li>`;
      } else {
        const isActive = item.slug === currentSlug;
        menuHtml += `<li class="menu-item ${isActive ? 'active' : ''}">
          <a href="${item.slug}.html" class="menu-link">${item.title}</a>
        </li>`;
      }
    });
    menuHtml += '</ul>';

    headerEl.innerHTML = `
      <div class="top-nav-left">
        <a href="bo-tong-quan.html" class="brand-logo">
          <div class="brand-icon">A</div>
          <span>ABC Copilot</span>
        </a>
        ${menuHtml}
      </div>
      <div class="top-nav-right">
        <div class="user-profile">
          <span>Nguyễn Thị Mai</span>
          <span class="role-badge">Business Owner</span>
        </div>
      </div>
    `;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderNav);
  } else {
    renderNav();
  }
})();
