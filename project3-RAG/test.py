import os
from google import genai

# ================= 配置区 =================
# 1. 替换为你自己的 API KEY
API_KEY = "你的_GEMINI_API_KEY"

# 2. 设置本地代理地址（请根据你的代理工具修改端口，通常是 7890）
# 如果不设置代理，国内环境通常无法连接
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'
# ==========================================

def call_gemini():
    try:
        # 初始化客户端
        client = genai.Client(api_key= 'apikey')
        
        # 调用 Gemini 3 Flash 模型（速度最快且免费额度高）
        response = client.models.generate_content(
            model='gemini-2.5-flash' ,
            contents='请用中文简单介绍一下你自己，并给中国开发者一个鼓励。'
        )
        
        print("-" * 30)
        print("Gemini 的回答：")
        print(response.text)
        print("-" * 30)
        
    except Exception as e:
        print(f"调用失败，错误信息: {e}")
        print("提示：请检查 API Key 是否正确，以及本地代理是否已开启。")

if __name__ == "__main__":
    call_gemini()
