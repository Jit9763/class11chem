/**
 * Premium Chemistry Simulators Logic
 * Includes: Burette (Meniscus Zoom), Pipette, Analytical Balance, and Sig-Fig Parser
 */

const ChemistrySims = {
    // --- BURETTE LOGIC ---
    burette: {
        volume: 50.0, // Initial volume in mL
        flowRate: 0,
        interval: null,
        
        init() {
            const liquid = document.getElementById('burette-liquid');
            const display = document.getElementById('burette-reading');
            const slider = document.getElementById('stopcock-slider');
            
            slider.addEventListener('input', (e) => {
                const flow = parseFloat(e.target.value);
                this.flowRate = flow;
                
                if (flow > 0 && !this.interval) {
                    this.startFlow();
                } else if (flow === 0) {
                    this.stopFlow();
                }
            });
        },

        startFlow() {
            this.interval = setInterval(() => {
                if (this.volume > 0) {
                    this.volume -= (this.flowRate / 50); // Scale flow
                    if (this.volume < 0) this.volume = 0;
                    this.updateUI();
                } else {
                    this.stopFlow();
                }
            }, 50);
        },

        stopFlow() {
            clearInterval(this.interval);
            this.interval = null;
        },

        updateUI() {
            const liquid = document.getElementById('burette-liquid');
            const display = document.getElementById('burette-reading');
            const magLiquid = document.getElementById('mag-liquid');
            
            const heightPerc = (this.volume / 50) * 100;
            liquid.style.height = heightPerc + '%';
            magLiquid.style.height = heightPerc + '%';
            display.innerText = (50 - this.volume).toFixed(2) + ' mL';
        }
    },

    // --- ANALYTICAL BALANCE LOGIC ---
    balance: {
        targetWeight: 0,
        currentWeight: 0,
        
        weigh(target) {
            this.targetWeight = target;
            const display = document.getElementById('balance-digits');
            
            // Simulation of fluctuation before settling
            let steps = 0;
            const interval = setInterval(() => {
                const noise = (Math.random() - 0.5) * (0.01 / (steps + 1));
                this.currentWeight = this.targetWeight + noise;
                display.innerText = this.currentWeight.toFixed(4);
                
                steps++;
                if (steps > 20) {
                    clearInterval(interval);
                    display.innerText = this.targetWeight.toFixed(4);
                }
            }, 50);
        }
    },

    // --- SIGNIFICANT FIGURES DETAILED LOGIC ---
    sigFigs: {
        analyze(numStr) {
            numStr = numStr.trim();
            if (numStr === "" || isNaN(numStr)) return null;

            let rules = [];
            let count = 0;
            let s = numStr.replace(/^-/, ''); // Remove negative sign

            if (!s.includes('.')) {
                // Integer Logic
                let firstNonZero = s.search(/[1-9]/);
                let lastNonZero = s.search(/[1-9](?!.*[1-9])/);
                
                if (firstNonZero === -1) {
                    count = 0;
                    rules.push("शून्य (Zero) अकेला सार्थक नहीं है।");
                } else {
                    count = lastNonZero + 1 - 0; // Trailing zeros in integers are ambiguous, usually not sig
                    // Standard convention: trailing zeros in integer without decimal are NOT sig
                    count = lastNonZero - firstNonZero + 1;
                    rules.push("नियम 1: सभी गैर-शून्य अंक सार्थक होते हैं।");
                    if (s.endsWith('0')) rules.push("नियम 2: बिना दशमलव वाली संख्या के अंत में आने वाले शून्य आमतौर पर सार्थक नहीं होते।");
                }
            } else {
                // Decimal Logic
                let clean = s.replace('.', '');
                let firstNonZero = clean.search(/[1-9]/);
                
                if (firstNonZero === -1) {
                    count = 0;
                    rules.push("दशमलव के बाद केवल शून्य सार्थक नहीं होते यदि उनसे पहले कोई अंक न हो।");
                } else {
                    count = clean.length - firstNonZero;
                    rules.push("नियम 1: सभी गैर-शून्य अंक सार्थक होते हैं।");
                    rules.push("नियम 3: दशमलव वाली संख्या में अंत में आने वाले शून्य सार्थक होते हैं।");
                    if (s.startsWith('0.')) rules.push("नियम 4: शुरुआत में आने वाले शून्य (Leading zeros) कभी सार्थक नहीं होते।");
                }
            }

            return { count, rules };
        }
    },

    // --- PARTICLE BEHAVIOR LOGIC (Solid/Liquid/Gas) ---
    particles: {
        state: 'solid',
        canvas: null,
        ctx: null,
        items: [],
        animId: null,
        
        init(canvasId) {
            this.canvas = document.getElementById(canvasId);
            if (!this.canvas) return;
            this.ctx = this.canvas.getContext('2d');
            this.createParticles();
            if (this.animId) cancelAnimationFrame(this.animId);
            this.animate();
        },

        setState(newState) {
            this.state = newState;
            this.createParticles();
        },

        createParticles() {
            this.items = [];
            const count = this.state === 'gas' ? 25 : 80;
            const size = this.state === 'solid' ? 8 : 7;
            
            for(let i=0; i<count; i++) {
                let x, y;
                if (this.state === 'solid') {
                    // Grid arrangement for solid
                    const cols = 10;
                    const spacing = 25;
                    x = (this.canvas.width/2 - 125) + (i % cols) * spacing;
                    y = (this.canvas.height/2 - 75) + Math.floor(i / cols) * spacing;
                } else {
                    x = Math.random() * this.canvas.width;
                    y = Math.random() * this.canvas.height;
                }

                this.items.push({
                    x: x,
                    y: y,
                    vx: (Math.random() - 0.5) * (this.state === 'gas' ? 6 : 1),
                    vy: (Math.random() - 0.5) * (this.state === 'gas' ? 6 : 1),
                    radius: size
                });
            }
        },

        animate() {
            if (!this.ctx) return;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            
            this.items.forEach(p => {
                this.ctx.beginPath();
                this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                
                // Colors: Blue for Solid, Cyan for Liquid, Red/Pink for Gas
                if (this.state === 'solid') this.ctx.fillStyle = '#3b82f6';
                else if (this.state === 'liquid') this.ctx.fillStyle = '#22d3ee';
                else this.ctx.fillStyle = '#f43f5e';
                
                this.ctx.fill();
                this.ctx.strokeStyle = 'white';
                this.ctx.lineWidth = 1;
                this.ctx.stroke();

                if (this.state === 'gas') {
                    p.x += p.vx; p.y += p.vy;
                    if(p.x < 0 || p.x > this.canvas.width) p.vx *= -1;
                    if(p.y < 0 || p.y > this.canvas.height) p.vy *= -1;
                } else if (this.state === 'solid') {
                    // High-frequency vibration
                    p.x += (Math.random() - 0.5) * 0.8;
                    p.y += (Math.random() - 0.5) * 0.8;
                } else {
                    // Liquid: restricted movement
                    p.x += p.vx * 0.5; p.y += p.vy * 0.5;
                    if(p.x < 0 || p.x > this.canvas.width) p.vx *= -1;
                    if(p.y < 0 || p.y > this.canvas.height) p.vy *= -1;
                }
            });
            this.animId = requestAnimationFrame(() => this.animate());
        }
    }
};

// Global Exposure
window.ChemistrySims = ChemistrySims;
window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('burette-liquid')) ChemistrySims.burette.init();
});
