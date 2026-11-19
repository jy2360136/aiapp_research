
  const promptsByView = {
    home: ['今天有哪些板块异动？', '超节点概念今天为什么异动？', '帮我快速复盘今日行情'],
    chat: ['再帮我分析一下主要风险', '看看同行业估值对比', '把结论整理成要点'],
    trade: ['帮我检查这笔委托的风险', '当前持仓风险怎么看？', '银证转账多久到账？'],
    watchlist: ['我的自选股有哪些异动？', '帮我复盘今日自选', '自选股有哪些新公告？']
  };
  const titleByView = { home: '盯盘', trade: '交易', watchlist: '自选', chat: 'AI 对话' };

  function copyScreensToBottomPhone() {
    const source = document.querySelector('.phone-a .screen-stack');
    const target = document.querySelector('.phone-b .screens-b');
    source.querySelectorAll('.screen').forEach(function(screen) {
      const clone = screen.cloneNode(true);
      clone.classList.remove('active');
      target.appendChild(clone);
    });
  }

  function setupPhone(phone) {
    const screens = Array.from(phone.querySelectorAll('.screen'));
    const tabs = Array.from(phone.querySelectorAll('[data-screen]'));
    const promptRail = phone.querySelector('.prompt-rail');
    const composers = Array.from(phone.querySelectorAll('.composer'));
    const input = phone.querySelector('.ai-input');
    const toast = phone.querySelector('.toast');
    const backdrop = phone.querySelector('.sheet-backdrop');
    let currentView = 'home';
    let previousView = 'home';
    let toastTimer = null;

    function toastMessage(text) {
      clearTimeout(toastTimer);
      toast.textContent = text;
      toast.classList.add('show');
      toastTimer = setTimeout(function() { toast.classList.remove('show'); }, 2100);
    }

    function renderPrompts(view) {
      const list = promptsByView[view] || [];
      promptRail.innerHTML = '';
      list.forEach(function(text) {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'prompt-chip';
        btn.innerHTML = '<span class="spark">✦</span>' + text;
        btn.addEventListener('click', function() {
          input.value = text;
          updateComposer();
          input.focus();
        });
        promptRail.appendChild(btn);
      });
    }

    function updateComposer() {
      composers.forEach(function(form) { form.classList.toggle('has-text', input.value.trim().length > 0); });
    }

    function showView(view) {
      currentView = view;
      const secondary = ['settings', 'privacy', 'search'].indexOf(view) !== -1;
      phone.classList.toggle('secondary', secondary);
      screens.forEach(function(screen) { screen.classList.toggle('active', screen.dataset.view === view); });
      tabs.forEach(function(tab) { tab.classList.toggle('active', tab.dataset.screen === view); });
      const aiButton = phone.querySelector('.ai-orb');
      if (aiButton) aiButton.classList.toggle('active', view === 'chat');
      const title = phone.querySelector('.page-title');
      if (title) title.textContent = titleByView[view] || '设置';
      if (!secondary) {
        previousView = view;
        renderPrompts(view);
      }
      const activeScreen = phone.querySelector('.screen[data-view="' + view + '"]');
      if (activeScreen) activeScreen.scrollTop = 0;
    }

    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() { showView(tab.dataset.screen); });
    });

    phone.querySelectorAll('[data-open-chat]').forEach(function(btn) {
      btn.addEventListener('click', function() { showView('chat'); });
    });
    phone.querySelectorAll('[data-open-settings]').forEach(function(btn) {
      btn.addEventListener('click', function() { showView('settings'); });
    });
    phone.querySelectorAll('[data-open-search]').forEach(function(btn) {
      btn.addEventListener('click', function() {
        showView('search');
        const searchInput = phone.querySelector('[data-search-input]');
        if (searchInput) setTimeout(function() { searchInput.focus(); }, 100);
      });
    });
    phone.querySelectorAll('[data-back]').forEach(function(btn) {
      btn.addEventListener('click', function() { showView(previousView); });
    });
    phone.querySelectorAll('[data-back-settings]').forEach(function(btn) {
      btn.addEventListener('click', function() { showView('settings'); });
    });
    phone.querySelectorAll('[data-open-privacy]').forEach(function(btn) {
      btn.addEventListener('click', function() { showView('privacy'); });
    });

    input.addEventListener('input', updateComposer);
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && !e.isComposing) {
        e.preventDefault();
        if (input.value.trim()) submitQuestion();
      }
    });
    composers.forEach(function(form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (input.value.trim()) submitQuestion();
      });
    });
    function submitQuestion() {
      const question = input.value.trim();
      const latest = phone.querySelector('.latest-question');
      if (latest) latest.textContent = question;
      input.value = '';
      updateComposer();
      showView('chat');
      toastMessage('已进入AI对话 · 回复内容沿用现有版本');
    }

    phone.querySelectorAll('[data-open-attachment]').forEach(function(btn) {
      btn.addEventListener('click', function() { backdrop.classList.add('open'); });
    });
    backdrop.addEventListener('click', function(e) {
      if (e.target === backdrop) backdrop.classList.remove('open');
    });
    phone.querySelectorAll('.attachment-item').forEach(function(btn) {
      btn.addEventListener('click', function() {
        backdrop.classList.remove('open');
        toastMessage(btn.dataset.demo + '入口：原型演示');
      });
    });

    phone.querySelectorAll('[data-demo]').forEach(function(button) {
      button.addEventListener('click', function() {
        toastMessage(button.dataset.demo + '：原型仅展示入口，业务内容沿用现有版本');
      });
    });

    phone.querySelectorAll('.display-options button').forEach(function(btn) {
      btn.addEventListener('click', function() {
        phone.querySelectorAll('.display-options button').forEach(function(x) { x.classList.remove('active'); });
        btn.classList.add('active');
      });
    });

    const sortHeaders = Array.from(phone.querySelectorAll('.sort-head'));
    sortHeaders.forEach(function(header) {
      header.addEventListener('click', function() {
        const tableBody = phone.querySelector('.stock-table tbody');
        if (!tableBody) return;
        const key = header.dataset.sort;
        const isAscending = !header.classList.contains('asc');
        sortHeaders.forEach(function(h) { h.classList.remove('asc', 'desc'); });
        header.classList.add(isAscending ? 'asc' : 'desc');
        const rows = Array.from(tableBody.querySelectorAll('tr'));
        rows.sort(function(a, b) {
          const av = Number(a.dataset[key]);
          const bv = Number(b.dataset[key]);
          return isAscending ? av - bv : bv - av;
        });
        rows.forEach(function(row) { tableBody.appendChild(row); });
      });
    });

    renderPrompts('home');
    showView('home');
  }

  copyScreensToBottomPhone();
  document.querySelectorAll('.phone').forEach(setupPhone);

  const slides = Array.from(document.querySelectorAll('.slide'));
  const pageLinks = Array.from(document.querySelectorAll('[data-page-link]'));
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting && entry.intersectionRatio > 0.45) {
          pageLinks.forEach(function(link) { link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id); });
        }
      });
    }, { threshold: [0.45, 0.7] });
    slides.forEach(function(slide) { observer.observe(slide); });
  }
