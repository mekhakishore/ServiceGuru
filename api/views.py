from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from rest_framework.decorators import action

from api.serializers import CustomerSeializer,WorkSerializer

from rest_framework.generics import CreateAPIView

from api.models import Customer


class CustomerViewSetView(ModelViewSet):

    serializer_class=CustomerSeializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(technician=self.request.user)


     #url:http://127.0.0.1:8000/api/customer/{id}/add_work

     #method :POST

    @action(methods=["post"],detail=True)

    def add_work(self,request,*args,**kwargs):    
        
        id=kwargs.get("pk")
        
        customer_instance=Customer.objects.get(id=id)

        serializer=WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        


    #rest_framework>generics.py
        # class createapiview

#class WorkCreateView(CreateAPIView):    

#    serializer_class=WorkSerializer

#    def perform_create(self,serializer):

#        id=self.kwargs.get("pk")

#        customer_instance=Customer.objects.get(id=id)
 #       serializer.save(customer=customer_instance)


        

        







  



  
        


       














