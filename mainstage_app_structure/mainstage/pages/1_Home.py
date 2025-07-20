import streamlit as st
import os
from utils.database import get_spotlight_user, get_all_users

st.title("🌟 Today's Spotlight")

user_id, _ = get_spotlight_user()
users = get_all_users()

# ✅ Build dynamic path to logo image
current_dir = os.path.dirname(_file_)
logo_path = os.path.join(current_dir, "..", "assets", "logo.png")

if not user_id:
    st.warning("No spotlight user selected yet.")
else:
    spotlight_user = None
    for u in users:
        if u[0] == user_id:
            spotlight_user = u
            break

    if spotlight_user:
        name, bio, image_url = spotlight_user[1], spotlight_user[2], spotlight_user[3]
        col1, col2 = st.columns([1, 3])

        with col1:
            if image_url and os.path.exists(image_url):
                st.image(image_url, width=60)
            else:
                # ✅ Use relative logo path for deployment
                st.image(logo_path, width=60)

        with col2:
            st.markdown(f"## 🧑 {name}")
            st.markdown(f"📜 {bio}")
    else:
        st.error("Spotlight user not found in database.")

# 🌍 Navigation link to Community Posts
st.divider()
st.page_link("pages/Posts.py", label="🌍 Community Posts")
