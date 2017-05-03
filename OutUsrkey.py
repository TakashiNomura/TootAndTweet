from mastodon import Mastodon

mastodon = Mastodon(
    client_id="app_key.txt",
    api_base_url = "https://mstdn.jp")

mastodon.log_in(
    "登録メールアドレス",
    "パスワード",
    to_file = "user_key.txt")
