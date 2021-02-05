from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
from backpython.settings import FILES_ROOT

# This key will serve all examples in this document.
KEY = "3d7dbe5381d04035b5c322b6d3260e82"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://djangotaskpruebadany.cognitiveservices.azure.com/"


def DetectFaceEmotions(imageName, imageUrl):

    # Create an authenticated FaceClient.
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    # Detect a face in an image that contains a single face
    fileURL = FILES_ROOT + imageUrl
    single_face_image = open(fileURL, "rb")
    single_image_name = imageName
    # We use detection model 3 to get better performance.
    detected_faces = face_client.face.detect_with_stream(
        image=single_face_image,
        detection_model="detection_01",
        return_face_attributes=["emotion"],
    )

    if not detected_faces:
        raise Exception("No face detected from image {}".format(single_image_name))

    # Convert width height to a point in a rectangle
    def getRectangle(faceDictionary):
        rect = faceDictionary.face_rectangle
        left = rect.left
        top = rect.top
        right = left + rect.width
        bottom = top + rect.height

        return ((left, top), (right, bottom))

    # Download the image from the url
    img = Image.open(single_face_image)

    # For each face returned use the face rectangle and draw a red box.
    print("Drawing rectangle around face... see popup for results.")
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        faceEmotions = face.face_attributes.emotion
        draw.rectangle(getRectangle(face), outline="red", width=5)

    # Display the image in the users default image browser.
    img.save(fileURL)
    single_face_image.close()

    return faceEmotions
