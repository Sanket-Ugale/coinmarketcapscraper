from django.urls import include, path

from scraper import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/taskmanager/start_scraping', views.StartScrapingView.as_view()),
    path('api/taskmanager/scraping_status/<uuid:job_id>', views.ScrapingStatusView.as_view()),
]