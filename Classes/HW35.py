class VideoContent:
    """
    VideoContent class to represent a piece of video content with its attributes and methods.
    """

    # Class field
    total_videos = 0

    def __init__(self, title, licensor, duration):
        """
        Initialize the video content instance.

        :param title: Title of the video
        :param licensor: Licensor of the video content
        :param duration: Duration of the video in seconds
        """
        self.title = title
        self.licensor = licensor
        self.duration = duration
        VideoContent.total_videos += 1

    def get_duration_minutes(self):
        """
        Calculate the duration of the video in minutes.

        :return: Duration in minutes
        """
        return self.duration / 60

    def display_info(self):
        """
        Display information about the video content.
        """
        print(
            f"Title: {self.title}, Licensor: {self.licensor}, Duration: {self.duration} seconds ({self.get_duration_minutes()} minutes)")

    @classmethod
    def display_total_videos(cls):
        """
        Display the total number of video content instances created.
        """
        print(f"Total number of videos: {cls.total_videos}")

    @staticmethod
    def is_premium(duration):
        """
        Determine if a video is considered premium based on its duration.

        :param duration: Duration of the video in seconds
        :return: True if the video is premium (longer than 1200 seconds), False otherwise
        """
        return duration > 1200


class Publisher:
    """
    Publisher class to represent a publisher with its attributes and methods.
    """

    # Class field
    total_publishers = 0

    def __init__(self, name, website):
        """
        Initialize the publisher instance.

        :param name: Name of the publisher
        :param website: Website of the publisher
        """
        self.name = name
        self.website = website
        self.videos = []
        Publisher.total_publishers += 1

    def add_video(self, video):
        """
        Add a video to the publisher's list of videos.

        :param video: An instance of VideoContent
        """
        self.videos.append(video)

    def display_info(self):
        """
        Display information about the publisher.
        """
        print(f"Publisher: {self.name}, Website: {self.website}")
        print("Videos:")
        for video in self.videos:
            video.display_info()

    @classmethod
    def display_total_publishers(cls):
        """
        Display the total number of publisher instances created.
        """
        print(f"Total number of publishers: {cls.total_publishers}")


# Creating instances and demonstrating their functionality

# VideoContent instances
video1 = VideoContent("News Highlights", "TV Station", 900)
video2 = VideoContent("Weekly Roundup", "News Agency", 1500)

video1.display_info()  # Display video1 information
video2.display_info()  # Display video2 information
VideoContent.display_total_videos()  # Display total number of video instances
print(VideoContent.is_premium(video2.duration))  # Check if video2 is premium

# Publisher instances
publisher1 = Publisher("News Publisher", "www.newspublisher.com")
publisher2 = Publisher("Entertainment Publisher", "www.entertainmentpublisher.com")

publisher1.add_video(video1)  # Add video1 to publisher1
publisher1.add_video(video2)  # Add video2 to publisher1

publisher1.display_info()  # Display publisher1 information
Publisher.display_total_publishers()  # Display total number of publisher instances