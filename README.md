# OpenAIonURL_App

<img width="560" alt="image" src="https://github.com/margauxvp/OpenAIonURL_App/assets/33750077/53f31a05-9a46-4300-a3fc-3cbaaa3c0f41">

# AI News Chat

This Streamlit-based app allows you to interact with OpenAI's GPT model for getting summaries of recent AI news. Ask any question about AI, and the model will provide you with a summary based on information from Azure Cognitive Search. The source of data that is used for this app is the following URL: https://techcrunch.com/category/artificial-intelligence/

![Untitled video](https://github.com/margauxvp/OpenAIonURL_App/assets/33750077/5ab56fbc-f2cd-41cf-af85-0ab3689ad85d)

## Setup

1. **Environment Variables**: Create a `.env` file in the project directory with your API keys.

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    SEARCH_KEY=your_azure_search_key
    ```

2. **Azure OpenAI Configuration**: Customize the parameters in the code:

    ```python
    openai.api_base = "your_azure_openai_endpoint"
    openai.api_key = "your_openai_api_key"
    deployment_id = "your_deployment_id"
    ```

3. **Azure AI Search Configuration**: Provide your Azure AI Search information:

    ```python
    search_endpoint = "your_search_endpoint"
    search_key = "your_azure_search_key"
    search_index_name = "your_search_index_name"
    ```

4. **BYOD (Bring Your Own Data)**: If using your own data, configure the `setup_byod` function by providing your deployment ID.

## Running the App

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run your_script_name.py
    ```

    Replace `your_script_name.py` with your Python script containing the provided code.

3. Access the app in your web browser by opening the displayed URL.

## Usage

1. **Input**: Paste your AI news-related question in the text input.

2. **Ask Button**: Click "Ask about recent AI News" to interact with the GPT model.

3. **Result**: The GPT model's response will be displayed with a styled background.

https://github.com/margauxvp/OpenAIonURL_App/assets/33750077/1c472854-ec53-411c-909f-8d3d0b77d1ab

Feel free to explore and chat about the exciting world of AI news! 🤖

