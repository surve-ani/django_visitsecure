from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import Company, Branch, Department
from .serializers import CompanySerializer, BranchSerializer, DepartmentSerializer
from authentication.permissions import IsAdminUser, IsSecurityUser

# Create your views here.

class CompanyListApiView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        print("CompanyListApiView GET request received")
        print("Request user:", request.user)

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=CompanySerializer,
        security=[{'Bearer': []}]
    )
    def post(self, request):
        print("CompanyListApiView POST request received")
        print("Request user:", request.user)

        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class CompanyDetailApiView(APIView):

    def get(self, request, company_id):
        try:
            print("CompanyDetailApiView GET request received")
            print("Request user:", request.user)

            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=CompanySerializer
    )
    def patch(self, request, company_id):
        try:
            print("CompanyDetailApiView PATCH request received")
            print("Request user:", request.user)

            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, company_id):
        try:
            print("CompanyDetailApiView DELETE request received")
            print("Request user:", request.user)

            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

        company.delete()
        return Response({"message": "Company deleted successfully"}, status=204)


class BranchListApiView(APIView):

    def get(self, request):
        print("BranchListApiView GET request received")
        print("Request user:", request.user)

        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=BranchSerializer
    )
    def post(self, request):
        print("BranchListApiView POST request received")
        print("Request user:", request.user)

        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    