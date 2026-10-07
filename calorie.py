import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Kusuma's Calorie Calculator",
    page_icon="🍎",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff1eb, #ace0f9);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #d35400;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555555;
    margin-bottom: 30px;
}

.calculator-box {
    background: rgba(255, 255, 255, 0.90);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
}

.result-box {
    background: linear-gradient(135deg, #ff9966, #ff5e62);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-top: 25px;
}

.calorie-number {
    font-size: 40px;
    font-weight: bold;
}

.info-box {
    background: #fff8e7;
    padding: 18px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.markdown(
    "<div class='main-title'>🍎 Kusuma's Calorie Calculator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>✨ Estimate Your Daily Calorie Requirement ✨</div>",
    unsafe_allow_html=True
)


# ---------------- CALCULATOR ----------------
st.markdown(
    "<div class='calculator-box'>",
    unsafe_allow_html=True
)

st.subheader("👤 Enter Your Details")

# Gender
gender = st.selectbox(
    "⚧️ Gender",
    ["Male", "Female"]
)

# Age
age = st.number_input(
    "🎂 Age",
    min_value=10,
    max_value=100,
    value=20,
    step=1
)

# Weight
weight = st.number_input(
    "⚖️ Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=60.0,
    step=0.5
)

# Height
height = st.number_input(
    "📏 Height (cm)",
    min_value=100.0,
    max_value=230.0,
    value=165.0,
    step=0.5
)

# Activity
activity = st.selectbox(
    "🏃 Select Your Activity Level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Very hard exercise"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- CALCULATE BUTTON ----------------
st.write("")

if st.button("🔥 Calculate Calories", use_container_width=True):

    # ---------------- BMR CALCULATION ----------------
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161


    # ---------------- ACTIVITY FACTOR ----------------
    if activity.startswith("Sedentary"):
        activity_factor = 1.2

    elif activity.startswith("Lightly"):
        activity_factor = 1.375

    elif activity.startswith("Moderately"):
        activity_factor = 1.55

    elif activity.startswith("Very"):
        activity_factor = 1.725

    else:
        activity_factor = 1.9


    # ---------------- DAILY CALORIE CALCULATION ----------------
    daily_calories = bmr * activity_factor


    # ---------------- RESULT ----------------
    st.markdown(
        f"""
        <div class='result-box'>
            <div style='font-size:22px;'>🔥 Estimated Daily Calories</div>
            <div class='calorie-number'>{daily_calories:.0f} kcal</div>
            <div>per day</div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ---------------- BMR ----------------
    st.subheader("📊 Your Calculation")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🔥 BMR",
            f"{bmr:.0f} kcal"
        )

    with col2:
        st.metric(
            "⚡ Daily Requirement",
            f"{daily_calories:.0f} kcal"
        )


    # ---------------- INTERPRETATION ----------------
    st.subheader("💡 Simple Interpretation")

    st.info(
        f"Based on the details you entered, your estimated daily "
        f"calorie requirement is approximately **{daily_calories:.0f} kcal per day**."
    )

    st.markdown(
        """
        <div class='info-box'>
        <b>📌 What does this mean?</b><br><br>
        
        🔹 <b>BMR</b> is the approximate number of calories your body
        needs for basic functions like breathing and circulation.<br><br>
        
        🔹 Your <b>daily calorie requirement</b> also considers your
        physical activity level.<br><br>
        
        🔹 This number is an estimate and should not be treated as
        a medical or nutritional prescription.
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<center>🍎 Kusuma's Calorie Calculator • Stay Active • Stay Healthy 🌿</center>",
    unsafe_allow_html=True
)