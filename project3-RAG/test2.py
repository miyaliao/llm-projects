import os
from google import genai

# 配置代理和 API Key
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'

client = genai.Client(api_key="apikey")

# 生成向量
result = client.models.embed_content(
    model='gemini-embedding-exp-03-07',
    contents="这是我需要转化成向量的文本"
)

# 打印生成的向量前 5 位
print(f"向量维度: {len(result.embeddings[0].values)}")
print(f"向量示例: {result.embeddings[0].values[:5]}")
