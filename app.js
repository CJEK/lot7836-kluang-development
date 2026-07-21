const languages = {
  zh: {
    'nav.overview': '项目总览',
    'nav.viewport': '3D 整体视角',
    'nav.recommended': '主推方案',
    'nav.styles': '3套风格比较',
    'nav.area': '空间面积表',
    'nav.gantt': '建造工期表',
    'nav.drawings': '2D 概念图集',
    'nav.compliance': '规范与测试',
    'nav.budget': '造价拆解',
    'action.print': '打印提案',
    'action.share': '分享链接',
    'menu.aria': '切换导航菜单',
    'hero.title': '50 × 75ft 现代热带 Container Loft Bungalow 完整开发提案',
    'hero.lead': '正面 50ft 大面宽 × 75ft 屋身进深 (3,750 sqft) | 双 40ft High Cube 集装箱 + 24ft 挑高大厅 (40ft 建筑面宽，满足两侧 5ft 退缩) + 750sqft 二层 Loft 阁楼 | 包含开放式厨房、双卫生间与集中排水管线。',
    'hero.notice': '概念设计提案，所有结构、消防、排水及退缩最终须由注册建筑师 (Ar.)、P.Eng 及主管机构 (MPK/BOMBA/IWK) 确认。',
    'recommended.title': '主推：马六甲 Batu Angin 风砖屏风度假风',
    'recommended.text': '采用 Batu Angin 通风花砖双层防热墙、30° 高坡斜屋顶与中央 Raised Jack Roof 拔风天窗 (+47ft 顶高)，利用热浮力自然对流排热，配合 50mm PU 隔热包覆，打造自然降温 3-5°C 的热带仓储别墅。',
    'recommended.reviewTitle': '专业设计与工程控制要点',
    'recommended.reviewText': '• 布局：左右侧摆 2 个 40ft HC 集装箱 (各 8ft 宽)，中间打通 24ft 挑高大厅 (总面宽 40ft，完美预留两侧 5ft 退缩)。\n• 水电：左集装箱后段设开放式厨房与油脂拦截器，右集装箱设双卫生间集中排污至后方 8PE 化粪池。\n• 结构：集装箱切口全围焊接 100x100mm 方钢圈补强，地面 150mm 加厚混凝土地坪。',
    'styles.title': '3 套独立度假风外观与室内 3D 效果图 (每套 4 视角无重复切图)',
    'styles.text': '每套风格均精细绘制 4 张完全独立、不重复的专属 3D 效果图（正面全景、75ft 侧立面、45° 轴测后方、室内大厅）。点击图片可左右全屏顺序切图。',
    'styles.controls': '共享控制线：2 × 40ft HC 集装箱, 24ft 中厅, 35ft 后区 Loft, 30° 屋顶 (+24\' 檐高 / +38\'-5" 屋脊 / +47\' 拔风塔顶)。',
    'drawings.title': '2D 概念工程示意图集 (点击图片全屏查看)',
    'drawings.text': '包含 9 张标准 AutoCAD 工程规图（平面图、立面图、集装箱切割 Detail、厨房排水图、BOMBA 消防图、T&C 测试图、总平面图、三相供电避雷图、地基防蚁防潮大样图）。点击任意图纸均可放大查看细节。',
    'drawings.notice': '注：本图集为概念工程示意图，点击图纸即可放大查看细节，不提供文件下载。',
    'budget.title': 'RM400k – RM450k 精准预算拆解与试算器',
    'budget.text': '通过模组化集装箱改造与柱网优化节约 30% 结构资金，重投入于地坪基坑、防热拔风与防水管线。',
    'budget.foundation': '150mm 工业加厚地坪与基坑工程',
    'budget.structure': '集装箱改造、切割加固与钢骨架',
    'budget.loft': '750sqft Mezzanine Loft 阁楼与楼梯',
    'budget.roof': '30° 坡屋面、PU 隔热板与拔风塔',
    'budget.mep': '厨房排水、双厕湿区、生化化粪池与三相电',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. 概念设计提案。',
    'image.style2.front': '风格 2 外观 3D 全景',
    'image.gif': '风格 2 0-1 集装箱改造施工动画'
  },
  en: {
    'nav.overview': 'Overview',
    'nav.viewport': '3D Viewports',
    'nav.recommended': 'Recommended',
    'nav.styles': '3 Style Studies',
    'nav.area': 'Area Schedule',
    'nav.gantt': 'Gantt Timeline',
    'nav.drawings': '2D Drawings',
    'nav.compliance': 'Compliance & T&C',
    'nav.budget': 'Budget Plan',
    'action.print': 'Print',
    'action.share': 'Share',
    'menu.aria': 'Toggle Menu',
    'hero.title': '50 × 75ft Modern Tropical Container Loft Bungalow Proposal',
    'hero.lead': '50ft Frontage × 75ft Depth (3,750 sqft) | Twin 40ft HC Containers + 24ft Hall (40ft Building Width, 5ft Side Setbacks) + 750sqft Loft | Integrated Kitchen & Wet-Core Drainage.',
    'hero.notice': 'Conceptual proposal. All structure, fire safety, drainage and setbacks subject to Ar. / P.Eng / MPK / BOMBA / IWK review.',
    'recommended.title': 'Recommended: Batu Angin Breeze Block Resort Style',
    'recommended.text': 'Featuring Batu Angin breeze block double-skin facade, 30° pitched roof and Raised Jack Roof monitor (+47ft peak), using thermal buoyancy for passive cooling (3-5°C temperature reduction).',
    'recommended.reviewTitle': 'Design & Engineering Highlights',
    'recommended.reviewText': '• Layout: Two 40ft HC containers on sides, opening a 24ft central hall (40ft total width for 5ft side setbacks).\n• Plumbing: Open kitchen with grease trap on left; twin restrooms on right connecting to rear 8PE septic tank.\n• Structure: Cut-outs reinforced with 100x100mm RHS steel frames on 150mm concrete slab.',
    'styles.title': '3 Distinct Architectural & Interior 3D Renders (4 Unique Angles Each)',
    'styles.text': 'Each style features 4 unique, non-duplicate 3D renders (Front, 75ft Side, 45° Rear, Interior). Click any image to slide left/right in Lightbox mode.',
    'styles.controls': 'Shared Controls: 2 × 40ft HC, 24ft Hall, 35ft Rear Loft, 30° Roof (+24\' Eave / +38\'-5" Ridge / +47\' Jack Roof).',
    'drawings.title': '2D Conceptual Drawing Set (Click to View Fullscreen)',
    'drawings.text': 'Complete set of 9 AutoCAD-standard engineering diagrams. Click any card to inspect drawing details.',
    'drawings.notice': 'Note: Conceptual diagrams only. Click any drawing to view fullscreen.',
    'budget.title': 'RM400k – RM450k Budget Breakdown & Estimator',
    'budget.text': 'Optimized container modularity saves 30% structural cost, re-invested into foundation, heat insulation and waterproofing.',
    'budget.foundation': '150mm Concrete Slab & Substructure',
    'budget.structure': 'Container Conversion & Steel Frame',
    'budget.loft': '750sqft Mezzanine Loft & Stair',
    'budget.roof': '30° Roof, PU Insulation & Jack Roof Monitor',
    'budget.mep': 'Kitchen Drainage, Restrooms, Septic Tank & Electrical',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. Conceptual Proposal.',
    'image.style2.front': 'Style 2 Exterior 3D Render',
    'image.gif': 'Style 2 Container Build Sequence GIF'
  }
};

const styles = [
  {
    key: 'style2',
    badge: 'STYLE 02 · RECOMMENDED MAIN FOCUS',
    name: ['🟢 风格 2 · 马六甲 Batu Angin 风砖屏风墙 (推荐主推)', 'Style 2 · Batu Angin Screen Wall (Recommended)'],
    materials: ['材质解构：橄榄森林绿 PU 隔热屋顶 + 赤陶与白色 Batu Angin 通风花砖屏风墙 + 暖沙色粗抹灰质感漆', 'Materials: Forest Green PU Roof + Terracotta/White Breeze Blocks + Warm Sand Stucco'],
    features: [
      '✅ 双层墙防热屏风 (Double-Skin Facade)：Batu Angin 通风花砖隔绝正午热辐射，降低室内温度 3-5°C。',
      '✅ 全天候穿堂风：利用风砖网格形成天然微风对流，大幅减少空调电费开支。',
      '✅ 度假村高级质感：粗抹灰结合热带绿植中庭，打造极其独特的现代奢华度假气质。'
    ],
    images: [
      { src: 'assets/style2-ext.jpg?v=26', label: ['1/4 正面 50ft 外观全景 (落座 150mm 地坪)', '1/4 Front Exterior 3D'] },
      { src: 'assets/style2-side.jpg?v=26', label: ['2/4 75ft 侧立面与服务排水 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style2-rear.jpg?v=26', label: ['3/4 45° 轴测后方全景与拔风塔 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style2-int.jpg?v=26', label: ['4/4 室内花砖日光中庭 3D 图', '4/4 Interior Atrium 3D'] }
    ]
  },
  {
    key: 'style1',
    badge: 'STYLE 01',
    name: ['🔴 风格 1 · 居銮赤陶红现代热带风', 'Style 1 · Terracotta Modern Tropical'],
    materials: ['材质解构：赤陶红高坡斜屋顶 + 米白色波纹钢板墙面 + 暖木色 WPC 木塑格栅 + 柚木百叶拔风塔', 'Materials: Terracotta Red Roof + Cream Corrugated Steel + Warm Wood WPC Louvers'],
    features: [
      '✅ 高耸拔风塔 (Jack Roof)：中央 Raised Monitor 天窗利用热浮力原理快速向上排出室内高空积热。',
      '✅ WPC 木塑格栅遮阳：暖木色格栅修饰开窗，兼顾隐私遮阳与传统马来 Kampung 建筑亲切感。',
      '✅ 挑高开放大厅：24ft 大面宽中央大厅结合裸露柚木屋架，室内视野极其开阔通透。'
    ],
    images: [
      { src: 'assets/style1-ext.jpg?v=26', label: ['1/4 正面 50ft 外观全景 (落座 150mm 地坪)', '1/4 Front Exterior 3D'] },
      { src: 'assets/style1-side.jpg?v=26', label: ['2/4 75ft 侧立面 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style1-rear.jpg?v=26', label: ['3/4 45° 轴测后方全景与拔风塔 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style1-int.jpg?v=26', label: ['4/4 室内挑高大厅 3D 图', '4/4 Interior Hall 3D'] }
    ]
  },
  {
    key: 'style3',
    badge: 'STYLE 03',
    name: ['⚪ 风格 3 · 南洋纯白复古谷仓风', 'Style 3 · Nanyang White Barn'],
    materials: ['材质解构：全纯白波纹金属板墙面与屋顶 (最高太阳反射率 SRI) + 深色柚木百叶推拉门扇', 'Materials: Pure White Corrugated Cladding (High SRI) + Dark Teak Plantation Shutters'],
    features: [
      '✅ 超高 SRI 太阳反射率：全纯白包覆高效反射太阳辐射热，大幅降低集装箱箱体吸热率。',
      '✅ 南洋殖民风采：深色柚木百叶推拉门与纯白谷仓轮廓形成优雅对比，极富南洋复古会所调性。',
      '✅ 极简明亮空间：室内双倍层高纯白钢桁架 ceiling 结合柚木地板，极简而富有质感。'
    ],
    images: [
      { src: 'assets/style3-ext.jpg?v=26', label: ['1/4 正面 50ft 外观全景 (落座 150mm 地坪)', '1/4 Front Exterior 3D'] },
      { src: 'assets/style3-side.jpg?v=26', label: ['2/4 75ft 侧立面 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style3-rear.jpg?v=26', label: ['3/4 45° 轴测后方全景与拔风塔 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style3-int.jpg?v=26', label: ['4/4 室内纯白大厅 3D 图', '4/4 Interior White Hall 3D'] }
    ]
  }
];

const drawings = [
  ['A-101', ['DWG A-101 2D 建筑平面图', 'DWG A-101 Floor Plan'], ['50x75ft 地块、双 40ft HC 集装箱、24ft 挑高大厅与后区 35ft 阁楼平面布局。', '50x75ft footprint, twin 40ft HC containers, 24ft hall and rear loft.'], 'assets/floorplan-bp.jpg?v=26'],
  ['A-102', ['DWG A-102 建筑正立面图', 'DWG A-102 Elevation'], ['控制标高：+24ft 主屋檐、+38ft-5in 主屋脊与 +47ft 拔风塔顶，30° 坡屋顶结构。', 'Level controls: +24ft eave, +38ft-5in ridge and +47ft Jack Roof.'], 'assets/elevation-bp.jpg?v=26'],
  ['S-101', ['DWG S-101 集装箱切割加固 Detail', 'DWG S-101 Container Detail'], ['侧墙切割开窗、切口周圈 100x100x4.5mm RHS 方钢框焊接与 M20 锚栓加固。', '100x100x4.5mm RHS steel frame reinforcement & M20 anchor bolts.'], 'assets/container_splicing_blueprint.jpg?v=26'],
  ['M-101', ['DWG M-101 厨房与集中排水图', 'DWG M-101 Kitchen & Drainage'], ['左集装箱 25ft 厨房、50L 油脂拦截器、DN100 黑水管(1:40坡度)及 8PE 化粪池。', 'Kitchen grease trap, DN100 blackwater pipe (1:40 slope) & 8PE septic tank.'], 'assets/kitchen_drainage_blueprint.jpg?v=26'],
  ['F-101', ['DWG F-101 BOMBA 消防逃生图', 'DWG F-101 Fire & Egress Plan'], ['SD1-SD6 烟感、FE1-FE4 灭火器、1.5m 门净宽、Loft 第二逃生梯及疏散路线。', 'SD1-SD6 detectors, FE1-FE4 extinguishers, 1.5m exit doors & 2nd escape stair.'], 'assets/fire_safety_egress_blueprint.jpg?v=26'],
  ['T-101', ['DWG T-101 5 大工程打压测试图', 'DWG T-101 T&C Testing Plan'], ['8 Bar 给水打压、24h 湿区闭水、4h 屋顶高压喷淋及 30mA RCCB 漏电测试。', '8 Bar water pressure, 24h flood test, 4h roof spray & 30mA RCCB tests.'], 'assets/tc_testing_blueprint.jpg?v=26'],
  ['G-101', ['DWG G-101 总平面规划图', 'DWG G-101 Site Plan'], ['Jalan Pakis 正面沿街、指北针、40x50ft 建筑占地、15ft 前退缩、10ft 后退缩及 U 型排水沟。', 'Jalan Pakis frontage, 40x50ft footprint, 15ft front & 10ft rear setbacks.'], 'assets/siteplan-bp.jpg?v=26'],
  ['E-101', ['DWG E-101 三相供电与避雷接地图', 'DWG E-101 Electrical & Solar'], ['TNB 3-Phase 63A 配电箱、30mA RCCB、+47ft 拔风塔纯铜避雷针与 10kW 光伏预留。', 'TNB 3-Phase 63A DB, 30mA RCCB, +47ft copper lightning rod & 10kW solar PV ready.'], 'assets/electrical_wiring_blueprint.jpg?v=26'],
  ['X-101', ['DWG X-101 地基防白蚁防潮剖面图', 'DWG X-101 Foundation & Spec'], ['150mm 地坪、0.2mm HDPE 防潮隔气膜、MS 828 防白蚁屏障与 Standing Seam 屋面大样。', '150mm slab, 0.2mm HDPE DPM, MS 828 anti-termite barrier & standing seam detail.'], 'assets/soil_termite_waterproof_blueprint.jpg?v=26']
];

let activeGallery = [];
let activeGalleryIndex = 0;

function language() { return document.documentElement.dataset.language || 'zh'; }

function renderCards() {
  const lang = language();
  const isZh = lang === 'zh';
  const viewFull = isZh ? '🔍 点击全屏查看' : '🔍 Click to view';

  const styleGrid = document.getElementById('style-grid');
  if (styleGrid) {
    styleGrid.innerHTML = styles.map((style, sIndex) => `
      <article class="style-card" style="margin-bottom: 36px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
          <span style="font-size:0.75rem; font-weight:800; color:#059669; background:#ecfdf5; padding:4px 10px; border-radius:6px; border:1px solid #a7f3d0;">${style.badge}</span>
        </div>
        <h3 style="font-size:1.25rem; margin-top:0; margin-bottom:6px; color:#0f172a;">${style.name[isZh ? 0 : 1]}</h3>
        <p style="font-size:0.85rem; color:#64748b; margin-bottom:16px;">${style.materials[isZh ? 0 : 1]}</p>

        <!-- 4-Image Interactive Gallery Grid -->
        <div class="image-pair-4" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 16px;">
          ${style.images.map((imgObj, iIndex) => `
            <button class="image-button gallery-trigger" data-style-index="${sIndex}" data-image-index="${iIndex}" style="background:none; border:none; padding:0; cursor:pointer; text-align:left;">
              <div style="position:relative; overflow:hidden; border-radius:8px; aspect-ratio:1.38; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
                <img src="${imgObj.src}" alt="${imgObj.label[isZh ? 0 : 1]}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
                <span style="position:absolute; bottom:6px; right:6px; background:rgba(15,23,42,0.85); color:#fff; padding:3px 8px; border-radius:4px; font-size:0.7rem; font-weight:600;">${imgObj.label[isZh ? 0 : 1]}</span>
              </div>
            </button>
          `).join('')}
        </div>

        <div style="background:#f8fafc; border-radius:10px; padding:14px; border:1px solid #f1f5f9;">
          <ul style="margin:0; padding-left:18px; color:#334155; font-size:0.85rem; line-height:1.6;">
            ${style.features.map(feat => `<li>${feat}</li>`).join('')}
          </ul>
        </div>
      </article>`).join('');
  }

  const drawingGrid = document.getElementById('drawing-grid');
  if (drawingGrid) {
    drawingGrid.innerHTML = drawings.map(([number, title, description, hdSrc]) => `
      <article class="drawing-card image-button" data-image="${hdSrc || `assets/drawings/${number.toLowerCase()}-preview.png?v=26`}" data-caption="${number} ${title[isZh ? 0 : 1]}" style="cursor:pointer; background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:16px; transition: transform 0.2s, box-shadow 0.2s;">
        <div style="position:relative; aspect-ratio:1.42; overflow:hidden; border-radius:8px; margin-bottom:12px; border:1px solid #cbd5e1;">
          <img src="assets/drawings/${number.toLowerCase()}-preview.png?v=26" alt="${number}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
          <span style="position:absolute; top:8px; left:8px; background:#0284c7; color:#fff; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:700;">${number}</span>
        </div>
        <h3 style="font-size:1.05rem; margin:0 0 6px; color:#0f172a;">${title[isZh ? 0 : 1]}</h3>
        <p style="font-size:0.83rem; color:#64748b; margin-bottom:8px;">${description[isZh ? 0 : 1]}</p>
        <span style="color:#0284c7; font-size:0.8rem; font-weight:700;">${viewFull}</span>
      </article>`).join('');
  }

  updateCostCalculator();
}

function updateCostCalculator() {
  const loftInput = document.getElementById('loft-area');
  const styleSelect = document.getElementById('style-select');
  const areaValue = document.getElementById('loft-area-value');
  const totalValue = document.getElementById('estimated-total');
  const rateValue = document.getElementById('estimated-rate');
  const savingsValue = document.getElementById('estimated-savings');

  if (!loftInput || !styleSelect || !areaValue || !totalValue || !rateValue) return;

  const loftArea = Number(loftInput.value);
  const styleAllowance = { style1: 0, style2: 15000, style3: 10000 };
  const estimatedTotal = 425000 + ((loftArea - 750) * 55) + (styleAllowance[styleSelect.value] || 0);

  areaValue.textContent = `${loftArea.toLocaleString('en-MY')} sqft`;
  totalValue.textContent = `RM ${Math.round(estimatedTotal).toLocaleString('en-MY')}`;
  rateValue.textContent = `RM ${(estimatedTotal / 3750).toFixed(2)} / sqft`;
  if (savingsValue) savingsValue.textContent = `RM 35,000 (Clear Span 优化)`;
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

function openLightboxGallery(gallery, index) {
  activeGallery = gallery;
  activeGalleryIndex = index;
  updateLightboxContent();

  const modal = document.getElementById('lightbox');
  if (modal) {
    if (typeof modal.showModal === 'function') modal.showModal();
    else modal.classList.add('active');
  }
}

function updateLightboxContent() {
  if (!activeGallery.length) return;
  const current = activeGallery[activeGalleryIndex];
  const modalImg = document.getElementById('lightbox-img');
  const modalCaption = document.getElementById('lightbox-caption');
  const modalCounter = document.getElementById('lightbox-counter');

  if (modalImg) modalImg.src = current.src || current;
  if (modalCaption) modalCaption.textContent = current.caption || current.label || 'Lot 7836 View';
  if (modalCounter) modalCounter.textContent = `${activeGalleryIndex + 1} / ${activeGallery.length}`;
}

function nextLightboxImage() {
  if (!activeGallery.length) return;
  activeGalleryIndex = (activeGalleryIndex + 1) % activeGallery.length;
  updateLightboxContent();
}

function prevLightboxImage() {
  if (!activeGallery.length) return;
  activeGalleryIndex = (activeGalleryIndex - 1 + activeGallery.length) % activeGallery.length;
  updateLightboxContent();
}

function openSingleLightbox(src, caption) {
  openLightboxGallery([{ src: src, caption: caption }], 0);
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

  const loftInput = document.getElementById('loft-area');
  const styleSelect = document.getElementById('style-select');
  if (loftInput) loftInput.addEventListener('input', updateCostCalculator);
  if (styleSelect) styleSelect.addEventListener('change', updateCostCalculator);

  document.querySelectorAll('.nav-links a').forEach(link => link.addEventListener('click', () => document.body.classList.remove('menu-open')));
  
  document.addEventListener('click', event => {
    const galBtn = event.target.closest('.gallery-trigger');
    if (galBtn) {
      const sIndex = parseInt(galBtn.dataset.styleIndex, 10);
      const iIndex = parseInt(galBtn.dataset.imageIndex, 10);
      const isZh = language() === 'zh';
      const styleObj = styles[sIndex];
      const galleryList = styleObj.images.map(img => ({
        src: img.src,
        caption: `${styleObj.name[isZh ? 0 : 1]} — ${img.label[isZh ? 0 : 1]}`
      }));
      openLightboxGallery(galleryList, iIndex);
      return;
    }

    const card = event.target.closest('.image-button');
    if (card && card.dataset.image) {
      openSingleLightbox(card.dataset.image, card.dataset.caption);
    }
  });

  const prevBtn = document.getElementById('lightbox-prev');
  const nextBtn = document.getElementById('lightbox-next');
  if (prevBtn) prevBtn.addEventListener('click', e => { e.stopPropagation(); prevLightboxImage(); });
  if (nextBtn) nextBtn.addEventListener('click', e => { e.stopPropagation(); nextLightboxImage(); });

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

  window.addEventListener('keydown', e => {
    const modal = document.getElementById('lightbox');
    if (modal && (modal.open || modal.classList.contains('active'))) {
      if (e.key === 'ArrowRight') nextLightboxImage();
      if (e.key === 'ArrowLeft') prevLightboxImage();
      if (e.key === 'Escape') {
        if (typeof modal.close === 'function') modal.close();
        else modal.classList.remove('active');
      }
    }
  });

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
