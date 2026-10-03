/**
 * Navigation JS for Store Employee Portal (se-*)
 * Injects topnav header dynamically into <header id="app-topnav"></header>
 */
(function initEmployeeNav() {
  const currentSlug = document.body.getAttribute('data-screen') || '';

  const navConfig = [
    {
      title: "Bán hàng ▾",
      children: [
        { label: "Bán hàng POS", slug: "se-ban-hang" },
        { label: "Giao ca & kết sổ", slug: "se-giao-ca" },
        { label: "Đổi trả & hoàn tiền", slug: "se-doi-tra-hang" }
      ]
    },
    {
      title: "Kho ▾",
      children: [
        { label: "Kiểm kê tồn kho", slug: "se-kiem-ke-ton-kho" },
        { label: "Ghi nhận nhập kho", slug: "se-nhap-kho" }
      ]
    },
    { title: "Sản phẩm", slug: "se-tra-cuu-san-pham" }
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
        <a href="se-ban-hang.html" class="brand-logo">
          <div class="brand-icon" style="background: var(--color-success);">SE</div>
          <span>ABC Copilot — POS Employee</span>
        </a>
        ${menuHtml}
      </div>
      <div class="top-nav-right">
        <div class="user-profile">
          <span>Lê Văn Nam</span>
          <span class="role-badge" style="background: rgba(31, 157, 85, 0.3); color: #86efac; border-color: rgba(31, 157, 85, 0.5);">Store Employee</span>
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
