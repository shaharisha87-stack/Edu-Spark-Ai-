# EduSpark AI — Smart Study

EduSpark AI is a beginner-friendly AI study assistant built with Streamlit and Cerebras.

## Features

- **Smart Summary:** Turn uploaded study material into simple notes and key points.
- **Quiz Generator:** Create multiple-choice practice questions.
- **Ask Your Notes:** Ask questions and receive answers grounded in the uploaded material.
- **Flashcards:** Generate question-and-answer revision cards.
- **Downloads:** Save generated summaries, quizzes, and flashcards as Markdown files.

## Technology

- Python
- Streamlit
- Cerebras Cloud SDK
- PyPDF

## Run locally (optional)

1. Install Python.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the `CEREBRAS_API_KEY` environment variable, or create
   `.streamlit/secrets.toml` containing:

   ```toml
   CEREBRAS_API_KEY = "your_api_key_here"
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Deploy with GitHub and Streamlit Community Cloud

1. Create a public GitHub repository and upload `app.py`, `requirements.txt`,
   `README.md`, and `.gitignore`.
2. Open https://share.streamlit.io/ and connect GitHub.
3. Select this repository and set the main file to `app.py`.
4. Deploy the app.
5. In the deployed app settings, open **Secrets** and add:

   ```toml
   CEREBRAS_API_KEY = "your_api_key_here"
   ```

6. Save and reboot the app.

## Important security note

Never upload your Cerebras API key to GitHub. Do not commit `.streamlit/secrets.toml`.
Use Streamlit Community Cloud's Secrets settings for a deployed application.

## Notes and limitations

- This starter version supports text-based PDF files and TXT files.
- Scanned handwritten PDFs need OCR and are not supported in this first version.
- Very long documents are limited to the first 20,000 characters for each AI request.
- The model name is configurable in the sidebar. Select a model currently available
  in your Cerebras account.
- AI-generated study material can contain mistakes. Students should verify important
  facts against their course material.
