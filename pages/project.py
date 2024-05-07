import streamlit as st 
from streamlit_extras.stoggle import stoggle

def show_project():
    st.write("Welcome to Interactive project")

    # Define the HTML code to embed the Power BI report
    power_bi_embed_code = """
    <iframe width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMTcxMWQ0NWUtOTg1Mi00YmYwLTg1NTUtMWU0MDc4OGI2ZjA2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>
    """

    st.write("Superstore PowerBI Report")
    # Display the embedded Power BI report in Streamlit only when the toggle is True
    if stoggle("Toggle Me to View the project",power_bi_embed_code):
        st.markdown(power_bi_embed_code, unsafe_allow_html=True)


    st.write( "More Project on the Way with detailed solution and case study. Stay Tuned")



if __name__ == "__main__":
    show_project()


