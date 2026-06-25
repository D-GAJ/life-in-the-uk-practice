js_code = """
function startRandomExam() {
    const mockKeys = Object.keys(questionsDB).filter(k => k.startsWith("Mock Exam"));
    if (mockKeys.length === 0) return alert("No Mock Exams available.");
    const randomKey = mockKeys[Math.floor(Math.random() * mockKeys.length)];
    startTest(questionsDB[randomKey], randomKey);
}
"""

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

if 'function startRandomExam()' not in content:
    with open('js/app.js', 'a', encoding='utf-8') as f:
        f.write("\n" + js_code + "\n")
