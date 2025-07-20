# import streamlit as st
# import sqlite3
# import os
# from utils.database import DB_FILE

# def get_leaderboard():
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT users.name, users.image_url, COUNT(votes.id) as vote_count
#         FROM users
#         LEFT JOIN votes ON users.id = votes.voted_user_id
#         GROUP BY users.id
#         ORDER BY vote_count DESC
#         LIMIT 10;
#     """)
#     results = cursor.fetchall()
#     conn.close()
#     return results

# # Set page config
# st.set_page_config(page_title="🏆 Leaderboard", layout="centered")
# st.title("🏆 MainStage Leaderboard")

# # Load leaders
# leaders = get_leaderboard()

# if leaders:
#     for i, (name, image_url, votes) in enumerate(leaders, start=1):
#         col1, col2 = st.columns([1, 6])

#         with col1:
#             # ✅ Show user's image if available and file exists
#             if image_url and os.path.exists(image_url):
#                 st.image(image_url, width=60)
#             else:
#                 # 🖼️ Show app logo if user has no image
#                 st.image("D:\\mainstage_app_structure\\mainstage\\assets\\logo.png", width=60)

#         with col2:
#             st.markdown(f"### {i}. {name}")
#             st.markdown(f"⭐ **Votes:** `{votes}`")
#             st.markdown("---")
# else:
#     st.info("No votes yet. Be the first to shine! ✨")











# import streamlit as st
# import sqlite3
# import os
# from utils.database import DB_FILE

# # Load leaderboard data
# def get_leaderboard():
#     conn = sqlite3.connect(DB_FILE)
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT users.name, users.image_url, COUNT(votes.id) as vote_count
#         FROM users
#         LEFT JOIN votes ON users.id = votes.voted_user_id
#         GROUP BY users.id
#         ORDER BY vote_count DESC
#         LIMIT 10;
#     """)
#     results = cursor.fetchall()
#     conn.close()
#     return results

# # Set Streamlit page config
# st.set_page_config(page_title="🏆 Leaderboard", layout="centered")
# st.title("🏆 MainStage Leaderboard")

# # Get leaderboard data
# leaders = get_leaderboard()

# # Get logo path dynamically
# logo_path = os.path.join("assets", "logo.png")

# if leaders:
#     for i, (name, image_url, votes) in enumerate(leaders, start=1):
#         col1, col2 = st.columns([1, 6])

#         with col1:
#             # ✅ Show user image if valid path and file exists
#             if image_url and os.path.exists(image_url):
#                 st.image(image_url, width=60)
#             elif os.path.exists(logo_path):
#                 st.image(logo_path, width=60)
#             else:
#                 st.text("📷")

#         with col2:
#             st.markdown(f"### {i}. {name}")
#             st.markdown(f"⭐ **Votes:** `{votes}`")
#             st.markdown("---")
# else:
#     st.info("No votes yet. Be the first to shine! ✨")










import streamlit as st
import sqlite3
import os
from utils.database import DB_FILE

# ✅ Build dynamic path to logo image
current_dir = os.path.dirname(__file__)
logo_path = os.path.join(current_dir, "..", "assets", "logo.png")

def get_leaderboard():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.name, users.image_url, COUNT(votes.id) as vote_count
        FROM users
        LEFT JOIN votes ON users.id = votes.voted_user_id
        GROUP BY users.id
        ORDER BY vote_count DESC
        LIMIT 10;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Page settings
st.set_page_config(page_title="🏆 Leaderboard", layout="centered")
st.title("🏆 MainStage Leaderboard")

# ✅ Load leaders
leaders = get_leaderboard()

if leaders:
    for i, (name, image_url, votes) in enumerate(leaders, start=1):
        col1, col2 = st.columns([1, 6])

        with col1:
            # ✅ Show user's image if available and file exists
            if image_url and os.path.exists(image_url):
                st.image(image_url, width=60)
            else:
                # ✅ Use relative logo path for deployment
                st.image(logo_path, width=60)

        with col2:
            st.markdown(f"### {i}. {name}")
            st.markdown(f"⭐ **Votes:** `{votes}`")
            st.markdown("---")
else:
    st.info("No votes yet. Be the first to shine! ✨")

