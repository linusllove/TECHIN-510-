import streamlit as st

st.set_page_config(
    page_title="Tianyi Mu",
    page_icon="🤖",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
) 

col1, col2 = st.columns([0.5, 0.5])
with col1:
   st.image('photo.jpg', width=300, caption='Profile Image')
with col2:
    st.markdown(
        """
    # Tianyi Mu (He/Him)
                
    Student at [GIX](https://gix.uw.edu/)
    """
    )

st.markdown(
    """
# Education

- [University of Southern California](https://www.usc.edu/)
- [University of Washington](https://www.washington.edu/)

# Work Experience

- [Resume](https://drive.google.com/file/d/1LmliGla8-iHmYFBjubRD7nGZklnAZ3EN/view?usp=sharing)

# Interesting Projects

- [Project 1]
- [Project 2]
- [Project 3]
- [Project 4]
"""
)

st.markdown(
    """
# Pictures
""")




ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href=" " target="_blank">Streamlit</a ><br 'style= top:3px;'>
with < img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a ></p >
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)