# ------------------------------
# Import Libraries
# ------------------------------
import streamlit as st
import numpy as np
import soundfile as sf
import io
from PIL import Image, ImageDraw
from scipy.signal import sawtooth
import random
import streamlit.components.v1 as components

# ------------------------------
# Load the Kyma Logo
# ------------------------------
logo_image = Image.open('logo.png')

# ------------------------------
# 1. Define Frequencies and Emotional Intentions
# ------------------------------

solfeggio_frequencies = {
    "174 Hz - Foundation and Stability": 174.0,
    "285 Hz - Healing Tissues and Organs": 285.0,
    "396 Hz - Liberating Guilt and Fear": 396.0,
    "417 Hz - Facilitating Change": 417.0,
    "528 Hz - Transformation and DNA Repair": 528.0,
    "639 Hz - Harmonizing Relationships": 639.0,
    "741 Hz - Expression and Solutions": 741.0,
    "852 Hz - Awakening Intuition": 852.0,
    "963 Hz - Spiritual Connection": 963.0,
}

brainwave_frequencies = {
    "Delta (0.5 - 4 Hz)": 2.0,
    "Theta (4 - 8 Hz)": 6.0,
    "Alpha (8 - 14 Hz)": 10.0,
    "Beta (14 - 30 Hz)": 20.0,
    "Gamma (30 - 100 Hz)": 40.0,
}

emotional_intentions = {
    "Love": "Pink",
    "Calm": "Light Blue",
    "Healing": "Green",
    "Gratitude": "Gold",
    "Courage": "Red"
}

color_mapping = {
    "Pink": "#FFC0CB",
    "Light Blue": "#ADD8E6",
    "Green": "#008000",
    "Gold": "#FFD700",
    "Red": "#FF0000"
}

# ------------------------------
# 2. User Interface with Streamlit
# ------------------------------

# Set custom page configuration
st.set_page_config(
    page_title="Kyma - 🎶 Binaural Beats & Cymatics",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🎶",
)

# Add custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #FFFFFF;
        }
        .sidebar .sidebar-content {
            background-color: #F0F2F6;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #262730;
        }
    </style>
    """, unsafe_allow_html=True)

# Display the Kyma logo at the top of the app
st.image(logo_image, use_column_width=True)

# Display app title and description
st.title("🎶 Binaural Beats with Cymatics & Emotional Intentions")
st.write("Generate personalized binaural beats with visualizations based on solfeggio frequencies, brainwave patterns, or emotional intentions.")

# Display the Kyma logo in the sidebar
st.sidebar.image(logo_image, use_column_width=True)

# Sidebar Controls
st.sidebar.header("🔧 Audio Controls")

with st.sidebar.expander("Frequency Selection"):
    # Selection for Frequency Type
    frequency_type = st.radio(
        "Select Frequency Type",
        ("Solfeggio Frequency", "Brainwave Pattern", "Custom Frequency", "Emotional Intention"),
        index=0
    )

    # Frequency Selection Based on User Choice
    base_freq = 0.0
    beat_freq = 0.0
    color = "#1e90ff"  # Default color for visualizations

    if frequency_type == "Solfeggio Frequency":
        solfeggio_choice = st.selectbox("🌎 Select Solfeggio Frequency", options=list(solfeggio_frequencies.keys()), index=0)
        base_freq = solfeggio_frequencies[solfeggio_choice]
        beat_freq = 10.0

    elif frequency_type == "Brainwave Pattern":
        brainwave_choice = st.selectbox("🧐 Select Brainwave Pattern", options=list(brainwave_frequencies.keys()), index=0)
        base_freq = 200.0
        beat_freq = brainwave_frequencies[brainwave_choice]

    elif frequency_type == "Custom Frequency":
        base_freq_input = st.text_input("✏️ Base Frequency (Hz)", value="440.0")
        try:
            base_freq = float(base_freq_input)
            if base_freq <= 0:
                st.error("Please enter a positive number for the base frequency.")
        except ValueError:
            st.error("Invalid input. Please enter a numeric value for the base frequency.")
            base_freq = 440.0
        beat_freq = 10.0

    elif frequency_type == "Emotional Intention":
        emotional_intention = st.selectbox("💖 Select Emotional Intention", options=list(emotional_intentions.keys()), index=0)
        base_freq = random.choice(list(solfeggio_frequencies.values()))
        beat_freq = 10.0
        color = emotional_intentions[emotional_intention]

with st.sidebar.expander("Additional Controls"):
    # Additional Controls
    panning = st.slider("Panning (Left - Right)", -1.0, 1.0, 0.0, help="Adjust the stereo panning of the audio.")
    volume = st.slider("Volume", 0.0, 1.0, 0.5, help="Adjust the playback volume.")
    duration_input = st.text_input("Duration (seconds)", "10")
    try:
        duration = float(duration_input)
        if duration <= 0:
            st.error("Please enter a positive number for the duration.")
    except ValueError:
        st.error("Invalid input. Please enter a numeric value for the duration.")
        duration = 10.0

    # Generate waveform selection
    waveform = st.selectbox("Select Waveform", options=["Sine", "Square", "Sawtooth", "Triangle"])

# Generate Button
generate_button = st.sidebar.button("Generate")

# ------------------------------
# 3. Generate Binaural Beats or Isochronic Tones
# ------------------------------

if generate_button:
    if base_freq <= 0 or beat_freq <= 0:
        st.error("Frequencies must be positive numbers.")
    else:
        with st.spinner('Generating audio, please wait...'):
            sample_rate = 44100
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

            # Function to generate waveform
            def generate_waveform(waveform_type, frequency, t):
                if waveform_type == "Sine":
                    return np.sin(2 * np.pi * frequency * t)
                elif waveform_type == "Square":
                    return np.sign(np.sin(2 * np.pi * frequency * t))
                elif waveform_type == "Sawtooth":
                    return sawtooth(2 * np.pi * frequency * t)
                elif waveform_type == "Triangle":
                    return 2 * np.abs(sawtooth(2 * np.pi * frequency * t)) - 1

            # Generate Stereo Audio with Panning and Volume Adjustments
            left_wave = generate_waveform(waveform, base_freq, t)
            right_wave = generate_waveform(waveform, base_freq + beat_freq, t)

            left_channel = volume * left_wave * (1 - abs(panning))
            right_channel = volume * right_wave * (1 + abs(panning))
            stereo_audio = np.vstack((left_channel, right_channel)).T

            # Isochronic Tone Generation
            isochronic_tone = sawtooth(2 * np.pi * beat_freq * t, width=0.5)
            isochronic_tone = np.repeat(isochronic_tone[:, np.newaxis], 2, axis=1) * volume

            # Combine audio
            combined_audio = stereo_audio + isochronic_tone

            # Normalize audio to prevent clipping
            max_amplitude = np.max(np.abs(combined_audio))
            if max_amplitude > 1:
                combined_audio = combined_audio / max_amplitude

            # Prepare audio for playback
            audio_buffer = io.BytesIO()
            sf.write(audio_buffer, combined_audio, sample_rate, format="WAV")
            audio_buffer.seek(0)

        st.success('Audio generation complete!')

        # Audio Output
        st.audio(audio_buffer, format="audio/wav")
        st.download_button("Download Audio", data=audio_buffer, file_name="binaural_beats.wav")

# ------------------------------
# 4. Animated Cymatic Visualization with Downloadable Still Frame
# ------------------------------

st.markdown("## 🌌 Cymatic Visualization")

# Map color names to CSS color codes
visualization_color = color_mapping.get(color, "#FFFFFF")

animation_html = f"""
<html>
<head>
    <style>
        #waveCanvas {{
            border: 1px solid black;
            width: 100%;
            height: 500px;
            background-color: black;
        }}
    </style>
</head>
<body>
    <canvas id="waveCanvas"></canvas>
    <script>
        var canvas = document.getElementById('waveCanvas');
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        var ctx = canvas.getContext('2d');

        var width = canvas.width;
        var height = canvas.height;
        var frequency = {base_freq};
        var amplitude = 1;
        var waveSpeed = {beat_freq};
        var t = 0;
        var visualizationColor = '{visualization_color}';

        function drawPattern() {{
            ctx.clearRect(0, 0, width, height);
            ctx.fillStyle = visualizationColor;

            var numPoints = 600;
            for (let x = 0; x < width; x += width / numPoints) {{
                for (let y = 0; y < height; y += height / numPoints) {{
                    let distance = Math.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2);
                    let value = Math.sin(frequency * 0.001 * distance - t);
                    if (Math.abs(value) < 0.05) {{
                        ctx.beginPath();
                        ctx.arc(x, y, 1, 0, 2 * Math.PI);
                        ctx.fill();
                    }}
                }}
            }}

            t += waveSpeed * 0.05;
            requestAnimationFrame(drawPattern);
        }}

        window.onload = function() {{
            drawPattern();
        }}
    </script>
</body>
</html>
"""

# Display the animated cymatic visualization
components.html(animation_html, height=500, scrolling=False)

# Create a still frame image for download
if st.sidebar.button("Download Still Frame"):
    img_size = (800, 800)
    img = Image.new("RGB", img_size, "black")
    draw = ImageDraw.Draw(img)

    num_points = 600
    for x in range(0, img_size[0], img_size[0] // num_points):
        for y in range(0, img_size[1], img_size[1] // num_points):
            distance = np.sqrt((x - img_size[0] / 2) ** 2 + (y - img_size[1] / 2) ** 2)
            value = np.sin(base_freq * 0.001 * distance)
            if abs(value) < 0.05:
                draw.ellipse((x, y, x + 2, y + 2), fill=visualization_color)

    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    st.download_button(
        label="Download Cymatic Still Frame",
        data=img_buffer,
        file_name="cymatic_still_frame.png",
        mime="image/png"
    )

# ------------------------------
# 5. Scientific Validation and Education
# ------------------------------

st.markdown("## 🧪 Scientific Validation")
st.write("""
We are committed to providing an evidence-based approach to binaural beats, brainwave entrainment, and cymatics. Below are some key research studies that explore these phenomena:
""")

# Binaural Beats and Brainwave Entrainment
st.markdown("### **1. Binaural Beats and Brainwave Entrainment**")

st.markdown("""
**Lane et al. (1998)**  
*Binaural auditory beats affect vigilance performance and mood.*  
**Journal:** Physiology & Behavior, 63(2), 249-252.  
[DOI: 10.1016/S0031-9384(97)00436-8](https://doi.org/10.1016/S0031-9384(97)00436-8)

This study investigates how binaural beats influence vigilance and mood, finding that certain frequencies can affect alertness and emotional states.

---

**Wahbeh et al. (2007)**  
*Binaural beat technology in humans: a pilot study to assess psychologic and physiologic effects.*  
**Journal:** The Journal of Alternative and Complementary Medicine, 13(1), 25-32.  
[DOI: 10.1089/acm.2006.6196](https://doi.org/10.1089/acm.2006.6196)

This pilot study explores the psychological and physiological effects of binaural beat technology, suggesting potential benefits for mood enhancement and stress reduction.

---

**Goodin et al. (2012)**  
*The effect of binaural beat audio on cognitive processing: a pilot study.*  
**Journal:** Current Psychology, 31(1), 125-135.  
[DOI: 10.1007/s12144-012-9136-5](https://doi.org/10.1007/s12144-012-9136-5)

This study examines how binaural beats may influence cognitive functions such as attention and memory, indicating potential cognitive enhancement effects.
""")

# Cymatics
st.markdown("### **2. Cymatics**")

st.markdown("""
**Jenny (2001)**  
*Cymatics: A Study of Wave Phenomena & Vibration.*  
**Publisher:** MACROmedia Publishing.

Hans Jenny's seminal work demonstrates how sound vibrations create geometric patterns in various media, laying the foundation for the field of cymatics.
""")

# Disclaimer
st.markdown("""
**Disclaimer:** The studies referenced are for informational purposes. Individual results may vary. Please consult a healthcare professional for personalized advice.
""")

# Additional Resources
st.markdown("""
### **Additional Resources**

- **National Institutes of Health (NIH):** [Music and Health](https://www.nih.gov/news-events/news-releases/nih-researchers-explore-how-music-may-affect-brain)
- **American Psychological Association (APA):** [The Power of Music](https://www.apa.org/monitor/2013/11/music)
""")

# Educational Content
st.markdown("## 📚 Educational Content")
st.write("""
- **Binaural Beats**: When two slightly different frequencies are presented to each ear, the brain perceives a third tone called a binaural beat. This phenomenon is thought to promote a brainwave state matching the frequency difference. For more details, see [Lane et al. (1998)](https://doi.org/10.1016/S0031-9384(97)00436-8).

- **Brainwave Entrainment**: Techniques like binaural beats synchronize brainwave frequencies with an external stimulus, potentially promoting relaxation, focus, or meditation. Learn more from [Huang & Charyton (2008)](https://pubmed.ncbi.nlm.nih.gov/18806909/).

- **Cymatics**: Cymatics is the study of visible sound and vibration. When sound frequencies interact with physical mediums like sand or water, they create intricate patterns. Explore this concept in Hans Jenny's work, *Cymatics: A Study of Wave Phenomena & Vibration*.
""")

st.markdown("Enjoy your journey with sound and visuals!")

# ------------------------------
# Footer
# ------------------------------
st.markdown("""
<hr>
<center>
<p>© 2023 Kyma. All rights reserved.</p>
</center>
""", unsafe_allow_html=True)
