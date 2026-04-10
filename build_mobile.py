import re
import os

out_name = "ch1_mobile.html"

# CSS overrides to make the huge widths shrink automatically on mobile
mobile_css = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        /* Mobile Specific Overrides */
        body { margin: 0; padding: 0; overflow-x: hidden; }
        #contentToCopy { overflow-x: hidden; width: 100vw; max-width: 100%; box-sizing: border-box; }
        
        @media (max-width: 800px) {
            html { font-size: 11px !important; }
            div[style*="padding: 60px 5vw"] { padding: 30px 15px !important; }
            div[style*="100vw"] { width: 100% !important; max-width: 100% !important; }
            h1 { font-size: 3rem !important; }
            h2 { font-size: 2.5rem !important; }
            .header-banner { padding: 40px !important; border-radius: 0 0 30px 30px !important; }
            table { display: block; overflow-x: auto; white-space: nowrap; }
            #beakerLabel { font-size: 2rem !important; }
            /* Make inline-flex math wraps nicely */
            span[style*="display: inline-flex"] { flex-wrap: wrap; }
        }
    </style>
"""

# Extract Head from copy_master_ch1
master_html = open("copy_master_ch1.html", "r", encoding="utf-8").read()

head_match = re.search(r'(<head>)(.*?)(</head>)', master_html, re.IGNORECASE | re.DOTALL)
head_content = head_match.group(2) + mobile_css
head_full = f"<head>{head_content}</head>"

# Extract Main Content until the nav blocker.
# In copy_master_ch1, the bottom navigation starts with an identifiable div:
body_content = ""
content_match = re.search(r'(<div id="contentToCopy">)(.*?)(<h3 style="margin-top: 0; font-size: 3rem;">कल की क्लास के लिए तैयार! 🚀</h3>)', master_html, re.IGNORECASE | re.DOTALL)

if content_match:
    # We take the content, but we have to crop out the parent div of the h3
    # The parent div has: <div style="margin-top: 100px; padding: 71px; ...
    raw_content = content_match.group(2)
    clean_content = re.sub(r'<div\s+style="[^\"]*margin-top:\s*100px;\s*padding:\s*71px[^>]*>\s*$', '', raw_content, re.IGNORECASE | re.DOTALL)
    body_content += clean_content

# Now process part 9, 10, 11, 12
script_content = ""
for p in [9, 10, 11, 12]:
    part_file = f"ch1_parts/ch1_part{p}.html"
    if os.path.exists(part_file):
        part_html = open(part_file, "r", encoding="utf-8").read()
        section_match = re.search(r'(<section id="part\d+".*?>.*?</section>)', part_html, re.IGNORECASE | re.DOTALL)
        if section_match:
            body_content += "\n\n" + section_match.group(1)
        
        script_match = re.search(r'(<script>.*?</script>)', part_html, re.IGNORECASE | re.DOTALL)
        if script_match and "updateMolarityLab" in script_match.group(1):
            # Only add if it's the chemistry script
            script_content += "\n" + script_match.group(1)

# Compile the final document
final_doc = f"""<!DOCTYPE html>
<html lang="hi">
{head_full}
<body style="margin: 0; padding: 0;">
    <div id="contentToCopy" style="overflow:-x: hidden;">
        {body_content}
        
        <!-- MOBILE MASTER END BANNER -->
        <div style="margin-top: 50px; padding: 40px; background: #064e3b; text-align: center; color: white;">
            <h2>सम्पूर्ण अध्याय 1 समाप्त</h2>
            <p>यह मोबाइल संस्करण है।</p>
        </div>
    </div>
    {script_content}
</body>
</html>
"""

with open(out_name, "w", encoding="utf-8") as f:
    f.write(final_doc)

print("Created Mobile Complete Master:", out_name)
