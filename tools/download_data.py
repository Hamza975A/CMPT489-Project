from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="./")
mySoccerNetDownloader.downloadDataTask(task="tracking-2023", split=["train","test","challenge"])