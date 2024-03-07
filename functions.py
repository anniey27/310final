from lyricsgenius import Genius
import keys


def find_songs(lyric):
    genius = Genius(keys.MY_API_KEY)
    results = genius.search_lyrics(lyric)
    if results:
        songs_info = []
        base_url = "https://genius.com"
        for key in results['sections']:
            for hit in key['hits']:
                title = hit['result']['title']
                artist = hit['result']['artist_names']
                snippet = hit['highlights'][0]['value']
                thumbnail = hit['result']['header_image_thumbnail_url']
                url = base_url + str(hit['result']['path'])
                songs_info.append({'title': title, 'artist': artist, 'snippet': snippet, 'thumbnail': thumbnail,
                                   'url': url})
        return songs_info

    else:
        return None


def main():
    print("-- Trying to find song --")
    print(find_songs("castle"))


if __name__ == "__main__":
    try:
        main()
    except (NameError, SyntaxError):
        # pass does "nothing" - it is useful if you are trying to nothing in your code,
        # but still need a line to avoid a syntax error
        pass
