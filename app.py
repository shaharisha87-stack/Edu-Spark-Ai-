import json
from pathlib import Path
from datetime import datetime

import streamlit as st

NOTES_FILE = Path("notes.json")


def load_notes():
    if not NOTES_FILE.exists():
        return []

    try:
        return json.loads(NOTES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_notes(notes):
    NOTES_FILE.write_text(
        json.dumps(notes, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


st.set_page_config(page_title="Smart Notes", page_icon="📝", layout="centered")

st.title("📝 Smart Notes")
st.write("Write, organize, and search your notes.")

notes = load_notes()

with st.form("new_note", clear_on_submit=True):
    title = st.text_input("Title")
    content = st.text_area("Your note", height=160)
    submitted = st.form_submit_button("Save note")

    if submitted:
        if title.strip() and content.strip():
            notes.insert(
                0,
                {
                    "id": datetime.now().isoformat(),
                    "title": title.strip(),
                    "content": content.strip(),
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                },
            )
            save_notes(notes)
            st.success("Note saved!")
            st.rerun()
        else:
            st.warning("Please enter both a title and note.")

st.divider()

search = st.text_input("🔎 Search notes")
filtered_notes = [
    note
    for note in notes
    if search.lower() in note["title"].lower()
    or search.lower() in note["content"].lower()
]

if not filtered_notes:
    st.info("No notes found. Add your first note above!")
else:
    for note in filtered_notes:
        with st.expander(f"📌 {note['title']} — {note['created_at']}"):
            st.write(note["content"])
            if st.button("Delete note", key=f"delete_{note['id']}"):
                notes = [item for item in notes if item["id"] != note["id"]]
                save_notes(notes)
                st.rerun()
