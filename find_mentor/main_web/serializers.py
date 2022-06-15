from dataclasses import fields
from  rest_framework import serializers
from . import models


class GikiansSerializer(serializers.ModelSerializer):
   class Meta:
      model=models.Gikians
      fields=('reg_no','id','username','hash','email','name','year','faculty')
   


