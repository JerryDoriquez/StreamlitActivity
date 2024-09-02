import streamlit as st


st.title("Welcome to My Portfolio")
st.header("About Me")


st.subheader("Autobiography")
st.write("Hi! My name is Jerry E. Doriquez Jr. I'm a 4th Year BSIT Student in Cebu Institute of Technology - University!")
st.write("I have a degree in Computer Science and have worked on various projects including web apps, data analysis, and AI models.")


st.image("Image.jpg", caption="Jerry Doriquez")


with st.expander("More about me"):
    st.write("In my free time, I enjoy playing games, reading books, and watching interesting movie series. I am somewhat of a boring person but that does not make me discouraged on finding new friends to hangout with.")

st.subheader("Portfolio")



st.write("### My Introduction Video")
st.video("https://cebuinstituteoftechnology.sharepoint.com/sites/IT334-G4SY23-24.2S/_layouts/15/stream.aspx?id=%2Fsites%2FIT334-G4SY23-24%2E2S%2FShared%20Documents%2FGeneral%2F01%20Assignment%20-%20Future%20Me%2FDoriquez%2EJerryJr%2EFutureMe%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ee293f078-5ea1-4bd4-9ae5-e56abc70d2b2")
st.video("https://cebuinstituteoftechnology.sharepoint.com/sites/IT317-G3SY2023.1STTh/_layouts/15/stream.aspx?id=%2Fsites%2FIT317-G3SY2023%2E1STTh%2FShared%20Documents%2FGeneral%2F01%20Assignment%20-%20Self%20Intro%2FDoriquez%2EJerry%2EIntro%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ee782d666-9493-4863-8d07-dbd6d2ca7a8c")

st.write("### My Skills")
skills = {
    "Programming Languages": ["Python", "JavaScript", "C", "Java"],
    "Web Technologies": ["Django", "React", "HTML/CSS"],
    "Tools": ["Git", "Docker", "Jupyter"]
}
st.table(skills)


st.subheader("Contact Me")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
    st.write(f"Thank you, {name}! Your message has been sent.")
