from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializer import ImageSerializer
from .face import DetectFaceEmotions
from .emotions import emotions
from .models import Image
from backpython.settings import FILES_ROOT
import os

# Create your views here.
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def UploadFace(request):
    """
    Funcion para subir documento en formato formulario html
    {
        "nombre": "",
        "image": "",
    }
    """

    serializerUpload = ImageSerializer(data=request.data)

    if serializerUpload.is_valid():
        serializerUpload.save()

        faceEmotions = DetectFaceEmotions(
            imageUrl=serializerUpload.data["image"]
        )


        if faceEmotions == 1:
            return Response("No se encontro una cara", status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(
            {
                "emotions": emotions(faceEmotions.as_dict()),
                "image": serializerUpload.data["image"],
                "name": serializerUpload.data["name"],
            },
            status=status.HTTP_200_OK,
        )
    return Response(serializerUpload.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def DeleteFace(request):
    b = Image.objects.get()
    file = FILES_ROOT+"/uploads/"+str(b.image)
    os.remove(file)
    b.delete()
    return Response('Se elimino la imagen', status=status.HTTP_200_OK)
