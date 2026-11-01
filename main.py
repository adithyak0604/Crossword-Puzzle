from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Crossword Puzzle", layout="wide")

project_dir = Path(__file__).parent
html = (project_dir / "app.html").read_text(encoding="utf-8")

components.html(html, height=850, scrolling=True)
