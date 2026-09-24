import streamlit as st
import pandas as pd
import pickle
import os

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Grocery Sales Prediction",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# 2. LOAD RANDOM FOREST MODEL
# ==========================================

MODEL_PATH = "random_forest_model.pkl"

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model.")
    st.error(str(e))
    st.stop()

# ==========================================
# 3. GROCERY BACKGROUND AND CSS
# ==========================================

st.markdown("""
<style>

/* Grocery background image */
.stApp {
    background-image:
        linear-gradient(
            rgba(240, 255, 245, 0.88),
            rgba(240, 255, 245, 0.88)
        ),
        url("https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=1920&q=85");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main heading */
.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #075E35;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    font-size: 19px;
    color: #263C32;
}

/* Section headings */
.section-title {
    font-size: 27px;
    font-weight: 750;
    color: #075E35;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Information cards */
.info-card {
    background: rgba(205, 245, 220, 0.95);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #B7E6C7;
    text-align: center;
    color: #123D28;
    font-size: 17px;
    font-weight: 600;
}

/* Prediction result card */
.result-card {
    background: linear-gradient(135deg, #075E35, #16864D);
    padding: 28px;
    border-radius: 18px;
    text-align: center;
    color: white;
    box-shadow: 0 5px 18px rgba(0, 60, 30, 0.20);
}

/* Result text */
.result-label {
    font-size: 20px;
    font-weight: 600;
    color: white;
}

.result-value {
    font-size: 40px;
    font-weight: 800;
    color: white;
}

/* General text */
p, label, .stMarkdown {
    color: #183B2B;
}

/* Input boxes */
div[data-baseweb="input"] {
    background-color: white;
    border-radius: 8px;
}

div[data-baseweb="input"] input {
    color: #111111 !important;
}

/* Predict button */
.stButton > button {
    background-color: #087A3E;
    color: white;
    border-radius: 10px;
    border: none;
    font-size: 20px;
    font-weight: 700;
    padding: 12px 25px;
    width: 100%;
}

.stButton > button:hover {
    background-color: #045A2D;
    color: white;
}

/* Hide Streamlit menu and footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. HEADER
# ==========================================

st.markdown("""
<div class="main-title">
    🛒 Grocery Sales AI
</div>

<div class="subtitle">
    Smart daily sales prediction for better grocery store planning
</div>

<br>

<p style="font-size:17px;">
    Use our trained Random Forest Regression model
    to estimate expected daily grocery sales.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:rgba(190,245,210,0.92);
    padding:15px;
    border-radius:12px;
    font-size:17px;
    font-weight:600;
    color:#075E35;">
    🟢 AI-powered &nbsp; | &nbsp;
    📊 Data-driven &nbsp; | &nbsp;
    🛒 Grocery-focused
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# 5. STORE INFORMATION
# ==========================================

st.markdown(
    '<div class="section-title">🏬 Store Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        🏬 Store 44
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        🛒 GROCERY I
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        🌳 Random Forest Regressor
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================
# 6. USER INPUTS
# ==========================================

st.markdown(
    '<div class="section-title">📝 Enter Prediction Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    onpromotion = st.number_input(
        "🛍️ Number of Products on Promotion",
        min_value=0,
        max_value=10000,
        value=20,
        step=1
    )

    year = st.number_input(
        "📅 Year",
        min_value=2013,
        max_value=2035,
        value=2017,
        step=1
    )

    month = st.selectbox(
        "🗓️ Month",
        options=list(range(1, 13)),
        index=7
    )

with col2:

    day = st.number_input(
        "📌 Day",
        min_value=1,
        max_value=31,
        value=16,
        step=1
    )

    day_of_week = st.selectbox(
        "📆 Day of Week (Monday = 0)",
        options=list(range(7)),
        index=2
    )

# ==========================================
# 7. PREDICTION
# ==========================================

st.write("")

predict_button = st.button(
    "🛒 Predict Grocery Sales",
    use_container_width=True
)

if predict_button:

    # Validate date
    try:
        input_date = pd.Timestamp(
            year=int(year),
            month=int(month),
            day=int(day)
        )

        actual_day_of_week = input_date.dayofweek

        if int(day_of_week) != actual_day_of_week:
            st.warning(
                f"The selected date falls on weekday "
                f"{actual_day_of_week} (Monday = 0). "
                "Please check the Day of Week input."
            )

        # Prepare model input in the trained feature order
        input_data = pd.DataFrame(
            [[
                int(onpromotion),
                int(year),
                int(month),
                int(day),
                int(day_of_week)
            ]],
            columns=[
                "onpromotion",
                "year",
                "month",
                "day",
                "day_of_week"
            ]
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Display prediction
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card">

            <div class="result-label">
                🛒 PREDICTED DAILY SALES
            </div>

            <div class="result-value">
                {prediction:,.2f}
            </div>

            <div style="font-size:18px;color:white;">
                Estimated sales in units
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.success(
            "Prediction generated successfully "
            "using the Random Forest Regressor."
        )

        # Business applications
        st.markdown(
            '<div class="section-title">💡 Business Applications</div>',
            unsafe_allow_html=True
        )

        b1, b2, b3 = st.columns(3)

        with b1:
            st.markdown("""
            <div class="info-card">
                📦 Inventory Planning
            </div>
            """, unsafe_allow_html=True)

        with b2:
            st.markdown("""
            <div class="info-card">
                🛍️ Stock Management
            </div>
            """, unsafe_allow_html=True)

        with b3:
            st.markdown("""
            <div class="info-card">
                📊 Purchase Planning
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "Note: Predictions are estimates based on historical "
            "data and the trained model. Actual sales may differ."
        )

    except ValueError:
        st.error(
            "Please enter a valid date and prediction details."
        )

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.exception(e)

# ==========================================
# 8. FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    color:#075E35;
    font-size:15px;
    font-weight:600;">

    Grocery Sales Prediction Using Machine Learning
    <br>
    Store 44 | Random Forest Regression

</div>
""", unsafe_allow_html=True)
month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=8,
    step=1
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=16,
    step=1
)

day_of_week = st.selectbox(
    "Day of Week",
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ][x]
)

st.divider()

# Prediction button
if st.button("🔮 Predict Sales"):

    input_data = pd.DataFrame({
        "onpromotion": [onpromotion],
        "year": [year],
        "month": [month],
        "day": [day],
        "day_of_week": [day_of_week]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"📊 Predicted Grocery Sales: {prediction:,.2f}"
    )

    st.info(
        "This prediction is generated using the trained "
        "Random Forest Regression model."
    )
