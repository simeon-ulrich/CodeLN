from django.test import TestCase
from rest_framework.test import APIClient
from .models import Badge, Model3d, CustomUser
from .utils import check_collector_badge, check_pioneer_badge, check_star_badge
from django.utils import timezone

class BadgeTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', email='testuser@gmail.com', password="admin099987@")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_badges(self):
        badge1 = Badge.objects.create(user=self.user, badge_type='Star')
        badge2 = Badge.objects.create(user=self.user, badge_type='Collector')
        response = self.client.get(f'/api/action/user/{self.user.id}/badges/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_check_collector_badge(self):
        for i in range(6):
            Model3d.objects.create(user=self.user, views=100)
        check_collector_badge(self.user.id)
        self.assertEqual(Badge.objects.filter(user_id=self.user.id, badge_type='Collector').count(), 1)

    def test_check_pionneer_badge(self):
        self.user.date_joined = timezone.now() - timezone.timedelta(days=400)
        self.user.save()
        check_pioneer_badge(self.user.id, self.user.date_joined)
        self.assertEqual(Badge.objects.filter(user_id=self.user.id, badge_type='Pionneer').count(), 1)

    def test_check_star_badge(self):
        model = Model3d.objects.create(user=self.user, views=1500)
        check_star_badge(self.user.id, model.id)
        self.assertEqual(Badge.objects.filter(user_id=self.user.id, badge_type='Star').count(), 1)
