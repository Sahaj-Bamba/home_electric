from django.shortcuts import render

# Create your views here.


def user_room(request):
    if request.method == 'POST':
        data = request.POST.copy()
        request.session['room_number'] = data.get('hidden_room')

    return render(request, 'accounts\\room.html', {})

