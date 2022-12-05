from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        print(dir(request.user))
        return render(request, "web/index.html", {})
