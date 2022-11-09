from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.permissions import AllowAny




class ProcessClaim(APIView):
    """
    Process API claims.

    * Require input file
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Return 
        """
        print(request.FILES)

        return Response({})
