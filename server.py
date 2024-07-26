from fastapi import FastAPI, File, UploadFile
import paddleocr
import logging
app = FastAPI()

@app.post("/ocr")
async def ocr_image(image_file: UploadFile):
    ocr_model = paddleocr.PaddleOCR(lang='en')
    result = ocr_model.ocr(image_file.file.read(),cls=True)
    return {"text": result}

def setup_logging() -> logging.Logger:
    """Set up the logging configuration."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler("ocr.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


@app.post("/ocr")
async def ocr_image(image_file: UploadFile):
    logger = setup_logging()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

    ocr_model = paddleocr.PaddleOCR(lang='en', use_angle_cls=True)
    result = ocr_model.ocr(image_file.file.read(),cls=True)
    return {"text": result}
