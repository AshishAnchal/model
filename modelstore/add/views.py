from django.shortcuts import render
# from django.http import  JsonResponse
from .models import Attend 

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
    if request.method == "POST":
        roll = request.POST.get("roll")
        attendance = request.POST.get("attend")
        date = request.POST.get("date")
        lat = request.POST.get("latitude")
        lng = request.POST.get("longitude")

        Attend.objects.create(
            roll=roll,
            attendance=attendance,
            tarikh=date,
            latitude=lat if lat else None,
            longitude=lng if lng else None
        )
    return render(request,'recognize.html')    

def test(request):
    return render (request,'test.html')