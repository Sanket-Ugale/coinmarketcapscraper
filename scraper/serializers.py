from rest_framework import serializers
from .models import Job, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'  # include other fields if needed

    def get_tasks(self, obj):
        tasks = obj.task_set.all()
        return TaskSerializer(tasks, many=True).data