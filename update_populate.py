import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_populate = """function populateTestSelector() {
    els.testSelector.innerHTML = '';
    
    // Group keys
    const mockExams = [];
    const chapterTests = [];
    
    Object.keys(questionsDB).forEach(key => {
        if (key.startsWith("Mock Exam")) {
            mockExams.push(key);
        } else if (key.startsWith("Chapter")) {
            chapterTests.push(key);
        } else {
            mockExams.push(key);
        }
    });
    
    // Sort Mock Exams
    mockExams.sort((a, b) => {
        const numA = parseInt(a.replace(/\\D/g, '')) || 0;
        const numB = parseInt(b.replace(/\\D/g, '')) || 0;
        return numA - numB;
    });
    
    // Sort Chapter Tests
    chapterTests.sort((a, b) => {
        const partsA = a.split('-');
        const partsB = b.split('-');
        const chapA = parseInt(partsA[0].replace(/\\D/g, '')) || 0;
        const chapB = parseInt(partsB[0].replace(/\\D/g, '')) || 0;
        if (chapA !== chapB) return chapA - chapB;
        const testA = parseInt(partsA[1].replace(/\\D/g, '')) || 0;
        const testB = parseInt(partsB[1].replace(/\\D/g, '')) || 0;
        return testA - testB;
    });
    
    // Create section builder
    const createSection = (title, keys, labelFormatter) => {
        if (keys.length === 0) return;
        const section = document.createElement('div');
        section.style.marginBottom = '40px';
        
        const header = document.createElement('h2');
        header.innerText = title;
        header.style.marginBottom = '20px';
        header.style.color = '#333';
        header.style.fontSize = '1.4rem';
        header.style.fontWeight = 'normal';
        section.appendChild(header);
        
        const grid = document.createElement('div');
        grid.className = 'test-grid';
        grid.style.display = 'grid';
        grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(220px, 1fr))';
        grid.style.gap = '15px';
        
        const dailyTests = getDailyTestRecommendation();
        
        keys.forEach(key => {
            const card = document.createElement('div');
            card.className = 'test-card';
            if (dailyTests.includes(key)) {
                card.style.boxShadow = '0 0 8px rgba(26, 115, 232, 0.5)';
            }
            
            const formattedTitle = labelFormatter(key);
            
            card.innerHTML = `
                <div class="test-card-top">${formattedTitle}</div>
                <hr>
                <div class="test-card-bottom">
                    <span>Take the test</span>
                    <span class="test-card-icon">&rarr;</span>
                </div>
            `;
            
            card.onclick = () => startTest(questionsDB[key], key);
            grid.appendChild(card);
        });
        
        section.appendChild(grid);
        els.testSelector.appendChild(section);
    };

    createSection('Life in the UK Tests', mockExams, key => {
        const num = key.replace(/\\D/g, '');
        return `Life in the UK Test ${num}`;
    });
    
    createSection('Tests by chapter', chapterTests, key => {
        // e.g., "Chapter 5 - Test 5" -> "Chapter 5 Test 5"
        return key.replace(' - ', ' ');
    });
}"""

# Safely replace the function
js = re.sub(r'function populateTestSelector\(\) \{.*?\n\}', lambda m: new_populate, js, flags=re.DOTALL)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
