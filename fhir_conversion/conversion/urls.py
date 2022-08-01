from django.urls import path

from conversion import views

urlpatterns = [
    path('hl7tofhir/<str:template_name>/<str:resource_name>/',
         views.hl7_to_fhir_conversion,
         name='hl7_to_fhir_conversion')
]