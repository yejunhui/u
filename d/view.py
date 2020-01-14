from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib import messages
from d import d
from d import goldPlay
import random

def ms(request,mass,page):
    messages.success(request, mass)
    # return render(request, 'login.html', cont)
    return redirect(page)


#登录
def login(request):
    #数据字典
    cont = {}
    #时候
    cont['t']=d.t
    cont['user']=d.user
    response = redirect('index')

    if request.POST:
        d.user= request.POST['user']
        d.password = request.POST['password']
        if 'checkbox' in request.POST:
            request.session['checkbox'] = request.POST['checkbox']
        else:
            request.session['checkbox'] = 'off'
        if request.POST['user'] == '':
            messages.success(request, '请输入用户信息!')
            return render(request, 'login.html', cont)
        else:
            if request.POST['password'] == '':
                messages.success(request, '请输入用户信息!')
                return render(request, 'login.html', cont)
            else:
                if request.POST['checkbox'] !='on':
                    messages.success(request, '请同意服务协议!')
                    return render(request, 'login.html', cont)
                else:
                    if d.user in d.userList:
                        messages.success(request, '用户已登录,请重试!')
                        del d.userList[d.user]
                        return render(request, 'login.html', cont)

                    else:
                        response.set_cookie('userName',d.user)
                        response.set_cookie(d.user,d.password)
                        request.session[d.user]= d.password
                        #d.userList[d.user]=d.password
                        return response

    else:
        response.delete_cookie('userName')
        if d.user in request.session:
            del request.session[d.user]
        return render(request,'login.html',cont)

#注册
def loginIn(request):
    cont={}
    cont['user'] = None
    # 时候
    cont['t'] = d.t

    if request.POST:
        if request.POST['password'] == request.POST['password2']:
            cont['ts']='T'
            cont['user'] = request.POST['user']
            cont['password'] = request.POST['password']
            d.d[cont['user']]=[cont['password'],['']]
            return redirect('login')
        else:
            return render(request, 'loginIn.html', cont)
    else:
        return render(request,'loginIn.html',cont)

#主页
def index(request):
    cont = {}
    # 时候
    cont['t'] = d.t
    #设置用户信息
    cont['tss'] = d.ts
    cont['user']= request.COOKIES.get('userName')
    cont['password']= '********'#'cookie:'+str(request.COOKIES.get(request.COOKIES.get('userName')))+'session:'+str(request.session.get(request.COOKIES.get('userName')))
    cont['checkbox']= request.session.get('checkbox')
    cont['r']=d.r
    cont['i']= range(10,120)

    if request.COOKIES.get('userName') in d.d :
        if 'index' in d.d[request.COOKIES.get('userName')][1]:
            if request.COOKIES.get(request.COOKIES.get('userName'))  == d.d[request.COOKIES.get('userName')][0]:
                d.userList[d.user] = d.password
                cont['ts'] = d.d[request.COOKIES.get('userName')][1]
                return render(request,'index.html',cont)
            else:
                messages.success(request, '密码信息不正确!')
                return redirect('login')
        else:
            messages.success(request, '用户信息不正确!')
            return redirect('login')
    else:
        messages.success(request, '请先登录!')
        return redirect('login')

'''    else:

        messages.success(request, '请先登录!')
        return redirect('login')
'''


#PLAN系统
def plan(request):
    cont = {}
    # 时候
    cont['t'] = d.t
    cont['user'] = request.COOKIES.get('userName')

    if d.verify(request):
        return render(request, 'plan.html', cont)
    else:
        messages.success(request, '抱歉，没有该页面的访问权限!')
        return redirect('index')

#STOCK系统
def Stock(request):
    cont = {}
    # 时候
    cont['t'] = d.t
    cont['user'] = request.COOKIES.get('userName')

    if d.verify(request):
        return render(request,'stock.html',cont)
    else:
        messages.success(request, '抱歉，没有该页面的访问权限!')
        return redirect('index')

#GOLD系统
def gold(request):
    cont = {}
    # 时候
    cont['t'] = d.t
    cont['user'] = request.COOKIES.get('userName')

    if d.verify(request):
        cont['r'] = goldPlay.request1()
        return render(request,'gold.html',cont)
    else:
        messages.success(request, '抱歉，没有该页面的访问权限!')
        return redirect('index')
#阳光煊煊
def sunnyGirl(request):
    cont= {}
    # 时候
    cont['t'] = d.t
    cont['user'] = request.COOKIES.get('userName')

    if d.verify(request):
        return render(request,'sunnyGirl.html',cont)
    else:
        messages.success(request, '抱歉，没有该页面的访问权限!')
        return redirect('index')

def cle(request):
    response = redirect('login')
    response.delete_cookie('userName')
    if d.user in d.userList:
        del d.userList[d.user]
    if d.user in request.session:
        del request.session[d.user]
    d.user=None
    return response