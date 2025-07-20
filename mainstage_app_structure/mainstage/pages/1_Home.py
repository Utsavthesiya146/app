# import streamlit as st
# import os
# from utils.database import get_spotlight_user, get_all_users

# st.title("🌟 Today's Spotlight")

# user_id, _ = get_spotlight_user()
# users = get_all_users()

# if not user_id:
#     st.warning("No spotlight user selected yet.")
# else:
#     spotlight_user = None
#     for u in users:
#         if u[0] == user_id:
#             spotlight_user = u
#             break

#     if spotlight_user:
#         name, bio, image_path = spotlight_user[1], spotlight_user[2], spotlight_user[3]
#         col1, col2 = st.columns([1, 3])

#         with col1:
#             if image_path and os.path.exists(image_path):
#                 st.image(image_path, width=180)
#             else:
#                 st.image("https://via.placeholder.com/180", caption="No Image")

#         with col2:
#             st.markdown(f"## 🧑 {name}")
#             st.markdown(f"📜 {bio}")
#     else:
#         st.error("Spotlight user not found in database.")

# # 🌍 Navigation link to Community Posts
# st.divider()
# st.page_link("pages/Posts.py", label="🌍 Community Posts")


# import streamlit as st
# import os
# from utils.database import get_spotlight_user, get_all_users

# # ✅ Display logo (works in deployment and locally)
# def get_logo_path():
#     possible_paths = [
#         "assets/logo.png",
#         os.path.join(os.path.dirname(__file__), "../assets/logo.png"),
#         os.path.join(os.getcwd(), "assets/logo.png"),
#     ]
#     for path in possible_paths:
#         if os.path.exists(path):
#             return path
#     return None

# logo_path = get_logo_path()
# if logo_path:
#     st.image(logo_path, width=60)
# else:
#     st.warning("⚠️ Logo not found in assets/logo.png")

# # 🌟 Main content
# st.title("🌟 Today's Spotlight")

# user_id, _ = get_spotlight_user()
# users = get_all_users()

# if not user_id:
#     st.warning("No spotlight user selected yet.")
# else:
#     spotlight_user = None
#     for u in users:
#         if u[0] == user_id:
#             spotlight_user = u
#             break

#     if spotlight_user:
#         name, bio, image_path = spotlight_user[1], spotlight_user[2], spotlight_user[3]
#         col1, col2 = st.columns([1, 3])

#         with col1:
#             if image_path and os.path.exists(image_path):
#                 st.image(image_path, width=180)
#             else:
#                 st.image("https://via.placeholder.com/180", caption="No Image")

#         with col2:
#             st.markdown(f"## 🧑 {name}")
#             st.markdown(f"📜 {bio}")
#     else:
#         st.error("Spotlight user not found in database.")

# # 🌍 Navigation link to Community Posts
# st.divider()
# st.page_link("pages/Posts.py", label="🌍 Community Posts")



# import streamlit as st
# import os
# from utils.database import get_spotlight_user, get_all_users

# # ✅ Display logo (works in deployment and locally)
# def get_logo_path():
#     possible_paths = [
#         "assets/logo.png",
#         os.path.join(os.path.dirname(__file__), "../assets/logo.png"),
#         os.path.join(os.getcwd(), "assets/logo.png"),
#     ]
#     for path in possible_paths:
#         if os.path.exists(path):
#             return path
#     return None

# logo_path = get_logo_path()
# if logo_path:
#     st.image(logo_path, width=60)
# else:
#     st.warning("⚠️ Logo not found in assets/logo.png")

# # 🌟 Main content
# st.title("🌟 Today's Spotlight")

# user_id, _ = get_spotlight_user()
# users = get_all_users()

# if not user_id:
#     st.warning("No spotlight user selected yet.")
# else:
#     spotlight_user = None
#     for u in users:
#         if u[0] == user_id:
#             spotlight_user = u
#             break

#     if spotlight_user:
#         name, bio, image_path = spotlight_user[1], spotlight_user[2], spotlight_user[3]
#         col1, col2 = st.columns([1, 3])

#         with col1:
#             if image_path:
#                 abs_img_path = os.path.abspath(image_path)
#                 if os.path.exists(abs_img_path):
#                     st.image(abs_img_path, width=180)
#                 else:
#                     st.image("https://via.placeholder.com/180", caption="Image not found")
#             else:
#                 st.image("https://via.placeholder.com/180", caption="No Image")

#         with col2:
#             st.markdown(f"## 🧑 {name}")
#             st.markdown(f"📜 {bio}")
#     else:
#         st.error("Spotlight user not found in database.")

# # 🌍 Navigation link to Community Posts
# st.divider()
# st.page_link("pages/Posts.py", label="🌍 Community Posts")






import streamlit as st
import os
from utils.database import get_spotlight_user, get_all_users

# ✅ Display logo (relative path only)
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=60)
else:
    st.warning("⚠️ Logo not found")

# 🌟 Main content
st.title("🌟 Today's Spotlight")

user_id, _ = get_spotlight_user()
users = get_all_users()

if not user_id:
    st.warning("No spotlight user selected yet.")
else:
    spotlight_user = None
    for u in users:
        if u[0] == user_id:
            spotlight_user = u
            break

    if spotlight_user:
        name, bio, image_path = spotlight_user[1], spotlight_user[2], spotlight_user[3]
        col1, col2 = st.columns([1, 3])

        with col1:
            if image_path:
                # Make sure path is relative inside the app directory (e.g. assets/profile1.png)
                if os.path.exists(image_path):
                    st.image(image_path, width=180)
                else:
                    st.image("https://via.placeholder.com/180", caption="Image not found")
            else:
                st.image("https://via.placeholder.com/180", caption="No Image")

        with col2:
            st.markdown(f"## 🧑 {name}")
            st.markdown(f"📜 {bio}")
    else:
        st.error("Spotlight user not found in database.")

# 🌍 Navigation link to Community Posts
st.divider()
st.page_link("pages/Posts.py", label="🌍 Community Posts")

