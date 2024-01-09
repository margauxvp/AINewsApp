from dotenv import load_dotenv
import openai, os, requests
import streamlit as st
from streamlit_chat import message
import re


# Load environment variables from .env file
load_dotenv()

openai.api_type = "azure"
# Azure OpenAI on your own data is only supported by the 2023-08-01-preview API version
openai.api_version = "2023-08-01-preview"

# Azure OpenAI setup
openai.api_base = "https://gpt4turbovision21122023.openai.azure.com/" # Add your endpoint here
openai.api_key = os.getenv("OPENAI_API_KEY") # Add your OpenAI API key here
deployment_id = "gpt-4-32k" # Add your deployment ID here

# Azure AI Search setup
search_endpoint = "https://searchainews.search.windows.net"; # Add your Azure AI Search endpoint here
search_key = os.getenv("SEARCH_KEY"); # Add your Azure AI Search admin key here
search_index_name = "ainewsindex"; # Add your Azure AI Search index name here

def setup_byod(deployment_id: str) -> None:
    """Sets up the OpenAI Python SDK to use your own data for the chat endpoint.

    :param deployment_id: The deployment ID for the model to use with your own data.

    To remove this configuration, simply set openai.requestssession to None.
    """

    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):

        def send(self, request, **kwargs):
            request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
            return super().send(request, **kwargs)

    session = requests.Session()

    # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
    session.mount(
        prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
        adapter=BringYourOwnDataAdapter()
    )

    openai.requestssession = session

setup_byod(deployment_id)

# Chat with OpenAI and Search
def ask_gpt(question):
    message_text = [{"role": "user", "content": '' + question + ''}]

    completion = openai.ChatCompletion.create(
        messages=message_text,
        deployment_id=deployment_id,
        dataSources=[  # camelCase is intentional, as this is the format the API expects
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": search_endpoint,
                    "key": search_key,
                    "indexName": search_index_name,
                }
            }
        ]
    )
    answer = completion.choices[0].message.content # this is done to remove the sources e.g. content[doc1][doc2], in a next part we should link them.
    return re.sub(r'\[doc[^\]]*\]', '', answer)

# Streamlit App
# Set page title and favicon
st.set_page_config(page_title="AI News Chat", page_icon=":robot_face:")

# Add a fun emoji and style the intro text
st.title("🤖 Chat about what's hot in AI!")
st.write("Ask any question about recent AI news, and I'll provide you with a summary!")

# Get user input
user_input = st.text_input("Describe what you would like to know about in AI:")

# Wait until the user clicks the button
if st.button("Ask about recent AI News"):
    # Get the answer from the GPT model
    answer = ask_gpt(user_input)
    
    # Style the answer with a different background color
    st.markdown(f"<div style='background-color: #f7f7f7; padding: 10px; border-radius: 5px;'>{answer}</div>", unsafe_allow_html=True)

