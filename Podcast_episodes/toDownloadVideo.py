import yt_dlp
import ffmpeg
import os

def download_video():
    # Ask for the LinkedIn video post link
    url = input("Enter the video post link: ")
    
    # Configuration options for yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save the video with its title as the filename
        'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
    }

    try:
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download complete.")
            # Get the downloaded file name
            downloaded_file = ydl.prepare_filename(ydl.extract_info(url, download=False))
            return downloaded_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert_mp4_to_mp3(mp4_file):
    if mp4_file and mp4_file.endswith(".mp4"):
        # Ask user for the custom filename for the MP3 file
        custom_filename = input("Enter the desired filename for the MP3 (without extension): ")
        mp3_file = f"{custom_filename}.mp3"  # Add .mp3 extension to the custom filename
        
        # Use ffmpeg to convert the MP4 file to MP3
        try:
            ffmpeg.input(mp4_file).output(mp3_file, audio_bitrate='192k').run()
            print(f"Conversion complete: {mp3_file}")
            # Optionally, remove the original MP4 file
            os.remove(mp4_file)
            print(f"Removed original video file: {mp4_file}")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")
    else:
        print("The file is not a valid MP4 file.")

if __name__ == "__main__":
    # Step 1: Download the video
    mp4_file = download_video()

    # Step 2: Convert the downloaded MP4 to MP3
    convert_mp4_to_mp3(mp4_file)
