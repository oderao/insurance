from django.shortcuts import render,render_to_response
from django.forms.models import model_to_dict

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from .serializers import RiskNameSerializer,RiskDetailsSerializer
from .models import RiskName,RiskDetails
from rest_framework.response import Response



class RiskNameViewSet(viewsets.ModelViewSet):

	serializer_class = RiskNameSerializer
	

	queryset = RiskName.objects.all()

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

	#get single risk type from using query params
	def list(self, request, *args, **kwargs):
		if request.method == 'GET' and request.query_params:
			name = self.request.query_params.get('name')
			if name:
				risk_names = RiskName.objects.all().filter(name=name)
				if risk_names:
					serializer = RiskNameSerializer(risk_names, many=True)
					return Response(serializer.data)
				if not risk_names:
					return Response({'response':'risk_type not found'})
		return Response({'response':'enter risk_type in query params'})



	
class RiskDetailsViewSet(viewsets.ModelViewSet):
	serializer_class = RiskDetailsSerializer

	queryset = RiskDetails.objects.all()

	#get all risk details using foreign key risk name
	#return custom error message if not found
	def list(self, request, *args, **kwargs):
		serializer_context = {
            'request': request,
        }
		if request.method == 'GET' and request.query_params:
			name = self.request.query_params.get('risk_name')
			if name:
				_risk_names = RiskName.objects.get(name=name)
				_risk_names = _risk_names.riskdetails_set.filter(risk_name__name=name)
				if _risk_names:
					serializer = RiskDetailsSerializer(_risk_names,context=serializer_context, many=True)
					return Response(serializer.data)
				if not _risk_names:
					return Response({'response':'risk_details not found'})
		return Response({'response':'enter risk_type in query params'})



def test_vue(request):

	context = {}
	if request.GET.get('name'):
	#return all risk details for given risk name
		name = request.GET.get('name')
		risk_details = RiskDetails.objects.filter(risk_name__name=name).values().first()
		if risk_details:
			context = risk_details
	return render_to_response('insurance/risk_details.html',context=risk_details)