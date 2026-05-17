import streamlit as st
from agent_core import run_research

st.set_page_config(page_title='AI Research Agent', page_icon='🤖')
st.title('🤖 AI Research Agent')
st.caption('Enter any topic — AI will research and write a full report!')

topic = st.text_input(
    'Research Topic:',
    placeholder='e.g. Latest trends in Generative AI 2026'
)

if st.button('🔍 Start Research', type='primary'):
    if topic:
        with st.spinner('Agent is researching... please wait ⏳'):
            try:
                report, steps = run_research(topic)

                with st.expander('🔎 What the Agent Did:'):
                    for step in steps:
                        st.write(f'✅ {step}')

                st.subheader('📄 Research Report')
                st.markdown(report)

                st.download_button(
                    label='⬇️ Download Report',
                    data=report,
                    file_name=f'report.txt',
                    mime='text/plain'
                )
            except Exception as e:
                st.error(f'Error: {str(e)}')
    else:
        st.warning('Please enter a research topic!')