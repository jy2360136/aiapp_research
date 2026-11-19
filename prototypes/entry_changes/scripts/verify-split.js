const http = require('node:http');
const fs = require('node:fs');
const { pathToFileURL } = require('node:url');

function getJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

(async () => {
  const pages = await getJson('http://127.0.0.1:9223/json/list');
  const page = pages.find((item) => item.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve, { once: true });
    ws.addEventListener('error', reject, { once: true });
  });

  let seq = 0;
  const pending = new Map();
  const exceptions = [];
  ws.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    if (message.method === 'Runtime.exceptionThrown') {
      exceptions.push(message.params.exceptionDetails.exception?.description || message.params.exceptionDetails.text);
    }
    if (message.id && pending.has(message.id)) {
      const task = pending.get(message.id);
      pending.delete(message.id);
      message.error ? task.reject(message.error) : task.resolve(message.result);
    }
  });

  const call = (method, params = {}) => new Promise((resolve, reject) => {
    const id = ++seq;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
  const evaluate = async (expression) => (await call('Runtime.evaluate', {
    expression,
    returnByValue: true,
    awaitPromise: true
  })).result.value;
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const screenshot = async (path) => {
    const result = await call('Page.captureScreenshot', { format: 'png', fromSurface: true });
    fs.writeFileSync(path, Buffer.from(result.data, 'base64'));
  };

  await call('Runtime.enable');
  await call('Page.enable');
  await call('Emulation.setDeviceMetricsOverride', {
    width: 1440,
    height: 1100,
    deviceScaleFactor: 1,
    mobile: false
  });

  const mainUrl = pathToFileURL('D:/aiapp竞品调研/prototypes/entry_changes/main_top_navigation.html').href;
  await call('Page.navigate', { url: mainUrl });
  await sleep(900);
  const mainState = JSON.parse(await evaluate(`JSON.stringify({
    slides: document.querySelectorAll('.slide').length,
    hasIntro: !!document.querySelector('#intro'),
    hasTopPrototype: !!document.querySelector('#prototype-a'),
    hasBottomPrototype: !!document.querySelector('#prototype-b'),
    hasExploreCard: !!document.querySelector('.change-card.explore'),
    pageLinks: [...document.querySelectorAll('[data-page-link]')].map(x => x.textContent.trim())
  })`));
  await evaluate(`document.querySelector('#prototype-a').scrollIntoView({block:'start'}); true`);
  await sleep(180);
  await screenshot('D:/aiapp竞品调研/prototypes/entry_changes/previews/verify-main-top-cdp.png');
  await evaluate(`document.querySelector('.phone-a [data-open-settings]').click(); true`);
  await sleep(150);
  const settingsState = JSON.parse(await evaluate(`JSON.stringify({
    active: document.querySelector('.phone-a [data-view="settings"]').classList.contains('active'),
    backVisible: (() => { const el = document.querySelector('.phone-a [data-view="settings"] [data-back]'); const r = el && el.getBoundingClientRect(); return !!(r && r.width > 0 && r.height > 0); })(),
    title: document.querySelector('.phone-a [data-view="settings"] h2')?.textContent.trim() || '',
    titleCentered: (() => { const el = document.querySelector('.phone-a [data-view="settings"] h2'); if (!el) return false; const r = el.getBoundingClientRect(); const sr = el.closest('.screen').getBoundingClientRect(); return Math.abs((r.left + r.width/2) - (sr.left + sr.width/2)) < 2; })()
  })`));
  await screenshot('D:/aiapp竞品调研/prototypes/entry_changes/previews/verify-main-settings-cdp.png');

  const bottomUrl = pathToFileURL('D:/aiapp竞品调研/prototypes/entry_changes/bottom_dock_variant.html').href;
  await call('Page.navigate', { url: bottomUrl });
  await sleep(900);
  const bottomState = JSON.parse(await evaluate(`JSON.stringify({
    slides: document.querySelectorAll('.slide').length,
    hasBottomPrototype: !!document.querySelector('#prototype-b'),
    hasPhoneA: !!document.querySelector('.phone-a'),
    bottomPhoneScreens: document.querySelectorAll('.phone-b .screen').length,
    bottomTabs: [...document.querySelectorAll('.phone-b .bottom-tab')].map(x => x.textContent.trim()),
    hasDock: !!document.querySelector('.phone-b .bottom-dock'),
    hasChatLaunch: !!document.querySelector('.phone-b .chat-launch')
  })`));
  await screenshot('D:/aiapp竞品调研/prototypes/entry_changes/previews/verify-bottom-dock-cdp.png');
  await evaluate(`document.querySelector('.phone-b [data-screen="trade"]').click(); true`);
  await sleep(120);
  const interactionState = JSON.parse(await evaluate(`JSON.stringify({
    tradeActive: document.querySelector('.phone-b [data-view="trade"]').classList.contains('active'),
    title: document.querySelector('.phone-b .page-title').textContent.trim(),
    promptText: document.querySelector('.phone-b .prompt-rail').textContent.trim()
  })`));

  console.log(JSON.stringify({ mainState, settingsState, bottomState, interactionState, exceptions }, null, 2));
  ws.close();
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
