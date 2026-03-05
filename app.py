"""Automotive Inventory Query System for AtliQ Shoe Store
Streamlit application with Natural Language to SQL conversion"""

import streamlit as st
import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SeqToSeqLMOutputParser
from few_shot_examples import few_shots
import mysql.connector

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AtliQ Shoe Inventory Assistant",
    page_icon="👟",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1f77b4;
    text-align: center;
    padding: 1rem;
}
.sub-header {
    font-size: 1.2rem;
    color: #666;
    text-align: center;
    margin-bottom: 2rem;
}
.query-box {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def get_few_shot_db_chain():
    """Create and return the LangChain SQL Database Chain with few-shot learning"""
    
    # Initialize Google PaLM LLM
    api_key = os.getenv('GOOGLE_API_KEY')
    llm = GooglePalm(google_api_key=api_key, temperature=0.1)
    
    # Connect to MySQL database
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_NAME', 'atliq_shoes')
    
    db = SQLDatabase.from_uri(
        f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )
    
    # Create the SQL Database Chain
    db_chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True,
        return_intermediate_steps=True
    )
    
    return db_chain

def process_query(question):
    """Process natural language query and return result"""
    try:
        chain = get_few_shot_db_chain()
        
        # Add few-shot examples to the prompt
        few_shot_prompt = """You are an expert in converting English questions to SQL queries.
Here are some examples:

"""
        
        for example in few_shots[:3]:  # Use first 3 examples
            few_shot_prompt += f"Question: {example['Question']}\n"
            few_shot_prompt += f"SQL: {example['SQLQuery']}\n\n"
        
        few_shot_prompt += f"Now convert this question to SQL:\nQuestion: {question}\nSQL:"
        
        response = chain(few_shot_prompt)
        
        return response
    
    except Exception as e:
        return {'error': str(e)}

# Main UI
st.markdown('<h1 class="main-header">👟 AtliQ Shoe Store Inventory Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ask questions about our shoe inventory in natural language</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This AI-powered system allows you to query shoe inventory 
    using natural language. Powered by:
    - **Google PaLM LLM**
    - **LangChain**
    - **MySQL Database**
    - **Few-Shot Learning**
    """)
    
    st.header("📊 Database Tables")
    st.write("""
    - **Shoes**: Products information
    - **Inventory**: Stock quantities
    - **Discounts**: Promotional discounts
    """)
    
    st.header("💡 Example Questions")
    st.write("""
    - How many Nike shoes do we have?
    - What is the total price of inventory?
    - Show me all shoes under $100
    - Which store has the most stock?
    - What discounts are active?
    """)

# Main chat interface
query = st.text_input(
    "Ask a question about inventory:",
    placeholder="e.g., How many Adidas shoes in size 10 do we have?"
)

if st.button("🔍 Search", use_container_width=True):
    if query:
        with st.spinner('Processing your query...'):
            result = process_query(query)
            
            if 'error' in result:
                st.error(f"❌ Error: {result['error']}")
            else:
                # Display results
                st.success("✅ Query processed successfully!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📝 Your Question")
                    st.info(query)
                
                with col2:
                    st.subheader("💬 Answer")
                    if 'result' in result:
                        st.write(result['result'])
                    else:
                        st.write(result)
                
                # Show intermediate steps if available
                if 'intermediate_steps' in result:
                    with st.expander("🔍 View SQL Query"):
                        steps = result['intermediate_steps']
                        if len(steps) > 0 and 'sql_cmd' in steps[0]:
                            st.code(steps[0]['sql_cmd'], language='sql')
                
                # Add to message history
                st.session_state.messages.append({
                    'question': query,
                    'answer': result.get('result', str(result))
                })
    else:
        st.warning("⚠️ Please enter a question")

# Display conversation history
if st.session_state.messages:
    st.divider()
    st.subheader("📜 Conversation History")
    
    for idx, msg in enumerate(reversed(st.session_state.messages[-5:])):
        with st.container():
            st.markdown(f"**Q{len(st.session_state.messages)-idx}:** {msg['question']}")
            st.markdown(f"**A:** {msg['answer']}")
            st.divider()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Built with ❤️ using Streamlit, LangChain & Google PaLM | © 2026 AtliQ Shoes</div>",
    unsafe_allow_html=True
)
