from django.urls import path, include
from slack_api.views import BotSettings
from slack_api.views import handle_slack_event

urlpatterns = [
    # path('', BotSettings.as_view()),
     path('', handle_slack_event, name='slack_event')
]