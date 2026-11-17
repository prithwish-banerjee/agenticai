
import streamlit as st
from youtube_analyzer import build_youtube_agent

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="YouTube AI Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #1a1640, #24243e);
    color: white;
}

/* Main container */
.block-container {
    max-width: 1000px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 40px 20px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        rgba(124, 58, 237, 0.25),
        rgba(59, 130, 246, 0.15)
    );
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
}

.hero p {
    font-size: 17px;
    color: #c4c4d4;
}

/* Input styling */
.stTextInput input {
    background-color: #201d3a !important;
    color: white !important;
    border: 1px solid #51458c !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

/* Button styling */
.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    font-size: 17px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton button:hover {
    background: linear-gradient(90deg, #6d28d9, #1d4ed8);
    transform: translateY(-2px);
    color: white;
}

/* Feature cards */
.feature-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 22px;
    text-align: center;
    min-height: 145px;
}

.feature-card h3 {
    color: #c4b5fd;
    font-size: 19px;
}

.feature-card p {
    color: #c4c4d4;
    font-size: 14px;
}

/* Footer */
.custom-footer {
    text-align: center;
    color: #9292a8;
    margin-top: 60px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

# ---------------- HEADER ----------------

st.html("""
<div class="hero">
    <h1>🎥 YouTube AI Analyzer</h1>
    <p>
        Turn any YouTube video into meaningful insights.
        <br>
        Powered by Artificial Intelligence.
    </p>
</div>
""")


# ---------------- AGENT ----------------

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()


# ---------------- INPUT SECTION ----------------

st.markdown("### 🔗 Analyze Your YouTube Video")

st.write(
    "Paste a YouTube video URL below and let AI generate "
    "a detailed analysis for you."
)

video_url = st.text_input(
    "YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=example",
    label_visibility="collapsed"
)

analyze_button = st.button("✨ Analyze Video")


# ---------------- ANALYSIS ----------------

if analyze_button:

    if not video_url.strip():
        st.warning("⚠️ Please enter a YouTube video URL.")

    elif not (
        "youtube.com/" in video_url.lower()
        or "youtu.be/" in video_url.lower()
    ):
        st.error("Please enter a valid YouTube URL.")

    else:

        try:
            with st.spinner(
                "🤖 AI is analyzing your video... Please wait."
            ):

                response = agent.run(
                    f"Analyze this YouTube video in detail: {video_url}"
                )

            st.success("✅ Video analysis completed successfully!")

            st.markdown("---")

            st.markdown("## 📊 Analysis Report")

            with st.container(border=True):
                st.markdown(response.content)

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")


# ---------------- FEATURES ----------------

st.markdown("---")

st.markdown(
    "<h2 style='text-align:center;'>✨ What Can This Tool Do?</h2>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧠 AI Insights</h3>
        <p>Understand the key concepts and important ideas of a video.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📝 Smart Summary</h3>
        <p>Get a structured summary of lengthy YouTube videos.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Save Time</h3>
        <p>Extract useful information without watching the entire video.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="custom-footer">
    Built by Prithwish Banerjee
    <br><br>
    © 2026 YouTube AI Analyzer
</div>
""", unsafe_allow_html=True)
