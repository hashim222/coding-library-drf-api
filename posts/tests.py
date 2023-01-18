from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """Post list views test cases"""

    def setUp(self):
        User.objects.create_user(username='hashimtest', password='welcome22')

    def test_can_list_posts(self):
        hashimtest = User.objects.get(username='hashimtest')
        Post.objects.create(owner=hashimtest, title='My post title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='hashimtest', password='welcome22')
        response = self.client.post(
            '/posts/', {'title': 'My post title', 'caption': 'my message'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post(
            '/posts/', {'title': 'My post title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """Post detail view tests cases"""

    def setUp(self):
        hashimtest = User.objects.create_user(
            username='hashimtest', password='welcome22')
        hash = User.objects.create_user(username='hash', password='welcome22')
        Post.objects.create(
            owner=hashimtest, title='a title', caption='hashimtest content'
        )
        Post.objects.create(
            owner=hash, title='another title', caption='hashs content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='hashimtest', password='welcome22')
        response = self.client.put(
            '/posts/1/', {'title': 'a new title', 'caption': 'Updated post'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='hashimtest', password='welcome22')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
