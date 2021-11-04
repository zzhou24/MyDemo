from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
# Create your views here.

def index(request):

    # 在数据库添加记录
    # ob = Users()
    # ob.name = 'Wangwu'
    # ob.age = 22
    # ob.phone = '13812345434'
    # ob.save()

    # 删除操作
    # mod = Users.objects
    # user = mod.get(id = 6)
    # user.delete()
    return HttpResponse("首页 </br></br> <a  href = '/users'>用户信息管理</a>")

def indexUsers(request):
    ulist = Users.objects.all()
    context = {'userslist':ulist}
    return render(request, 'myapp/users/index.html',context)

def addUsers(request):
    return render(request, 'myapp/users/add.html')

def insertUsers(request):
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'添加成功!'}
    except:
        context = {'info':'添加失败!'}
    return render(request, 'myapp/users/info.html', context)

def delUsers(request, uid = 0):
    try:
        ob = Users.objects.get(id  = uid)
        ob.delete()
        context = {'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request, 'myapp/users/info.html', context)

def editUsers(request,uid =0 ):
    # 注意uid参数
    try:
        ob = Users.objects.get(id  = uid)
        context = {'uu':ob}
        return render(request, 'myapp/users/edit.html', context)
    except:
        context = {'info':'删除失败!'}
    return render(request, 'myapp/users/edit.html', context)

def updateUsers(request):
    try:
        uid = request.POST['id'] # 获取需要修改的记录的id号
        ob = Users.objects.get(id = uid) # 访问要修改的记录
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'修改成功!'}
    except:
        context = {'info':'修改失败!'}
    return render(request, 'myapp/users/info.html', context)
