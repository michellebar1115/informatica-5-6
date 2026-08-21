import qrcode

def main():
    qr = qrcode.QRCode(version=1,box_size=5,border=5)
    song = "https://www.youtube.com/watch?v=khnokW3Mw24&list=RDkhnokW3Mw24&start_radio=1"
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="pink", back_color="white")
    img.save("youtube-qr.png")
if __name__=="__main__":
    main()
