from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    return HttpResponse(f"""<h2>Django</h2> <p>О дивный  новый мир!</p>""")


def about(request):
    return HttpResponse(f"""<h2>Давыдовский Константин Викторович</h2> <p>Уставший путник.</p>
        <a href=https://vk.com/id45427336>VK</a>""")

