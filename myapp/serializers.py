from rest_framework import serializers
from .models import AssingnedAuthority

class AssingnedAuthoritySerializer(serializers.ModelSerializer):
  class Meta:
    model = AssingnedAuthority
    fields = ['id', 'members_name', 'phone', 'password']