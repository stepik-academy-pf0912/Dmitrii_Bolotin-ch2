app_notification = '''Приложение в разработке.
Введите ”videos” чтобы посмотреть список видео.
Введите “tags” чтобы посмотреть список тегов.
Введите “playlists” чтобы посмотреть список тегов.
Введите “about” чтобы получить информацию.
'''

video_request = 'videos'
tags_request = 'tags'
playlists_request = 'playlists'
app_info_request = 'about'

# videos ------------------

video_1_title = "ИгроСториз: Mafia 4, GTA 6 и BioShock Online – Take-Two дает бой конкурентам на PS5 и Xbox Series X"
video_1_link = "05GPNjBtF48"

video_2_title = "Поиграли в Sekiro: Shadows Die Twice. Свежо, но знакомо"
video_2_link = "nwPs5f4WLN8"

video_3_title = "Gothic Remake - Актуально ли в 2021 году ? [Мнение после Демки]"
video_3_link = "eVtx5Y6lFjk"

# tags --------------------

tags = "action, fps, strategy, bloggers, letsplayers, simulator, arcade"

# playlists --------------

playlist_1_title = "ИгроСториз"
playlist_2_title = "Репортажи"
playlist_3_title = "Обзоры"

# common notifications ---

not_found_info = 'К сожалению, ничего не понятно!'
about_info = '''Stepik Media – О приложении. 
Это – кинотеатр полезных  видео про видеоигры.'''

# helpers ----------------

def get_videos_info():
    video_titles = [video_1_title, video_2_title, video_3_title]
    video_links = [video_1_link, video_2_link, video_3_link]
    video_info = 'У нас есть {0} видео:\n\n'.format(len(video_titles))

    for i, title in enumerate(video_titles):
        video_info += '{video_title}: youtu.be/{video_link}\n'.format(video_title=title, video_link=video_links[i])

    return video_info

def get_playlists_info():
    playlists = [playlist_1_title, playlist_2_title, playlist_3_title]
    return 'У нас есть {0} плейлиста: {1}'.format(len(playlists), ', '.join(playlists))

# main part -------------

def start_app():
    print(app_notification)

    tags_info = 'У нас есть {0} тегов: {1}.'.format(len(tags.split()), tags)

    user_request = input("Введите команду для продолжения: ")

    if user_request == video_request:
        print(get_videos_info())
    elif user_request == tags_request:
        print(tags_info)
    elif user_request == playlists_request:
        print(get_playlists_info())
    elif user_request == app_info_request:
        print(about_info)
    else:
        print(not_found_info)


start_app()