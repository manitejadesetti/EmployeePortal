import csv,io
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

from .models import AddEmployee

def home(request):
    return render(request,'EMP/home.html')

@csrf_exempt
def showform(request):
    if request.is_ajax():
        name = request.POST.get('uname')
        email = request.POST.get('email')
        phonenum = request.POST.get('phonenum')
        success = AddEmployee(username=name, emailId=email, mobileNumber=phonenum)
        success.save()
    return render(request,'EMP/addEmpl.html')

def showTable(request):
    if(AddEmployee.objects.count()):
        table = AddEmployee.objects.all()
        context={'table':table}
        return render(request,'EMP/table.html', context)
    else:
        context={'records':"no records found"}
        return render(request,'EMP/table.html',context)
def download(request):
    return render(request,'EMP/download.html')

def searchEmployee(request):
    return render(request,'EMP/search.html')

def empsearch(request):
    item = request.GET['searchtext']
    table = AddEmployee.objects.all()
    data=[]

    for items in AddEmployee.objects.all():
         if  item in items.username or item in items.emailId or item in items.mobileNumber:
             data.append(items)


    context = {'table': data, 'item': item}
    if len(data) == 0:
        return render(request,'EMP/search.html',{'msg':"no records found"})
    if item=="":
        return HttpResponseRedirect("/EMP/search/")
    return render(request, 'EMP/searchdata.html', context)


def objectDelete(request, item_id):
    object = get_object_or_404(AddEmployee, pk=item_id)
    object.delete()
    return redirect(showTable)
def objectUpdate(request, item_id):
    object = AddEmployee.objects.get(id=item_id)
    context ={'name':object.username, 'email':object.emailId,'phno':object.mobileNumber,'item_id':item_id}
    return render(request,'EMP/update.html',context)
@csrf_exempt
def update(request):
    if request.is_ajax():
        AddEmployee.objects.filter(emailId=request.POST.get('email')).update(
            username=request.POST.get('uname'), mobileNumber=request.POST.get('phonenum'))
        return redirect(showTable)


@permission_required('admin.can_add_log_entry')
def uploadCSV(request):

    template='EMP/upload.html'

    prompt= {
        'order':'Order of the CSV should be Username,EmailId,MobileNumber'
    }

    if(request.method=='GET'):
        return render(request,template,prompt)
    try:
        csv_file=request.FILES["file"]
        if not csv_file.name.endswith('.csv'):
            return render(request,template,{'msg':"This is not a csv file"})
        data_set=csv_file.read().decode('UTF-8')
        io_string =io.StringIO(data_set)
        next(io_string)
        i=0
        for column in csv.reader(io_string,delimiter=','):
            try:
                emp = AddEmployee(
                username=column[0],
                emailId=column[1],
                mobileNumber=column[2]

            )


                emp.save()
            except:
                context ={'msg':"email already exist"}
                return render(request,template,context)


    except:
        print("no file")
    return render(request, template)

def downloadCSV(request):
    items=AddEmployee.objects.all()
    response=HttpResponse(content_type='text/save')
    response['content-Disposition'] = 'attachment; filename="Employee.csv"'

    writer=csv.writer(response,delimiter=',')
    writer.writerow(['username','emailId','mobileNumber'])

    for item in items:
        writer.writerow([item.username, item.emailId, item.mobileNumber])

    return response