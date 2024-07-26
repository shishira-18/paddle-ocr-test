from fastapi import FastAPI, File, UploadFile
import paddleocr

app = FastAPI()

@app.post("/ocr")
async def ocr_image(image_file: UploadFile):
    ocr_model = paddleocr.PaddleOCR(lang='en')
    result = ocr_model.ocr(image_file.file.read(),cls=True)
    return {"text": result}

