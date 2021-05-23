from os import stat
from tkinter import Checkbutton
from tkinter.constants import BOTTOM, NONE


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

if __name__=="__main__":
    try:
        import tkinter as tk
        from tkinter import filedialog
        from cryptography.fernet import Fernet
    except ModuleNotFoundError:
        import os
        print("Module Not Found ")
        print("Installing Module")
        os.system("pip install cryptography")
        print("Complete Installation")
        print("Re-run the code")
    # generate_key()
    fonts=["System","Terminal","Fixedsys","Modern","Roman","Script","Courier","MS Serif","MS Sans Serif","Small Fonts","Bell Gothic Std Black","Bell Gothic Std Light","Eccentric Std","Stencil Std","Tekton Pro","Tekton Pro Cond","Tekton Pro Ext","Trajan Pro","Rosewood Std Regular","Prestige Elite Std","Poplar Std","Orator Std","OCR A Std","Nueva Std Cond","Minion Pro SmBd","Minion Pro Med","Minion Pro Cond","Mesquite Std","Lithos Pro Regular","Kozuka Mincho Pro R","@Kozuka Mincho Pro R","Kozuka Mincho Pro M","@Kozuka Mincho Pro M","Kozuka Mincho Pro L","@Kozuka Mincho Pro L","Kozuka Mincho Pro H","@Kozuka Mincho Pro H","Kozuka Mincho Pro EL","@Kozuka Mincho Pro EL","Kozuka Mincho Pro B","@Kozuka Mincho Pro B","Kozuka Gothic Pro R","@Kozuka Gothic Pro R","Kozuka Gothic Pro M","@Kozuka Gothic Pro M","Kozuka Gothic Pro L","@Kozuka Gothic Pro L","Kozuka Gothic Pro H","@Kozuka Gothic Pro H","Kozuka Gothic Pro EL","@Kozuka Gothic Pro EL","Kozuka Gothic Pro B","@Kozuka Gothic Pro B","Hobo Std","Giddyup Std","Cooper Std Black","Charlemagne Std","Chaparral Pro","Brush Script Std","Blackoak Std","Birch Std","Adobe Garamond Pro","Adobe Garamond Pro Bold","Adobe Kaiti Std R","@Adobe Kaiti Std R","Adobe Heiti Std R","@Adobe Heiti Std R","Adobe Fangsong Std R","@Adobe Fangsong Std R","Adobe Caslon Pro","Adobe Caslon Pro Bold","Adobe Arabic","Adobe Devanagari","Adobe Hebrew","Adobe Ming Std L","@Adobe Ming Std L","Adobe Myungjo Std M","@Adobe Myungjo Std M","Adobe Song Std L","@Adobe Song Std L","Kozuka Gothic Pr6N B","@Kozuka Gothic Pr6N B","Kozuka Gothic Pr6N EL","@Kozuka Gothic Pr6N EL","Kozuka Gothic Pr6N H","@Kozuka Gothic Pr6N H","Kozuka Gothic Pr6N L","@Kozuka Gothic Pr6N L","Kozuka Gothic Pr6N M","@Kozuka Gothic Pr6N M","Kozuka Gothic Pr6N R","@Kozuka Gothic Pr6N R","Kozuka Mincho Pr6N B","@Kozuka Mincho Pr6N B","Kozuka Mincho Pr6N EL","@Kozuka Mincho Pr6N EL","Kozuka Mincho Pr6N H","@Kozuka Mincho Pr6N H","Kozuka Mincho Pr6N L","@Kozuka Mincho Pr6N L","Kozuka Mincho Pr6N M","@Kozuka Mincho Pr6N M","Kozuka Mincho Pr6N R","@Kozuka Mincho Pr6N R","Letter Gothic Std","Minion Pro","Myriad Hebrew","Myriad Pro","Myriad Pro Cond","Myriad Pro Light","Rosewood Std Fill","Marlett","Arial","Arabic Transparent","Arial Baltic","Arial CE","Arial CYR","Arial Greek","Arial TUR","Batang","@Batang","BatangChe","@BatangChe","Gungsuh","@Gungsuh","GungsuhChe","@GungsuhChe","Courier New","Courier New Baltic","Courier New CE","Courier New CYR","Courier New Greek","Courier New TUR","DaunPenh","DokChampa","Estrangelo Edessa","Euphemia","Gautami","Vani","Gulim","@Gulim","GulimChe","@GulimChe","Dotum","@Dotum","DotumChe","@DotumChe","Impact","Iskoola Pota","Kalinga","Kartika","Khmer UI","Lao UI","Latha","Lucida Console","Malgun Gothic","@Malgun Gothic","Mangal","Meiryo","@Meiryo","Meiryo UI","@Meiryo UI","Microsoft Himalaya","Microsoft JhengHei","@Microsoft JhengHei","Microsoft YaHei","@Microsoft YaHei","MingLiU","@MingLiU","PMingLiU","@PMingLiU","MingLiU_HKSCS","@MingLiU_HKSCS","MingLiU-ExtB","@MingLiU-ExtB","PMingLiU-ExtB","@PMingLiU-ExtB","MingLiU_HKSCS-ExtB","@MingLiU_HKSCS-ExtB","Mongolian Baiti","MS Gothic","@MS Gothic","MS PGothic","@MS PGothic","MS UI Gothic","@MS UI Gothic","MS Mincho","@MS Mincho","MS PMincho","@MS PMincho","MV Boli","Microsoft New Tai Lue","Nyala","Microsoft PhagsPa","Plantagenet Cherokee","Raavi","Segoe Script","Segoe UI","Segoe UI Semibold","Segoe UI Light","Segoe UI Symbol","Shruti","SimSun","@SimSun","NSimSun","@NSimSun","SimSun-ExtB","@SimSun-ExtB","Sylfaen","Microsoft Tai Le","Times New Roman","Times New Roman Baltic","Times New Roman CE","Times New Roman CYR","Times New Roman Greek","Times New Roman TUR","Tunga","Vrinda","Shonar Bangla","Microsoft Yi Baiti","Tahoma","Microsoft Sans Serif","Angsana New","Aparajita","Cordia New","Ebrima","Gisha","Kokila","Leelawadee","Microsoft Uighur","MoolBoran","Symbol","Utsaah","Vijaya","Wingdings","Andalus","Arabic Typesetting","Simplified Arabic","Simplified Arabic Fixed","Sakkal Majalla","Traditional Arabic","Aharoni","David","FrankRuehl","Levenim MT","Miriam","Miriam Fixed","Narkisim","Rod","FangSong","@FangSong","SimHei","@SimHei","KaiTi","@KaiTi","AngsanaUPC","Browallia New","BrowalliaUPC","CordiaUPC","DilleniaUPC","EucrosiaUPC","FreesiaUPC","IrisUPC","JasmineUPC","KodchiangUPC","LilyUPC","DFKai-SB","@DFKai-SB","Lucida Sans Unicode","Arial Black","Calibri","Cambria","Cambria Math","Candara","Comic Sans MS","Consolas","Constantia","Corbel","Franklin Gothic Medium","Gabriola","Georgia","Palatino Linotype","Segoe Print","Trebuchet MS","Verdana","Webdings","Haettenschweiler","MS Outlook","Book Antiqua","Century Gothic","Bookshelf Symbol 7","MS Reference Sans Serif","MS Reference Specialty","Bradley Hand ITC","Freestyle Script","French Script MT","Juice ITC","Kristen ITC","Lucida Handwriting","Mistral","Papyrus","Pristina","Tempus Sans ITC","Garamond","Monotype Corsiva","Agency FB","Arial Rounded MT Bold","Blackadder ITC","Bodoni MT","Bodoni MT Black","Bodoni MT Condensed","Bookman Old Style","Calisto MT","Castellar","Century Schoolbook","Copperplate Gothic Bold","Copperplate Gothic Light","Curlz MT","Edwardian Script ITC","Elephant","Engravers MT","Eras Bold ITC","Eras Demi ITC","Eras Light ITC","Eras Medium ITC","Felix Titling","Forte","Franklin Gothic Book","Franklin Gothic Demi","Franklin Gothic Demi Cond","Franklin Gothic Heavy","Franklin Gothic Medium Cond","Gigi","Gill Sans MT","Gill Sans MT Condensed","Gill Sans Ultra Bold","Gill Sans Ultra Bold Condensed","Gill Sans MT Ext Condensed Bold","Gloucester MT Extra Condensed","Goudy Old Style","Goudy Stout","Imprint MT Shadow","Lucida Sans","Lucida Sans Typewriter","Maiandra GD","OCR A Extended","Palace Script MT","Perpetua","Perpetua Titling MT","Rage Italic","Rockwell","Rockwell Condensed","Rockwell Extra Bold","Script MT Bold","Tw Cen MT","Tw Cen MT Condensed","Tw Cen MT Condensed Extra Bold","Algerian","Baskerville Old Face","Bauhaus 93","Bell MT","Berlin Sans FB","Berlin Sans FB Demi","Bernard MT Condensed","Bodoni MT Poster Compressed","Britannic Bold","Broadway","Brush Script MT","Californian FB","Centaur","Chiller","Colonna MT","Cooper Black","Footlight MT Light","Harlow Solid Italic","Harrington","High Tower Text","Jokerman","Kunstler Script","Lucida Bright","Lucida Calligraphy","Lucida Fax","Magneto","Matura MT Script Capitals","Modern No. 20","Niagara Engraved","Niagara Solid","Old English Text MT","Onyx","Parchment","Playbill","Poor Richard","Ravie","Informal Roman","Showcard Gothic","Snap ITC","Stencil","Viner Hand ITC","Vivaldi","Vladimir Script","Wide Latin","Century","Wingdings 2","Wingdings 3","Arial Unicode MS","@Arial Unicode MS","Arial Narrow","Rupee Foradian","Rupee","DevLys 010","Calibri Light","Monoton","Ubuntu Medium","Ubuntu","Ubuntu Light","Yatra One","HelvLight","Lato","Great Vibes"]
    color=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    
    # Pre Define Varibales
    file_extension=".secret"
    file_opened=None
    theme_color1=["black","grey"]
    theme_color2=[
        "#2f3e46",
        "#354f52",
        "#52796f",
        "#84a98c",
        "#cad2c5",
    ] # https://coolors.co/cad2c5-84a98c-52796f-354f52-2f3e46
    theme_color3=[
        "#0a0908",
        "#22333b",
        "#5e503f",
        "#c6ac8f",
        "#eae0d5",
    ] # https://coolors.co/0a0908-22333b-eae0d5-c6ac8f-5e503f

    theme_font=["theme_color[0]"]
    # f1_left_sec_hsize=(250,300)#(min,max)

    # Root Window
    root = tk.Tk()
    root.title("Encryption/Decryption")
    root.geometry("800x580")
    # root.configure(background=theme_color1[0])
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    #Functions
    def exit_button():
        root.destroy()

    # def resize(e):
    #     pass
    #     # print(e,f1_left_sec.winfo_width(),f1_left_sec_hsize[0]*2,e.width,f1_left_sec_hsize[1]*2)
    #     # if(e.width<=f1_left_sec_hsize[0]*2):
    #     #     print("setting w",f1_left_sec_hsize[0])
    #     #     f1_left_sec.config(width=f1_left_sec_hsize[0])
    #     #     # f1_left_sec.pack(expand=False)
    #     # elif(e.width>=f1_left_sec_hsize[1]*2):
    #     #     print("setting w",f1_left_sec_hsize[1])
    #     #     f1_left_sec.config(width=f1_left_sec_hsize[1])
    #     #     # f1_left_sec.pack(expand=False)
    #     # else:
    #     #     print("setting w",f1_left_sec_hsize[0])
    #     #     f1_left_sec.config(width=250)
    #     # #     f1_left_sec.pack(expand=True)

    def encrypt_open_file():
        root_open_close_file_frame.tkraise()
        # filedialog.askopenfilename(
        #     initialdir = "/",
        #     title = "Select a File ",
        #     filetypes = (
        #         ("Text files","*.txt*"),
        #         ("all files","*.*")
        #     ),
        # )

    def decrypt_open_file():
        root_open_close_file_frame.tkraise()
        # filedialog.askopenfilename(
        #     initialdir = "/",
        #     title = "Select an Encrypted File ",
        #     filetypes = (
        #         ("Secret files","*"+file_extension+"*"),
        #         # ("all files","*.*")
        #     ),
        # )

    def open_encrypt_file():
        global file_opened
        filename=filedialog.askopenfilename(
            # initialdir = "/",
            title = "Select an Encrypted File ",
            filetypes = (
                ("Secret files","*"+file_extension+"*"),
                ("all files","*.*")
            ),
        )
        if(filename):
            file_opened=filename
            # print(file_opened)
            root_editor_frame.tkraise()
            f2_head_label.config(text="Text Editor : Selected File :- "+filename.split("/")[-1])
            data=open(file_opened,"rb+")
            # f2_test_area.insert(tk.END, decrypt_message(data.read()))
            f2_test_area.insert(tk.END, data.read())
            data.close()

    def open_editor():
        # f2_open_button.config(state=tk.NORMAL)
        root_editor_frame.tkraise()

    def button_generate_key():
        pass

    def save(data):
        # print(f2_test_area.get(1.0,tk.END))
        data.seek(0)
        data.truncate(0)
        data.write(f2_test_area.get(1.0,tk.END).encode())
        # data.write(encrypt_message(f2_test_area.get(1.0,tk.END)).encode())
        f2_test_area.insert(tk.END, data.read())
        print("File Saved")

    def f3_back_button_pressed():
        root_open_close_file_frame.tkraise()

    def f2_back_button_pressed():
        global file_opened
        f2_test_area.delete(1.0,tk.END) # For clearing 
        f2_head_label.config(text="Text Editor : No File Selected ")
        # if(file_opened):
            # f2_save_button_pressed()
        f2_save_button.config(state=tk.DISABLED)
        file_opened=None
        root_home_frame.tkraise()

    def f2_save_button_pressed():
        print("Saveing button Pressed")
        data=open(file_opened,"rb+")
        data.seek(0)
        data.truncate(0)
        data.write(f2_test_area.get(1.0,tk.END).encode())
        # data.write(encrypt_message(f2_test_area.get(1.0,tk.END)).encode())
        f2_test_area.insert(tk.END, data.read())
        data.close()
        print("File Saved")
        pass

    def f2_open_button_pressed():
        global file_opened
        # if(file_opened):
        #     f2_save_button_pressed()
        filename=filedialog.askopenfilename(
            # initialdir = "/",
            title = "Select an Encrypted File ",
            filetypes = (
                ("all files","*.*"),
                # ("Secret files","*"+file_extension+"*"),
            ),
        )
        if(filename):
            f2_test_area.delete(1.0,tk.END)
            file_opened=filename
            # root_editor_frame.tkraise()
            f2_head_label.config(text="Text Editor : Selected File :- "+filename.split("/")[-1])
            f2_save_button.config(state=tk.NORMAL)
            
            data=open(filename,"rb+")
            # f2_test_area.insert(tk.END, decrypt_message(data.read()))
            f2_test_area.insert(tk.END, data.read())
            data.close()

    def color_theme(theme_color):   
        # Background 
        
        # Root
        root.configure(background=theme_color[0])

        # Root Home F1 
        root_home_frame.config(background=theme_color[0])
        f1_left_sec_brand.config(background=theme_color[0])
        f1_left_sec_brand_name.config(background=theme_color[0])
        f1_left_sec_menu.config(background=theme_color[1])
        for i in [f1_left_sec_menu_1,f1_left_sec_menu_2,f1_left_sec_menu_3,f1_left_sec_menu_4,f1_left_sec_menu_0,f1_left_sec_menu_5]:
            i.config(background=theme_color[1],activebackground=theme_color[1])
        
        f1_right_sec.config(background=theme_color[-1])
        root_editor_frame.config(background=theme_color[0])
        
        # Root Editor F2
        f2_back_button.config(background=theme_color[0],activebackground=theme_color[0])
        f2_back_button.bind("<Enter>",func=lambda e: f2_back_button.config(bg=theme_color[-2],fg=theme_color[0]))
        f2_back_button.bind("<Leave>",func=lambda e: f2_back_button.config(bg=theme_color[0],fg=theme_color[-1]))

        f2_open_button.config(background=theme_color[0],activebackground=theme_color[0])
        f2_open_button.bind("<Enter>",func=lambda e: f2_open_button.config(bg=theme_color[-2],fg=theme_color[0]))
        f2_open_button.bind("<Leave>",func=lambda e: f2_open_button.config(bg=theme_color[0],fg=theme_color[-1]))

        f2_save_button.config(background=theme_color[0],activebackground=theme_color[0])
        f2_save_button.bind("<Enter>",func=lambda e: f2_save_button.config(bg=theme_color[-2],fg=theme_color[0]))
        f2_save_button.bind("<Leave>",func=lambda e: f2_save_button.config(bg=theme_color[0],fg=theme_color[-1]))

        f2_head_label.config(background=theme_color[0])

        f2_test_area.config(background=theme_color[-1],selectbackground=theme_color[-2])
        f2_text_box_frame.config(bg="Black")
        # f2_text_area_scrollbar.config(bg="#ce4257")

        #Root Open Close Frame F3
        root_open_close_file_frame.config(background=theme_color[-1])
        f3_back_button.config(background=theme_color[0],activebackground=theme_color[0])
        f3_back_button.bind("<Enter>",func=lambda e: f3_back_button.config(bg=theme_color[-2],fg=theme_color[0]))
        f3_back_button.bind("<Leave>",func=lambda e: f3_back_button.config(bg=theme_color[0],fg=theme_color[-1]))
        
        f3_head_label.config(background=theme_color[0])

        # Text Color

        # Root Home F1
        f1_left_sec_brand_name.config(fg=theme_color[-1])
        for i in [f1_left_sec_menu_1,f1_left_sec_menu_2,f1_left_sec_menu_3,f1_left_sec_menu_4,f1_left_sec_menu_0,f1_left_sec_menu_5]:
            i.config(fg=theme_color[-1])
            
        f1_left_sec_menu_0.bind("<Enter>",func=lambda e: f1_left_sec_menu_0.config(fg=theme_color[2]))
        f1_left_sec_menu_1.bind("<Enter>",func=lambda e: f1_left_sec_menu_1.config(fg=theme_color[2]))
        f1_left_sec_menu_2.bind("<Enter>",func=lambda e: f1_left_sec_menu_2.config(fg=theme_color[2]))
        f1_left_sec_menu_3.bind("<Enter>",func=lambda e: f1_left_sec_menu_3.config(fg=theme_color[2]))
        f1_left_sec_menu_4.bind("<Enter>",func=lambda e: f1_left_sec_menu_4.config(fg=theme_color[2]))
        f1_left_sec_menu_5.bind("<Enter>",func=lambda e: f1_left_sec_menu_5.config(fg=theme_color[2]))

        f1_left_sec_menu_0.bind("<Leave>",func=lambda e: f1_left_sec_menu_0.config(fg=theme_color[-1]))
        f1_left_sec_menu_1.bind("<Leave>",func=lambda e: f1_left_sec_menu_1.config(fg=theme_color[-1]))
        f1_left_sec_menu_2.bind("<Leave>",func=lambda e: f1_left_sec_menu_2.config(fg=theme_color[-1]))
        f1_left_sec_menu_3.bind("<Leave>",func=lambda e: f1_left_sec_menu_3.config(fg=theme_color[-1]))
        f1_left_sec_menu_4.bind("<Leave>",func=lambda e: f1_left_sec_menu_4.config(fg=theme_color[-1]))
        f1_left_sec_menu_5.bind("<Leave>",func=lambda e: f1_left_sec_menu_5.config(fg=theme_color[-1]))
        
        # Root Editor F2
        f2_back_button.config(fg=theme_color[-1])
        f2_open_button.config(fg=theme_color[-1])
        f2_save_button.config(fg=theme_color[-1])
        f2_head_label.config(fg=theme_color[-1])
        f2_test_area.config(fg=theme_color[0])

        #Root Open Close Frame F3
        f3_back_button.config(fg=theme_color[-1])
        f3_head_label.config(fg=theme_color[-1])
    
    #Root Frame 1
    root_home_frame=tk.Frame(root)
    root_home_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
    # root_home_frame.bind("<Configure>",resize)

    # Root Frame 1 Left Navigation
    f1_left_sec=tk.Frame(root_home_frame)
    f1_left_sec.pack(side=tk.LEFT,fill=tk.BOTH)

    # Root Frame 1 left Nav Brand
    f1_left_sec_brand=tk.Frame(f1_left_sec)
    f1_left_sec_brand.pack(side=tk.TOP,fill=tk.BOTH)

    f1_left_sec_brand_name=tk.Label(f1_left_sec_brand,text="Encryptor/Decryptor",font=(fonts[0],12))
    f1_left_sec_brand_name.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH,pady=10)

    # Root Frame 1 Left Nav Menu
    f1_left_sec_menu=tk.Frame(f1_left_sec,height=10)
    f1_left_sec_menu.pack(side=tk.BOTTOM,expand=True,fill=tk.BOTH)

    # Root Frame 1 Left Nav Menu List
    f1_left_sec_menu_1=tk.Button(f1_left_sec_menu,text="Encryptor a File",command=encrypt_open_file)
    f1_left_sec_menu_2=tk.Button(f1_left_sec_menu,text="Decryptor a File",command=decrypt_open_file)
    f1_left_sec_menu_3=tk.Button(f1_left_sec_menu,text="Open Encrypted File",command=open_encrypt_file)
    f1_left_sec_menu_4=tk.Button(f1_left_sec_menu,text="Generate a Key",command=button_generate_key)
    f1_left_sec_menu_5=tk.Button(f1_left_sec_menu,text="Open Editor",command=open_editor)
    f1_left_sec_menu_0=tk.Button(f1_left_sec_menu,text="Exit",command=exit_button)
    f1_left_sec_menu_0.pack(side=tk.BOTTOM,fill=tk.X,padx=5,pady=15)

    for i in [f1_left_sec_menu_1,f1_left_sec_menu_2,f1_left_sec_menu_3,f1_left_sec_menu_4,f1_left_sec_menu_5]:
        i.pack(fill=tk.X,padx=5,pady=15)

    for i in [f1_left_sec_menu_1,f1_left_sec_menu_2,f1_left_sec_menu_3,f1_left_sec_menu_4,f1_left_sec_menu_0,f1_left_sec_menu_5]:
        i.config(bd=0,font=(fonts[0],12))

    # Root Frame 1 Right Section
    f1_right_sec=tk.Frame(root_home_frame)
    f1_right_sec.pack(side=tk.RIGHT,expand=1,fill=tk.BOTH)

    f1_right_sec_head=tk.Label(f1_right_sec,text="Recent Files")
    f1_right_sec_head.pack(fill=tk.X,expand=True,side=tk.TOP)

    login_btn = tk.PhotoImage(file = "./icon/icon (1).png")
    login_btn2 = tk.PhotoImage(file = "./icon/icon (2).png")
    f1_button=tk.Button(f1_right_sec,image=login_btn,borderwidth=0,command=lambda : f1_button.config(image=login_btn2))
    f1_button.pack()
    # f1_button.bind("<>",func=lambda : f1_button.config(image=login_btn2))

    #Root Frame 2
    root_editor_frame=tk.Frame(root)
    root_editor_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)

    # Root Frame 2 Head Bar
    f2_head=tk.Frame(root_editor_frame)
    f2_head.pack(side=tk.TOP,fill=tk.X)

    f2_back_button=tk.Button(f2_head,text="Back",command=f2_back_button_pressed)
    f2_back_button.config(bd=0,font=(fonts[0],10))
    f2_back_button.pack(side=tk.LEFT,fill=tk.BOTH,ipadx=3,ipady=3)

    f2_open_button=tk.Button(f2_head,text="Open",command=f2_open_button_pressed)
    f2_open_button.config(bd=0,font=(fonts[0],10))
    f2_open_button.pack(side=tk.RIGHT,fill=tk.BOTH,ipadx=3,ipady=3)
    # f2_open_button.config(state=tk.DISABLED)

    f2_save_button=tk.Button(f2_head,text="Save",command=f2_save_button_pressed)
    f2_save_button.config(bd=0,font=(fonts[0],10))
    f2_save_button.pack(side=tk.RIGHT,fill=tk.BOTH,ipadx=3,ipady=3)
    f2_save_button.config(state=tk.DISABLED)

    f2_head_label=tk.Label(f2_head,text="Text Editor : No File Selected")
    f2_head_label.config(font=(fonts[0],10))
    f2_head_label.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)
    
    # Root Frame 2 Rest Page
    f2_text_box_frame=tk.Frame(root_editor_frame)
    f2_text_box_frame.pack(fill=tk.BOTH,expand=True,)#padx=5,pady=5)

    f2_test_area = tk.Text(f2_text_box_frame,bd=0,height=1,width=1,font=("Corbel", 12),undo=True)
    f2_test_area.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    f2_text_area_scrollbar=tk.Scrollbar(f2_text_box_frame,command=f2_test_area.yview)
    f2_test_area.config(yscrollcommand=f2_text_area_scrollbar.set)
    f2_text_area_scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

    #Root Frame 3
    root_open_close_file_frame=tk.Frame(root)
    root_open_close_file_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
    
    # Root Frame 3 Head Bar
    f3_head=tk.Frame(root_open_close_file_frame)
    f3_head.pack(side=tk.TOP,fill=tk.X)

    f3_back_button=tk.Button(f3_head,text="Back",command=f3_back_button_pressed)
    f3_back_button.config(bd=0,font=(fonts[0],10))
    f3_back_button.pack(side=tk.LEFT,fill=tk.BOTH,ipadx=3,ipady=3)

    f3_head_label=tk.Label(f3_head,text="Encreption of Files")
    f3_head_label.config(font=(fonts[0],10))
    f3_head_label.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

    # Root Frame 3 Rest Page  
    f3_add_frame=tk.Frame(root_open_close_file_frame)
    f3_add_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True,padx=20,pady=20)

    f3_name_listbox_label=tk.Label(f3_add_frame,text="Name"+"size".rjust(20," "),anchor=tk.W)
    f3_name_listbox_label.pack(side=tk.TOP,fill=tk.X)

    f3_name_listbox_frame=tk.Frame(f3_add_frame)
    f3_name_listbox_frame.pack(expand=True,fill=tk.BOTH)

    f3_name_listbox=tk.Listbox(f3_name_listbox_frame,selectmode=tk.MULTIPLE,relief=tk.FLAT,highlightthickness=0,bd=5,activestyle=tk.NONE)
    f3_name_listbox.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)
    
    f3_scroll=tk.Scrollbar(f3_name_listbox_frame,command=f3_name_listbox.yview)
    f3_name_listbox.config(yscrollcommand=f3_scroll.set)
    f3_scroll.pack(side=tk.RIGHT,fill=tk.Y)

    for i in range(100):
        # f3_check=Checkbutton(f3_name_listbox,text="Hello"+(str(i)+"kb").rjust(20," "))
        # f3_check.pack(fill=tk.X,expand=True)
        f3_name_listbox.insert(tk.END,"Hello"+str(i),)

    # Root F3 Destination buttons
    f3_execution_frame=tk.Frame(root_open_close_file_frame)
    f3_execution_frame.pack(fill=tk.X,side=tk.BOTTOM,padx=20,pady=20)

    f3_file_location_label=tk.Label(f3_execution_frame,text="Destination Location :",anchor=tk.W)
    f3_file_location_label.pack(side=tk.LEFT,fill=tk.BOTH)
    f3_file_location_label=tk.Entry(f3_execution_frame,selectborderwidth=0)
    f3_file_location_label.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=5,padx=5)
    f3_file_location_label.insert(0,"Enter the Location of file to be saved")
    f3_execute_button=tk.Button(f3_execution_frame,text="Encrypt")
    f3_execute_button.pack(side=tk.RIGHT,ipadx=5)
    f3_add_button=tk.Button(f3_execution_frame,text="Select Folder")
    f3_add_button.pack(side=tk.RIGHT,ipadx=5)

    
    # Root F3 Add buttons
    f3_add_bottom_frame=tk.Frame(root_open_close_file_frame)
    f3_add_bottom_frame.pack(fill=tk.X,side=tk.BOTTOM,padx=20)

    f3_remove_button=tk.Button(f3_add_bottom_frame,text="Remove Selected")
    f3_remove_button.pack(side=tk.RIGHT,ipadx=10)
    f3_add_button=tk.Button(f3_add_bottom_frame,text="Add Files")
    f3_add_button.pack(side=tk.RIGHT,ipadx=10)


    # Which Page to Be Seen First  
    # root_open_close_file_frame.tkraise()
    # root_editor_frame.tkraise()
    root_home_frame.tkraise()
    color_theme(theme_color2)
    root.mainloop()