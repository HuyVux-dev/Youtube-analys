from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()
api_key = os.getenv("YOUR_API_KEY")


def get_youtube_comments(api_key, video_id):
    # Tạo dịch vụ YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    comments = []
    try:
        # Khởi tạo yêu cầu để lấy danh sách bình luận
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100  # Số lượng bình luận mỗi lần lấy (tối đa 100)
        )
        response = request.execute()

        # Lặp qua tất cả các bình luận và thêm vào danh sách
        while request:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comments.append(f"{author}: {comment}")

            # Kiểm tra xem còn trang tiếp theo của bình luận không (nextPageToken)
            if 'nextPageToken' in response:
                request = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    pageToken=response['nextPageToken'],
                    maxResults=100
                )
                response = request.execute()
            else:
                break

    except HttpError as e:
        print(f"Lỗi khi gọi API: {e}")

    return comments


# Ví dụ sử dụng
video_id = "A4tjw6u1z2Q"  # Thay thế bằng ID video của bạn
comments = get_youtube_comments(api_key, video_id)

# In ra các bình luận
for idx, comment in enumerate(comments):
    print(f"{idx + 1}. {comment}")