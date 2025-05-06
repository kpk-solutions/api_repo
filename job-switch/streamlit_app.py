import streamlit as st
import requests
import plotly.express as px
from app.logger import logger

def get_job_demand(skill):
    url = f"http://fastapi:8000/get-jobs/{skill}"
    response = requests.get(url)
    return response.json()

def get_job_trend(skill):
    url = f"http://localhost:8000/job-demand-trend/{skill}"
    response = requests.get(url)
    return response.json()

# Streamlit UI
st.title("Job Demand Tracker")

skill = st.text_input("Enter a Skill", "Python")
if st.button("Get Job Demand"):
    demand_data = get_job_demand(skill)
    logger.info(f"demand_data: {demand_data}")
    st.write(f"Job Count: {demand_data['job_count']}")
    # st.write(f"Job Count: {demand_data}")
    
    trend_data = get_job_trend(skill)
    st.plotly_chart(trend_data)  # Assuming `trend_data` contains Plotly chart data
