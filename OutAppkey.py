from mastodon import Mastodon
Mastodon.create_app("toot & tweet",
    api_base_url = "https://mstdn.jp",
    to_file = "app_key.txt"
)
