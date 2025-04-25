import streamlit as st
from langgraph.graph_flow import run_graph

def main():
    st.set_page_config(page_title="Deep Research AI Agent", layout="centered")

    st.title("🧠 Deep Research AI Agent")
    st.write("Ask any research-level question and get a summarized AI response.")

    query = st.text_input("🔍 Enter your research query:")

    if st.button("Run Research", key="run_button"):
        if not query.strip():
            st.warning("⚠️ Please enter a valid query.")
            return

        with st.spinner("Running deep research..."):
            try:
                result = run_graph(query)
                st.success("✅ Research Completed")

                if "research" in result:
                    with st.expander("📚 Research Details"):
                        st.write(result["research"])

                if "answer" in result:
                    st.subheader("🎯 Final Answer")
                    st.write(result["answer"])
                else:
                    st.warning("⚠️ No answer was generated.")

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
