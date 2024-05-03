import streamlit as st 
from PIL import Image


def show_home():
    # General settings
    PAGE_TITLE = "Digital CV | Nithish Singh"
    PAGE_ICON = ":atom:"
    NAME = "Nithish Singh"
    DESCRIPTION = """
    Data Analyst, assisting enterprises by supporting data-driven decision-making.
    """
    EMAIL = "nithishsingha@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://linkedin.com/in/nithishsingh",
        "GitHub": "https://github.com/nithishsingh",
        "Blog": "https://github.com/nithishsingh",
    }

    # Load resources
    css_file = "styles\main.css"
    resume_file_path = "assets\\NithishSingh.pdf"
    profile_pic_path = r"assets\photo.png"
    logo_path = r"assets\atoms.svg"

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    with open(resume_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    profile_pic = Image.open(profile_pic_path)

    # Hero Section
    
    col1, col2 = st.columns(2, gap = "small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file_path,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # Social links

    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # Summary section
    st.markdown('## Summary', unsafe_allow_html=True)
    st.info('''
    Dynamic Data Analyst skilled in Python, SQL, and cloud computing. Proven track record in delivering actionable insights, leading teams, and enhancing brand loyalty. Proficient in visualization tools like Power BI and Tableau. Committed to continuous learning and recently completed a successful data science internship.
    ''')


    st.write("----")

    # Custom function for printing text
    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    def txt2(a, b):
        col1, col2 = st.columns([1,4])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)

    def txt3(a, b):
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    def txt4(a, b, c):
        col1, col2, col3 = st.columns([1.5,2,2])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

    #####################
    st.markdown('''
    ## Education
    ''')

    txt('**Bachelor of Engineering** (Computer Science Engineering), *Adhiyamaan College Of Engineering*, Hosur, TN, India',
    '06/2016 - 05/2020')
    st.markdown('''
	- Awarded Best Student for outstanding academic performance during 2017.
	- Conducted iFest, Python Tutorial, showcasing leadership and organizational skills.
	- Graduated with a major in Computer Science Engineering.
	- Developed a strong foundation in computer science principles, including programming, algorithms, and data structures.
	- Engaged in practical coursework and projects to apply theoretical knowledge to real-world problems.
	- Participated in extracurricular activities and events to enhance teamwork, leadership, and communication skills.
    ''')

    #####################
    st.markdown('''
    ## Work Experience
    ''')

    txt('**Data Analyst**, NielsenIQ, Chennai, TN, India', '11/2021 - 01/2023')
    st.markdown('''
    - Identified new market segments through retail & CPG data analysis, boosting a major FMCG client's sales by 15% in 6 months.
    - Built a 25% more accurate sales forecasting model, empowering clients with optimized inventory decisions.
    - Led a team uncovering key drivers of brand loyalty, resulting in a 10% repeat purchase increase for a major retailer.
    - Communicated complex data insights effectively to stakeholders using Power BI & Tableau.
    - Mentored junior team members in data analysis best practices and tools.
    ''')

    txt('**Network Support Engineer** ,GEE VEE FAB, Hosur, TN, India', '05/2019 - 10/2021')
    st.markdown('''
    - Developed & implemented disaster recovery plans, guaranteeing business continuity during unforeseen events.
    - Enhanced network stability & reduced downtime by 30% through network optimization.
    - Consistently exceeded client expectations with timely technical support, achieving a 95% satisfaction rate.
    - Elevated network security & user awareness through protocol implementation & training programs.
    - Increased network security by 40% through new security protocols and training programs for employees.
    ''')

    #####################
    st.markdown('''
    ## Projects
    ''')

    txt('**Stock Prediction**, Predicting stock prices using a TensorFlow LSTM neural network for times series forecasting', '(07/2021)')
    txt('**IPL Data Analysis**, Analyzing IPL data between 2018 - 2020, finding patterns and answering questions ','(04/2021)')

    #####################
    st.markdown('''
    ## Course Work
    ''')

    txt('**Data Analysis with Python**', 'IBM')
    txt('**Machine Learning Bootcamp with Data Science**', 'Udemy')

    #####################
    st.markdown('''
    ## Internship
    ''')

    txt('**Data Science Intern**', 'BCG Job Simulation, Forage, 03/2024')
    st.markdown('''
    - Completed a customer churn analysis simulation for XYZ Analytics, demonstrating advanced data analytics skills.
    - Conducted efficient data analysis using Python, including Pandas and NumPy.
    - Optimized a random forest model, achieving an 85% accuracy rate in predicting customer churn.
    - Delivered a concise executive summary for informed decision-making based on analysis.
    ''')
    
	#####################
    st.markdown('''
    ## Skills
    ''')
    txt3('Programming', '`Python`, `R`, `Linux`')
    txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
    txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
    txt3('BI Tools', '`Power BI`, `Tabluae`, `Looker`, `QlikView`')
    txt3('Machine Learning', '`scikit-learn`')
    txt3('Deep Learning', '`TensorFlow`')
    txt3('Web development', '`streamlit`, `HTML`, `CSS`,`Nextjs`')
    txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

    #####################
    


    



if __name__ == "__main__":
    show_home()