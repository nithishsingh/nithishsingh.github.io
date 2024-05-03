


import os



# --- PATH SETTINGS ---

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "styles", "main.css")

with open(css_file) as f:
    styles = f.read()
styled_div = {"style": styles}  


with open(css_file) as f:
    print("<style>{}</style>".format(f.read()))

