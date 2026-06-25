const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
let js = fs.readFileSync('js/app.js', 'utf8');

js += `
function startRandomExam() {
    const mockKeys = Object.keys(questionsDB).filter(k => k.startsWith("Mock Exam"));
    if (mockKeys.length === 0) return alert("No Mock Exams available.");
    const randomKey = mockKeys[Math.floor(Math.random() * mockKeys.length)];
    startTest(questionsDB[randomKey], randomKey);
}
`;

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (e) => {
  console.error("VIRTUAL CONSOLE ERROR:");
  console.error(e.stack || e);
});
virtualConsole.on("jsdomError", (e) => {
  console.error("JSDOM ERROR:");
  console.error(e.stack || e);
});

const dom = new JSDOM(html, { 
    url: "http://localhost/",
    runScripts: "dangerously",
    virtualConsole
});

const script = dom.window.document.createElement("script");
script.textContent = js;
dom.window.document.body.appendChild(script);

setTimeout(() => {
    console.log("Done. If there are no errors above, it worked.");
}, 1000);
