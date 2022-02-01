from pytube import YouTube
print("welcome dears to my app to download any videos you want by python taha")
URL=input("Enter your url video:")
video=YouTube(URL)
streams=set()
print("loading please wait a moments!")
for stream in video.streams.filter(type="video"):
        streams.add(stream.resolution) 
print("your videos is avilable now follow your qualities")
while(True):
    try:
        Res=input("Please Dears enter your qualities")
        stream=video.stream.filter(file_extension="mp3").get_by_Resolution(Res)
        print("videos is downloading please wait a moments")
        stream.download()
        print("download success")
        break
    except:
        print("you cant download video in this quality please choose other quality please")