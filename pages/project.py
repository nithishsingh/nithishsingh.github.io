import streamlit as st 
from streamlit_extras.stoggle import stoggle

def show_project():

    
    st.title("**Interactive Data Analysis Project Showcase**")
    st.write("Welcome to the interactive project showcase! Explore the Superstore PowerBI Report below and get insights into the data analysis process.")
    
    # Define the project description
    st.header("**Project Description**")
    st.write("This project involves analyzing the sales data of a superstore using PowerBI. The objective is to uncover key insights and trends to inform business decisions.")
    
    # Define the solution
    st.header("**Solution**")
    st.write("Utilizing PowerBI, we created an interactive dashboard that visualizes sales performance across different product categories, regions, and time periods. The dashboard provides actionable insights to improve inventory management, optimize sales strategies, and enhance overall profitability.")
    
    # Define the skills used
    st.header("**Skills Demonstrated**")
    st.write("This project showcases proficiency in data analysis, data visualization, and dashboard creation using PowerBI. Additionally, it highlights the ability to extract meaningful insights from complex datasets and communicate findings effectively.")
    
    # Define the key takeaways
    st.header("**Key Takeaways**")
    st.write("1. **Insightful Visualization**: Gain a deeper understanding of sales trends and performance through interactive visualizations.")
    st.write("2. **Actionable Insights**: Identify opportunities for improving sales strategies, optimizing inventory, and enhancing profitability.")
    st.write("3. **Skill Development**: Enhance your data analysis and visualization skills by exploring the PowerBI dashboard.")
    

    # Define the HTML code to embed the Power BI report
    power_bi_embed_code = """
    <iframe width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMTcxMWQ0NWUtOTg1Mi00YmYwLTg1NTUtMWU0MDc4OGI2ZjA2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>
    """
    
    # Display the embedded Power BI report in Streamlit only when the toggle is True
    st.header("**Superstore PowerBI Report**")
    stoggle("Click to View the Project", power_bi_embed_code)

    # Define the concluding statement
    st.header("**More Projects Coming Soon!**")
    st.write("Stay tuned for more exciting projects featuring detailed solutions, case studies, and demonstrations of advanced data analytics techniques.")







if __name__ == "__main__":
    show_project()
