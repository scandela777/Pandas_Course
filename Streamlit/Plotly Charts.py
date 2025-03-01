import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#Title
st.title("Streamlit Charts")

#Read Data
df = pd.read_csv('Streamlit/employees.csv', header = 0).convert_dtypes()

labels = df[df.columns[0]]
parents = df[df.columns[1]]

data = go.Treemap(
    ids = labels,
    labels = labels,
    parents = parents,
    root_color = "lightgray"
)

fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Icicle(
    ids = labels,
    labels = labels,
    parents = parents,
    root_color = "lightgray"
)

fig = go.Figure(data)
st.plotly_chart(fig, use_container_width= True)

data = go.Sunburst(
    ids = labels,
    labels= labels,
    parents=parents,
    insidetextorientation='horizontal' #Set the text orientation
)

fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))

fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)