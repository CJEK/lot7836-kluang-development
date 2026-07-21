/* ==========================================================================
   Lot 7836 Development Pack - Application Logic (V3.1 Production Stable)
   ========================================================================== */

let currentBpSrc = 'assets/container_splicing_blueprint.jpg';
let currentBpTitle = '集装箱切割与拼接 CAD 节点图 (Container Modification Detail)';

const translations = {
  zh: {
    'nav.overview': '项目总览', 'nav.controls': '设计控制线', 'nav.engineering': '工程预验算', 'nav.views': '多方位外观展示', 'nav.build': '0-1 施工 GIF', 'nav.blueprints': 'CAD 切割/施工图纸', 'nav.budget': '造价拆解',
    'action.print': '🖨️ 打印提案总册', 'action.share': '🔗 分享项目链接',
    'blueprint.title': '2D 施工图纸与集装箱切割工程图 (CAD Engineering Blueprints)', 'blueprint.intro': '符合马来西亚 MPK 规范的 2D 施工图纸，包含集装箱切割补强、拼接与风砖锚固工程节点。',
    'budget.title': 'RM400k - RM450k 预算拆解与降本策略 (Budget Breakdown)', 'budget.intro': '通过内部柱网优化省下 30% 结构资金，重投入于基坑地坪、防热与防水。',
    'calculator.eyebrow': 'INTERACTIVE BOQ ESTIMATOR', 'calculator.title': '动态 BOQ 造价计算器', 'calculator.note': '基准为 900 sqft Loft、Style 1 和 RM425,000；仅供初步预算，报价与审批另计。', 'calculator.loft': 'Loft 阁楼面积', 'calculator.style': '风格选择', 'calculator.total': '预估总造价', 'calculator.rate': '每 3,750 sqft 建筑占地',
    'style.one': 'Style 1 · 赤陶红现代热带', 'style.two': 'Style 2 · Batu Angin 风砖屏风', 'style.three': 'Style 3 · 南洋纯白谷仓'
  },
  en: {
    'nav.overview': 'Overview', 'nav.controls': 'Design Controls', 'nav.engineering': 'Engineering Checks', 'nav.views': 'Architectural Views', 'nav.build': 'Build GIF', 'nav.blueprints': 'CAD Blueprints', 'nav.budget': 'Cost Plan',
    'action.print': '🖨️ Print Proposal', 'action.share': '🔗 Share Proposal',
    'blueprint.title': '2D Construction Drawings & Container Modification Details', 'blueprint.intro': 'MPK-oriented drawing set covering container reinforcement, connections and Batu Angin screen-wall anchors.',
    'budget.title': 'RM400k - RM450k Budget Breakdown & Value Strategy', 'budget.intro': 'Optimised internal columns release budget for foundations, heat control and waterproofing.',
    'calculator.eyebrow': 'INTERACTIVE BOQ ESTIMATOR', 'calculator.title': 'Dynamic BOQ Cost Calculator', 'calculator.note': 'Based on a 900 sqft loft, Style 1 and RM425,000; preliminary budgeting only.', 'calculator.loft': 'Loft area', 'calculator.style': 'Style selection', 'calculator.total': 'Estimated total cost', 'calculator.rate': 'Per 3,750 sqft footprint',
    'style.one': 'Style 1 · Terracotta Modern Tropical', 'style.two': 'Style 2 · Batu Angin Screen Wall', 'style.three': 'Style 3 · Nanyang White Barn'
  },
  bm: {
    'nav.overview': 'Gambaran Projek', 'nav.controls': 'Kawalan Reka Bentuk', 'nav.engineering': 'Semakan Kejuruteraan', 'nav.views': 'Paparan Seni Bina', 'nav.build': 'GIF Pembinaan', 'nav.blueprints': 'Pelan CAD', 'nav.budget': 'Pelan Kos',
    'action.print': '🖨️ Cetak Cadangan', 'action.share': '🔗 Kongsi Cadangan',
    'blueprint.title': 'Lukisan Pembinaan 2D & Butiran Ubah Suai Kontena', 'blueprint.intro': 'Set lukisan berorientasikan MPK meliputi tetulang kontena, sambungan dan sauh dinding skrin Batu Angin.',
    'budget.title': 'Pecahan Bajet RM400k - RM450k & Strategi Nilai', 'budget.intro': 'Kolum dalaman dioptimumkan supaya bajet disalurkan kepada asas, kawalan haba dan kalis air.',
    'calculator.eyebrow': 'PENGANGGAR BOQ INTERAKTIF', 'calculator.title': 'Kalkulator Kos BOQ Dinamik', 'calculator.note': 'Berasaskan loteng 900 sqft, Gaya 1 dan RM425,000; untuk bajet awal sahaja.', 'calculator.loft': 'Keluasan loteng', 'calculator.style': 'Pilihan gaya', 'calculator.total': 'Anggaran jumlah kos', 'calculator.rate': 'Setiap tapak bangunan 3,750 sqft',
    'style.one': 'Gaya 1 · Tropika Moden Terracotta', 'style.two': 'Gaya 2 · Dinding Skrin Batu Angin', 'style.three': 'Gaya 3 · Bangsal Putih Nanyang'
  }
};

const hotspotSpecs = {
  jack: {
    zh: ['拔风塔 · Raised Jack Roof', '+47ft 顶脊形成 +1ft 至 +47ft 的 46ft 热压高度；设计工况下约提供 5,087 CFM 的自然排风。'],
    en: ['Raised Jack Roof', '+47ft ridge creates a 46ft thermal-pressure height from the +1ft intake; design condition delivers approximately 5,087 CFM.'],
    bm: ['Bumbung Jack Dinaikkan', 'Rabung +47ft menghasilkan ketinggian tekanan haba 46ft dari salur masuk +1ft; keadaan reka bentuk memberi kira-kira 5,087 CFM.']
  },
  breeze: {
    zh: ['Batu Angin 双层屏风', '通风花砖与后置实体墙形成遮阳空气层；“85% 辐射热阻隔”属材料与开口率待供应商验证的性能目标。'],
    en: ['Batu Angin Double-Skin', 'Vent blocks and the backing wall form a shaded air layer; the 85% radiant-heat reduction remains a supplier-verified performance target.'],
    bm: ['Skrin Dwi-Lapis Batu Angin', 'Blok pengudaraan dan dinding belakang membentuk lapisan udara bernaung; pengurangan haba sinaran 85% ialah sasaran yang perlu disahkan pembekal.']
  },
  rhs: {
    zh: ['RHS 100×100mm 切口加固', '集装箱等离子切割开口周边设置 100×100mm RHS 概念框；焊缝、节点、荷载路径与钢材等级须由结构工程师签证。'],
    en: ['RHS 100×100mm Cut Reinforcement', 'A 100×100mm RHS concept frame reinforces container cut-outs; welds, connections, load paths and steel grade require structural-engineer sign-off.'],
    bm: ['Tetulang Potongan RHS 100×100mm', 'Rangka konsep RHS 100×100mm mengukuhkan bukaan kontena; kimpalan, sambungan, laluan beban dan gred keluli perlu disahkan jurutera struktur.']
  }
};

// Blueprint Selector Switcher using precise button reference
function switchBlueprint(src, title, desc, btnEl) {
  const bpImg = document.getElementById('bp-img');
  const bpTitle = document.getElementById('bp-title');
  const bpDesc = document.getElementById('bp-desc');
  const bpBtns = document.querySelectorAll('.bp-btn');

  currentBpSrc = src;
  currentBpTitle = title;

  if (bpImg) bpImg.src = src;
  if (bpTitle) bpTitle.textContent = title;
  if (bpDesc) bpDesc.textContent = desc;

  bpBtns.forEach(btn => {
    if (btn === btnEl) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

function toggleHotspot(key) {
  const tooltip = document.getElementById('hotspot-tooltip');
  const title = document.getElementById('hotspot-title');
  const detail = document.getElementById('hotspot-detail');
  const language = document.documentElement.dataset.language || 'zh';
  const buttons = document.querySelectorAll('.blueprint-hotspot');
  const selected = document.querySelector(`.blueprint-hotspot.hotspot-${key}`);
  const spec = hotspotSpecs[key]?.[language] || hotspotSpecs[key]?.zh;

  if (!tooltip || !title || !detail || !spec || !selected) return;

  const isAlreadyOpen = tooltip.classList.contains('active') && selected.classList.contains('active');
  buttons.forEach(button => {
    button.classList.remove('active');
    button.setAttribute('aria-expanded', 'false');
  });

  if (isAlreadyOpen) {
    tooltip.classList.remove('active');
    return;
  }

  title.textContent = spec[0];
  detail.textContent = spec[1];
  selected.classList.add('active');
  selected.setAttribute('aria-expanded', 'true');
  tooltip.classList.add('active');
}

function closeHotspot() {
  document.getElementById('hotspot-tooltip')?.classList.remove('active');
  document.querySelectorAll('.blueprint-hotspot').forEach(button => {
    button.classList.remove('active');
    button.setAttribute('aria-expanded', 'false');
  });
}

function formatCurrency(value) {
  return `RM ${Math.round(value).toLocaleString('en-MY')}`;
}

function formatRate(value) {
  return `RM ${value.toLocaleString('en-MY', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

function updateCostCalculator() {
  const loftInput = document.getElementById('loft-area');
  const styleSelect = document.getElementById('style-select');
  const areaValue = document.getElementById('loft-area-value');
  const totalValue = document.getElementById('estimated-total');
  const rateValue = document.getElementById('estimated-rate');
  if (!loftInput || !styleSelect || !areaValue || !totalValue || !rateValue) return;

  const loftArea = Number(loftInput.value);
  const styleAllowance = { style1: 0, style2: 15000, style3: 10000 };
  const estimatedTotal = 425000 + ((loftArea - 900) * 51) + styleAllowance[styleSelect.value];

  areaValue.textContent = `${loftArea.toLocaleString('en-MY')} sqft`;
  totalValue.textContent = formatCurrency(estimatedTotal);
  rateValue.textContent = `${formatRate(estimatedTotal / 3750)} / sqft`;
}

function setLanguage(language) {
  const dictionary = translations[language];
  if (!dictionary) return;

  document.documentElement.lang = language === 'bm' ? 'ms' : language;
  document.documentElement.dataset.language = language;
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const translation = dictionary[element.dataset.i18n];
    if (translation) element.textContent = translation;
  });
  document.querySelectorAll('.language-btn').forEach(button => {
    const isActive = button.dataset.lang === language;
    button.classList.toggle('active', isActive);
    button.setAttribute('aria-pressed', String(isActive));
  });

  localStorage.setItem('lot7836-language', language);
  updateCostCalculator();

  const activeHotspot = document.querySelector('.blueprint-hotspot.active');
  const hotspotKey = activeHotspot?.className.match(/hotspot-(jack|breeze|rhs)/)?.[1];
  if (hotspotKey) {
    const spec = hotspotSpecs[hotspotKey][language];
    const title = document.getElementById('hotspot-title');
    const detail = document.getElementById('hotspot-detail');
    if (title && detail && spec) {
      title.textContent = spec[0];
      detail.textContent = spec[1];
    }
  }
}

// Lightbox Modal Functions with Lock-scroll and Keyboard ESC Listener
function openLightbox(imgSrc, caption) {
  const modal = document.getElementById('lightbox');
  const modalImg = document.getElementById('lightbox-img');
  const modalCaption = document.getElementById('lightbox-caption');

  if (modal && modalImg) {
    modalImg.src = imgSrc;
    modalCaption.textContent = caption || 'Lot 7836 Architectural Detail';
    modal.classList.add('active');
    document.body.classList.add('no-scroll');
  }
}

function closeLightbox() {
  const modal = document.getElementById('lightbox');
  if (modal) {
    modal.classList.remove('active');
    document.body.classList.remove('no-scroll');
  }
}

// Keyboard ESC support for Lightbox
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeLightbox();
  }
});

// Copy Share Link
function copyShareLink() {
  const input = document.getElementById('share-link-input');
  if (input) {
    input.select();
    input.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(input.value).then(() => {
      alert('已成功复制当前项目开发提案分享链接！您可以发送给顾问、承包商或家人查看。');
    }).catch(err => {
      alert('复制失败，请手动选择框内链接复制。');
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateCostCalculator();
  document.documentElement.dataset.language = 'zh';
  const savedLanguage = localStorage.getItem('lot7836-language');
  if (savedLanguage && translations[savedLanguage]) setLanguage(savedLanguage);
});

// Active Nav link highlight on scroll
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');
  
  let scrollY = window.pageYOffset;
  
  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 120;
    const sectionId = current.getAttribute('id');
    
    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + sectionId) {
          link.classList.add('active');
        }
      });
    }
  });
});
