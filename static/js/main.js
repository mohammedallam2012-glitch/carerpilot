/* CV 2030 — Shared JavaScript */

// ─── TOAST NOTIFICATION ───
function showToast(message, type) {
  type = type || 'success';
  var bg = type === 'error' ? '#EF4444' : type === 'warning' ? '#F59E0B' : '#10B981';
  var toast = document.createElement('div');
  toast.className = 'cv-toast';
  toast.textContent = message;
  toast.style.cssText =
    'position:fixed;bottom:24px;left:50%;transform:translateX(-50%);' +
    'background:' + bg + ';' +
    'color:#fff;padding:14px 28px;border-radius:12px;font-weight:700;' +
    'font-size:.9rem;z-index:9999;box-shadow:0 8px 32px rgba(0,0,0,.15);' +
    'font-family:Cairo,sans-serif;animation:fadeInUp .3s ease;';
  document.body.appendChild(toast);
  setTimeout(function(){ toast.style.opacity='0'; toast.style.transition='.3s'; }, 3000);
  setTimeout(function(){ toast.remove(); }, 3300);
}

// ─── SIDEBAR TOGGLE ───
document.addEventListener('DOMContentLoaded', function(){
  var toggle = document.getElementById('sidebarToggle');
  if(toggle){
    toggle.addEventListener('click', function(){
      document.querySelector('.sidebar').classList.toggle('open');
    });
  }
});

// ─── AUTO COUNTER ANIMATION ───
function animateCounter(el) {
  var target = parseFloat(el.getAttribute('data-target'));
  var suffix = el.getAttribute('data-suffix') || '';
  var prefix = el.getAttribute('data-prefix') || '';
  var isFloat = el.getAttribute('data-float') === 'true';
  var divide = parseFloat(el.getAttribute('data-divide')) || 1;
  var duration = 2000;
  var steps = 60;
  var inc = target / steps;
  var cur = 0, count = 0;
  var t = setInterval(function(){
    count++;
    cur = Math.min(cur + inc, target);
    var display = cur / divide;
    el.textContent = prefix + (isFloat ? display.toFixed(1) : Math.floor(display)) + suffix;
    if(count >= steps) clearInterval(t);
  }, duration / steps);
}

document.addEventListener('DOMContentLoaded', function(){
  var counterObserver = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        animateCounter(e.target);
        counterObserver.unobserve(e.target);
      }
    });
  }, {threshold: 0.5});
  document.querySelectorAll('[data-target]').forEach(function(el){
    counterObserver.observe(el);
  });
});
