import instaloader
import tkinter as tk
from tkinter import ttk,messagebox


def get_user_info(username):

    bot=instaloader.Instaloader()
    profile=instaloader.Profile.from_username(bot.context,username)

    userİnfo={
        "Username":profile.username,
        "Followers":profile.followers,
        "Followees":profile.followees,
        "Post Count":profile.mediacount,
        "Last Post Date":getLastPostDate(profile)
    }
    return userİnfo

def getLastPostDate(profile):
    lastPost=None

    for post in profile.get_posts():
        if not lastPost or post.date_utc > lastPost.date_utc:
            lastPost=post
    return lastPost.date_utc.strftime("%Y-%m-%d %H:%M:%S")
    

def showUser():
    username=entry_username.get()
    user_info= get_user_info(username)
    if isinstance(user_info,dict):
        for widget in tree.get_children():
            tree.delete(widget)
        tree.insert("","end",values=(
            user_info["Username"],
            user_info["Followers"],
            user_info["Followees"],
            user_info["Post Count"],
            user_info["Last Post Date"]
        ))
    else:
        messagebox.showerror("HATA",user_info)


root=tk.Tk()
root.title("Instagram Kullanıcı Bilgi Görüntüleyici")

frame=tk.Frame(root)
frame.pack(padx=20,pady=20)

label = tk.Label(root, text="Kullanıcı Adı:")
label.pack(padx=5, pady=5)

entry_username = tk.Entry(root)
entry_username.pack(padx=5, pady=5)

search_button = tk.Button(root, text="Bilgileri Görüntüle", command=showUser)
search_button.pack(padx=5, pady=5)


tree=ttk.Treeview(root,columns=("Username","Followers","Followees","Post Count","Last Post Date"))
tree.heading("Username",text="Kullanıcı Adı:")
tree.heading("Followers",text="Takipçiler")
tree.heading("Followees",text="Takip Edilenler")
tree.heading("Post Count",text="Gönderi Sayısı")
tree.heading("Last Post Date",text="Son Gönderi Tarihi")
tree.pack(padx=20,pady=20)


root.mainloop()