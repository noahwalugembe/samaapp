
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from api.models.dashboards import Dashboard
from api.serializers.dashboards import DashboardSerializer

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

#import csv
import csv
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from django.db.models import Q
from django.db import connection

from datetime import datetime


	
class level_Of_TutionlListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    
    def get_queryset(self):
        queryset_results = queryset
        
    def get(self, request, *args, **kwargs): 
        queryset = Dashboard.objects.all().only("boarding_fee_S3", "day_fee_S3","boarding_fee_S5")
        
        return HttpResponse(queryset)
    
    #queryset =Dashboard.objects.filter('boarding_fee_S3','day_fee_S3,boarding_fee_S5')

    
    
    
	
class Size_Of_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    queryset =Dashboard.objects.filter(olevel_students='1')
	

    

class FileuploadListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
	
    def get_queryset(self):
        queryset_results = queryset
		
    
    def get(self, request, *args, **kwargs):
	    
        with open('C:/Users/NOAH1/Documents/samaapp/api/views/Book1.csv' ) as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:  
                date = datetime.strptime(row['date_school_enrolled'], "%m/%d/%Y") 
                d=datetime.strftime(date, "%Y-%m-%d")
                #t= int(row['number_of_teachers'].strip())
                #s= int(row['number_of_students'].strip())
                
                p = Dashboard(community_unit=row['community_unit'], school_id =row[ 'school_id'], name=row['name'],olevel_students=row[ 'olevel_students'],alevel_students=row['alevel_students'],boarding_students=row['boarding_students'],day_students=row['Day_students'], boarding_fee_S3=row['boarding _fee_for _S3'],day_fee_S3=row[ 'day_fee_S3'],boarding_fee_S5=row[ 'boarding_fee_S5'], day_fee_S5=row[ 'day_fee_S5'],female_students =row[ 'female_students'],male_students=row['male_students'], 
                              number_of_students=row['number_of_students'].strip(),
                              number_of_teachers=row['number_of_teachers'].strip(),
                              location=row['location'],
                              date_school_enrolled= d
				   ) 
                
                              
                p.save()
                
  

class OlevelVsAlevelAndOlevelListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
       
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        olevel_students=Dashboard.objects.filter(olevel_students='1').count()
        alevel_students=Dashboard.objects.filter(alevel_students='1',olevel_students='1').count()
    
        q = Dashboard.objects.annotate(num_authors=Count('olevel_students'))        
        return HttpResponse(olevel_students/alevel_students)
    
    
class Teacher_To_Student_RatioListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    queryset =Dashboard.objects.filter(olevel_students='1')
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        xnumber_of_students=Dashboard.objects.filter(number_of_students='1').count()
        xnumber_of_teachers=Dashboard.objects.filter(number_of_teachers='1').count()
        
        cursor = connection.cursor()
        cursor_teachers = connection.cursor()
        cursor_students = connection.cursor()
        
        cursor_teachers.execute("SELECT  SUM(number_of_teachers) FROM api_dashboard")
        
        cursor_students.execute("SELECT  SUM(number_of_students) FROM api_dashboard")
        
        row_teachers = cursor_teachers.fetchall()  
        row_students = cursor_students.fetchall() 
        
        t=row_teachers.pop(0)
        s=row_students.pop(0)
        
        num_teachers = int(t[0])
        num_students = int(s[0])
        ratio=num_teachers/num_students
       
        return HttpResponse(ratio)
       
        


    
class Number_Of_EnroledSchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        cursor = connection.cursor()
        
        cursor.execute("SELECT  COUNT(number_of_students) FROM api_dashboard")
        school_number = cursor.fetchall() 
        
        s=school_number.pop(0)
    
             
             
        return HttpResponse(s)    
    
    
class Most_And_Least_Partner_SchoolsListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    #queryset = Dashboard.objects.all()
    
    
    def get_queryset(self):
        olevel_students=Dashboard.objects.filter(olevel_students='1')
       
    def get(self, request, *args, **kwargs):
        
        cursor_min = connection.cursor()
        cursor_max = connection.cursor()
        
        #cursor.execute("SELECT community_unit, school_id,name FROM api_dashboard GROUP BY community_unit")
        cursor_min.execute("SELECT community_unit, COUNT(community_unit) as c FROM api_dashboard GROUP BY community_unit ORDER BY c ASC     LIMIT 1")
        cursor_max.execute("SELECT community_unit, COUNT(community_unit) as c FROM api_dashboard GROUP BY community_unit ORDER BY c DESC LIMIT 1")
        
        schools_min = cursor_min.fetchall()
        schools_max = cursor_max.fetchall() 
        
        schools_min.append("min")
        schools_max.append("max")
        
              
    
        return HttpResponse(schools_min+schools_max)  

