from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Song, Singer

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_songs=Song.objects.all().count()
    num_singers=Singer.objects.count()  # Метод 'all()' применён по умолчанию.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_songs':num_songs,'num_singers':num_singers, 'num_visits':num_visits},
    )

class SongListView(generic.ListView):
    model = Song
    paginate_by = 20

class SongDetailView(generic.DetailView):
    model = Song

    def song_detail_view(request,pk):
        try:
            song_id=Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404("Book does not exist")

        #book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/song_detail.html',
            context={'song':song_id,}
        )

    def chords_view(pk):
        song_id=Song.objects.get(pk=pk)
        song_id.lyrics = song_id.lyrics.replace('[', '<span class = "chord">').replace(']', '</span>')
        return song_id.lyrics

class SingerListView(generic.ListView):
    model = Singer

class SingerDetailView(generic.DetailView):
    model = Singer