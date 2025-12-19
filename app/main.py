import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

# 在导入应用程序配置之前加载 .env 文件到环境变量
load_dotenv()

from app.core.application import create_app
from app.log.logger import get_main_logger

# 创建 FastAPI 应用
app: FastAPI = create_app()

# 添加健康检查路由
@app.get("/healthz")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    logger = get_main_logger()
    logger.info("Starting application server...")
    uvicorn.run(app, host="0.0.0.0", port=8001)
