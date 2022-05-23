from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title="Cursos API - Segurança")
app.include_router(api_router, prefix=settings.API_V1_STR)

# /api/v1/cursos
# /api/v1/usuarios
 
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)

"""
2
token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NTM3OTE2NzMsImlhdCI6MTY1MzE4Njg3Mywic3ViIjoiMiJ9.eOcXx-KZjClxBsVXZX-rUjTas6KGFEG_1JDY8-1dTKU

tipo: "bearer"

3
token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NTM3OTM4MDcsImlhdCI6MTY1MzE4OTAwNywic3ViIjoiMyJ9.fsTN-1SNiQRvfdGP39ftxab3_12GDAko9GCh7EHj3uM
"""