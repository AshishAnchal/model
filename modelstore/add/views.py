from django.shortcuts import render
# from django.http import  JsonResponse
from .models import Attend , Entry
from datetime import date

def home(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        attend = request.POST.get('attend')
        date = request.POST.get('date')
        name = request.POST.get('name')
        Attend.objects.create(
            name=name,
            roll=roll,
            tarikh=date,
            attendance=attend
        )
        if attend == "Present":
            print(name ,roll, "Present" , date)
        elif attend == "Absent":
            print(name,roll, "Absent", date)

    return render(request, "home.html")

def show(request):
    data = Attend.objects.all()
    return render(request, "show.html", {"data": data})

def filter(request):
    if request.method == 'POST':
        attendance = request.POST.get('attend')
        

        data = Attend.objects.filter(attendance=attendance)
        return render(request, "show.html", {'data': data})

    return render(request, "filter.html")

from django.shortcuts import render
from .models import Attend

def report(request):
    if request.method == "POST":
        roll = request.POST.get('roll')

        records = Attend.objects.filter(roll=roll)

        if records.exists(): 
            total = records.count()
            present = records.filter(attendance="Present").count()
            absent = records.filter(attendance="Absent").count()

            student = records.first()
            # name = student.name if student else "N/A"

            percentage = (present / total) * 100 if total > 0 else 0

            return render(request, "report.html", {
                'total': total,
                'present': present,
                'absent': absent,
                'percentage': round(percentage, 2),
                'roll': roll,
                'data': records
            })
        else:
            return render(request, "report.html", {
                'error': "Roll no. not found"
            })

    return render(request, "report.html")

def capture(request):
    return render(request,"capture.html")
    
def recognize(request):
    msg = ""

    today = date.today()
    entries = Entry.objects.all()

    for e in entries:
        if not Attend.objects.filter(roll=e.roll, tarikh=today).exists():
            Attend.objects.create(
                roll=e.roll,
                classname=e.classname,
                tarikh=today,
                attendance="Absent"
            )

    if request.method == "POST":
        roll = request.POST.get("roll")
        attendance = request.POST.get("attend")
        lat = request.POST.get("latitude")
        lng = request.POST.get("longitude")

        if Attend.objects.filter(roll=roll, tarikh=today).exists():
            Attend.objects.filter(roll=roll, tarikh=today).update(
                attendance=attendance,
                latitude=lat if lat else None,
                longitude=lng if lng else None
            )
            msg = "Attendance updated (Present)"
        else:
            msg = "Error: Student not found"

    return render(request, 'recognize.html', {"msg": msg})

def test(request):
    msg = ""

    if request.method == "POST":
        roll = request.POST.get("roll")
        name = request.POST.get("name")
        classname = request.POST.get("classname")
        Entry.objects.create(roll=roll, name=name , classname=classname)
        msg = "Entry saved successfully ✅"

    return render(request, "test.html", {"msg": msg})

def transfer_data(request):
    today = date.today()
    entries = Entry.objects.all()

    for e in entries:
        if not Attend.objects.filter(roll=e.roll, classname=e.classname).exists():
            Attend.objects.create(
                roll=e.roll,
                classname=e.classname,
                tarikh=today,
                attendance="Absent"
            )

    return render(request, "entry.html", {"data": entries,"aajkadate":today,"attendance":"Absent"})

def entryfilter(request):
     if request.method == 'POST':
        classname = request.POST.get('classname')
        

        data = Entry.objects.filter(classname=classname)
        return render(request, "entry.html", {'data': data})

     return render(request,'entryfilter.html')
 
def query(request):
    data = Entry.objects.all()
    
    return render(request, "query_selector.html",{"data": data}) 
