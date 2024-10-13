from pytube import YouTube
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def get_title(url):
    yt = yt = YouTube(url)
    return yt.title


def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    query_params = parse_qs(parsed_url.query)
    # Lấy video ID từ tham số 'v'
    video_id = query_params.get("v")
    if video_id:
        return video_id[0]
    if parsed_url.netloc == "youtu.be":
        return parsed_url.path[1:]
    return None



from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

# ID của video YouTube
video_id = "A4tjw6u1z2Q"

# Hàm tự động lấy transcript theo ngôn ngữ có sẵn
def get_transcript_automatically(video_id):
    try:
        # Lấy danh sách các transcript có sẵn
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # In ra danh sách các transcript khả dụng
        print("Các transcript có sẵn:")
        for transcript in transcript_list:
            print(f" - {transcript.language_code} ({transcript.language})")

        # Ưu tiên lấy transcript tiếng Anh nếu có
        try:
            transcript = transcript_list.find_transcript(['en'])
            print("Transcript Tiếng Anh đã được chọn.")
        except NoTranscriptFound:
            # Nếu không có transcript tiếng Anh, lấy transcript đầu tiên khả dụng
            transcript = list(transcript_list)[0]  # Lấy transcript đầu tiên có sẵn
            print(f"Transcript '{transcript.language}' đã được chọn.")

        # Lấy transcript và gộp nội dung thành đoạn văn kèm thời gian
        full_transcript = ""
        for entry in transcript.fetch():
            start_time = entry['start']
            text = entry['text']
            full_transcript += f"[{start_time:.2f}s]: {text}\n"

        # In ra đoạn văn đã gộp
        print("\nNội dung transcript:")
        print(full_transcript.strip())

    except Exception as e:
        print("Không thể lấy được transcript:", e)

# Ví dụ sử dụng
video_id = "e1mgHCC4Ld4"  # Thay thế bằng ID video của bạn

# Gọi hàm để lấy transcript
get_transcript_automatically(video_id)

