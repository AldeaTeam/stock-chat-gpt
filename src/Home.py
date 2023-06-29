import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="OpenAI | StockChat 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[@AIdea-StockChat](https://github.com/AldeaTeam/stock-chat-gpt)")

    st.write("**Medium:** "
"[@AIdea-StockChat](https://github.com/AldeaTeam)")

    st.write("**Github:** [@AIdea](https://github.com/AldeaTeam)")
    st.write("**Mail** : sleu2030@126.com")
    st.write("**Created by Yvann**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>StockChat, your personal assistant for stock analysis 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Stocky, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript with more coming soon! 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#StockChat's Pages
st.subheader("🚀 StockChat's Pages")
st.write("""
- **Stock-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (can't process the whole file just index useful parts(max 4) for respond to the user ) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) + (soon) Summarize data
- **Stock-Sheet** (beta): Chat on tabular data (CSV) | for precise information | can process the whole file (with python code) | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation (experimental)
- **Stock-Video**: Summarize videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)

- (soon) **StockChat-Website**: Chat with any website you provide
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**StockChat is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)





