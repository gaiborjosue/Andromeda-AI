import pyshorteners

link = input("Enter the link here:  ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)