from django.shortcuts import render, redirect
from .models import VoteingCampaign,Candidate,Student,Vote,ROLE_CHOICES
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from datetime import timedelta
import datetime
import pytz
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Count

# Create your views here.
def hello(request):
   return render(request, "Elections\login.html", {})

def login_request(request):

   if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('campaign_list')
   else:
      form = AuthenticationForm()
   return render(request, 'Elections\login.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect("login")

@login_required
def displayCampaignDetails(request,pk):

   if request.method == "POST":
      vcmp= get_object_or_404(VoteingCampaign, pk=pk)
      vcand = get_object_or_404(Candidate, pk=request.POST.get("candidate"))

      vote = Vote(votingCampaign=vcmp,voteForCandidate=vcand,vote=True,votedBy=request.user)
      vote.save()

   campaign = get_object_or_404(VoteingCampaign, pk=pk)
   candidates = Candidate.objects.filter(votingCampaign=pk)
   votingEntry=Vote.objects.filter(votingCampaign=pk,votedBy=request.user).first()

   d = timedelta(minutes=800) # change this value to get results
   expiryDate = campaign.datetime + d

   expired = not (datetime.datetime.now().replace(tzinfo=None) < expiryDate.replace(tzinfo=None))

   student = Student.objects.get(user=request.user)
   if not campaign.departmentDetails == student.departmentDetails:
      raise PermissionDenied

   # if expired:
   #    label = []
   #    data = []
   #    vote_result = Vote.objects.filter(votingCampaign=pk).values('voteForCandidate').order_by('voteForCandidate').annotate(count=Count('voteForCandidate'))
   #    for voter in vote_result:
   #       sd = Candidate.objects.get(pk=voter["voteForCandidate"])
   #       print(sd)
   #       label.append(sd.candidate.firstName+" "+sd.candidate.lastName)
   #       data.append(voter["count"])
   #       vote_result_data={
   #          "lable":label,
   #          "data":data
   #       }
         
   #    return render(request, "Elections\campaignDetails.html", {"data":candidates,"votingEntry":votingEntry,"expiryDate":expiryDate, "expired": expired,"vote_result_data":vote_result_data})
   # return render(request, "Elections\campaignDetails.html", {"data":candidates,"votingEntry":votingEntry,"expiryDate":expiryDate, "expired": expired})
   label = []
   data = []
   vote_result = Vote.objects.filter(votingCampaign=pk).values('voteForCandidate').order_by('voteForCandidate').annotate(count=Count('voteForCandidate'))
   vote_result_data = None
   for voter in vote_result:
      sd = Candidate.objects.get(pk=voter["voteForCandidate"])
      print(sd)
      label.append(sd.candidate.firstName+" "+sd.candidate.lastName)
      data.append(voter["count"])
      vote_result_data={
         "lable":label,
            "data":data
      }
      
   return render(request, "Elections\campaignDetails.html", {"data":candidates,"votingEntry":votingEntry,"expiryDate":expiryDate, "expired": expired,"vote_result_data":vote_result_data})

@login_required
def displayOnGoingCampaigns(request):
   #display only if user is logged in
   student = Student.objects.get(user=request.user)
   data = VoteingCampaign.objects.filter(departmentDetails=student.departmentDetails,classDetails=student.classDetails).order_by('-datetime')
   spl_campaign_data = None
   
   for item in data:
      d = timedelta(minutes=800) # change this value to get results
      expiryDate = item.datetime + d
      expired = not (datetime.datetime.now().replace(tzinfo=None) < expiryDate.replace(tzinfo=None))
      item.expired = "Expired" if expired else "Ongoing" 

   if student.role == 'SCR':
      spl_campaign_data=VoteingCampaign.objects.filter(level="SPS")
      for item in spl_campaign_data:
         d = timedelta(minutes=800) # change this value to get results
         expiryDate = item.datetime + d
         expired = not (datetime.datetime.now().replace(tzinfo=None) < expiryDate.replace(tzinfo=None))
         item.expired = "Expired" if expired else "Ongoing" 
   
   return render(request, "Elections\campaignsList.html", {"data":data,"department":student.departmentDetails,"class":student.classDetails,"spl_campaign_data":spl_campaign_data})