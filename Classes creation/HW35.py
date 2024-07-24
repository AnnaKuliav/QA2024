class VideoContent:
    total_videos = 0

    def __init__(self, title, licensor, duration):

        self.title = title
        self.licensor = licensor
        self.duration = duration
        VideoContent.total_videos += 1

    def get_duration_minutes(self):
       return self.duration / 60

    def display_info(self):
        print(
            f"Title: {self.title}, Licensor: {self.licensor}, Duration: {self.duration} seconds ({self.get_duration_minutes()} minutes)")

    @classmethod
    def display_total_videos(cls):
        print(f"Total number of videos: {cls.total_videos}")

    @staticmethod
    def is_premium(duration):
        return duration > 1200


class Publisher:
    total_publishers = 0

    def __init__(self, name, website):
        self.name = name
        self.website = website
        self.videos = []
        Publisher.total_publishers += 1

    def add_video(self, video):
        self.videos.append(video)

    def display_info(self):
        print(f"Publisher: {self.name}, Website: {self.website}")
        print("Videos:")
        for video in self.videos:
            video.display_info()

    @classmethod
    def display_total_publishers(cls):
        print(f"Total number of publishers: {cls.total_publishers}")



video1 = VideoContent("News Highlights", "TV Station", 900)
video2 = VideoContent("Weekly Roundup", "News Agency", 1500)

video1.display_info()
video2.display_info()
VideoContent.display_total_videos()
print(VideoContent.is_premium(video2.duration))


publisher1 = Publisher("News Publisher", "www.newspublisher.com")
publisher2 = Publisher("Entertainment Publisher", "www.entertainmentpublisher.com")

publisher1.add_video(video1)
publisher1.add_video(video2)

publisher1.display_info()
Publisher.display_total_publishers()