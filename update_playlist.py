import requests

# aici poți integra logica de generare token/post_id
channels = {
    "Antena 1": "https://p11.magicplaces.eu/antena1/index.m3u8",
    "Pro TV": "https://p9.magicplaces.eu/protvhd/video.m3u8",
    "Digi Sport 1": "https://p13.magicplaces.eu/digisport1hd/index.m3u8",
    "Prima Sport 1": "https://p13.magicplaces.eu/primasport1hd/video.m3u8",
}

with open("playlist.m3u8", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, url in channels.items():
        f.write(f"#EXTINF:-1,{name}\n{url}\n")
