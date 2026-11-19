
const fs = require('node:fs');
const { pathToFileURL } = require('node:url');
const http = require('node:http');
function getJson(url){ return new Promise((resolve,reject)=>{ http.get(url,res=>{let d='';res.on('data',c=>d+=c);res.on('end',()=>resolve(JSON.parse(d)));}).on('error',reject); }); }
(async()=>{
  const list = await getJson('http://127.0.0.1:9223/json/list');
  const page = list.find(x=>x.type==='page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
  let seq=0; const pending=new Map();
  ws.addEventListener('message', ev=>{const msg=JSON.parse(ev.data); if(msg.id&&pending.has(msg.id)){const p=pending.get(msg.id);pending.delete(msg.id);msg.error?p.reject(msg.error):p.resolve(msg.result);}});
  const call=(method,params={})=>new Promise((resolve,reject)=>{const id=++seq;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  async function evaluate(expression){const r=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});return r.result.value;}
  async function shot(name){const r=await call('Page.captureScreenshot',{format:'png',fromSurface:true});fs.writeFileSync('C:/Users/Administrator/Desktop/aiapp竞品调研/prototype-assets/'+name,Buffer.from(r.data,'base64'));}
  await call('Page.enable'); await call('Runtime.enable');
  const url=pathToFileURL('C:/Users/Administrator/Desktop/aiapp竞品调研/掌小宝AI入口调整原型.html').href;
  await call('Page.navigate',{url}); await sleep(1600);
  const metrics=await evaluate("JSON.stringify({height:document.documentElement.scrollHeight,innerHeight,slides:[...document.querySelectorAll('.slide')].map(x=>({id:x.id,top:x.offsetTop,height:x.offsetHeight}))})");
  console.log(metrics);
  await evaluate("document.getElementById('prototype-a').scrollIntoView({block:'start'});"); await sleep(500);
  await shot('v2-a-home-cdp.png');
  await evaluate("document.querySelector('.phone-a [data-screen=\"trade\"]').click();"); await sleep(250); await shot('v2-a-trade-cdp.png');
  await evaluate("document.querySelector('.phone-a [data-screen=\"watchlist\"]').click();"); await sleep(250); await shot('v2-a-watchlist-cdp.png');
  await evaluate("document.querySelector('.phone-a [data-open-chat]').click();"); await sleep(250); await shot('v2-a-chat-cdp.png');
  await evaluate("document.getElementById('prototype-b').scrollIntoView({block:'start'});"); await sleep(500); await shot('v2-b-home-cdp.png');
  await evaluate("document.querySelector('.phone-b [data-open-chat]').click();"); await sleep(250); await shot('v2-b-chat-cdp.png');
  const errs=await evaluate("JSON.stringify(window.__errors||[])");
  console.log('errors',errs);
  ws.close();
})().catch(e=>{console.error(e);process.exit(1)});
