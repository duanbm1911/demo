from django.core.management.base import BaseCommand
from core.models import Event, About
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Load sample data for Opera website'

    def handle(self, *args, **kwargs):
        # Create Events
        events_data = [
            {
                'title': 'La Traviata',
                'description': 'Vở opera bất hủ của Verdi về câu chuyện tình yêu bi thương của Violetta và Alfredo. Với dàn nhạc giao hưởng và giọng ca opera đẳng cấp.',
                'date': timezone.now() + timedelta(days=30),
                'price_min': 500000,
                'price_max': 2000000,
                'icon': '🎭',
                'is_featured': True,
            },
            {
                'title': 'Carmen',
                'description': 'Tác phẩm kinh điển của Bizet với những giai điệu nồng nàn và kịch tính. Câu chuyện tình yêu đầy ám ảnh tại Seville.',
                'date': timezone.now() + timedelta(days=38),
                'price_min': 600000,
                'price_max': 2500000,
                'icon': '🎼',
                'is_featured': True,
            },
            {
                'title': 'Madama Butterfly',
                'description': 'Bi kịch cảm động của Puccini về tình yêu và hy sinh của Cio-Cio-San. Một trong những vở opera được yêu thích nhất.',
                'date': timezone.now() + timedelta(days=45),
                'price_min': 500000,
                'price_max': 2000000,
                'icon': '🎵',
                'is_featured': True,
            },
            {
                'title': 'The Phantom of the Opera',
                'description': 'Vở nhạc kịch huyền thoại của Andrew Lloyd Webber. Câu chuyện bí ẩn và lãng mạn dưới hầm Opera Paris.',
                'date': timezone.now() + timedelta(days=53),
                'price_min': 700000,
                'price_max': 3000000,
                'icon': '🎹',
                'is_featured': False,
            },
            {
                'title': 'Rigoletto',
                'description': 'Kiệt tác của Verdi kể về bi kịch của người cha và tình yêu đầy nước mắt.',
                'date': timezone.now() + timedelta(days=61),
                'price_min': 500000,
                'price_max': 2000000,
                'icon': '🎪',
                'is_featured': False,
            },
            {
                'title': 'Don Giovanni',
                'description': 'Opera hài hước và kịch tính của Mozart về Don Juan, kẻ sát gái khét tiếng.',
                'date': timezone.now() + timedelta(days=72),
                'price_min': 550000,
                'price_max': 2200000,
                'icon': '🎺',
                'is_featured': False,
            },
        ]

        for event_data in events_data:
            Event.objects.get_or_create(
                title=event_data['title'],
                defaults=event_data
            )

        # Create About content
        about_data = [
            {
                'title': 'Hồ Gươm Opera - Nơi nghệ thuật hội tụ',
                'content': '''Tọa lạc tại trung tâm Hà Nội, Hồ Gươm Opera là nhà hát opera đầu tiên tại Việt Nam mang đến những trải nghiệm nghệ thuật đẳng cấp quốc tế.

Với hệ thống âm thanh hiện đại, sân khấu chuyên nghiệp và đội ngũ nghệ sĩ tài năng, chúng tôi cam kết mang đến những buổi biểu diễn xuất sắc nhất cho khán giả Việt Nam.

Hồ Gươm Opera không chỉ là nơi biểu diễn opera cổ điển mà còn là không gian văn hóa nghệ thuật đa dạng với các chương trình âm nhạc, ballet và kịch nghệ đương đại.''',
                'order': 1,
            }
        ]

        for about in about_data:
            About.objects.get_or_create(
                title=about['title'],
                defaults=about
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))
