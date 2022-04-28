from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class Genre(models.Model):
    """
    Model representing a song genre.
    """
    name = models.CharField(max_length=200, help_text="Enter song genre")

    def __str__(self) -> str:
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Singer(models.Model):
    """
    Model representing an singer.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a short description")
    

    def get_absolute_url(self):
        """
        Returns the url to access a particular singer instance.
        """
        return reverse('singer-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class Song(models.Model):
    """
    Model representing a song.
    """
    name = models.CharField(max_length=200)
    singer = models.ForeignKey('Singer', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because song can only have one singer, but singers can have multiple songs
    # Singer as a string rather than object because it hasn't been declared yet in the file.
    lyrics = models.TextField(help_text="Enter a song text")
    chords = models.TextField(help_text="Enter the list of chords")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this song")
    # ManyToManyField used because genre can contain many songs. Songs can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url to access a particular song instance.
        """
        return reverse('song-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'