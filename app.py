

import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg 



pages = ["Home","Project", "GitHub"]

# --- PATH SETTINGS ---

parent_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(parent_dir, "styles", "main.css")
resume_file = os.path.join(parent_dir, "assets", "Nithish Singh.pdf")
profile_pic = os.path.join(parent_dir, "assets", "passport.jpg")
logo_path = os.path.join(parent_dir, "assets", "atoms.svg")
urls = {"GitHub": "https://github.com/nithishsingh"}
styles = {
	"nav": {
        "background-color": "#222831",  # Background color of the navigation bar
        "font-color": "#EEEEEE",  # Font color of the navigation bar
		"justify-content": "center"
    },
	"img": {
		"padding-rig\ht": "10px",
	},
    "div": {
        "max-width": "31.25rem",  # Maximum width of the navigation bar
    },
    "span": {
        "color": "#EEEEEE",  # Color of text in navigation links
        "border-radius": "0.5rem",  # Border radius of navigation links
        "padding": "0.4375rem 0.625rem",  # Padding of navigation links
        "margin": "0 0.125rem",  # Margin of navigation links
    },
    "active": {
        "background-color": "#00ADB5",  # Background color of the active page
		"color": "var(--text-color)",
		"font-color" : "Black"
    },
    "hover": {
        "background-color": "#393E46",  # Background color on hover
    },
	"a": {  # Style for anchor elements (social media links)
        "color": "white",  # white color for the social media links
        "text-decoration": "none",  # Remove underline from the links if needed
        "font-weight": "bold"  # Optionally set font weight
    }
}




# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nithish Singh"
PAGE_ICON =":full_moon_with_face:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="collapsed" )



page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    adjust=True,
)

functions = {
    "Home": pg.show_home,
    "Project" : pg.show_project,
    
}
go_to = functions.get(page)
if go_to:
    go_to()




