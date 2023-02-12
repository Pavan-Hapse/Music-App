from MusicPlayer.MusicApp.models import Musics

def MusicList(request):
    music = Musics.objects.all()


