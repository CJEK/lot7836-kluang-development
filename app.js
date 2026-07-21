/* ==========================================================================
   Lot 7836 Development Pack - Application Logic (V3.1 Production Stable)
   ========================================================================== */

let currentBpSrc = 'assets/container_splicing_blueprint.jpg';
let currentBpTitle = '集装箱切割与拼接 CAD 节点图 (Container Modification Detail)';

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
