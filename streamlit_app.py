import streamlit as st
from notion_client import Client

st.title("🔗 Test invio a Notion")

NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
DATABASE_ID = st.secrets["DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)

if st.button("Invia riga di test a Notion"):
    try:
        response = notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "Nome": {"title": [{"text": {"content": "Test da Streamlit"}}]},
                "Tipo": {"rich_text": [{"text": {"content": "Streamlit"}}]},
                "Ore_Fresatura": {"number": 1.0},
                "Ore_Erosione": {"number": 1.0},
                "Totale": {"number": 2.0},
                "Ore_Fresatura_hhmm": {"rich_text": [{"text": {"content": "01:00"}}]},
                "Ore_Erosione_hhmm": {"rich_text": [{"text": {"content": "01:00"}}]},
                "Totale_hhmm": {"rich_text": [{"text": {"content": "02:00"}}]}
            }
        )
        st.success("✅ Riga inserita correttamente!")
    except Exception as e:
        st.error(f"❌ Errore: {e}")
