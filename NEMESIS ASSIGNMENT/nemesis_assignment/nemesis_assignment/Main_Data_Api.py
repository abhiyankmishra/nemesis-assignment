from django.shortcuts import render
from .import pool
from django.contrib import auth


def signupinterface(request):
    try:

        return render(request,"signup.html",{'msg':''})
    except Exception as e:
        print(e)



def submitsignupinterface(request):
    try:
         Username = request.POST['Username']
         Email = request.POST['Email']
         psw= request.POST['psw']
         Address = request.POST['Address']

         db,cmd=pool.connection()
         q="insert into nemesisuser(username,email,password,address) values('{0}','{1}','{2}','{3}')".\
             format(Username,Email,psw,Address)
         cmd.execute(q)
         db.commit()
         db.close()

         return render(request, "signup.html",{'msg':'Registration done, please try to login'})
    except Exception as e :
        # print("**********",e)
        return render(request, "signup.html",{'msg':'Registration not done'})




def logininterface(request):
    return render(request,"login.html",{'msg':''})

def checklogininterface(request):
    try:

     email = request.POST['Email']
     psw = request.POST['psw']

     db, cmd = pool.connection()
     q="select * from nemesisuser where email='{0}' and password='{1}'".format(email,psw)

     cmd.execute(q)
     row=cmd.fetchone()
     db.close()

     if(row):

         request.session["admin"]=row
         return displayallusers(request)

     else:
         return render(request, "login.html",{'msg':'Invalid credentials'})
    except Exception as e:
        print(e)
        return render(request, "login.html", {'msg': 'server error'})

def displayallusers(request):
   try:
       tokenn = request.session["admin"]
       db, cmd = pool.connection()
       q="select * from nemesisuser"

       cmd.execute(q)
       rows = cmd.fetchall()
       db.close()

       return render(request, "displayallusers.html", {'data': rows,'token':tokenn})
   except Exception as e:
       return render(request, "login.html", {'msg': 'you need to login first'})



def userdisplaybyusername(request):
    try:

        uname=request.GET["uid"]
        db,cmd=pool.connection()
        q="select * from nemesisuser where username='{0}'".format(uname)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()

        return render(request,"editbyusername.html", {'data': row})
    except Exception as e:
        print("ERRRRRRRRRRRRRRRRRRRRRROR",e)
        return displayallusers(request)


def updatebyusername(request):
     try:

        Username = request.POST['Username']
        Email = request.POST['Email']
        # psw = request.POST['psw']
        Address = request.POST['Address']

        db,cmd=pool.connection()
        q = "update  nemesisuser set email='{0}',address='{1}' where username='{2}'".\
            format(Email, Address, Username)
        cmd.execute(q)
        db.commit()
        db.close()

        return displayallusers(request)
     except Exception as e:
         return displayallusers(request)


def userdeletebyusername(request):
    try:

        uname=request.GET["uid"]
        db, cmd = pool.connection()
        q="delete from nemesisuser where username='{0}'".format(uname)
        cmd.execute(q)
        db.commit()
        db.close()
        return displayallusers(request)
    except:
        return displayallusers(request)


def logout(request):
    auth.logout(request)
    return render(request, "login.html", {'msg': 'Logged out successfully'})
