from rest_framework import serializers
from .models import CustomUser, ClassModel, Course, Message

class ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError:
            # If it's not a valid image file, assume it's a URL
            return data

class CustomUserSerializer(serializers.ModelSerializer):
    myClasses = serializers.PrimaryKeyRelatedField(queryset=ClassModel.objects.all(), many=True)
    myCourses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    image = ImageField(allow_null=True, required=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = '__all__'
        extra_kwargs = {
            'myClasses': {'required': False},
            'myCourses': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
         # Extract the class_id from the validated_data
        class_id = validated_data.pop('class_id', None)
        course_id = validated_data.pop('course_id', None)

        # Handle myClasses and myCourses
        my_classes_data = validated_data.pop('myClasses', [])
        my_courses_data = validated_data.pop('myCourses', [])

        user = super().create(validated_data)
        user.set_password(password)

        # Check if class_id is provided and is a valid integer
        if class_id is not None and isinstance(class_id, int) and course_id is not None and isinstance(class_id, int):
            try:
                # Attempt to get the ClassModel instance
                class_instance = ClassModel.objects.get(pk=class_id)
                course_instance = Course.objects.get(pk=course_id)
                # Add the class to myClasses
                user.myClasses.add(class_instance)
                user.myCourses.add(course_instance)
            except ClassModel.DoesNotExist:
                # Handle the case where the ClassModel does not exist
                pass

        user.save()

        return user
    

class ClassModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassModel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        
# class MessageSerializer(serializers.ModelSerializer):
#     replies = serializers.SerializerMethodField()

#     def get_replies(self, obj):
#         # Recursive serialization to include replies for each message
#         replies = Message.objects.filter(repliesTo=obj)
#         return MessageSerializer(replies, many=True).data

#     class Meta:
#         model = Message
#         fields = ['id', 'author', 'post', 'created', 'replies', 'repliesTo']
        
class MessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        # Fetch only the IDs of messages that reply to the current message
        replies_ids = Message.objects.filter(repliesTo=obj).values_list('id', flat=True)
        return list(replies_ids)

    class Meta:
        model = Message
        fields = ['id', 'author', 'post', 'created', 'replies', 'repliesTo']