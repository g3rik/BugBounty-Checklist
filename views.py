from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Website, MasterChecklist, Result, MasterTopic
from django.views.decorators.csrf import csrf_exempt
import pdfplumber

def website_list(request):
    websites = Website.objects.all()
    return render(request, 'website.html', {'websites': websites})

# def checklist_detail(request, website_id):
#     website = get_object_or_404(Website, id=website_id)
#     points = Result.objects.filter(website=website)
#     return render(request, 'checklist_detail.html', {'website': website, 'points': points})


def checklist_detail(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    points = Result.objects.filter(website=website).select_related('checkpoint__topic')
    grouped_checklists = {}
    for point in points:
        topic = point.checkpoint.topic
        title = point.checkpoint.title
        if topic not in grouped_checklists:
            grouped_checklists[topic] = [point]
        else:
            grouped_checklists[topic].append(point)

    print (grouped_checklists)
    
    return render(request, 'checklist_detail.html', {'website': website, 'grouped_checklists': grouped_checklists})


@csrf_exempt
def update_checklist_data(request):
    if request.method == 'POST':
        point_id = request.POST.get('point_id')
        output = request.POST.get('output')
        result_obj = Result.objects.get(id=point_id)
        result_obj.output = output
        result_obj.save()
        print(result_obj.id)
        print(result_obj.output)
        return redirect('checklist_detail', website_id=result_obj.website.id)

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        website_obj = Website.objects.create(name=name, url=url)
        MasterChecklist_obj = MasterChecklist.objects.all().order_by('-id')
        for checklist in MasterChecklist_obj:
            Result.objects.create(website=website_obj, checkpoint=checklist)
    else:
        return render(request, 'add_target_page.html')
    return render(request, 'website.html')

# def change(a):
#     topic_obj = MasterTopic.objects.get(id=a)
#     for i in range(35,37):
#         checklist_obj = MasterChecklist.objects.get(id=i)
#         checklist_obj.topic = topic_obj
#         checklist_obj.save()

#     return 'done'

# # change(1)

# print(MasterTopic.objects.get(id=1).title)