// prototype/_shared/nav-owner.js — dùng cho mọi màn thuộc portal Business Owner (prefix bo-)
const ABC_NAV = [
  { label: "Tổng quan", slug: "bo-tong-quan" },
  { label: "Sản phẩm", children: [
      { label: "Danh sách sản phẩm", slug: "bo-san-pham-danh-sach" },
      { label: "Danh mục", slug: "bo-san-pham-danh-muc" },
      { label: "Nhà cung cấp", slug: "bo-nha-cung-cap" },
  ]},
  { label: "Kho", children: [
      { label: "Tồn kho", slug: "bo-kho-ton-kho" },
      { label: "Lô hàng & hạn dùng", slug: "bo-kho-lo-hang" },
      { label: "Điều chỉnh tồn kho", slug: "bo-kho-dieu-chinh" },
  ]},
  { label: "Bán hàng", children: [
      { label: "Đơn hàng", slug: "bo-don-hang" },
      { label: "Khách hàng", slug: "bo-khach-hang" },
      { label: "Thanh toán", slug: "bo-thanh-toan" },
  ]},
  { label: "Tài chính", children: [
      { label: "Chi phí", slug: "bo-chi-phi" },
      { label: "Dòng tiền", slug: "bo-dong-tien" },
  ]},
  { label: "AI Insights", children: [
      { label: "Copilot", slug: "bo-ai-copilot" },
      { label: "Phân tích kinh doanh", slug: "bo-ai-phan-tich" },
      { label: "Cảnh báo bất thường", slug: "bo-ai-canh-bao" },
      { label: "Dự báo nhu cầu", slug: "bo-ai-du-bao" },
      { label: "Inventory Intelligence", slug: "bo-ai-ton-kho-thong-minh" },
      { label: "Mô phỏng What-if", slug: "bo-ai-mo-phong" },
  ]},
  // ĐÃ SỬA: chỉ còn "Nhân viên & phân quyền" — Audit log/Cấu hình hệ thống
  // KHÔNG thuộc Business Owner, chuyển sang portal System Admin (nav-admin.js).
  { label: "Quản lý", slug: "bo-quan-ly-nhan-vien" },
];

(function renderNav() {
  const activeSlug = document.body.dataset.screen || "";
  const container = document.getElementById("app-topnav");
  if (!container) { console.error("nav-owner.js: thiếu <div id=\"app-topnav\"></div>"); return; }
  function isActive(item) {
    if (item.slug === activeSlug) return true;
    if (item.children) return item.children.some(c => c.slug === activeSlug);
    return false;
  }
  const html = ABC_NAV.map(item => {
    const activeClass = isActive(item) ? " nav-menu-active" : "";
    if (!item.children) return `<a class="nav-menu-item${activeClass}" href="${item.slug}.html">${item.label}</a>`;
    const dropdown = item.children.map(c => {
      const childActive = c.slug === activeSlug ? " nav-dropdown-active" : "";
      return `<a class="nav-dropdown-item${childActive}" href="${c.slug}.html">${c.label}</a>`;
    }).join("");
    return `<div class="nav-menu-group${activeClass}"><span class="nav-menu-item">${item.label} ▾</span><div class="nav-dropdown">${dropdown}</div></div>`;
  }).join("");
  container.innerHTML = `<div class="topnav-brand">ABC Copilot — Business Owner</div><nav class="topnav-menu">${html}</nav>`;
})();
