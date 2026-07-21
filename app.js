const languages = {
  zh: {
    'menu.aria': '打开菜单', 'nav.overview': '项目总览', 'nav.recommended': '推荐方案', 'nav.styles': '风格比较', 'nav.drawings': '图纸包', 'nav.budget': '造价',
    'action.print': '打印提案', 'action.share': '复制分享链接', 'hero.title': '50 × 75ft 现代热带集装箱住宅概念提案', 'hero.lead': '以两只纵向 40ft High Cube 集装箱、34ft 挑高大厅与后方钢构 Loft 组成的中英双语概念方案。',
    'hero.notice': '概念设计，非施工或送审图。所有结构、消防、排水、退缩与主管机关要求须由 Ar./P.Eng/MPK/BOMBA/IWK 确认。', 'caption.concept': '概念渲染 - 空间及施工细节仍须经专业设计确认。',
    'recommended.title': '推荐：Batu Angin 风砖屏风方案', 'recommended.text': '以通风花砖、深檐、PU 隔热屋面和 Raised Jack Roof 作为热带被动降温策略。5,087 CFM 为概念输入下的预估值，并非保证风量。', 'recommended.gif': '概念流程示意；集装箱切割、补强和防水须以经签署的施工节点为准。', 'recommended.reviewTitle': '施工前必须完成专业审查', 'recommended.reviewText': '退缩、消防接近、污水接驳、箱体改造、整体稳定及验收标准均须先获得现场及专业确认。',
    'styles.title': '三组外观与氛围研究', 'styles.text': '每组均受同一设计控制线约束。正面与室内为概念渲染；侧后图仅作材料、景观与氛围参考，不表示已核定体量或立面。', 'styles.controls': '共同控制：2 × 40ft HC 集装箱、34ft 大厅、后方 35ft 钢构延伸、30° 屋顶、+24′ 檐高 / +38′-5″ 主脊 / +47′ Jack Roof。',
    'drawings.title': '英文概念图纸与 CAD 源文件', 'drawings.text': '下载包包含 7 张英文概念图纸 PDF 和可编辑 DXF 源文件。所有图纸明确标示为非施工、非报批文件。', 'drawings.pdf': '打开英文概念图纸集', 'drawings.dxf': '下载可编辑 CAD 源文件', 'drawings.dxfNote': '可在兼容 AutoCAD 的软件中打开；需要时另存为 DWG。', 'drawings.notice': '退缩、BOMBA 消防接近、污水接驳、结构承载及测试验收均未被表示为已获批准；须待测量图与专业审查完成。',
    'budget.title': 'RM400k–RM450k 初步造价范围', 'budget.text': '仅作概念阶段预算。报价、税费、审批、地勘、专业签证和不可预见工程须另行核定。', 'budget.foundation': '基础及地坪工程', 'budget.structure': '集装箱改造及钢构', 'budget.loft': '阁楼及楼梯', 'budget.roof': '屋面及 Jack Roof', 'budget.mep': '排水、卫生及电气', 'footer': '施工前须完成专业审查。',
    'image.style2.front': '风格二概念渲染', 'image.gif': '风格二概念施工流程'
  },
  en: {
    'menu.aria': 'Open menu', 'nav.overview': 'Overview', 'nav.recommended': 'Preferred', 'nav.styles': 'Styles', 'nav.drawings': 'Drawing Set', 'nav.budget': 'Cost',
    'action.print': 'Print proposal', 'action.share': 'Copy share link', 'hero.title': '50 × 75ft Modern Tropical Container Bungalow', 'hero.lead': 'A bilingual concept proposal organised around two longitudinal 40ft High Cube containers, a 34ft double-height hall and a rear steel loft zone.',
    'hero.notice': 'Concept design only - not for construction or submission. Structure, fire, drainage, setbacks and authority requirements require Ar./P.Eng/MPK/BOMBA/IWK confirmation.', 'caption.concept': 'Concept render - spatial and construction details remain subject to professional design.',
    'recommended.title': 'Preferred direction: Batu Angin screen wall', 'recommended.text': 'Vent blocks, deep eaves, an insulated roof and the Raised Jack Roof form a tropical passive-cooling strategy. 5,087 CFM is a conceptual estimate, not a guaranteed airflow.', 'recommended.gif': 'Concept sequence only; final cutting, reinforcement and waterproofing require signed construction details.', 'recommended.reviewTitle': 'Required professional review', 'recommended.reviewText': 'Confirm site setbacks, fire access, sanitary connection, container modifications, structural stability and all testing criteria before construction.',
    'styles.title': 'Three exterior and atmosphere studies', 'styles.text': 'Each study is constrained by the same design controls. Front and interior images are concept renders; side and rear images are finish, landscape and atmosphere references only - not approved massing or elevations.', 'styles.controls': 'Shared control: 2 × 40ft HC containers, 34ft hall, 35ft rear steel extension, 30° roof, +24′ eave / +38′-5″ ridge / +47′ Jack Roof.',
    'drawings.title': 'English concept drawings and CAD source', 'drawings.text': 'The download pack includes seven English concept-drawing PDF sheets and editable DXF source files. Every sheet is clearly marked not for construction or submission.', 'drawings.pdf': 'Open English concept drawing set', 'drawings.dxf': 'Download editable CAD source', 'drawings.dxfNote': 'Open in AutoCAD-compatible software; save as DWG when required.', 'drawings.notice': 'No setback, BOMBA access, sewer connection, structural capacity or test acceptance is represented as approved. These remain pending site survey and professional review.',
    'budget.title': 'RM400k–RM450k preliminary cost range', 'budget.text': 'Concept-stage budget only. Tender pricing, taxes, approvals, investigations, professional sign-off and contingencies remain to be confirmed.', 'budget.foundation': 'Foundation and ground works', 'budget.structure': 'Container conversion and steelwork', 'budget.loft': 'Loft and stair', 'budget.roof': 'Roof and Jack Roof monitor', 'budget.mep': 'Drainage, sanitary and electrical', 'footer': 'Professional review required before construction.',
    'image.style2.front': 'Style 2 concept render', 'image.gif': 'Style 2 concept construction sequence'
  }
};

const styles = [
  { key: 'style2', name: ['风格 2 · Batu Angin 风砖屏风', 'Style 2 · Batu Angin Screen Wall'], front: 'assets/style2-ext.jpg?v=6', interior: 'assets/style2-int.jpg?v=6', side: 'assets/style2-side.jpg?v=6', rear: 'assets/style2-rear.jpg?v=6' },
  { key: 'style1', name: ['风格 1 · 赤陶现代热带', 'Style 1 · Terracotta Modern Tropical'], front: 'assets/style1-ext.jpg?v=6', interior: 'assets/style1-int.jpg?v=6', side: 'assets/style1-side.jpg?v=6', rear: 'assets/style1-rear.jpg?v=6' },
  { key: 'style3', name: ['风格 3 · 南洋纯白谷仓', 'Style 3 · Nanyang White Barn'], front: 'assets/style3-ext.jpg?v=6', interior: 'assets/style3-int.jpg?v=6', side: 'assets/style3-side.jpg?v=6', rear: 'assets/style3-rear.jpg?v=6' }
];

const drawings = [
  ['A-101', ['平面控制图', 'Floor plan'], ['两只 40ft HC、34ft 大厅与后方 35ft 钢构区的平面控制。', 'Plan control: two 40ft HC containers, 34ft hall and rear 35ft steel zone.']],
  ['A-102', ['正立面与标高', 'Front elevation'], ['标高控制：+24ft 檐高、+38ft-5in 主脊和 +47ft Jack Roof。', 'Level controls: +24ft eave, +38ft-5in ridge and +47ft Jack Roof.']],
  ['S-101', ['集装箱改造审查', 'Container modification'], ['仅为概念补强；切割和连接须经结构设计。', 'Concept reinforcement only; final cutting and connections require structural design.']],
  ['M-101', ['湿区排水审查', 'Wet-core drainage'], ['卫生排水协调概念；最终管路和接驳待 MEP 设计。', 'Concept sanitary coordination; final pipework and connection remain to be designed.']],
  ['F-101', ['消防与疏散审查', 'Fire and egress review'], ['仅为审查清单；BOMBA 策略须由专业人士确认。', 'Review checklist only; BOMBA strategy requires specialist approval.']],
  ['T-101', ['测试与调试计划', 'Testing schedule'], ['建议测试项目；方法和验收标准须经专业确认。', 'Proposed testing subjects; methods and acceptance criteria require professional confirmation.']],
  ['G-101', ['总平面审查图', 'Site review plan'], ['测量、退缩、消防接近与公共排水接驳待确认。', 'Survey, setbacks, fire access and public drainage connection remain pending confirmation.']]
];

function language() { return document.documentElement.dataset.language || 'zh'; }
function renderCards() {
  const lang = language();
  const isZh = lang === 'zh';
  const conceptLabel = isZh ? '概念渲染' : 'Concept render';
  const interiorLabel = isZh ? '室内概念渲染' : 'Interior concept render';
  const moodLabel = isZh ? '风格氛围参考' : 'Style mood reference';
  const sourceLabel = isZh ? 'DXF 源文件 ↓' : 'DXF source ↓';
  document.getElementById('style-grid').innerHTML = styles.map(style => `
    <article class="style-card">
      <h3>${style.name[lang === 'zh' ? 0 : 1]}</h3>
      <div class="image-pair">
        <button class="image-button" data-image="${style.front}" data-caption="${style.name[isZh ? 0 : 1]} — ${conceptLabel}"><img src="${style.front}" alt="${style.name[isZh ? 0 : 1]} ${conceptLabel}" loading="lazy" decoding="async"><span>${conceptLabel}</span></button>
        <button class="image-button" data-image="${style.interior}" data-caption="${style.name[isZh ? 0 : 1]} — ${interiorLabel}"><img src="${style.interior}" alt="${style.name[isZh ? 0 : 1]} ${interiorLabel}" loading="lazy" decoding="async"><span>${interiorLabel}</span></button>
      </div>
      <div class="image-pair reference-pair">
        <button class="image-button" data-image="${style.side}" data-caption="${style.name[isZh ? 0 : 1]} — ${moodLabel}"><img src="${style.side}" alt="${style.name[isZh ? 0 : 1]} ${moodLabel}" loading="lazy" decoding="async"><span>${moodLabel}</span></button>
        <button class="image-button" data-image="${style.rear}" data-caption="${style.name[isZh ? 0 : 1]} — ${moodLabel}"><img src="${style.rear}" alt="${style.name[isZh ? 0 : 1]} ${moodLabel}" loading="lazy" decoding="async"><span>${moodLabel}</span></button>
      </div>
    </article>`).join('');
  document.getElementById('drawing-grid').innerHTML = drawings.map(([number, title, description]) => `
    <article class="drawing-card"><img src="assets/drawings/${number.toLowerCase()}-preview.png?v=1" alt="${number} English concept drawing preview" loading="lazy" decoding="async"><span>${number}</span><h3>${title[isZh ? 0 : 1]}</h3><p>${description[isZh ? 0 : 1]}</p><a href="deliverables/dxf/${number.toLowerCase()}.dxf?v=1" download>${sourceLabel}</a></article>`).join('');
}

function setLanguage(next) {
  const dictionary = languages[next];
  if (!dictionary) return;
  document.documentElement.dataset.language = next;
  document.documentElement.lang = next === 'zh' ? 'zh-CN' : 'en';
  document.querySelectorAll('[data-i18n]').forEach(el => { if (dictionary[el.dataset.i18n]) el.textContent = dictionary[el.dataset.i18n]; });
  document.querySelectorAll('[data-i18n-alt]').forEach(el => { if (dictionary[el.dataset.i18nAlt]) el.alt = dictionary[el.dataset.i18nAlt]; });
  document.querySelectorAll('[data-i18n-title]').forEach(el => { if (dictionary[el.dataset.i18nTitle]) el.title = dictionary[el.dataset.i18nTitle]; });
  document.querySelector('.menu-toggle').setAttribute('aria-label', dictionary['menu.aria']);
  document.querySelectorAll('.language-btn').forEach(btn => { const active = btn.dataset.lang === next; btn.classList.toggle('active', active); btn.setAttribute('aria-pressed', String(active)); });
  localStorage.setItem('lot7836-language', next);
  renderCards();
}

function openLightbox(src, caption) {
  const dialog = document.getElementById('lightbox');
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-caption').textContent = caption;
  dialog.showModal();
}

document.addEventListener('DOMContentLoaded', () => {
  setLanguage(localStorage.getItem('lot7836-language') || 'zh');
  document.querySelectorAll('.language-btn').forEach(btn => btn.addEventListener('click', () => setLanguage(btn.dataset.lang)));
  document.querySelector('.menu-toggle').addEventListener('click', event => { const open = document.body.classList.toggle('menu-open'); event.currentTarget.setAttribute('aria-expanded', String(open)); });
  document.querySelectorAll('.nav-links a').forEach(link => link.addEventListener('click', () => document.body.classList.remove('menu-open')));
  document.addEventListener('click', event => { const card = event.target.closest('.image-button'); if (card) openLightbox(card.dataset.image, card.dataset.caption); });
  document.querySelector('.dialog-close').addEventListener('click', () => document.getElementById('lightbox').close());
  document.querySelector('[data-action="print"]').addEventListener('click', () => window.print());
  document.querySelector('[data-action="share"]').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(location.href); alert(language() === 'zh' ? '分享链接已复制。' : 'Share link copied.'); }
    catch { prompt(language() === 'zh' ? '复制此链接：' : 'Copy this link:', location.href); }
  });
});
