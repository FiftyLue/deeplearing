from django.shortcuts import render
from django.shortcuts import HttpResponse
from migrations import test

# Create your views here.
def index(request):
    #return HttpResponse("hello world!")
    return render(request,"index.html")
def upload(request):
    if request.method =='GET':
        return render(request,'index.html')
    if request.method == 'POST':
        print("12345")
        #test.p()
        file = request.FILES.get('file')              # 获取文件信息用 request.FILES.get
        print(file)                                   # 这里的get('file') 相当于 name = file
        # print(file) 可以直接显示文件名，是因为django FILES内部 重写了 __repr__ 方法
        if file:                                      # 如果文件存在
            with open(file.name,'wb') as f:               #  新建1张图片 ，图片名称为 上传的文件名
                for temp in file.chunks():                #  往图片添加图片信息
                    f.write(temp)
                    result = test.eval(file.name)
        return HttpResponse(result)
