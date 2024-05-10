import streamlit as st 


def show_project():

    st.markdown("<h1 style='text-align: center;'>Interactive Data Analysis Project Showcase</h1>", unsafe_allow_html=True)
    st.markdown("""
                
    * [Superstore Sales Analysis](#superstore-sales-analysis-report)
    * [COVID-19 Analytics Report](#covid-19-analytics-report)
    * [Telecom Churn Analysis Report](#telecom-churn-analysis-report)
                
                """,unsafe_allow_html=True)


    st.markdown("""

    # Superstore Sales Analysis Report

    ## Problem Statement
    The Superstore is a retail company that sells various products to customers across different regions. The author's aim is to develop and deliver useful analytics for the Superstore to optimize sales, inventory management, and customer satisfaction.

    ### Questions to Address:
    1. What are the overall sales trends over time?
    2. How do sales vary across different product categories and sub-categories?
    3. Which regions are the top performers in terms of sales and profit?
    4. What are some factors influencing customer satisfaction and retention?

    ## Solution Approach

    ### Data Collection and Preparation
    - **Data Source**: Superstore sales data is collected from internal databases or CSV files.
    - **Cleaning and Processing**: Data is cleaned and processed to handle missing values, outliers, and inconsistencies.

    ### Data Analysis and Visualization
    - **Sales Trends Analysis**: Utilize line charts or time series plots to visualize overall sales trends over time.
    - **Product Category Analysis**: Create bar charts or pie charts to analyze sales distribution across different product categories and sub-categories.
    - **Regional Performance Comparison**: Use geographical maps or bar charts to compare sales and profit performance across different regions.
    - **Customer Satisfaction Analysis**: Employ sentiment analysis or customer surveys to identify factors influencing customer satisfaction and retention, such as product quality, pricing, and customer service.

    ### Recommendations and Insights
    - **Product Category Strategy**: Recommend focusing on high-margin product categories and optimizing inventory management to meet customer demand.
    - **Regional Sales Strategy**: Propose targeted marketing campaigns and promotions in top-performing regions to further boost sales and profit.
    - **Customer Satisfaction Initiatives**: Suggest investing in customer service training and product quality improvement to enhance customer satisfaction and retention.
    - **Data-driven Decision Making**: Emphasize the importance of data-driven decision-making in driving business growth and improving overall performance.

                
                """, unsafe_allow_html=True)


    superstore_bi = """
    <iframe title="Superstore Dashboard" width="800" height="486" src="https://app.powerbi.com/view?r=eyJrIjoiMTcxMWQ0NWUtOTg1Mi00YmYwLTg1NTUtMWU0MDc4OGI2ZjA2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>
    """
    st.markdown(superstore_bi,unsafe_allow_html=True)

    st.markdown("""
                
            ## Skills Utilized
            - **Data Analysis**: Leveraged data analysis techniques to uncover insights into sales trends and regional performance.
            - **Data Visualization**: Utilized data visualization tools to present sales data and trends in a visually appealing and informative manner.
            - **Customer Analytics**: Employed customer analytics techniques to understand factors influencing customer satisfaction and retention.
            - **Business Strategy**: Developed actionable recommendations to drive business growth and improve overall performance.

            ## Conclusion
            In conclusion, this report provides valuable insights into Superstore sales trends, product performance, regional performance, and customer satisfaction. By leveraging data analytics and visualization techniques, the Superstore can make informed decisions to optimize sales, improve customer satisfaction, and drive business growth.

                """, unsafe_allow_html=True)


    st.write("---")


    st.markdown("""

    # COVID-19 Analytics Report

    ## Problem Statement
    The coronavirus disease 2019 (COVID-19) is rapidly spreading disease that has gained attention around the globe. The author's aim is to develop and deliver useful COVID-19 analytics for public use to combat and report the spread of COVID-19.

    ### Questions to Address:
    1. How's the current COVID-19 global statistics (total cases, new cases, total deaths, and total vaccination) at a glance?
    2. How's the performance of countries compared to each other?
    3. How's the COVID-19 vaccination distribution amongst countries?
    4. What are some of the factors driving full vaccination rate?

    ## Solution Approach

    ### Data Collection and Preparation
    - **Data Source**: COVID-19 data is collected from reliable sources like WHO, CDC, and John Hopkins University.
    - **Cleaning and Processing**: Data is cleaned and processed to remove inconsistencies and missing values.

    ### Data Analysis and Visualization
    - **Global Statistics Overview**: Utilize line charts and summary statistics to present global COVID-19 statistics such as total cases, new cases, total deaths, and total vaccinations.
    - **Country Performance Comparison**: Create bar charts or heatmaps to compare COVID-19 performance metrics across countries.
    - **Vaccination Distribution Visualization**: Use geographical maps or stacked bar charts to visualize the distribution of COVID-19 vaccinations among countries.
    - **Factors Driving Vaccination Rates**: Employ regression analysis or correlation matrices to identify factors influencing full vaccination rates, such as GDP, healthcare infrastructure, and public health policies.

    ### Recommendations and Insights
    - **Policy Recommendations**: Based on the analysis, recommend policy interventions to improve COVID-19 response, such as increasing vaccination coverage, implementing targeted lockdown measures, and enhancing healthcare capacity.
    - **Public Awareness Campaigns**: Propose public awareness campaigns to promote vaccination, mask-wearing, and social distancing.
    - **Data-driven Decision Making**: Emphasize the importance of data-driven decision-making in combating the spread of COVID-19 and mitigating its impact on public health and the economy.




    """, unsafe_allow_html= True)


    covid19_bi ="""<iframe title="Covid_19 Dashboard" width="800" height="486" src="https://app.powerbi.com/view?r=eyJrIjoiZGQ2Y2M2NjQtNzQ5My00NDg1LTgyMjgtMGQyNTFhZTM3NzQwIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>"""
    st.markdown(covid19_bi,unsafe_allow_html=True)


    st.markdown("""
                
    ## Skills Utilized
    - **Data Analysis**: Leveraged data analysis techniques to gain insights into COVID-19 trends and patterns.
    - **Data Visualization**: Utilized data visualization tools to present complex COVID-19 data in a clear and intuitive manner.
    - **Statistical Modeling**: Employed statistical modeling techniques to identify factors influencing COVID-19 vaccination rates.
    - **Communication**: Effectively communicated findings and recommendations to stakeholders through clear and concise reports.

    ## Conclusion
    In conclusion, this report provides valuable insights into the global COVID-19 situation and offers actionable recommendations to combat the spread of the virus. By leveraging data analytics and visualization techniques, we can better understand the dynamics of the pandemic and inform evidence-based decision-making to protect public health and safety.


                """,unsafe_allow_html=True)


    st.write("***")


    st.markdown("""

    # Telecom Churn Analysis Report

    ## Problem Statement
    Telecom companies often face challenges related to customer churn, where customers switch to competitors' services. The author's aim is to develop and deliver useful analytics for telecom companies to understand and reduce churn rates, thereby improving customer retention and profitability.

    ### Questions to Address:
    1. What are the overall churn rates over time?
    2. How do churn rates vary across different customer segments (e.g., age, gender, plan type)?
    3. What are the key factors influencing churn?
    4. How can the telecom company reduce churn and improve customer retention?

    ## Solution Approach

    ### Data Collection and Preparation
    - **Data Source**: Telecom churn data is collected from internal databases or CRM systems.
    - **Cleaning and Processing**: Data is cleaned and processed to handle missing values, outliers, and inconsistencies.

    ### Data Analysis and Visualization
    - **Churn Trends Analysis**: Utilize line charts or time series plots to visualize overall churn rates over time.
    - **Segmentation Analysis**: Create bar charts or pie charts to analyze churn rates across different customer segments.
    - **Factor Analysis**: Employ statistical techniques (e.g., logistic regression) or machine learning algorithms (e.g., decision trees) to identify key factors influencing churn.
    - **Predictive Modeling**: Build predictive models to forecast future churn and identify at-risk customers.

    ### Recommendations and Insights
    - **Segment-specific Strategies**: Develop targeted retention strategies for high-churn customer segments, such as offering personalized discounts or incentives.
    - **Service Quality Improvement**: Identify areas for service quality improvement based on factors influencing churn (e.g., network coverage, customer service satisfaction).
    - **Customer Engagement Initiatives**: Implement proactive customer engagement initiatives, such as loyalty programs or personalized marketing campaigns, to improve customer satisfaction and loyalty.
    - **Data-driven Decision Making**: Emphasize the importance of data-driven decision-making in identifying churn drivers and implementing effective retention strategies.



    """,unsafe_allow_html=True)


    churn_bi = """<iframe title="Churn Dashboard" width="800" height="486" src="https://app.powerbi.com/view?r=eyJrIjoiYTU0ZjY1MmYtY2E1Zi00YTkzLWIyNGQtNDIzY2NhMmY5ODI1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>"""
    
    st.markdown(churn_bi,unsafe_allow_html=True)

    st.markdown("""
                
    ## Skills Utilized
    - **Data Analysis**: Leveraged data analysis techniques to uncover insights into churn trends and factors influencing churn.
    - **Predictive Modeling**: Built predictive models to forecast churn and identify at-risk customers.
    - **Customer Segmentation**: Conducted segmentation analysis to understand churn patterns across different customer segments.
    - **Business Strategy**: Developed actionable recommendations to reduce churn and improve customer retention.

    ## Conclusion
    In conclusion, this report provides valuable insights into telecom churn trends, customer segmentation, and factors influencing churn. By leveraging data analytics and predictive modeling techniques, telecom companies can make informed decisions to reduce churn, improve customer retention, and enhance profitability.
                """)


    st.write("***")


    # Define the concluding statement
    st.header("**More Projects Coming Soon!**")
    st.write("Stay tuned for more exciting projects featuring detailed solutions, case studies, and demonstrations of advanced data analytics techniques.")







if __name__ == "__main__":
    show_project()
