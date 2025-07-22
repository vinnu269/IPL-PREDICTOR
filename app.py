import streamlit as st
import pickle
import pandas as pd

# Load the models and data
teams = pickle.load(open("team.pkl", "rb"))
cities = pickle.load(open("city.pkl", "rb"))
pipe = pickle.load(open("pipe.pkl", "rb"))

# Filter out any non-string values from cities (additional safety check)
cities = [city for city in cities if isinstance(city, str)]

st.title("IPL Win Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team", sorted(teams))
with col2:
    bowling_team = st.selectbox("Select the bowling team", sorted(teams))

selected_city = st.selectbox("Select host city", sorted(cities))

target = st.number_input("Target", min_value=1, max_value=350, value=150)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Score", min_value=0, max_value=350, value=0)
with col4:
    # Cricket-specific overs input
    overs_whole = st.number_input("Overs completed (whole number)", min_value=0, max_value=19, value=0)
    balls = st.selectbox("Balls in current over", [0, 1, 2, 3, 4, 5], index=0)
    overs = overs_whole + (balls / 10)  # Convert to decimal format (e.g., 5.3 for 5 overs 3 balls)
    st.write(f"Total overs: {overs_whole}.{balls}")
with col5:
    wickets = st.number_input("Wickets out", min_value=0, max_value=10, value=0)

if st.button("Predict Probability"):
    if batting_team == bowling_team:
        st.error("Batting and Bowling team cannot be the same!")
    else:
        try:
            # Calculate remaining balls
            balls_completed = overs_whole * 6 + balls
            remaining_balls = 120 - balls_completed
            
            # Calculate wickets left (remaining wickets)
            wickets_left = 10 - wickets
            
            # Calculate target left
            target_left = target - score
            
            # Calculate current run rate (avoid division by zero)
            if balls_completed > 0:
                crr = (score * 6) / balls_completed
            else:
                crr = 0
            
            # Calculate required run rate (avoid division by zero)
            if remaining_balls > 0:
                rrr = (target_left * 6) / remaining_balls
            else:
                rrr = 0 if target_left <= 0 else float("inf")
            
            # Create input DataFrame with exact feature names expected by the model
            input_df = pd.DataFrame({
                "batting_team": [batting_team],
                "bowling_team": [bowling_team], 
                "city": [selected_city],
                "Score": [score],
                "Wickets": [wickets_left],
                "Remaining Balls": [remaining_balls],
                "target_left": [target_left],
                "crr": [crr],
                "rrr": [rrr]
            })
            
            # Make prediction
            result = pipe.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]
            
            st.header(f"{batting_team} - {win*100:.1f}%")
            st.header(f"{bowling_team} - {loss*100:.1f}%")
            
        except Exception as e:
            st.error(f"Error in prediction: {e}")
            st.write("Input DataFrame:")
            st.write(input_df)
            st.write("Input DataFrame dtypes:")
            st.write(input_df.dtypes)



















    

