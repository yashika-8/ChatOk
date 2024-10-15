import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':'application/json'
}
history=[]
def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"chatok",
        "prompt":final_prompt,
        "stream":False

    }
    response=requests.post(url,headers=headers,data=json.dumps(data))
    print("API Response Status Code:", response.status_code)  # Log the status code
    print("API Response Text:", response.text)  # Log the response text

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("Error:",response.text)
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2,placeholder="Enter your prompt"),
    outputs=gr.Textbox(label="Response") 
)
interface.launch()