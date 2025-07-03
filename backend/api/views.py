import json
from django.http import JsonResponse



def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    # data['headers'] = request.headers
    # print(request.headers)
    data['headers'] = dict(request.headers)
    # json.dumps(dict(request.headers))
    data['content_type'] = request.content_type

    # return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    return JsonResponse(data)