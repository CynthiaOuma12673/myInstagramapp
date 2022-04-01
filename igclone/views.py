from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect,get_object_or_404
from .models import Follow, Image,Profile,Comments
from django.contrib.auth.models import User
from .forms import NewsLetterForm, UpdateUserForm, UpdateUserProfileForm, UserRegisterForm,PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.

