from zhipuai import ZhipuAI

client = ZhipuAI(api_key="75b89ab73566e4b15f26fa11c8041e86.JcBfL7ymVjAq5yS8"
                 )  # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {
            "role": "user",
            "content": "用js写一个hello world"
        },
    ],
    stream=True,
)
content = ""
for chunk in response:
    content += chunk.choices[0].delta.content
    # print(chunk.choices[0].delta.content)
print(content)
