import streamlit as st
from analyzer.main import scrape_page, analyze_with_gemini, revise_article_with_gemini, print_results, save_results

def main():
    st.title("MoEngage Documentation Analyzer")
    st.write("Analyze and improve MoEngage documentation using AI.")

    # Input URL
    url = st.text_input("Enter the MoEngage documentation URL:", "")
    if not url.startswith(('http://', 'https://')) and url:
        st.error("Please provide a valid URL starting with http:// or https://")

    # Analyze button
    if st.button("Analyze") and url:
        try:
            st.info("Scraping content from the URL. This may take a few minutes...")
            content = scrape_page(url)

            st.info("Analyzing content with AI...")
            analysis = analyze_with_gemini(content, url)

            st.info("Generating revised content...")
            revised_content = revise_article_with_gemini(content, analysis)

            # Display results
            st.success("Analysis completed successfully!")
            st.subheader("Analysis Results")
            st.json(analysis)

            st.subheader("Revised Content")
            st.text_area("Revised Article", revised_content, height=300)

            # Save results
            if st.button("Save Results"):
                save_results(url, analysis, revised_content)
                st.success("Results saved successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
