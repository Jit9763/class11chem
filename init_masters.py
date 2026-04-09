import os

chapters = [
    "रसायन विज्ञान की कुछ मूल अवधारणाएँ",
    "परमाणु की संरचना",
    "तत्त्वों का वर्गीकरण एवं गुणधर्मों में आवर्तिता",
    "रासायनिक आबंधन तथा आण्विक संरचना",
    "रासायनिक ऊष्मागतिकी",
    "साम्यावस्था",
    "अपचयोपचय अभिक्रियाएँ (रेडॉक्स अभिक्रियाएँ)",
    "कार्बनिक रसायन: कुछ आधारभूत सिद्धांत तथा तकनीकें",
    "हाइड्रोकार्बन"
]

def generate_copy_master(i, title):
    content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Chapter {i} COPY MASTER - Premium Notes</title>
</head>
<body>
    <div id="contentToCopy">
        <div style="font-family: 'Outfit', sans-serif; line-height: 1.8; color: #064e3b; max-width: 900px; margin: auto;">
            <div style="text-align: center; border-bottom: 4px solid #059669; padding-bottom: 30px; margin-bottom: 50px; background: #ecfdf5; padding-top: 40px; border-radius: 0 0 50px 50px;">
                <h1 style="color: #065f46; font-size: 3rem; margin-bottom: 10px;">अध्याय {i}: {title}</h1>
                <p style="font-size: 1.3rem; color: #047857; font-weight: 600;">प्रीमियम उच्च-घनत्व शैक्षणिक नोट्स</p>
            </div>

            <div style="background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #d1fae5;">
                <h2 style="color: #064e3b; border-left: 8px solid #059669; padding-left: 20px; margin-bottom: 30px;">अध्याय का परिचय (Introduction)</h2>
                <p style="font-size: 1.2rem; color: #1f2937;">यह अध्याय कक्षा 11 रसायन विज्ञान का एक अत्यंत महत्वपूर्ण भाग है। इसमें हम {title} के मूलभूत सिद्धांतों और बारीकियों का अध्ययन करेंगे।</p>
                
                <div style="margin-top: 50px; padding: 30px; background: #fffbeb; border: 2px dashed #f59e0b; border-radius: 15px; text-align: center;">
                    <p style="font-size: 1.5rem; color: #b45309; font-weight: bold;">⚠️ विस्तार सामग्री पर कार्य जारी है...</p>
                    <p style="color: #92400e;">हमारे विशेषज्ञ अध्यापक इस चैप्टर के "50-पेज उच्च-घनत्व नोट्स" तैयार कर रहे हैं। जल्द ही यहाँ विस्तृत सामग्री अपडेट की जाएगी।</p>
                </div>
            </div>

            <div style="margin-top: 60px; text-align: center; padding: 20px; color: #6b7280; font-style: italic; border-top: 1px solid #e5e7eb;">
                © 2026 रसायन विज्ञान प्रीमियम पोर्टल | गुणवत्तापूर्ण शिक्षा के लिए समर्पित
            </div>
        </div>
    </div>
</body>
</html>"""
    return content

def generate_qa_master(i, title):
    content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Chapter {i} Q&A MASTER - Premium Notes</title>
</head>
<body>
    <div id="contentToCopy">
        <div style="font-family: 'Outfit', sans-serif; line-height: 1.8; color: #1e1b4b; max-width: 900px; margin: auto;">
            <div style="text-align: center; border-bottom: 4px solid #8b5cf6; padding-bottom: 30px; margin-bottom: 50px; background: #f5f3ff; padding-top: 40px; border-radius: 0 0 50px 50px;">
                <h1 style="color: #4c1d95; font-size: 3rem; margin-bottom: 10px;">अध्याय {i}: प्रश्न-उत्तर बैंक</h1>
                <p style="font-size: 1.3rem; color: #6d28d9; font-weight: 600;">{title} - मास्टर Q&A</p>
            </div>

            <div style="background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #ede9fe;">
                <h2 style="color: #1e1b4b; border-left: 8px solid #8b5cf6; padding-left: 20px; margin-bottom: 30px;">महत्वपूर्ण बोर्ड एवं प्रतियोगी परीक्षा प्रश्न</h2>
                
                <div style="margin-top: 50px; padding: 30px; background: #fdf2f8; border: 2px dashed #db2777; border-radius: 15px; text-align: center;">
                    <p style="font-size: 1.5rem; color: #9d174d; font-weight: bold;">⚠️ Q&A अपडेट प्रक्रिया में है...</p>
                    <p style="color: #be185d;">इस अध्याय के लिए महत्वपूर्ण प्रश्नों का चयन किया जा रहा है। जल्द ही यहाँ NCERT सॉल्यूशंस और पिछले वर्षों के प्रश्न अपलोड किए जाएंगे।</p>
                </div>
            </div>

            <div style="margin-top: 60px; text-align: center; padding: 20px; color: #6b7280; font-style: italic; border-top: 1px solid #e5e7eb;">
                © 2026 रसायन विज्ञान प्रीमियम पोर्टल
            </div>
        </div>
    </div>
</body>
</html>"""
    return content

# Current directory
base_path = r"c:\Users\jiten\Desktop\class11\Chem11"

for i, title in enumerate(chapters, 1):
    copy_file = os.path.join(base_path, f"copy_master_ch{i}.html")
    qa_file = os.path.join(base_path, f"qa_master_ch{i}.html")
    
    # We skip ch1 for now as it has some content we might want to salvage/expand
    if i > 1:
        with open(copy_file, "w", encoding="utf-8") as f:
            f.write(generate_copy_master(i, title))
        with open(qa_file, "w", encoding="utf-8") as f:
            f.write(generate_qa_master(i, title))
    else:
        # Just ensure QA Master 1 is also premium look if not already (ch1 Notes we will rewrite anyway)
        with open(qa_file, "w", encoding="utf-8") as f:
            f.write(generate_qa_master(i, title))

print("All master files initialized with premium templates.")
