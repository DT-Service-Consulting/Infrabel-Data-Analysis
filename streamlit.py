import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)
import streamlit as st
import streamlit.components.v1 as components
# Import your preprocessing, analysis, and visualization functions
from preprocess import *
from visualization import *
from analysis import *

# Streamlit app title and description
st.title("Infrabel Data Analysis Report")

# Create two columns: one for the map and one for the color map info
col1, col2 = st.columns([5, 1])  # Adjust the width ratio as needed

# Column 1: Display the HTML map
with col1:
    st.title("ETCS Map")
    # Read the HTML map file
    with open('belgium_etcs_map (16).html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Display the HTML map using streamlit's components.html
    components.html(html_content, height=600, scrolling=True)

# Column 2: Display the color map information
with col2:
    st.write("### ETCS Level Colors")
    
    # Color mapping information
    st.write("""
    - **ETCS L1 FS**: Blue
    - **ETCS L2 FS**: Orange
    - **ETCS L1 LS**: Yellow
    - **ETCS 1+2**: Green
    - **TVM-430**: Cyan
    """)
# 1. Delay Patterns by Station and Tracks
st.header("1. Delay Patterns by Station and Tracks")
st.markdown("""
The visualization shows in **red circles** the stations with maximum waiting time, proportional to delay time. The lines with the highest delay timings are marked in **light red**. Magenta circles correspond to **incident hotspots** based on the number of incidents.
Key observations:
- Stations with the highest delays are located near the borders with **Netherlands** and **Germany**.
- Tracks near the borders also exhibit high delay timings.
            
**Caution**: This is based on one day of data (October 1st, 2024).
""")

# 2. Impact of Incidents on Delays
st.header("2. Impact of Incidents on Delays")
st.markdown("""
The incident that causes the **maximum delay** is "Intrusion in the lines." The **highest number of incidents** and delays occur on **Line 50A/3**.
Even if there is no particular incident, Line 50A/3 faces regular delays, possibly due to being a **crossroad of two major lines**.
""")

# Insert figure for incident impact
st.image('Common_incidents.png', caption="Impact of Incidents on Delays")
st.image('top_10_lines.png', caption="Top 10 lines with Delay")
st.image('heatmap.png', caption="Primary Types of Delay at Key Lines")
st.image('50A3.png', caption="Location of 50A/3")

# 3. Role of ETCS on Line 50A/3
st.header("3. Role of ETCS on Line 50A/3")
st.markdown("""
After analyzing the **ETCS level** of Line 50A/3, it was found to be at **L2 FS level**, which also corresponds to the **highest number of incidents per line**.
Despite the frequent incidents, ETCS helps in faster recovery, though there is **no significant daily impact** observed due to **small sample size**, as tested by the **Mann-Whitney U test**.
""")

# Insert figure for ETCS role on Line 50A/3
st.image('weighted_incidents.png', caption="Incidents weighted per line on ETCS levels")
st.image('recovery.png', caption="Recovery levels on Non-ECTS vs ECTS levels")
st.image('daily_delay.png', caption="Daily Delay per Line")
st.write(" As it is evident, the number of sample size of No ETCS lines is less than 27 so performed Mann-Whitney U test ")

# 4. ETCS vs. Non-ETCS Lines Over 5 Years
st.header("4. ETCS vs. Non-ETCS Lines Over 5 Years")
st.markdown("""
Over the past 5 years, during incidents, **tracks with ETCS recover faster** compared to non-ETCS lines.
In winter, **non-ETCS lines** experience much longer delays than ETCS lines.
""")

# Insert figure for ETCS vs. Non-ETCS over time
st.image('over 5 years.png', caption="ETCS vs. Non-ETCS Lines Over 5 Years")

# 5. Length of Track vs. Delays
st.header("5. Length of Track vs. Delays")
st.markdown("""
The **length of the track** does not seem to have any significant impact on delay timings.
""")

# Insert figure for track length vs. delay
st.image('correlation.png', caption="Track Length vs. Delay Timings")

# 6. Delays from Departure to Arrival
st.header("6. Delays from Departure to Arrival")
st.markdown("""
If a train is **late at departure**, it generally **does not recover** during its journey, resulting in a **late arrival** as well.
""")

# Insert figure for departure vs. arrival delays
st.image('departure arrival.png', caption="Departure vs. Arrival Delay Patterns")

# 7. Predictive Modeling for ETCS Impact
st.header("7. Predictive Modeling for ETCS Impact")
st.markdown("""
Using predictive modeling, it was found that having ETCS has an **impact of approximately 27%** on predicting delay times, with an **R-squared value of 0.58**.
This indicates that ETCS contributes significantly to the ability to forecast train delays.
""")

# Insert figure for predictive modeling
st.image('feature_importance.png', caption="ETCS Impact on Delay Prediction")

# Conclusion

st.write("### Analysis Summary")
st.write("""
This analysis explored train delays, incident hotspots, and the impact of the European Train Control System (ETCS) on the Belgian railway network, focusing on the data from October 1st, 2024. The key findings are as follows:

**Delay Patterns**: The stations with the longest delays are located near the borders with Netherlands and Germany, with certain tracks (notably Line 50A/3) experiencing higher delays.

**Incident Hotspots**: The most frequent cause of delays was "Intrusion in the lines", with Line 50A/3 showing the highest number of incidents and delays.

**ETCS Impact**: Line 50A/3, which operates at the L2 FS ETCS level, experienced frequent delays, but ETCS helped with faster recovery times during incidents compared to non-ETCS lines.

**ETCS vs. Non-ETCS**: Over a 5-year period, tracks equipped with ETCS showed significantly faster recovery times from incidents, particularly in winter, where non-ETCS lines faced much longer delays.

**Track Length**: There was no significant relationship between the length of the track and the delay time, suggesting that other factors, such as incidents or infrastructure, play a larger role.

**Departure Delays**: If a train is late at departure, it tends to stay late, resulting in delayed arrivals as well.

**Predictive Modeling**: Predictive models showed that ETCS contributed 27% to explaining delay times, with an R-squared value of 0.58, indicating its importance in forecasting train delays.

""")

st.write("### Next Steps")
st.write("""
**Data Expansion**: Expand the dataset beyond a single day to cover a larger time frame (e.g., several months or years) to identify consistent patterns in train delays and incidents. This will improve the robustness of the insights.

**Explore Seasonal Variations**: Investigate seasonal effects on delays, especially during winter months, when non-ETCS lines experience significantly longer delays. This could help determine how much ETCS mitigates winter-related disruptions.

**Incident Analysis**: Perform a deeper analysis of the types of incidents causing delays (e.g., intrusions, technical failures) and evaluate the effectiveness of current mitigation strategies. Focus on Line 50A/3 and other lines with high incidents.

**Infrastructure Improvement**: Explore whether infrastructure improvements near border stations (e.g., upgrading to higher ETCS levels) could reduce delays, especially for stations with persistent high wait times.

**ETCS Optimization**: Study whether enhancing the ETCS system (e.g., upgrading from L2 FS to higher levels or implementing ETCS on non-ETCS lines) could lead to improved recovery times and reduced delays.

**Operational Adjustments**: Investigate the impact of scheduling adjustments for trains that are consistently late at departure. This could minimize cumulative delays and improve overall punctuality.

**Enhance Predictive Models**: Incorporate additional variables (e.g., weather conditions, maintenance schedules, crew shifts) to improve the accuracy of delay predictions, and develop a more comprehensive model for real-time applications. Due to lack of time only Random Forest regressor has been used, but a plethora of Machine Learning Models can be used for predictive Modelling.
         
**Identify Ripple Effect**: Separate primary and secondary delays in the dataset. This will allow for a better understanding of cascading delays. A solution can be developed to assign secondary delays to the appropriate causes, which can inform better operational decisions to minimize the ripple effect of delays.
  
**Dashboards**: Incorporating real-time data on train delays, incidents, and infrastructure conditions into the dashboard can greatly enhance decision-making. Dynamic dashboards that show live data on train movements, delays, and predicted disruptions will help railway operators manage delays more effectively.
 Develop a real-time dashboard to track delays, categorize them as primary or secondary, and predict the impact of current incidents. Real-time visualization can also inform infrastructure maintenance scheduling and provide immediate responses to reduce cascading delays.
         
**IT Maintaince**: Even though intrusions are the most common cause of delay, infrastructure-related issues (e.g., track problems, maintenance requirements) cause the most disruptive delays. These often result in severe network-wide delays.
Prioritize maintenance schedules for critical infrastructure that frequently causes delays. Analyzing data over time will allow you to predict when and where infrastructure maintenance is needed, helping to prevent future disruptions.
""")
st.image('disruptive incidents.png', caption="Most Disruptive Incidents")