from fastapi import FastAPI, File, UploadFile
import dophin_scheduler

"""
 启动命令：uvicorn MoCA_ROI_app:app --reload --host 10.123.234.39 --port 65530
"""


app = FastAPI()

# single img upload

# @app.post("/img_process")
# async def create_processed_img(file: Union[UploadFile, None] = File(
#     default=None, description="A image about complete MoCA quantity tabule photoed by user")):  # 比File有优势，更适用于处理图像、视频、二进制文件等大型文件，不会占用所有内存
#     """
#     Recoganize the ROI of MoCA quantity table
#
#     Parameters:
#         file:Union[UploadFile, None]
#             A received image file(jpg,png) upload by user
#     Returns:
#         ROI_JSON:JSON str
#             a processed image include ROI
#     """
#
#     print("file_name:", file.filename, "received")
#     if not file:
#         return {"message": "No upload image sent"}
#     else:
#         contents = await file.read()  # UploadFile->string
#         nparr = np.fromstring(contents, np.uint8)  # str -> ndarray
#         ori_img = cv.imdecode(nparr, cv.IMREAD_COLOR)
#         ROI_show = MoCA_ROI_Crop.main(ori_img)
#         _, encoded_ROI = cv.imencode(".jpg", ROI_show)  # ndarray->jpg
#         ROI_bytes = encoded_ROI.tobytes()  # jpg->bytes
#         print("successfully Rec")
#         return Response(content=ROI_bytes, media_type="image/jpg")




@app.post("/test")
async def root():
    message = dophin_scheduler.main()
    return {"message": message}



## 识别
# @app.get("/ROI_show/")
# async def ROI_catch(image: np.ndarray):
#     if not image:
#         return {"message": "No image receive"}
#     else:
#         ROI_show = MoCA_ROI_Crop.main(image)
#         return ROI_show


if __name__ == '__main__':
    pass
