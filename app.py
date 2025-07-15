# AI PROJECT IMAGE GENERATE,  
import streamlit as st
import requests

st.title("Ad-Photo Studio")

# Generate Image with enhanced prompt
if 'data1' not in st.session_state:
    st.session_state.data1 = "" 

def gen_image(en_prompt, api_key):
    try:
        model_version = "2.2"
        url = "https://engine.prod.bria-api.com/v1/text-to-image/hd/" + model_version

        payload = {
        "prompt": en_prompt,
        "num_results": 1,
        "sync": True
        }
        headers = {
        "Content-Type": "application/json",
        "api_token": api_key
        }
        response = requests.post(url, json=payload, headers=headers)
        st.session_state.data1 = response.json()
    except:
        st.scatter_chart.data1 = None
    return st.session_state.data1

# sidebar api key
with st.sidebar:
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    st.session_state.api_key = st.text_input("Enter your API key", type='password')

# radio buttons
var_radio=st.radio("->",options=['Generate Image', 'b', 'c', 'd'], horizontal=True, label_visibility='collapsed')

# line 
st.divider()

# Generate Image
if var_radio=='Generate Image':
    st.header("Generate Images")

    # Original prompt
    or_prompt = st.text_area("Enter your prompt", max_chars=25,)

    # Enhance prompt 
    if "en_prompt" not in st.session_state:
        st.session_state.en_prompt = ""

    if st.button("Enhance Prompt"):
        try:
            # Enhance prompt Generate
            url = "https://engine.prod.bria-api.com/v1/prompt_enhancer"

            payload = {
                "prompt": or_prompt
            }
            headers = {
                "Content-Type": "application/json",
                "api_token": st.session_state.api_key
            }
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()

            st.session_state.en_prompt =data["prompt variations"]
            st.write(st.session_state.en_prompt)
        except:
            st.warning("Please enter input fields")
    else:
        st.session_state.en_prompt=None

    # expender More/Additonal info
    with st.expander("Debug: Session State:"):
        prompts = {
            "Original Prompt":or_prompt,
            "Enhanced Prompt":st.session_state.en_prompt
        }
        st.write(prompts)

    # Generate Image with enhanced prompt
    st.button("Generate Image", on_click=gen_image, args=(st.session_state.en_prompt, st.session_state.api_key))
    st.write(st.session_state.data1)


elif var_radio=='b':
    st.header("Coming Soon!")
elif var_radio=='c':
    st.header("Coming Soon!")
elif var_radio=='d':
    st.header("Coming Soon!")

    