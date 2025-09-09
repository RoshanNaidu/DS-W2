import streamlit as st
import pandas as pd
import plotly.express as px
from apputil import *

# -----------------------------
# App Header
# -----------------------------
st.set_page_config(page_title="Coin Combinations App", layout="wide")
st.title("💰 Coin Combinations Calculator")
st.markdown("""
This app calculates **all possible ways** to make a given amount of cents 
using **only pennies and nickels**.
It also provides **interactive visualizations** and summaries for better understanding.
""")

# -----------------------------
# CSS-only Coin Animation
# -----------------------------
st.markdown("""
<style>
@keyframes fall {
  0% { transform: translateY(-50px) rotate(0deg); opacity: 1; }
  100% { transform: translateY(600px) rotate(360deg); opacity: 0; }
}
.coin {
  position: absolute;
  top: -50px;
  font-size: 24px;
  animation: fall 4s linear infinite;
}
.coin1 { left: 10%; animation-duration: 3s; }
.coin2 { left: 25%; animation-duration: 4s; }
.coin3 { left: 40%; animation-duration: 5s; }
.coin4 { left: 60%; animation-duration: 3.5s; }
.coin5 { left: 80%; animation-duration: 4.5s; }
</style>

<div class="coin coin1">🪙</div>
<div class="coin coin2">🪙</div>
<div class="coin coin3">🪙</div>
<div class="coin coin4">🪙</div>
<div class="coin coin5">🪙</div>
""", unsafe_allow_html=True)



# -----------------------------
# User Input
# -----------------------------
amount = st.number_input(
    "Enter an amount in cents:", 
    min_value=0, max_value=1000, step=1, value=10
)

if amount is not None:
    total_ways, combinations = ways(amount)
    st.success(f"There are **{total_ways} different ways** to make {amount} cents using pennies and nickels.")

    # -----------------------------
    # Display all combinations
    # -----------------------------
    st.subheader("All Possible Combinations")
    df_combinations = pd.DataFrame(combinations, columns=["Pennies", "Nickels"])
    st.dataframe(df_combinations)

    # -----------------------------
    # Plot combinations
    # -----------------------------
    st.subheader("Visualizing Coin Combinations")
    fig = px.scatter(
        df_combinations,
        x="Nickels",
        y="Pennies",
        size="Pennies",
        color="Nickels",
        color_continuous_scale="Viridis",
        title=f"Pennies vs Nickels for {amount} cents",
        labels={"Nickels": "Number of Nickels", "Pennies": "Number of Pennies"}
    )
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Bonus: Summary Statistics
    # -----------------------------
    st.subheader("Summary Statistics")
    st.markdown(f"""
    - Maximum pennies used: {df_combinations['Pennies'].max()}  
    - Minimum pennies used: {df_combinations['Pennies'].min()}  
    - Maximum nickels used: {df_combinations['Nickels'].max()}  
    - Minimum nickels used: {df_combinations['Nickels'].min()}  
    - Average pennies per combination: {df_combinations['Pennies'].mean():.2f}  
    - Average nickels per combination: {df_combinations['Nickels'].mean():.2f}  
    """)

    # -----------------------------
    # Beyond Expectations: Interactive Filter
    # -----------------------------
    st.subheader("Filter Combinations")
    max_nickels = st.slider("Maximum number of nickels allowed", 0, amount//5, value=amount//5)
    filtered_df = df_combinations[df_combinations["Nickels"] <= max_nickels]
    st.write(f"Showing combinations with <= {max_nickels} nickels")
    st.dataframe(filtered_df)

    fig_filtered = px.scatter(
        filtered_df,
        x="Nickels",
        y="Pennies",
        size="Pennies",
        color="Nickels",
        color_continuous_scale="Plasma",
        title=f"Filtered Pennies vs Nickels (<= {max_nickels} nickels)"
    )
    st.plotly_chart(fig_filtered, use_container_width=True)
