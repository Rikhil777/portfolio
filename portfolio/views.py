from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Project, Skill, Experience, Education, Certification, Profile
from django.http import FileResponse, Http404
import os



def home(request):
    # get_or_none pattern — won't crash if profile not added yet
    profile        = Profile.objects.first()
    projects       = Project.objects.all()
    skills         = Skill.objects.all()
    experiences    = Experience.objects.all()
    educations     = Education.objects.all()
    certifications = Certification.objects.all()

    return render(request, 'portfolio/home.html', {
        'profile'       : profile,
        'projects'      : projects,
        'skills'        : skills,
        'experiences'   : experiences,
        'educations'    : educations,
        'certifications': certifications,
    })


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
    })
    
def certificate_detail(request, pk):
    cert = get_object_or_404(Certification, id=pk)
    return render(request, 'portfolio/certificate_detail.html', {
        'cert': cert,
    })

def certificate_download(request, pk):
    cert = get_object_or_404(Certification, id=pk)
    if not cert.certificate_file:
        raise Http404
    file_path = cert.certificate_file.path
    filename  = os.path.basename(file_path)
    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
        filename=filename
    )

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name    = form.cleaned_data['name']
#             email   = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             send_mail(
#                 subject=f'Portfolio contact from {name}',
#                 message=f'From: {email}\n\n{message}',
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[settings.EMAIL_HOST_USER],
#             )
#             return redirect('contact-success')
#     else:
#         form = ContactForm()

#     return render(request, 'portfolio/contact.html', {'form': form})
def contact(request):
    return render(request, 'portfolio/contact.html')

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')