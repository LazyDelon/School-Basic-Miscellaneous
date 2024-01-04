# import qrcode

# URL = "https://github.com/Milk-R?tab=repositories"

# Image = qrcode.make(URL)
# print(type(Image))

# Image.save("Github.png")


from MyQR import myqr

myqr.run(words = "https://github.com/LazyDelon",
         version=1,
         picture = 'New-loading.gif',
         level = "H", 
         colorized = True, 
         save_name = 'Github.gif') 