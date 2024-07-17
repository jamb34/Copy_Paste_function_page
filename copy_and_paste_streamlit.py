import shutil
import os
import streamlit as st

def copy_folder_contents(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for item in os.listdir(src_folder):
        s = os.path.join(src_folder, item)
        d = os.path.join(dest_folder, item)
        try:
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        except Exception as e:
            st.error(f"Failed to copy {s} to {d}: {e}")

# Streamlit interface
st.title("Copy and Paste Function")

src_folder = st.text_input("Initial folder")
dest_folder = st.text_input("Desired Destination ")

if st.button("Run Copy Process"):
    if src_folder and dest_folder:
        if os.path.exists(src_folder):
            copy_folder_contents(src_folder, dest_folder)
            st.success("Copying complete!")
        else:
            st.error("Source folder does not exist")
    else:
        st.warning("Please provide both source and destination folders")
