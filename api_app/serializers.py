from rest_framework import serializers
from . models import *


class StudentSerializer(serializers.ModelSerializer):
    # Validators ----- to add for modelserializer class this way
    # def start_with_r(value):
    #     if value[0].lower() != 'r':
    #         raise serializers.ValidationError('Name Should be Start with R')
    # name = serializers.CharField(validators = [start_with_r])
    # if we want to add argument in any field 
    # we need to add explicitly for that field
    # name = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = '__all__'
        # to make read_only for multiple fields then we can use like this!
        # ready_only_fields = ['name','roll']
        # We can also declare using extra_kwargs for it 
        # extra_kwargs = {'name':{'read_only' :True}}
        
    # Field Level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return 
    
    # Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
    
