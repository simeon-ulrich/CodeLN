
from .models import Model3d, Badge
from django.utils import timezone

def check_star_badge(user_id, model_id):
    model = Model3d.objects.get(id=model_id)
    if model.views >= 1000:
        badge, created = Badge.objects.get_or_create(user_id=user_id, badge_type='Star')
        if created:
            print(f'Star badge awarded to user {user_id}')

def check_collector_badge(user_id):
    model_count = Model3d.objects.filter(user_id=user_id).count()
    if model_count >= 5:
        badge, created = Badge.objects.get_or_create(user_id=user_id, badge_type='Collector')
        if created:
            print(f'Collector badge awarded to user {user_id}')

def check_pioneer_badge(user_id, user_joined_date):
    one_year_ago = timezone.now() - timezone.timedelta(days=365)
    if user_joined_date < one_year_ago:
        badge, created = Badge.objects.get_or_create(user_id=user_id, badge_type='Pionneer')
        if created:
            print(f'Pioneer badge awarded to user {user_id}')
