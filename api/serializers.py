from rest_framework import serializers

from .models import Task, Executor


class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    executor = serializers.SlugRelatedField(
        many=False,
        slug_field='name',
        queryset=Executor.objects.all()
    )

    class Meta:
        model = Task
        fields = ('id', 'title', 'comment', 'priority',
                  'created_at', 'executor')
