/**
 * Navigation, Modal and Dynamic Content Logic for Chemistry
 */

const chapters = [
  { id: 1, title: "रसायन विज्ञान की कुछ मूल अवधारणाएँ" },
  { id: 2, title: "परमाणु की संरचना" },
  { id: 3, title: "तत्त्वों का वर्गीकरण एवं गुणधर्मों में आवर्तिता" },
  { id: 4, title: "रासायनिक आबंधन तथा आण्विक संरचना" },
  { id: 5, title: "रासायनिक ऊष्मागतिकी" },
  { id: 6, title: "साम्यावस्था" },
  { id: 7, title: "अपचयोपचय अभिक्रियाएँ (रेडॉक्स अभिक्रियाएँ)" },
  { id: 8, title: "कार्बनिक रसायन: कुछ आधारभूत सिद्धांत तथा तकनीकें" },
  { id: 9, title: "हाइड्रोकार्बन" }
];

document.addEventListener('DOMContentLoaded', () => {
  renderChapters(chapters);

  const searchBar = document.getElementById('searchBar');
  if(searchBar) {
    searchBar.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase();
      const filtered = chapters.filter(c => c.title.toLowerCase().includes(term));
      renderChapters(filtered);
    });
  }
});

function renderChapters(data) {
  const grid = document.getElementById('chapter-grid');
  if(!grid) return; // If on notes_view.html, grid might not exist, that's fine.

  grid.innerHTML = '';

  data.forEach(chapter => {
    const card = document.createElement('div');
    card.className = 'chapter-card';
    
    let mobileBtn = '';
    if(chapter.id === 1) {
      mobileBtn = `<button class="btn-secondary" onclick="window.open('ch1_mobile.html', '_blank')" style="background: linear-gradient(135deg, #10b981, #059669); border-color: #34d399; color: white; display: flex; align-items: center; justify-content: center; gap: 8px;">📱 For Students (Mobile View)</button>`;
    }

    card.innerHTML = `
      <div class="chapter-num">${String(chapter.id).padStart(2, '0')}</div>
      <h3 class="chapter-title">${chapter.title}</h3>
      <div class="chapter-actions" style="display:flex; gap:10px; flex-direction: column; margin-top:20px; position:relative; z-index:10;">
        <button class="btn-primary" onclick="window.open('notes_html_view.html?id=${chapter.id}', '_blank')">🌍 संपूर्ण नोट्स देखें (Premium HTML)</button>
        <button class="btn-secondary" onclick="window.open('qa_view.html?id=${chapter.id}', '_blank')" style="background: #8b5cf6; border-color: #7c3aed;">❓ प्रश्न-उत्तर (Master Q&A)</button>
        ${mobileBtn}
      </div>
    `;
    grid.appendChild(card);
  });
}
