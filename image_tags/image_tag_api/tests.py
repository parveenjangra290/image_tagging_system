import io
from django.utils import timezone
from PIL import Image as pil_img
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

class CreateUpdateImageTagTests(APITestCase):
    
    def setUp(self):
        """
            Setup Test
        """
        self.test_image_id = False
        self.normal_user = User.objects.create(
            first_name="Parveen",
            last_name="Kumar",
            username="parveenkumar",
            email="parveenkumar@example.com",
            is_active=True)
        self.normal_user.set_password('parveen@123#')
        self.normal_user.save()
        self.existing_token = Token.objects.filter(user=self.normal_user)[0].key

    def generate_image(self):
        """
        Generate Image to pass in API.
        """
        file = io.BytesIO()
        image = pil_img.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_tag_create(self):
        """
            Create Tag
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.existing_token)
        data = {
            "name": "NewTag"
        }
        res = self.client.post('/api/v1/tag/', data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_image_create_update(self):
        """
        Test create/update image.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.existing_token)
        image_file = self.generate_image()

        data = {
            "image": image_file,
            "description": "test image"
        }
        res = self.client.post('/api/v1/image/', data, format='multipart')
        if res.status_code == status.HTTP_200_OK:
            self.test_image_id = res.json().get('id', False)
        print("Create Image API...")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print("Update Image API...", self.test_image_id)
        # Here we will update same image, created above
        update_data = {
            "description": "Updated test image"
        }
        url = '/api/v1/image/update/'+str(self.test_image_id)+'/'
        response = self.client.put(url, update_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('description'), 'Updated test image')



    def test_search_images(self):
        """
            Test Search Image API based on start date and end date.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.existing_token)
        url = '/api/v1/images/search/'
        params ={
            'start_date':  str(timezone.now().date()),
            'end_date': str(timezone.now().date())
        }
        res = self.client.get(url, params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
            
