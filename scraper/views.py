from celery import Task
from django.shortcuts import render
from scraper.models import Job
from scraper.tasks import scrape_coin
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job, Task
from .serializers import JobSerializer, TaskSerializer


def home(request):
    # send all routes with data
    routes= [
            {
                'path': '/',
                'description': 'Home page',
                'methods': ['GET'],
            },
            {
                'path': '/api/taskmanager/start_scraping',
                'description': 'Start scraping',
                'methods': ['POST'],
            },
            {
                'path': '/api/taskmanager/scraping_status/<uuid:job_id>',
                'description': 'Get scraping status',
                'methods': ['GET'],
            },
    ]
    return render(request, 'home.html', {'routes': routes})


from rest_framework import status

class StartScrapingView(APIView):
    def post(self, request):
        try:
            coins = request.data.get('coins')
            if not coins:
                return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            job_serializer = JobSerializer(data={})
            if job_serializer.is_valid():
                job = job_serializer.save()
                for coin in coins:
                    task_serializer = TaskSerializer(data={'job': job.id, 'coin': coin})
                    if task_serializer.is_valid():
                        task = task_serializer.save()
                        scrape_coin.delay(job.id, coin)
                    else:
                        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'job_id': str(job.id)}, status=status.HTTP_201_CREATED)
            else:
                return Response(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            tasks = Task.objects.filter(job=job)
            job_serializer = JobSerializer(job)
            task_serializer = TaskSerializer(tasks, many=True)
            return Response({
                'job_id': str(job.id),
                'tasks': task_serializer.data
            })
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=404)