import streamlit as st

st.set_page_config(
    page_title="Main",
    page_icon="💻",
)

st.write("# ✨GenAPK✨ ")

st.markdown(
    """ GenAPK is a groundbreaking platform that turns your ideas into fully functional mobile apps in less than a minute. Unlike website generators, which are common, mobile app generators are rare—and GenAPK stands out by not only generating clean, production-ready code but also building the app, hosting it, and letting you test it instantly—no manual coding, building, or downloading required. Share a link with friends to try your app on iOS or Android, and if you love it, publish the APK directly.

**With GenAPK you can:**

🔹 Automated App Generation:  Converts simple text prompts into production-ready Java/XML code, following Material Design best practices.  

🔹 End-to-End Workflow: Covers the full lifecycle: code generation, building, testing, and deployment.

🔹 Automated Builds: Automatically compiles and builds the app into an APK using Gradle, streamlining the process.

🔹 Instant testing and sharing: Deploys apps to Appetize for live testing on iOS & Android and generates shareable link for instant access without downloads.

🔹 Integrated Hosting: The only platform that not only generates the app but also hosts it immediately, eliminating deployment friction.

**Why GenAPK?**

💡 More Than Just Code: Unlike other generators, GenAPK doesn’t just output code—it builds and tests the app, allowing you use it right away.

🌐 Instant Sharing: Share your app with a link, no downloads or installations required.

📱 Cross-Platform: Apps work for both Android and iOS, allowing you to reach a wider audience.

**For:**

✔️ Entrepreneurs: Validate app ideas without coding or hiring developers.

✔️ Educators: Teach app development with real, functional examples.

✔️ Developers: Rapidly prototype and test MVPs.

✔️ Hobbyists: Build and share apps with friends for fun."""
)
nav = st.button("Get Started")
if nav:
    st.switch_page("pages/chat.py")
