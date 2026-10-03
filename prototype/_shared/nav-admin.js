/**
 * Navigation JS for System Administrator Portal (sa-*)
 * Injects topnav header dynamically into <header id="app-topnav"></header>
 */
(function initAdminNav() {
  const currentSlug = document.body.getAttribute('data-screen') || '';

  const navConfig = [
    { title: "Master Console", slug: "sa-master-console" },
    { title: "Cấu hình hệ thống", slug: "sa-cau-hinh-he-thong" },
    { title: "Doanh nghiệp", slug: "sa-quan-ly-doanh-nghiep" },
    { title: "An ninh hệ thống", slug: "sa-an-ninh-he-thong" },
    { title: "Audit Log", slug: "sa-audit-log" }
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
        <a href="sa-master-console.html" class="brand-logo">
          <div class="brand-icon" style="background: var(--color-danger);">SA</div>
          <span>ABC Copilot — Admin Console</span>
        </a>
        ${menuHtml}
      </div>
      <div class="top-nav-right">
        <div class="user-profile">
          <span>Trần Hoàng Long</span>
          <span class="role-badge" style="background: rgba(214, 69, 69, 0.3); color: #fca5a5; border-color: rgba(214, 69, 69, 0.5);">System Admin</span>
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
