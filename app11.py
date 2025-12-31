import streamlit as st
import requests
import subprocess

st.title('Web Game Generator')
prompt=st.text_area('Please describe the app or game you want to create')

generate_app = st.button('Generate Application')

generate_game = st.button('Generate Game')

if generate_app or generate_game:
    mode = 'app' if generate_app else 'game'
    response = requests.post(
        url='https://kambhampatirajesh.app.n8n.cloud/webhook-test/77358029-f1cd-47cc-82ce-5259ca6a6b34',
        json={'prompt': prompt, 'mode': mode}
    )
    if response.status_code == 200:
        code_text = response.json()[0]["output"]
        clean_code = (
            code_text.replace("python", "")
                     .replace("", "")
                     .strip()
        )
        with open("app50.py", "w", encoding="utf-8") as f:
            f.write(clean_code)
        subprocess.run(["python", "app50.py"])