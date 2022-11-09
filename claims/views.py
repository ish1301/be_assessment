from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from claims.models import Claim
from claims.serializers import ClaimFormSerializer, ClaimSerializer


class ClaimsViewSet(viewsets.ModelViewSet):
    """
    Process API claims.

    * Require input file
    """
    permission_classes = [AllowAny]
    parser_classes = (FileUploadParser,)
    queryset = Claim.objects.all()
    default_serializer_class = ClaimSerializer
    serializers_classes = {
        'create': ClaimFormSerializer,
    }

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)

    def post(self, request):
        """
        Return 
        """
        file_obj = request.data['file']
        print(file_obj)

        return Response({})

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)