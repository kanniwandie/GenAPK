# intuition2025

## Project Overview
This repository contains a Streamlit-based web application integrated with Google Generative AI (Gemini) to automatically generate and manage Android application projects using natural language prompts.

## Features
- **Natural Language to Android App**: Converts user prompts into fully functional Android apps.
- **Automated Gradle Building**: Automatically handles the building and compiling of Android apps.
- **Streamlit Interface**: User-friendly web-based interface.

## Project Structure
```
intuition2025/
├── pages/
│   ├── chat.py         # Chat interface with Gemini AI
│   ├── code.py         # Code viewer and project handler
│   └── present.py      # Presentation page
├── template/
│   ├── MyApp/          # Android app template
│   └── template.yaml
├── transform.py        # Transforms user prompts into Android apps
├── build.py            # Automates Gradle build
├── uploadtonet.py      # Handles file uploads
├── requestapi.py       # API requests and handling
├── schema.py           # Database or data schema management
└── ask.py              # Interface for AI queries
```

## Installation

1. Clone the repository:
```bash
git clone <repo_url>
cd intuition2025
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Streamlit App:
```bash
streamlit run main.py
```

### Project Workflow
- Enter your app idea in the chat interface.
- The AI generates an Android project based on your idea.
- Review the generated code and build the app directly through the provided interface.

## Contributing
1. Fork the repository
2. Create a new feature branch
```bash
git checkout -b feature/new-feature
```
3. Commit and push your changes
```bash
git commit -m "Add new feature"
git push origin feature/new-feature
```
4. Open a pull request

## License
This project is licensed under the MIT License.
