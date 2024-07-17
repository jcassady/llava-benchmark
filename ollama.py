import requests
import json

def generate_response(prompt, model='llava-llama3'):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        # "format": "json",
        "image": ["data/images/10.jpg"]

    }
    response = requests.post(url, json=data)
    # return json.loads(response.text)['response']

    response_chunks = []

    # Process the streamed data in chunks
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            response_chunks.append(chunk.decode("utf-8"))

    # print(response_chunks)
    
    joined_string = ""
    for response in response_chunks:
        print("\n", response)
        for element in response:
            print(element)
            joined_string += element
    
    print(">> ", joined_string)

prompt = """
Read and return the image's license plate as text only
"""
response = generate_response(prompt)
# print("\n", response)
