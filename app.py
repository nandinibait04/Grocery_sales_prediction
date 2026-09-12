import streamlit as st
import pandas as pd
import joblib


# ==================================================
# LOAD TRAINED MODEL
# ==================================================

model = joblib.load("random_forest_model.pkl")


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Grocery Sales AI",
    page_icon="🛒",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* =================================================
   MAIN BACKGROUND
   ================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #f1f8f3 0%,
        #e8f5ec 50%,
        #ffffff 100%
    );
}


/* =================================================
   NORMAL TEXT
   ================================================= */

.stApp p {
    color: #1f2937 !important;
}


/* =================================================
   MAIN TITLE
   ================================================= */

.main-title {
    color: #064e3b !important;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 5px;
}


/* =================================================
   SUBTITLE
   ================================================= */

.subtitle {
    color: #374151 !important;
    font-size: 19px;
    font-weight: 500;
    margin-bottom: 15px;
}


/* =================================================
   SECTION TITLES
   ================================================= */

.section-title {
    color: #064e3b !important;
    font-size: 28px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 18px;
}


/* =================================================
   INPUT LABELS
   ================================================= */

.stApp label {
    color: #064e3b !important;
    font-weight: 700 !important;
}


/* =================================================
   NUMBER INPUT BOX
   ================================================= */

.stApp input {
    background-color: #1f2937 !important;
    color: #ffffff !important;
    border: 1px solid #4b5563 !important;
    border-radius: 10px !important;
}


/* Input placeholder */

.stApp input::placeholder {
    color: #d1d5db !important;
}


/* =================================================
   SELECT BOX
   ================================================= */

div[data-baseweb="select"] > div {
    background-color: #1f2937 !important;
    color: #ffffff !important;
    border-radius: 10px !important;
    border: 1px solid #4b5563 !important;
}


/* Selected value */

div[data-baseweb="select"] span {
    color: #ffffff !important;
}


/* Dropdown arrow */

div[data-baseweb="select"] svg {
    fill: #ffffff !important;
}


/* Dropdown menu */

ul[role="listbox"] {
    background-color: #1f2937 !important;
}


/* Dropdown options */

ul[role="listbox"] li {
    color: #ffffff !important;
}


/* =================================================
   BUTTON
   ================================================= */

.stButton > button {
    width: 100%;
    height: 55px;

    background-color: #15803d !important;
    color: #ffffff !important;

    border: none;
    border-radius: 14px;

    font-size: 19px;
    font-weight: 800;
}


.stButton > button:hover {
    background-color: #166534 !important;
    color: #ffffff !important;
}


/* =================================================
   METRICS
   ================================================= */

[data-testid="stMetricLabel"] {
    color: #374151 !important;
    font-weight: 700 !important;
}


[data-testid="stMetricValue"] {
    color: #064e3b !important;
    font-weight: 800 !important;
}


/* =================================================
   ALERT / SUCCESS TEXT
   ================================================= */

[data-testid="stAlert"] p {
    color: #064e3b !important;
    font-weight: 600 !important;
}


/* =================================================
   FOOTER
   ================================================= */

.footer-box {
    background-color: #064e3b;
    border-radius: 15px;
    padding: 22px;
    margin-top: 40px;
    text-align: center;
}


.footer-main {
    color: #ffffff !important;
    font-size: 17px;
    font-weight: 800;
}


.footer-sub {
    color: #d1fae5 !important;
    font-size: 14px;
    margin-top: 7px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

left, right = st.columns([1.5, 1])


# --------------------------------------------------
# LEFT SIDE
# --------------------------------------------------

with left:

    st.markdown(
        '<div class="main-title">'
        '🛒 Grocery Sales AI'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Smart daily sales prediction for better grocery store planning'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Use our trained Random Forest Regression model "
        "to estimate expected daily grocery sales."
    )

    st.success(
        "🤖 AI-powered   •   📊 Data-driven   •   🛒 Grocery-focused"
    )


# --------------------------------------------------
# RIGHT SIDE IMAGE
# --------------------------------------------------

with right:

    try:

        st.image(
            "grocery.jpg",
            use_container_width=True
        )

    except:

        st.info(
            "🛒 Add grocery.jpg to the project folder "
            "to display the grocery image."
        )


# ==================================================
# STORE INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">'
    '🏪 Store Information'
    '</div>',
    unsafe_allow_html=True
)


store1, store2, store3 = st.columns(3)


with store1:

    st.success(
        "🏪 Store 44"
    )


with store2:

    st.success(
        "🛒 GROCERY I"
    )


with store3:

    st.success(
        "🤖 Random Forest Regressor"
    )


# ==================================================
# INPUT SECTION
# ==================================================

st.markdown(
    '<div class="section-title">'
    '📝 Enter Prediction Details'
    '</div>',
    unsafe_allow_html=True
)


input_left, input_right = st.columns(2)


# ==================================================
# LEFT INPUTS
# ==================================================

with input_left:

    onpromotion = st.number_input(
        "🛍️ Number of Products on Promotion",
        min_value=0,
        value=20,
        step=1
    )


    year = st.number_input(
        "📅 Year",
        min_value=2013,
        max_value=2030,
        value=2017,
        step=1
    )


    month = st.number_input(
        "📆 Month",
        min_value=1,
        max_value=12,
        value=8,
        step=1
    )


# ==================================================
# RIGHT INPUTS
# ==================================================

with input_right:

    day = st.number_input(
        "📌 Day",
        min_value=1,
        max_value=31,
        value=16,
        step=1
    )


    day_of_week = st.selectbox(
        "📅 Day of Week",
        options=[
            0,
            1,
            2,
            3,
            4,
            5,
            6
        ],
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


# ==================================================
# PREDICTION BUTTON
# ==================================================

st.write("")


predict = st.button(
    "🔮 Predict Grocery Sales"
)


# ==================================================
# PREDICTION
# ==================================================

if predict:


    # ------------------------------------------------
    # CREATE INPUT DATA
    # ------------------------------------------------

    input_data = pd.DataFrame({

        "onpromotion": [
            onpromotion
        ],

        "year": [
            year
        ],

        "month": [
            month
        ],

        "day": [
            day
        ],

        "day_of_week": [
            day_of_week
        ]

    })


    # ------------------------------------------------
    # MODEL PREDICTION
    # ------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]


    # ==================================================
    # PREDICTION RESULT
    # ==================================================

    st.markdown(
        '<div class="section-title">'
        '🎯 Prediction Result'
        '</div>',
        unsafe_allow_html=True
    )


    st.success(
        f"🛒 Expected Grocery Sales: ₹{prediction:,.2f}"
    )


    st.write(
        "Prediction generated using the trained "
        "Random Forest Regression model."
    )


    # ==================================================
    # MODEL PERFORMANCE
    # ==================================================

    st.markdown(
        '<div class="section-title">'
        '📊 Model Performance'
        '</div>',
        unsafe_allow_html=True
    )


    performance1, performance2 = st.columns(2)


    with performance1:

        st.metric(
            "🤖 Model Used",
            "Random Forest"
        )


    with performance2:

        st.metric(
            "🎯 R² Score",
            "0.8173"
        )


    # ==================================================
    # BUSINESS INSIGHTS
    # ==================================================

    st.markdown(
        '<div class="section-title">'
        '💡 Business Insights'
        '</div>',
        unsafe_allow_html=True
    )


    st.info(
        f"Based on the selected conditions, "
        f"the expected grocery sales are "
        f"₹{prediction:,.2f}."
    )


    st.write(
        "This prediction can help the shopkeeper with:"
    )


    business1, business2, business3, business4 = st.columns(4)


    with business1:

        st.success(
            "📦 Inventory Planning"
        )


    with business2:

        st.success(
            "🛍️ Stock Management"
        )


    with business3:

        st.success(
            "🚚 Purchase Planning"
        )


    with business4:

        st.success(
            "📈 Sales Decisions"
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    '<div class="footer-box">'
    '<div class="footer-main">'
    '🛒 Grocery Sales AI | Store 44 – GROCERY I'
    '</div>'
    '<div class="footer-sub">'
    'Smart prediction for smarter grocery management'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)