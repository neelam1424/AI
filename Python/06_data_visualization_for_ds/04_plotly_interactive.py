import pandas as pd
import plotly.express as px

df = pd.read_csv("data/students.csv")

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="course",
    hover_data=["name", "attendance", "city"],
    title="Interactive Study Hours vs Marks"
)

fig.show()

fig.write_html("charts/interactive_study_hours_vs_marks.html")