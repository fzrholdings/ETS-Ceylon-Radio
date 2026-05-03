import os
import subprocess

def stream_radio():
    songs_dir = "songs"
    
    songs = [f for f in os.listdir(songs_dir) if f.endswith('.mp3')]
    
    if not songs:
        print("Did not found any songs!")
        return

    while True:
        for song in songs:
            song_path = os.path.join(songs_dir, song)
            print(f"Now Playing: {song}")
            
            cmd = [
                'ffmpeg', '-re', '-i', song_path,
                '-c:a', 'libmp3lame', '-b:a', '128k',
                '-f', 'mp3', os.environ.get('STREAM_URL')
            ]
            subprocess.run(cmd)

if __name__ == "__main__":
    stream_radio()
