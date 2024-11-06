from django.db import models
from gtts import gTTS

# Create your models here.

class Audio(models.Model):
    text = models.TextField()
    # audio path 
    audio_file = models.FileField(upload_to='audio_file/', blank=True)

    def save(self, *args, **kwargs):
        if not self.audio_file:
            tts = gTTS(text=self.text, lang='en', tld='us')
            audio_file_path = f'media/{self.text[:10]}.mp3'  # Save audio with first 10 chars of text as filename
            tts.save(audio_file_path)
            self.audio_file = audio_file_path
        super().save(*args, **kwargs)  # Call the real save() method  # For auto-update of audio_file field

    def __str__(self):
        return self.text[:10] # Returns the first ten words of the text