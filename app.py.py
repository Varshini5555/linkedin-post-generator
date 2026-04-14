import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.subheader("LinkedIn Post Generator")

    # Create three columns for the dropdowns
    col1, col2, col3, col4 = st.columns(4)

    fs = FewShotPosts()

    
    name_options=fs.get_names()

    with col4:
        selected_name = st.selectbox("Writing Style", options=["Any"] + name_options)
    
    name = None if selected_name == "Any" else selected_name
    tags = fs.get_tags_by_name(selected_name)

    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    



    # Generate Button
    if st.button("Generate"):

        post = generate_post(selected_length, selected_language, selected_tag,name)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()