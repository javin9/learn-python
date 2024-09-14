from zhipuai import ZhipuAI
import requests

client = ZhipuAI(api_key="75b89ab73566e4b15f26fa11c8041e86.JcBfL7ymVjAq5yS8"
                 )  # 请填写您自己的APIKey

# response = client.videos.generations(model="cogvideox",
#                                      prompt="加菲猫开小汽车，游走在马路上，脸上的表情充满开心喜悦。")
# print(response)

response = client.videos.retrieve_videos_result(
    id="531717250146954018979475584655029711")

print(response)
