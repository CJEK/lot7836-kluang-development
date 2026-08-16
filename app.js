const languages = {
  zh: {
    'nav.overview': '项目总览',
    'nav.viewport': '3D 整体视角',
    'nav.recommended': '主推方案',
    'nav.styles': '3套风格比较',
    'nav.area': '单层空间表',
    'nav.approval': '报建审批合规',
    'nav.gantt': '建造工期表',
    'nav.drawings': '2D 概念图集',
    'nav.compliance': '规范与测试',
    'nav.budget': '造价拆解',
    'nav.tender': '招标工程量清单',
    'action.print': '打印提案',
    'action.share': '分享链接',
    'menu.aria': '切换导航菜单',
    'hero.title': '50 × 75ft 现代热带单层独栋别墅完整提案 (Banglo 1 Tingkat)',
    'hero.lead': '正面 50ft 大面宽 × 75ft 屋身进深 (3,750 sqft) | 纯平地单层全龄无障碍居住 | 20x15ft 双车位车廊 + 24ft 宽挑高客餐厅 + 豪华主卧套房 + 2次卧 + 干湿双厨房 + 家政洗衣房 (总建筑面积 2,300 sqft)。',
    'hero.notice': '单层住宅概念设计提案，所有结构、消防、排水及退缩最终须由注册建筑师 (Ar.)、P.Eng 及主管机构 (MPK/BOMBA/IWK) 确认。',
    'recommended.title': '主推：马六甲 Batu Angin 风砖单层热带度假独栋',
    'recommended.text': '专为马来西亚气候定制的单层平地住宅：采用 Batu Angin 通风花砖双层防热玄关、22° 经典热带坡屋顶与 1.2m 深挑檐 (+19ft 屋脊顶高)，配合 50mm PU 隔热包覆与纯平地 3房2卫+干湿双厨房，打造自然降温 3-5°C 的舒适全龄住宅。',
    'recommended.reviewTitle': '本地单层住宅设计与工程控制要点',
    'recommended.reviewText': '• 单层全龄格局：零楼梯纯平地地坪 (FL ±0.00m)，20x15ft 双车位车廊，中央 24ft 挑高客餐厅。\n• 严谨干湿厨房：开放式早餐干厨房 + 独立封闭式重油烟湿厨房 (配 50L 隔油池直通后院)。\n• 结构与防漏：集装箱切口全围焊 100mm 方钢圈，22° 坡顶采用 Standing Seam 直立锁边无外露螺丝防漏工法。',
    'styles.title': '3 套独立单层度假风外观与室内 3D 效果图 (每套 4 视角无重复切图)',
    'styles.text': '每套风格均精细绘制 4 张完全独立、不重复的专属 3D 效果图（正面 50ft 外观、75ft 侧立面、45° 轴测后方、室内客餐厅）。点击图片可左右全屏顺序切图。',
    'styles.controls': '共享控制线：纯单层 2,300 sqft (含双车位车廊), 24ft 客餐厅, 3房2卫+干湿厨房, 22° 坡屋顶 (+12\' 檐高 / +19\' 屋脊)。',
    'drawings.title': '2D 概念工程示意图集 (点击图片全屏查看)',
    'drawings.text': '包含 9 张标准 AutoCAD 工程规图（平面图、立面图、集装箱切割 Detail、干湿厨房排水图、BOMBA 消防图、T&C 测试图、总平面图、三相供电避雷图、地基防蚁防潮大样图）。点击任意图纸均可放大查看细节。',
    'drawings.notice': '注：本图集为概念工程示意图，点击图纸即可放大查看细节，不提供文件下载。',
    'budget.title': 'RM395k – RM435k 单层住宅预算拆解与试算器',
    'budget.text': '通过模组化集装箱改造与纯平地单层结构优化节约 35% 结构资金，重投入于地坪基坑、干湿双厨房、防热挑檐与防水管线。',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. 单层热带独栋住宅概念提案。',
    'image.style2.front': '风格 2 外观 3D 全景',
    'image.gif': '风格 2 单层住宅 8 阶段施工演进动画'
  },
  en: {
    'nav.overview': 'Overview',
    'nav.viewport': '3D Viewports',
    'nav.recommended': 'Recommended',
    'nav.styles': '3 Style Studies',
    'nav.area': 'Single-Storey Area',
    'nav.approval': 'Statutory Approval',
    'nav.gantt': 'Gantt Timeline',
    'nav.drawings': '2D Drawings',
    'nav.compliance': 'Compliance & T&C',
    'nav.budget': 'Budget Plan',
    'nav.tender': 'Tender BOQ',
    'action.print': 'Print',
    'action.share': 'Share',
    'menu.aria': 'Toggle Menu',
    'hero.title': '50 × 75ft Modern Tropical Single-Storey Bungalow Proposal',
    'hero.lead': '50ft Frontage × 75ft Depth (3,750 sqft) | 100% Single-Storey Ground Living | 20x15ft 2-Car Porch + 24ft High Ceiling Living/Dining + Master Suite + 2 Bedrooms + Dry & Wet Kitchens + Laundry (2,300 sqft Total Built-up).',
    'hero.notice': 'Single-storey conceptual proposal. All structure, fire safety, drainage and setbacks subject to Ar. / P.Eng / MPK / BOMBA / IWK review.',
    'recommended.title': 'Recommended: Batu Angin Breeze Block Single-Storey Resort',
    'recommended.text': 'Tailored for Malaysian tropical climate: Breeze block front screen foyer, 22° pitched roof with 1.2m overhang (+19ft ridge), 50mm PU insulation, and pure ground-level 3-bed 2-bath with wet/dry kitchens.',
    'recommended.reviewTitle': 'Local Single-Storey Engineering Highlights',
    'recommended.reviewText': '• Single-Storey Living: Zero-stair barrier-free ground slab (FL ±0.00m), 20x15ft 2-car porch, 24ft airy living/dining.\n• Dry & Wet Kitchens: Open breakfast dry kitchen + enclosed heavy wet kitchen with 50L grease trap.\n• Structure & Waterproofing: 100mm RHS steel frame reinforcement with standing seam screwless roofing.',
    'styles.title': '3 Distinct Single-Storey Architectural & Interior 3D Renders (4 Unique Angles Each)',
    'styles.text': 'Each style features 4 unique, non-duplicate 3D renders (Front 50ft, 75ft Side, 45° Rear, Living/Dining). Click any image to slide left/right in Lightbox mode.',
    'styles.controls': 'Shared Controls: 2,300 sqft Single-Storey (with Car Porch), 24ft Living/Dining, 3 Beds 2 Baths, 22° Roof (+12\' Eave / +19\' Ridge).',
    'drawings.title': '2D Conceptual Drawing Set (Click to View Fullscreen)',
    'drawings.text': 'Complete set of 9 AutoCAD-standard engineering diagrams. Click any card to inspect drawing details.',
    'drawings.notice': 'Note: Conceptual diagrams only. Click any drawing to view fullscreen.',
    'budget.title': 'RM395k – RM435k Single-Storey Budget & Estimator',
    'budget.text': 'Single-storey modular efficiency saves 35% structural cost, re-invested into foundation, dry/wet kitchens, 1.2m eaves and drainage.',
    'footer': '© 2026 Lot 7836 Kluang Development Pack. Single-Storey Conceptual Proposal.',
    'image.style2.front': 'Style 2 Exterior 3D Render',
    'image.gif': 'Style 2 Single-Storey Build Sequence GIF'
  }
};

const styles = [
  {
    key: 'style2',
    badge: 'STYLE 02 · RECOMMENDED MAIN FOCUS',
    name: ['🟢 风格 2 · 马六甲 Batu Angin 风砖屏风门廊 (推荐主推)', 'Style 2 · Batu Angin Screen Foyer (Recommended)'],
    materials: ['材质解构：橄榄森林绿 50mm PU 隔热屋顶 + 赤陶与白色 Batu Angin 通风花砖屏风玄关 + 暖沙色粗抹灰质感外墙', 'Materials: Forest Green PU Roof + Terracotta/White Breeze Blocks + Warm Sand Stucco'],
    features: [
      '✅ 双层墙防热玄关门廊：Batu Angin 通风花砖隔绝正午热辐射，阻挡直射强光，降低室内温度 3-5°C。',
      '✅ 本地干湿双厨房：中央开放式干厨房吧台 + 左侧独立重油烟湿厨房 (配 50L 隔油池直通后院)。',
      '✅ 纯单层全龄宜居：零楼梯全平地布局，主卧套房+双次卧，配 20x15ft 遮阳双车位车廊。'
    ],
    images: [
      { src: 'assets/style2-ext.jpg?v=32', label: ['1/4 正面 50ft 单层外观 (含车廊与风砖)', '1/4 Front Exterior 3D'] },
      { src: 'assets/style2-side.jpg?v=32', label: ['2/4 75ft 侧立面与 1.2m 挑檐 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style2-rear.jpg?v=32', label: ['3/4 45° 轴测后方与坡屋顶天窗 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style2-int.jpg?v=32', label: ['4/4 室内 24ft 挑高客餐厅全景 3D 图', '4/4 Interior Living/Dining 3D'] }
    ]
  },
  {
    key: 'style1',
    badge: 'STYLE 01',
    name: ['🔴 风格 1 · 居銮赤陶红现代热带单层风', 'Style 1 · Terracotta Modern Tropical'],
    materials: ['材质解构：赤陶红 22° 经典热带坡屋顶 + 米白色波纹钢板墙面 + 暖木色 WPC 木塑格栅遮阳门廊', 'Materials: Terracotta Red Roof + Cream Corrugated Steel + Warm Wood WPC Louvers'],
    features: [
      '✅ 22° 经典热带坡屋顶：中央持续排热天窗，利用热浮力自然排出热空气，室内通爽舒适。',
      '✅ 1.2m 宽深挑檐遮阳：暖木色格栅修饰开窗，兼顾隐私遮阳与传统马来 Kampung 建筑亲切感。',
      '✅ 挑高开放大厅：24ft 大面宽中央大厅结合裸露柚木屋架，室内视野极其开阔通透。'
    ],
    images: [
      { src: 'assets/style1-ext.jpg?v=32', label: ['1/4 正面 50ft 单层外观全景', '1/4 Front Exterior 3D'] },
      { src: 'assets/style1-side.jpg?v=32', label: ['2/4 75ft 侧立面 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style1-rear.jpg?v=32', label: ['3/4 45° 轴测后方全景 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style1-int.jpg?v=32', label: ['4/4 室内挑高客餐厅 3D 图', '4/4 Interior Hall 3D'] }
    ]
  },
  {
    key: 'style3',
    badge: 'STYLE 03',
    name: ['⚪ 风格 3 · 南洋纯白复古度假单层风', 'Style 3 · Nanyang White Resort'],
    materials: ['材质解构：全纯白波纹金属板墙面与坡屋顶 (最高太阳反射率 SRI) + 深色柚木百叶推拉门扇', 'Materials: Pure White Corrugated Cladding (High SRI) + Dark Teak Plantation Shutters'],
    features: [
      '✅ 超高 SRI 太阳反射率：全纯白包覆高效反射太阳辐射热，大幅降低集装箱箱体吸热率。',
      '✅ 南洋殖民风采：深色柚木百叶推拉门与纯白轮廓形成优雅对比，极富南洋复古会所调性。',
      '✅ 极简明亮空间：室内单层 3.8m 挑高纯白钢桁架天花结合抛光地坪，极简而富有质感。'
    ],
    images: [
      { src: 'assets/style3-ext.jpg?v=32', label: ['1/4 正面 50ft 单层外观全景', '1/4 Front Exterior 3D'] },
      { src: 'assets/style3-side.jpg?v=32', label: ['2/4 75ft 侧立面 3D 图', '2/4 75ft Side Facade 3D'] },
      { src: 'assets/style3-rear.jpg?v=32', label: ['3/4 45° 轴测后方全景 3D 图', '3/4 45° Rear Isometric 3D'] },
      { src: 'assets/style3-int.jpg?v=32', label: ['4/4 室内纯白客餐厅 3D 图', '4/4 Interior White Hall 3D'] }
    ]
  }
];

const drawings = [
  ['A-101', ['DWG A-101 2D 单层住宅建筑平面图', 'DWG A-101 Floor Plan'], ['50x75ft 地块、双 40ft HC 集装箱、20x15ft 双车位车廊、24ft 客餐厅、主卧套房+2次卧+干湿厨房。', '50x75ft footprint, twin 40ft HC containers, 2-car porch, 24ft living/dining, 3 beds, wet/dry kitchens.'], 'assets/floorplan-bp.jpg?v=32'],
  ['A-102', ['DWG A-102 单层建筑正立面与标高图', 'DWG A-102 Elevation'], ['严格住宅标高：FL ±0.00m 地坪、+12ft 主屋檐 (1.2m 深挑檐) 与 +19ft 22° 经典热带坡屋脊。', 'Residential levels: FL ±0.00m slab, +12ft eave (1.2m overhang) and +19ft 22° pitch ridge.'], 'assets/elevation-bp.jpg?v=32'],
  ['S-101', ['DWG S-101 集装箱切割加固 Detail', 'DWG S-101 Container Detail'], ['侧墙切割开窗、切口周圈 100x100x4.5mm RHS 方钢框焊接与 M20 锚栓加固。', '100x100x4.5mm RHS steel frame reinforcement & M20 anchor bolts.'], 'assets/container_splicing_blueprint.jpg?v=32'],
  ['M-101', ['DWG M-101 干湿双厨房与集中排水图', 'DWG M-101 Kitchen & Drainage'], ['湿厨房 50L 隔油池、主客卫 DN100 黑水管(1:40坡度)及后区 8PE 生化化粪池。', 'Wet kitchen grease trap, DN100 blackwater pipe (1:40 slope) & 8PE septic tank.'], 'assets/kitchen_drainage_blueprint.jpg?v=32'],
  ['F-101', ['DWG F-101 单层 BOMBA 消防逃生图', 'DWG F-101 Fire & Egress Plan'], ['平地双向出口、1.5m 门净宽、SD1-SD4 烟感、FE1-FE3 灭火器与 <12m 直线逃生距离。', 'Ground dual exits, 1.5m doors, SD1-SD4 detectors, FE1-FE3 extinguishers (<12m egress).'], 'assets/fire_safety_egress_blueprint.jpg?v=32'],
  ['T-101', ['DWG T-101 5 大工程打压测试图', 'DWG T-101 T&C Testing Plan'], ['8 Bar 给水打压、24h 湿区闭水、4h 屋顶高压喷淋及 30mA RCCB 漏电测试。', '8 Bar water pressure, 24h flood test, 4h roof spray & 30mA RCCB tests.'], 'assets/tc_testing_blueprint.jpg?v=32'],
  ['G-101', ['DWG G-101 单层总平面与退缩图', 'DWG G-101 Site Plan'], ['Jalan Pakis 沿街、指北针、15ft 前退缩 (双车位车廊)、10ft 后退缩与两侧 5ft 排水沟。', 'Jalan Pakis frontage, 15ft front (2-car porch), 10ft rear & 5ft side setbacks.'], 'assets/siteplan-bp.jpg?v=32'],
  ['E-101', ['DWG E-101 三相供电与避雷接地图', 'DWG E-101 Electrical & Solar'], ['TNB 3-Phase 63A 配电箱、30mA RCCB、+19ft 屋脊纯铜避雷针与 10kW 光伏预留。', 'TNB 3-Phase 63A DB, 30mA RCCB, +19ft copper lightning rod & 10kW solar PV ready.'], 'assets/electrical_wiring_blueprint.jpg?v=32'],
  ['X-101', ['DWG X-101 地基防白蚁防潮剖面图', 'DWG X-101 Foundation & Spec'], ['150mm 地坪、0.2mm HDPE 防潮隔气膜、MS 828 防白蚁屏障与 Standing Seam 坡屋面大样。', '150mm slab, 0.2mm HDPE DPM, MS 828 anti-termite barrier & standing seam detail.'], 'assets/soil_termite_waterproof_blueprint.jpg?v=32']
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
      <article class="drawing-card image-button" data-image="${hdSrc || `assets/drawings/${number.toLowerCase()}-preview.png?v=30`}" data-caption="${number} ${title[isZh ? 0 : 1]}" style="cursor:pointer; background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:16px; transition: transform 0.2s, box-shadow 0.2s;">
        <div style="position:relative; aspect-ratio:1.42; overflow:hidden; border-radius:8px; margin-bottom:12px; border:1px solid #cbd5e1;">
          <img src="assets/drawings/${number.toLowerCase()}-preview.png?v=30" alt="${number}" style="width:100%; height:100%; object-fit:cover; display:block;" loading="lazy">
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
  const areaInput = document.getElementById('builtup-area');
  const styleSelect = document.getElementById('style-select');
  const areaValue = document.getElementById('builtup-area-value');
  const totalValue = document.getElementById('estimated-total');
  const rateValue = document.getElementById('estimated-rate');
  const savingsValue = document.getElementById('estimated-savings');

  if (!areaInput || !styleSelect || !areaValue || !totalValue || !rateValue) return;

  const totalArea = Number(areaInput.value);
  const styleAllowance = { style1: 0, style2: 12000, style3: 8000 };
  const estimatedTotal = 415000 + ((totalArea - 2300) * 60) + (styleAllowance[styleSelect.value] || 0);

  areaValue.textContent = `${totalArea.toLocaleString('en-MY')} sqft`;
  totalValue.textContent = `RM ${Math.round(estimatedTotal).toLocaleString('en-MY')}`;
  rateValue.textContent = `RM ${(estimatedTotal / 3750).toFixed(2)} / sqft`;
  if (savingsValue) savingsValue.textContent = `RM 45,000 (免二层楼板及楼梯)`;
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

  const areaInput = document.getElementById('builtup-area');
  const styleSelect = document.getElementById('style-select');
  if (areaInput) areaInput.addEventListener('input', updateCostCalculator);
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
