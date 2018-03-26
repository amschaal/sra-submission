from rest_framework import serializers
from dnaorder.models import Submission, SubmissionType, SubmissionFile,\
    SubmissionStatus, Note
import os

class SubmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionType
        fields = ['id','name']

class SubmissionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionStatus
        fields = ['id','name']

class SubmissionSerializer(serializers.ModelSerializer):
    type = SubmissionTypeSerializer(read_only=True)
    status = SubmissionStatusSerializer(read_only=True)
    class Meta:
        model = Submission
        exclude = []

class SubmissionFileSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    def get_filename(self,instance):
        return os.path.basename(instance.file.name)
    def get_size(self,instance):
        return instance.formatted_size()
    def get_date(self,instance):
        return instance.formatted_date()
    class Meta:
        model = SubmissionFile
        exclude = []

class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    def get_created_by(self,instance):
        return str(instance.created_by)
    class Meta:
        model = Note
        exclude = []