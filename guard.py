def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    # filename="encrypt.bin"
    filename="test.txt"
    data=open(filename,"rb+")

    # data1=open("encrypt.bin","wb")
    # data1.write(encrypt_message(data.read()))
    # data1.close()
    
    # data2=open("encrypt.bin","rb")
    # print(decrypt_message(data2.read()) )
    # data2.close()

    lightblue="lightblue"
    root = tk.Tk()
    root.title("Encryption/Decryption")
    root.geometry("680x798")
    root.configure(background=lightblue)

    L = tk.Label(root, text =filename,font =("Courier", 14),background=lightblue)
    L.pack()
    
    box_frame=tk.Frame(root)
    box_frame.pack(fill=tk.BOTH,expand=True,padx=20,pady=5)

    T = tk.Text(box_frame,height=1,width=1,font=("Corbel", 12),undo=True)
    T.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    
    s=tk.Scrollbar(box_frame,command=T.yview)
    T.config(yscrollcommand=s.set)
    s.pack(side=tk.RIGHT,fill=tk.BOTH)
    
    def save():
        # print(T.get(1.0,tk.END))
        data.seek(0)
        data.truncate(0)
        data.write(T.get(1.0,tk.END).encode())
        # data.write(encrypt_message(T.get(1.0,tk.END)).encode())
        T.insert(tk.END, data.read())
        print("File Saved")

    def clear():
        T.delete(1.0,tk.END)

    def keyrelease(e):
        print(e)

    def keypress(e):
        print(e)
    
    b_frame=tk.Frame(root)
    b_frame.pack()

    b1 = tk.Button(b_frame, text = "Save",command=save)
    b1.grid(row=0,column=0)
    # b1.pack()
    
    b2 = tk.Button(b_frame, text = "Clear",command = clear) 
    b2.grid(row=0,column=1)
    # b2.pack()
    
    root.bind("<KeyRelease>",keyrelease)
    root.bind("<KeyPress>",keypress)
    # T.insert(tk.END, decrypt_message(data.read()))
    T.insert(tk.END, data.read())
    
    tk.mainloop()
    data.close()


def main2():
    lightblue="lightblue"

    # Root Window
    root = tk.Tk()
    root.title("Encryption/Decryption")
    root.geometry("800x580")
    root.configure(background=lightblue)

    # Pre Define Varibales
    left_sec_hsize=(250,300)#(min,max)
    
    #Functions
    def resize(e):
        print(e,left_sec.winfo_width())
        # if(e.width<=left_sec_hsize[0]*2):
        #     left_sec.config(width=left_sec_hsize[0])
        #     # left_sec.pack()
        # elif(e.width>=left_sec_hsize[1]*2):
        #     left_sec.config(width=left_sec_hsize[1])
        #     # left_sec.pack()
        # else:
        #     left_sec.config(width=left_sec_hsize[0])
        #     # left_sec.pack(expand=True)
    
    
    #Root Frame
    root_frame=tk.Frame(root,background=lightblue)
    root_frame.pack(expand=True,fill=tk.BOTH)
    root_frame.bind("<Configure>",resize)

    #Left Navigation
    left_sec=tk.Frame(root_frame,width=250,background=lightblue)
    left_sec.pack(side=tk.LEFT,fill=tk.BOTH)
    
    #left Nav Brand
    left_sec_brand=tk.Frame(left_sec,background='saddle brown')
    left_sec_brand.pack(side=tk.TOP,fill=tk.BOTH)
    
    left_sec_brand_name=tk.Label(left_sec_brand,text="Encryptor/Decryptor",background='saddle brown',fg="white",font=(fonts[0],12))
    left_sec_brand_name.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH,pady=10)

    #Left Nav Menu
    left_sec_menu=tk.Frame(left_sec,background=color[7],height=10)
    left_sec_menu.pack(side=tk.BOTTOM,expand=True,fill=tk.BOTH)

    left_sec_menu_1=tk.Button(left_sec_menu,text="Encryptor a File",
    background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    left_sec_menu_1.pack(fill=tk.X,padx=10,pady=15)

    left_sec_menu_2=tk.Button(left_sec_menu,text="Decryptor a File",
    background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    left_sec_menu_2.pack(fill=tk.X,padx=10,pady=15)

    left_sec_menu_3=tk.Button(left_sec_menu,text="Open Encrypted File",
    background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    left_sec_menu_3.pack(fill=tk.X,padx=10,pady=15)

    left_sec_menu_4=tk.Button(left_sec_menu,text="Generate a Key",
    background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    left_sec_menu_4.pack(fill=tk.X,padx=10,pady=15)
    
    left_sec_menu_5=tk.Button(left_sec_menu,text="Exit",
    background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    left_sec_menu_5.pack(side=tk.BOTTOM,fill=tk.X,padx=10,pady=15)

    left_sec_menu_1.bind("<Enter>",func=lambda e: left_sec_menu_1.config(fg="blue"))
    left_sec_menu_2.bind("<Enter>",func=lambda e: left_sec_menu_2.config(fg="blue"))
    left_sec_menu_3.bind("<Enter>",func=lambda e: left_sec_menu_3.config(fg="blue"))
    left_sec_menu_4.bind("<Enter>",func=lambda e: left_sec_menu_4.config(fg="blue"))
    left_sec_menu_5.bind("<Enter>",func=lambda e: left_sec_menu_5.config(fg="blue"))
    left_sec_menu_1.bind("<Leave>",func=lambda e: left_sec_menu_1.config(fg="black"))
    left_sec_menu_2.bind("<Leave>",func=lambda e: left_sec_menu_2.config(fg="black"))
    left_sec_menu_3.bind("<Leave>",func=lambda e: left_sec_menu_3.config(fg="black"))
    left_sec_menu_4.bind("<Leave>",func=lambda e: left_sec_menu_4.config(fg="black"))
    left_sec_menu_5.bind("<Leave>",func=lambda e: left_sec_menu_5.config(fg="black"))

    #Right Section
    right_sec=tk.Frame(root_frame)
    right_sec.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

    right_sec_head=tk.Label(right_sec,text="Recent Files")
    right_sec_head.pack(fill=tk.X,expand=True,side=tk.TOP)
    
    #Grid 
    # recent_1=tk.Button(right_sec,text="Recent File",
    # background=color[7], bd=0,activebackground=color[7],font=(fonts[0],12),fg="black",bg=color[7],)
    # recent_1.pack(padx=10,ipady=40,ipadx=40)
            
    tk.mainloop()

if __name__=="__main__":
    try:
        import tkinter as tk
        from cryptography.fernet import Fernet
    except ModuleNotFoundError:
        import os
        print("Module Not Found ")
        print("Installing Module")
        os.system("pip install cryptography")
        print("Complete Installation")
        print("Re-run the code")
    # generate_key()
    # main()
    fonts=["System","Terminal","Fixedsys","Modern","Roman","Script","Courier","MS Serif","MS Sans Serif","Small Fonts","Bell Gothic Std Black","Bell Gothic Std Light","Eccentric Std","Stencil Std","Tekton Pro","Tekton Pro Cond","Tekton Pro Ext","Trajan Pro","Rosewood Std Regular","Prestige Elite Std","Poplar Std","Orator Std","OCR A Std","Nueva Std Cond","Minion Pro SmBd","Minion Pro Med","Minion Pro Cond","Mesquite Std","Lithos Pro Regular","Kozuka Mincho Pro R","@Kozuka Mincho Pro R","Kozuka Mincho Pro M","@Kozuka Mincho Pro M","Kozuka Mincho Pro L","@Kozuka Mincho Pro L","Kozuka Mincho Pro H","@Kozuka Mincho Pro H","Kozuka Mincho Pro EL","@Kozuka Mincho Pro EL","Kozuka Mincho Pro B","@Kozuka Mincho Pro B","Kozuka Gothic Pro R","@Kozuka Gothic Pro R","Kozuka Gothic Pro M","@Kozuka Gothic Pro M","Kozuka Gothic Pro L","@Kozuka Gothic Pro L","Kozuka Gothic Pro H","@Kozuka Gothic Pro H","Kozuka Gothic Pro EL","@Kozuka Gothic Pro EL","Kozuka Gothic Pro B","@Kozuka Gothic Pro B","Hobo Std","Giddyup Std","Cooper Std Black","Charlemagne Std","Chaparral Pro","Brush Script Std","Blackoak Std","Birch Std","Adobe Garamond Pro","Adobe Garamond Pro Bold","Adobe Kaiti Std R","@Adobe Kaiti Std R","Adobe Heiti Std R","@Adobe Heiti Std R","Adobe Fangsong Std R","@Adobe Fangsong Std R","Adobe Caslon Pro","Adobe Caslon Pro Bold","Adobe Arabic","Adobe Devanagari","Adobe Hebrew","Adobe Ming Std L","@Adobe Ming Std L","Adobe Myungjo Std M","@Adobe Myungjo Std M","Adobe Song Std L","@Adobe Song Std L","Kozuka Gothic Pr6N B","@Kozuka Gothic Pr6N B","Kozuka Gothic Pr6N EL","@Kozuka Gothic Pr6N EL","Kozuka Gothic Pr6N H","@Kozuka Gothic Pr6N H","Kozuka Gothic Pr6N L","@Kozuka Gothic Pr6N L","Kozuka Gothic Pr6N M","@Kozuka Gothic Pr6N M","Kozuka Gothic Pr6N R","@Kozuka Gothic Pr6N R","Kozuka Mincho Pr6N B","@Kozuka Mincho Pr6N B","Kozuka Mincho Pr6N EL","@Kozuka Mincho Pr6N EL","Kozuka Mincho Pr6N H","@Kozuka Mincho Pr6N H","Kozuka Mincho Pr6N L","@Kozuka Mincho Pr6N L","Kozuka Mincho Pr6N M","@Kozuka Mincho Pr6N M","Kozuka Mincho Pr6N R","@Kozuka Mincho Pr6N R","Letter Gothic Std","Minion Pro","Myriad Hebrew","Myriad Pro","Myriad Pro Cond","Myriad Pro Light","Rosewood Std Fill","Marlett","Arial","Arabic Transparent","Arial Baltic","Arial CE","Arial CYR","Arial Greek","Arial TUR","Batang","@Batang","BatangChe","@BatangChe","Gungsuh","@Gungsuh","GungsuhChe","@GungsuhChe","Courier New","Courier New Baltic","Courier New CE","Courier New CYR","Courier New Greek","Courier New TUR","DaunPenh","DokChampa","Estrangelo Edessa","Euphemia","Gautami","Vani","Gulim","@Gulim","GulimChe","@GulimChe","Dotum","@Dotum","DotumChe","@DotumChe","Impact","Iskoola Pota","Kalinga","Kartika","Khmer UI","Lao UI","Latha","Lucida Console","Malgun Gothic","@Malgun Gothic","Mangal","Meiryo","@Meiryo","Meiryo UI","@Meiryo UI","Microsoft Himalaya","Microsoft JhengHei","@Microsoft JhengHei","Microsoft YaHei","@Microsoft YaHei","MingLiU","@MingLiU","PMingLiU","@PMingLiU","MingLiU_HKSCS","@MingLiU_HKSCS","MingLiU-ExtB","@MingLiU-ExtB","PMingLiU-ExtB","@PMingLiU-ExtB","MingLiU_HKSCS-ExtB","@MingLiU_HKSCS-ExtB","Mongolian Baiti","MS Gothic","@MS Gothic","MS PGothic","@MS PGothic","MS UI Gothic","@MS UI Gothic","MS Mincho","@MS Mincho","MS PMincho","@MS PMincho","MV Boli","Microsoft New Tai Lue","Nyala","Microsoft PhagsPa","Plantagenet Cherokee","Raavi","Segoe Script","Segoe UI","Segoe UI Semibold","Segoe UI Light","Segoe UI Symbol","Shruti","SimSun","@SimSun","NSimSun","@NSimSun","SimSun-ExtB","@SimSun-ExtB","Sylfaen","Microsoft Tai Le","Times New Roman","Times New Roman Baltic","Times New Roman CE","Times New Roman CYR","Times New Roman Greek","Times New Roman TUR","Tunga","Vrinda","Shonar Bangla","Microsoft Yi Baiti","Tahoma","Microsoft Sans Serif","Angsana New","Aparajita","Cordia New","Ebrima","Gisha","Kokila","Leelawadee","Microsoft Uighur","MoolBoran","Symbol","Utsaah","Vijaya","Wingdings","Andalus","Arabic Typesetting","Simplified Arabic","Simplified Arabic Fixed","Sakkal Majalla","Traditional Arabic","Aharoni","David","FrankRuehl","Levenim MT","Miriam","Miriam Fixed","Narkisim","Rod","FangSong","@FangSong","SimHei","@SimHei","KaiTi","@KaiTi","AngsanaUPC","Browallia New","BrowalliaUPC","CordiaUPC","DilleniaUPC","EucrosiaUPC","FreesiaUPC","IrisUPC","JasmineUPC","KodchiangUPC","LilyUPC","DFKai-SB","@DFKai-SB","Lucida Sans Unicode","Arial Black","Calibri","Cambria","Cambria Math","Candara","Comic Sans MS","Consolas","Constantia","Corbel","Franklin Gothic Medium","Gabriola","Georgia","Palatino Linotype","Segoe Print","Trebuchet MS","Verdana","Webdings","Haettenschweiler","MS Outlook","Book Antiqua","Century Gothic","Bookshelf Symbol 7","MS Reference Sans Serif","MS Reference Specialty","Bradley Hand ITC","Freestyle Script","French Script MT","Juice ITC","Kristen ITC","Lucida Handwriting","Mistral","Papyrus","Pristina","Tempus Sans ITC","Garamond","Monotype Corsiva","Agency FB","Arial Rounded MT Bold","Blackadder ITC","Bodoni MT","Bodoni MT Black","Bodoni MT Condensed","Bookman Old Style","Calisto MT","Castellar","Century Schoolbook","Copperplate Gothic Bold","Copperplate Gothic Light","Curlz MT","Edwardian Script ITC","Elephant","Engravers MT","Eras Bold ITC","Eras Demi ITC","Eras Light ITC","Eras Medium ITC","Felix Titling","Forte","Franklin Gothic Book","Franklin Gothic Demi","Franklin Gothic Demi Cond","Franklin Gothic Heavy","Franklin Gothic Medium Cond","Gigi","Gill Sans MT","Gill Sans MT Condensed","Gill Sans Ultra Bold","Gill Sans Ultra Bold Condensed","Gill Sans MT Ext Condensed Bold","Gloucester MT Extra Condensed","Goudy Old Style","Goudy Stout","Imprint MT Shadow","Lucida Sans","Lucida Sans Typewriter","Maiandra GD","OCR A Extended","Palace Script MT","Perpetua","Perpetua Titling MT","Rage Italic","Rockwell","Rockwell Condensed","Rockwell Extra Bold","Script MT Bold","Tw Cen MT","Tw Cen MT Condensed","Tw Cen MT Condensed Extra Bold","Algerian","Baskerville Old Face","Bauhaus 93","Bell MT","Berlin Sans FB","Berlin Sans FB Demi","Bernard MT Condensed","Bodoni MT Poster Compressed","Britannic Bold","Broadway","Brush Script MT","Californian FB","Centaur","Chiller","Colonna MT","Cooper Black","Footlight MT Light","Harlow Solid Italic","Harrington","High Tower Text","Jokerman","Kunstler Script","Lucida Bright","Lucida Calligraphy","Lucida Fax","Magneto","Matura MT Script Capitals","Modern No. 20","Niagara Engraved","Niagara Solid","Old English Text MT","Onyx","Parchment","Playbill","Poor Richard","Ravie","Informal Roman","Showcard Gothic","Snap ITC","Stencil","Viner Hand ITC","Vivaldi","Vladimir Script","Wide Latin","Century","Wingdings 2","Wingdings 3","Arial Unicode MS","@Arial Unicode MS","Arial Narrow","Rupee Foradian","Rupee","DevLys 010","Calibri Light","Monoton","Ubuntu Medium","Ubuntu","Ubuntu Light","Yatra One","HelvLight","Lato","Great Vibes"]
    color=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    main2()