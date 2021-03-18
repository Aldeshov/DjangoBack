import datetime

from rest_framework import serializers
from main.models import List, Task, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', )


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    task = serializers.CharField()
    created = serializers.DateField(read_only=True)
    due_on = serializers.DateField()
    owner = PersonSerializer(read_only=True)
    mark = serializers.BooleanField()
    list = ListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'task', 'created', 'due_on', 'owner', 'mark', 'list', )


class CreateUpdateTaskSerializer(serializers.Serializer):
    task = serializers.CharField()
    due_on = serializers.DateField()
    owner_id = serializers.IntegerField(write_only=True)
    mark = serializers.BooleanField()
    list_id = serializers.IntegerField(write_only=True)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task')
        instance.due_on = validated_data.get('due_on')
        instance.mark = validated_data.get('mark')
        instance.save()
        return instance

    def create(self, validated_data):
        new = Task.objects.create(task=validated_data.get('task'),
                                  created=datetime.datetime.now(),
                                  due_on=validated_data.get('due_on'),
                                  owner=Person.objects.get(id=validated_data.get('owner_id')),
                                  mark=validated_data.get('mark'),
                                  list=List.objects.get(id=validated_data.get('list_id')))
        return new
