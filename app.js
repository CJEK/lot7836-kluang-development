const languages = {
  zh: {
    'nav.overview': '项目总览',
    'nav.recommended': '主推方案',
    'nav.styles': '3套风格比较',
    'nav.drawings': '2D 概念图集',
    'nav.budget': '造价拆解',
    'action.print': '打印提案',
    'action.share': '分享链接',
    'menu.aria': '切换导航菜单',
    'hero.title': '50 × 75ft 现代热带 Container Loft Bungalow 完整开发提案',
    'hero.lead': '正面 50ft 面宽 × 75ft 进深 (3,750 sqft) | 双 40ft High Cube 集装箱 + 34ft 挑高大厅 + 900sqft 二层 Loft 阁楼 | 包含开放式厨房、双卫生间与集中排水管线。',
    'hero.notice': '概念设计提案，所有结构、消防、排水及退缩最终须由注册建筑师 (Ar.)、P.Eng 及主管机构 (MPK/BOMBA/IWK) 确认。',
    'recommended.title': '主推：马六甲 Batu Angin 风砖屏风度假风',
    'recommended.text': '采用 Batu Angin 通风花砖双层防热墙、30° 高坡斜屋顶与中央 Raised Jack Roof 拔风天窗 (+47ft 顶高)，利用热浮力自然对流排热，配合 50mm PU 隔热包覆，打造自然降温 3-5°C 的热带仓储别墅。',
    'recommended.reviewTitle': '专业设计与工程控制要点',
    'recommended.reviewText': '• 布局：左右侧摆 2 个 40ft HC 集装箱 (各 8ft 宽)，中间打通 34ft 挑高大厅。\n• 水电：左集装箱后段设开放式厨房与油脂拦截器，右集装箱设双卫生间集中排污至后方 8PE 化粪池。\n• 结构：集装箱切口全围焊接 100x100mm 方钢圈补强，地面 150mm 加厚混凝土地坪。',
    'styles.title': '3 套独立度假风外观与室内 3D 效果图',
    'styles.text': '每套风格均受同一设计控制线约束（50x75ft 占地、双 40ft HC、34ft 大厅、30° 屋顶）。点击任意图片均可全屏高清放大查看。',
    'styles.controls': '共享控制线：2 × 40ft HC 集装箱, 34ft 中厅, 35ft 后区 Loft, 30° 屋顶 (+24\' 檐高 / +38\'-5" 屋脊 / +47\' 拔风塔顶)。',
    'drawings.title': '2D 概念工程示意图集 (点击图片全屏查看)',
    'drawings.text': '包含 7 张标准 AutoCAD 工程规图（平面图、立面图、集装箱切割 Detail、厨房排水图、BOMBA 消防图、T&C 测试图、总平面图）。点击任意图纸均可放大查看细节。',
    'drawings.notice': '注：本图集为概念工程示意图，点击图纸即可放大查看细节，不提供文件下载。',
    'budget.title': 'RM400k – RM450k 精准预算拆解',
    'budget.text': '通过模组化集装箱改造与柱网优化节约 30% 结构资金，重投入于地坪基坑、防热拔风与防水管线。',
    'budget.foundation': '150mm 工业加厚地坪与基坑工程',
    'budget.structure': '集装箱改造、切割加固与钢骨架',
    'budget.loft': '900sqft Mezzanine Loft 阁楼与楼梯',
    'budget.roof': '30° 坡屋面、PU 隔热板与拔风塔',
    'budget.mep': '厨房排水、双厕湿区、生化化粪池与三相电',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. 概念设计提案。',
    'image.style2.front': '风格 2 外观 3D 全景',
    'image.gif': '风格 2 0-1 集装箱改造施工动画'
  },
  en: {
    'nav.overview': 'Overview',
    'nav.recommended': 'Recommended',
    'nav.styles': '3 Style Studies',
    'nav.drawings': '2D Drawings',
    'nav.budget': 'Budget Plan',
    'action.print': 'Print',
    'action.share': 'Share',
    'menu.aria': 'Toggle Menu',
    'hero.title': '50 × 75ft Modern Tropical Container Loft Bungalow Proposal',
    'hero.lead': '50ft Frontage × 75ft Depth (3,750 sqft) | Twin 40ft HC Containers + 34ft Hall + 900sqft Loft | Integrated Kitchen & Wet-Core Drainage.',
    'hero.notice': 'Conceptual proposal. All structure, fire safety, drainage and setbacks subject to Ar. / P.Eng / MPK / BOMBA / IWK review.',
    'recommended.title': 'Recommended: Batu Angin Breeze Block Resort Style',
    'recommended.text': 'Featuring Batu Angin breeze block double-skin facade, 30° pitched roof and Raised Jack Roof monitor (+47ft peak), using thermal buoyancy for passive cooling (3-5°C temperature reduction).',
    'recommended.reviewTitle': 'Design & Engineering Highlights',
    'recommended.reviewText': '• Layout: Two 40ft HC containers on sides, opening a 34ft high-ceiling central hall.\n• Plumbing: Open kitchen with grease trap on left; twin restrooms on right connecting to rear 8PE septic tank.\n• Structure: Cut-outs reinforced with 100x100mm RHS steel frames on 150mm concrete slab.',
    'styles.title': '3 Distinct Architectural & Interior 3D Renders',
    'styles.text': 'All 3 style packages follow the exact same design controls. Click any image to view in full-screen Lightbox.',
    'styles.controls': 'Shared Controls: 2 × 40ft HC, 34ft Hall, 35ft Rear Loft, 30° Roof (+24\' Eave / +38\'-5" Ridge / +47\' Jack Roof).',
    'drawings.title': '2D Conceptual Drawing Set (Click to View Fullscreen)',
    'drawings.text': 'Complete set of 7 AutoCAD-standard engineering diagrams. Click any card to inspect drawing details.',
    'drawings.notice': 'Note: Conceptual diagrams only. Click any drawing to view fullscreen.',
    'budget.title': 'RM400k – RM450k Budget Breakdown',
    'budget.text': 'Optimized container modularity saves 30% structural cost, re-invested into foundation, heat insulation and waterproofing.',
    'budget.foundation': '150mm Concrete Slab & Substructure',
    'budget.structure': 'Container Conversion & Steel Frame',
    'budget.loft': '900sqft Mezzanine Loft & Stair',
    'budget.roof': '30° Roof, PU Insulation & Jack Roof Monitor',
    'budget.mep': 'Kitchen Drainage, Restrooms, Septic Tank & Electrical',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. Conceptual Proposal.',
    'image.style2.front': 'Style 2 Exterior 3D Render',
    'image.gif': 'Style 2 Container Build Sequence GIF'
  }
};

const styles = [
  { key: 'style2', name: ['风格 2 · 马六甲 Batu Angin 风砖屏风墙 (推荐主推)', 'Style 2 · Batu Angin Screen Wall (Recommended)'], front: 'assets/style2-ext.jpg?v=9', interior: 'assets/style2-int.jpg?v=9', side: 'assets/style2-side.jpg?v=9', rear: 'assets/style2-rear.jpg?v=9' },
  { key: 'style1', name: ['风格 1 · 居銮赤陶红现代热带风', 'Style 1 · Terracotta Modern Tropical'], front: 'assets/style1-ext.jpg?v=9', interior: 'assets/style1-int.jpg?v=9', side: 'assets/style1-side.jpg?v=9', rear: 'assets/style1-rear.jpg?v=9' },
  { key: 'style3', name: ['风格 3 · 南洋纯白复古谷仓风', 'Style 3 · Nanyang White Barn'], front: 'assets/style3-ext.jpg?v=9', interior: 'assets/style3-int.jpg?v=9', side: 'assets/style3-side.jpg?v=9', rear: 'assets/style3-rear.jpg?v=9' }
];

const drawings = [
  ['A-101', ['DWG A-101 2D 建筑平面图', 'DWG A-101 Floor Plan'], ['50x75ft 地块、双 40ft HC 集装箱、34ft 挑高大厅与后区 35ft 阁楼平面布局。', '50x75ft footprint, twin 40ft HC containers, 34ft hall and rear loft.'], 'assets/floorplan-bp.jpg?v=9'],
  ['A-102', ['DWG A-102 建筑正立面图', 'DWG A-102 Elevation'], ['控制标高：+24ft 主屋檐、+38ft-5in 主屋脊与 +47ft 拔风塔顶，30° 坡屋顶结构。', 'Level controls: +24ft eave, +38ft-5in ridge and +47ft Jack Roof.'], 'assets/elevation-bp.jpg?v=9'],
  ['S-101', ['DWG S-101 集装箱切割加固 Detail', 'DWG S-101 Container Detail'], ['侧墙切割开窗、切口周圈 100x100x4.5mm RHS 方钢框焊接与 M20 锚栓加固。', '100x100x4.5mm RHS steel frame reinforcement & M20 anchor bolts.'], 'assets/container_splicing_blueprint.jpg?v=9'],
  ['M-101', ['DWG M-101 厨房与集中排水图', 'DWG M-101 Kitchen & Drainage'], ['左集装箱 25ft 厨房、50L 油脂拦截器、DN100 黑水管(1:40坡度)及 8PE 化粪池。', 'Kitchen grease trap, DN100 blackwater pipe (1:40 slope) & 8PE septic tank.'], 'assets/kitchen_drainage_blueprint.jpg?v=9'],
  ['F-101', ['DWG F-101 BOMBA 消防逃生图', 'DWG F-101 Fire & Egress Plan'], ['SD1-SD6 烟感、FE1-FE4 灭火器、1.5m 门净宽、Loft 第二逃生梯及疏散路线。', 'SD1-SD6 detectors, FE1-FE4 extinguishers, 1.5m exit doors & 2nd escape stair.'], 'assets/fire_safety_egress_blueprint.jpg?v=9'],
  ['T-101', ['DWG T-101 5 大工程打压测试图', 'DWG T-101 T&C Testing Plan'], ['8 Bar 给水打压、24h 湿区闭水、4h 屋顶高压喷淋及 30mA RCCB 漏电测试。', '8 Bar water pressure, 24h flood test, 4h roof spray & 30mA RCCB tests.'], 'assets/G-101', ['DWG G-101 总平面规划图', 'DWG G-101 Site Plan'], ['Jalan Pakis 正面沿街、指北针、40x50ft 建筑占地、15ft 前退缩、10ft 后退缩及 U 型排水沟。', 'Jalan Pakis frontage, 40x50ft footprint, 15ft front & 10ft rear setbacks.'], 'assets/siteplan-bp.jpg?v=9']
];

function language() { return document.documentElement.dataset.language || 'zh'; }

function renderCards() {
  const lang = language();
  const isZh = lang === 'zh';
  const frontLabel = isZh ? '正面全景 3D 图' : 'Front 3D View';
  const intLabel = isZh ? '室内挑高大厅 3D 图' : 'Interior 3D View';
  const sideLabel = isZh ? '75ft 侧立面 3D 图' : '75ft Side View';
  const rearLabel = isZh ? '45° 轴测全景 3D 图' : '45° Rear View';
  const viewFull = isZh ? '🔍 点击全屏放大查看' : '🔍 Click to view full screen';

  const styleGrid = document.getElementById('style-grid');
  if (styleGrid) {
    styleGrid.innerHTML = styles.map(style => `
      <article class="style-card" style="margin-bottom: 32px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
        <h3 style="font-size: 1.25rem; margin-top: 0; margin-bottom: 16px; color: #0f172a;">${style.name[isZh ? 0 : 1]}</h3>
        <div class="image-pair" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          <button class="image-button" data-image="${style.front}" data-caption="${style.name[isZh ? 0 : 1]} — ${frontLabel}" style="background:none; border:none; padding:0; cursor:pointer; text-align:left;">
            <div style="position:relative; overflow:hidden; border-radius:10px; aspect-ratio:16/9;">
              <img src="${style.front}" alt="${frontLabel}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
              <span style="position:absolute; bottom:8px; right:8px; background:rgba(0,0,0,0.7); color:#fff; padding:4px 10px; border-radius:6px; font-size:0.75rem;">${frontLabel}</span>
            </div>
          </button>
          <button class="image-button" data-image="${style.side}" data-caption="${style.name[isZh ? 0 : 1]} — ${sideLabel}" style="background:none; border:none; padding:0; cursor:pointer; text-align:left;">
            <div style="position:relative; overflow:hidden; border-radius:10px; aspect-ratio:16/9;">
              <img src="${style.side}" alt="${sideLabel}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
              <span style="position:absolute; bottom:8px; right:8px; background:rgba(0,0,0,0.7); color:#fff; padding:4px 10px; border-radius:6px; font-size:0.75rem;">${sideLabel}</span>
            </div>
          </button>
          <button class="image-button" data-image="${style.rear}" data-caption="${style.name[isZh ? 0 : 1]} — ${rearLabel}" style="background:none; border:none; padding:0; cursor:pointer; text-align:left;">
            <div style="position:relative; overflow:hidden; border-radius:10px; aspect-ratio:16/9;">
              <img src="${style.rear}" alt="${rearLabel}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
              <span style="position:absolute; bottom:8px; right:8px; background:rgba(0,0,0,0.7); color:#fff; padding:4px 10px; border-radius:6px; font-size:0.75rem;">${rearLabel}</span>
            </div>
          </button>
          <button class="image-button" data-image="${style.interior}" data-caption="${style.name[isZh ? 0 : 1]} — ${intLabel}" style="background:none; border:none; padding:0; cursor:pointer; text-align:left;">
            <div style="position:relative; overflow:hidden; border-radius:10px; aspect-ratio:16/9;">
              <img src="${style.interior}" alt="${intLabel}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
              <span style="position:absolute; bottom:8px; right:8px; background:rgba(0,0,0,0.7); color:#fff; padding:4px 10px; border-radius:6px; font-size:0.75rem;">${intLabel}</span>
            </div>
          </button>
        </div>
      </article>`).join('');
  }

  const drawingGrid = document.getElementById('drawing-grid');
  if (drawingGrid) {
    drawingGrid.innerHTML = drawings.map(([number, title, description, hdSrc]) => `
      <article class="drawing-card image-button" data-image="${hdSrc || `assets/drawings/${number.toLowerCase()}-preview.png?v=9`}" data-caption="${number} ${title[isZh ? 0 : 1]}" style="cursor:pointer; background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:16px; transition: transform 0.2s;">
        <div style="position:relative; aspect-ratio:1.42; overflow:hidden; border-radius:8px; margin-bottom:12px;">
          <img src="assets/drawings/${number.toLowerCase()}-preview.png?v=9" alt="${number}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
          <span style="position:absolute; top:8px; left:8px; background:#0284c7; color:#fff; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">${number}</span>
        </div>
        <h3 style="font-size:1.05rem; margin:0 0 6px; color:#0f172a;">${title[isZh ? 0 : 1]}</h3>
        <p style="font-size:0.85rem; color:#64748b; margin:0 0 10px; line-height:1.5;">${description[isZh ? 0 : 1]}</p>
        <div style="color:#0284c7; font-size:0.82rem; font-weight:600; display:flex; align-items:center; gap:4px;">
          ${viewFull}
        </div>
      </article>`).join('');
  }
}

function setLanguage(next) {
  const dictionary = languages[next];
  if (!dictionary) return;
  document.documentElement.dataset.language = next;
  document.documentElement.lang = next === 'zh' ? 'zh-CN' : 'en';
  document.querySelectorAll('[data-i18n]').forEach(el => { if (dictionary[el.dataset.i18n]) el.textContent = dictionary[el.dataset.i18n]; });
  document.querySelectorAll('[data-i18n-alt]').forEach(el => { if (dictionary[el.dataset.i18nAlt]) el.alt = dictionary[el.dataset.i18nAlt]; });
  document.querySelectorAll('[data-i18n-title]').forEach(el => { if (dictionary[el.dataset.i18nTitle]) el.title = dictionary[el.dataset.i18nTitle]; });
  
  const menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) menuToggle.setAttribute('aria-label', dictionary['menu.aria']);

  document.querySelectorAll('.language-btn').forEach(btn => {
    const active = btn.dataset.lang === next;
    btn.classList.toggle('active', active);
    btn.setAttribute('aria-pressed', String(active));
  });

  localStorage.setItem('lot7836-language', next);
  renderCards();
}

function openLightbox(src, caption) {
  const modal = document.getElementById('lightbox');
  const modalImg = document.getElementById('lightbox-img');
  const modalCaption = document.getElementById('lightbox-caption');

  if (modal && modalImg) {
    modalImg.src = src;
    if (modalCaption) modalCaption.textContent = caption || 'Lot 7836 Architectural Detail';
    if (typeof modal.showModal === 'function') {
      modal.showModal();
    } else {
      modal.classList.add('active');
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  setLanguage(localStorage.getItem('lot7836-language') || 'zh');
  document.querySelectorAll('.language-btn').forEach(btn => btn.addEventListener('click', () => setLanguage(btn.dataset.lang)));
  
  const menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', event => {
      const open = document.body.classList.toggle('menu-open');
      event.currentTarget.setAttribute('aria-expanded', String(open));
    });
  }

  document.querySelectorAll('.nav-links a').forEach(link => link.addEventListener('click', () => document.body.classList.remove('menu-open')));
  
  document.addEventListener('click', event => {
    const card = event.target.closest('.image-button');
    if (card && card.dataset.image) {
      openLightbox(card.dataset.image, card.dataset.caption);
    }
  });

  const dialogClose = document.querySelector('.dialog-close');
  if (dialogClose) {
    dialogClose.addEventListener('click', () => {
      const modal = document.getElementById('lightbox');
      if (modal) {
        if (typeof modal.close === 'function') modal.close();
        else modal.classList.remove('active');
      }
    });
  }

  const printBtn = document.querySelector('[data-action="print"]');
  if (printBtn) printBtn.addEventListener('click', () => window.print());

  const shareBtn = document.querySelector('[data-action="share"]');
  if (shareBtn) {
    shareBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(location.href);
        alert(language() === 'zh' ? '分享链接已复制。' : 'Share link copied.');
      } catch {
        prompt(language() === 'zh' ? '复制此链接：' : 'Copy this link:', location.href);
      }
    });
  }
});
