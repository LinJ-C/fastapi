from fastapi import APIRouter,Form, File, UploadFile


file = APIRouter()

@file.post('/files')
async def get_file(files: list[bytes]=File()):
    name = 1
    for fi in files:
        with open(f'{name}.txt','wb') as f:
            f.write(fi)
            f.close()
        name+=1
    return {f"文件长度":len(files)}
    
    
@file.post('/upload_files')
async def get_upload_file(files: list[UploadFile]):
    name =[]
    for fi in files:
        print(fi.filename)
        with open(f'{fi.filename}.txt','wb') as f:
            for fe in fi.file:
                f.write(fe)
            f.close()
        name.append(fi.filename)
    return {f"文件列表":name}
    