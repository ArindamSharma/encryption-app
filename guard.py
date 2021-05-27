# Encryption Decryption Functions
from os import terminal_size
from tkinter import YView, font
from tkinter.constants import LEFT, RIGHT
from tkinter.filedialog import test
from typing import Text


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
        exit()
    # generate_key()

    # Pre Define Varibales
    file_extension=".secret"
    file_opened=None
    themes_10=[
        # https://coolors.co/ 
        # Order Dark to Light
        ["#ffe169","#fad643","#edc531","#dbb42c","#c9a227","#b69121","#a47e1b","#926c15","#805b10","#76520e"][::-1],  #yelloish
        ["#001233","#001845","#002855","#023E7D","#0353A4","#0466C8","#33415C","#5C677D","#7D8597","#979DAC"],  #bluish
        ["#036666","#14746f","#248277","#358f80","#469d89","#56ab91","#67b99a","#78c6a3","#88d4ab","#99e2b4"],  #grennish
        ["#582F0E","#333D29","#414833","#7F4F24","#656D4A","#936639","#A68A64","#A4AC86","#B6AD90","#C2C5AA"],  #browngreen
        ["#edc4b3","#e6b8a2","#deab90","#d69f7e","#cd9777","#c38e70","#b07d62","#9d6b53","#8a5a44","#774936"][::-1],  # skincolor
        ["#012a4a","#013a63","#01497c","#014f86","#2a6f97","#2c7da0","#468faf","#61a5c2","#89c2d9","#a9d6e5"],  #bluish
        ["#03071e","#370617","#6a040f","#9d0208","#d00000","#dc2f02","#e85d04","#f48c06","#faa307","#ffba08"],  #redyellow
        ["#001219","#9B2226","#AE2012","#005F73","#BB3E03","#CA6702","#0A9396","#EE9B00","#94D2BD","#E9D8A6"],  #blueyellowred
        ["#d9ed92","#b5e48c","#99d98c","#76c893","#52b69a","#34a0a4","#168aad","#1a759f","#1e6091","#184e77"][::-1],  #yellowishgreenblue
        ["#583101","#603808","#6f4518","#8b5e34","#a47148","#bc8a5f","#d4a276","#e7bc91","#f3d5b5","#ffedd8"],  #brownish

    ]
    fonts=["System","Terminal","Fixedsys","Modern","Roman","Script","Courier","MS Serif","MS Sans Serif","Small Fonts","Bell Gothic Std Black","Bell Gothic Std Light","Eccentric Std","Stencil Std","Tekton Pro","Tekton Pro Cond","Tekton Pro Ext","Trajan Pro","Rosewood Std Regular","Prestige Elite Std","Poplar Std","Orator Std","OCR A Std","Nueva Std Cond","Minion Pro SmBd","Minion Pro Med","Minion Pro Cond","Mesquite Std","Lithos Pro Regular","Kozuka Mincho Pro R","@Kozuka Mincho Pro R","Kozuka Mincho Pro M","@Kozuka Mincho Pro M","Kozuka Mincho Pro L","@Kozuka Mincho Pro L","Kozuka Mincho Pro H","@Kozuka Mincho Pro H","Kozuka Mincho Pro EL","@Kozuka Mincho Pro EL","Kozuka Mincho Pro B","@Kozuka Mincho Pro B","Kozuka Gothic Pro R","@Kozuka Gothic Pro R","Kozuka Gothic Pro M","@Kozuka Gothic Pro M","Kozuka Gothic Pro L","@Kozuka Gothic Pro L","Kozuka Gothic Pro H","@Kozuka Gothic Pro H","Kozuka Gothic Pro EL","@Kozuka Gothic Pro EL","Kozuka Gothic Pro B","@Kozuka Gothic Pro B","Hobo Std","Giddyup Std","Cooper Std Black","Charlemagne Std","Chaparral Pro","Brush Script Std","Blackoak Std","Birch Std","Adobe Garamond Pro","Adobe Garamond Pro Bold","Adobe Kaiti Std R","@Adobe Kaiti Std R","Adobe Heiti Std R","@Adobe Heiti Std R","Adobe Fangsong Std R","@Adobe Fangsong Std R","Adobe Caslon Pro","Adobe Caslon Pro Bold","Adobe Arabic","Adobe Devanagari","Adobe Hebrew","Adobe Ming Std L","@Adobe Ming Std L","Adobe Myungjo Std M","@Adobe Myungjo Std M","Adobe Song Std L","@Adobe Song Std L","Kozuka Gothic Pr6N B","@Kozuka Gothic Pr6N B","Kozuka Gothic Pr6N EL","@Kozuka Gothic Pr6N EL","Kozuka Gothic Pr6N H","@Kozuka Gothic Pr6N H","Kozuka Gothic Pr6N L","@Kozuka Gothic Pr6N L","Kozuka Gothic Pr6N M","@Kozuka Gothic Pr6N M","Kozuka Gothic Pr6N R","@Kozuka Gothic Pr6N R","Kozuka Mincho Pr6N B","@Kozuka Mincho Pr6N B","Kozuka Mincho Pr6N EL","@Kozuka Mincho Pr6N EL","Kozuka Mincho Pr6N H","@Kozuka Mincho Pr6N H","Kozuka Mincho Pr6N L","@Kozuka Mincho Pr6N L","Kozuka Mincho Pr6N M","@Kozuka Mincho Pr6N M","Kozuka Mincho Pr6N R","@Kozuka Mincho Pr6N R","Letter Gothic Std","Minion Pro","Myriad Hebrew","Myriad Pro","Myriad Pro Cond","Myriad Pro Light","Rosewood Std Fill","Marlett","Arial","Arabic Transparent","Arial Baltic","Arial CE","Arial CYR","Arial Greek","Arial TUR","Batang","@Batang","BatangChe","@BatangChe","Gungsuh","@Gungsuh","GungsuhChe","@GungsuhChe","Courier New","Courier New Baltic","Courier New CE","Courier New CYR","Courier New Greek","Courier New TUR","DaunPenh","DokChampa","Estrangelo Edessa","Euphemia","Gautami","Vani","Gulim","@Gulim","GulimChe","@GulimChe","Dotum","@Dotum","DotumChe","@DotumChe","Impact","Iskoola Pota","Kalinga","Kartika","Khmer UI","Lao UI","Latha","Lucida Console","Malgun Gothic","@Malgun Gothic","Mangal","Meiryo","@Meiryo","Meiryo UI","@Meiryo UI","Microsoft Himalaya","Microsoft JhengHei","@Microsoft JhengHei","Microsoft YaHei","@Microsoft YaHei","MingLiU","@MingLiU","PMingLiU","@PMingLiU","MingLiU_HKSCS","@MingLiU_HKSCS","MingLiU-ExtB","@MingLiU-ExtB","PMingLiU-ExtB","@PMingLiU-ExtB","MingLiU_HKSCS-ExtB","@MingLiU_HKSCS-ExtB","Mongolian Baiti","MS Gothic","@MS Gothic","MS PGothic","@MS PGothic","MS UI Gothic","@MS UI Gothic","MS Mincho","@MS Mincho","MS PMincho","@MS PMincho","MV Boli","Microsoft New Tai Lue","Nyala","Microsoft PhagsPa","Plantagenet Cherokee","Raavi","Segoe Script","Segoe UI","Segoe UI Semibold","Segoe UI Light","Segoe UI Symbol","Shruti","SimSun","@SimSun","NSimSun","@NSimSun","SimSun-ExtB","@SimSun-ExtB","Sylfaen","Microsoft Tai Le","Times New Roman","Times New Roman Baltic","Times New Roman CE","Times New Roman CYR","Times New Roman Greek","Times New Roman TUR","Tunga","Vrinda","Shonar Bangla","Microsoft Yi Baiti","Tahoma","Microsoft Sans Serif","Angsana New","Aparajita","Cordia New","Ebrima","Gisha","Kokila","Leelawadee","Microsoft Uighur","MoolBoran","Symbol","Utsaah","Vijaya","Wingdings","Andalus","Arabic Typesetting","Simplified Arabic","Simplified Arabic Fixed","Sakkal Majalla","Traditional Arabic","Aharoni","David","FrankRuehl","Levenim MT","Miriam","Miriam Fixed","Narkisim","Rod","FangSong","@FangSong","SimHei","@SimHei","KaiTi","@KaiTi","AngsanaUPC","Browallia New","BrowalliaUPC","CordiaUPC","DilleniaUPC","EucrosiaUPC","FreesiaUPC","IrisUPC","JasmineUPC","KodchiangUPC","LilyUPC","DFKai-SB","@DFKai-SB","Lucida Sans Unicode","Arial Black","Calibri","Cambria","Cambria Math","Candara","Comic Sans MS","Consolas","Constantia","Corbel","Franklin Gothic Medium","Gabriola","Georgia","Palatino Linotype","Segoe Print","Trebuchet MS","Verdana","Webdings","Haettenschweiler","MS Outlook","Book Antiqua","Century Gothic","Bookshelf Symbol 7","MS Reference Sans Serif","MS Reference Specialty","Bradley Hand ITC","Freestyle Script","French Script MT","Juice ITC","Kristen ITC","Lucida Handwriting","Mistral","Papyrus","Pristina","Tempus Sans ITC","Garamond","Monotype Corsiva","Agency FB","Arial Rounded MT Bold","Blackadder ITC","Bodoni MT","Bodoni MT Black","Bodoni MT Condensed","Bookman Old Style","Calisto MT","Castellar","Century Schoolbook","Copperplate Gothic Bold","Copperplate Gothic Light","Curlz MT","Edwardian Script ITC","Elephant","Engravers MT","Eras Bold ITC","Eras Demi ITC","Eras Light ITC","Eras Medium ITC","Felix Titling","Forte","Franklin Gothic Book","Franklin Gothic Demi","Franklin Gothic Demi Cond","Franklin Gothic Heavy","Franklin Gothic Medium Cond","Gigi","Gill Sans MT","Gill Sans MT Condensed","Gill Sans Ultra Bold","Gill Sans Ultra Bold Condensed","Gill Sans MT Ext Condensed Bold","Gloucester MT Extra Condensed","Goudy Old Style","Goudy Stout","Imprint MT Shadow","Lucida Sans","Lucida Sans Typewriter","Maiandra GD","OCR A Extended","Palace Script MT","Perpetua","Perpetua Titling MT","Rage Italic","Rockwell","Rockwell Condensed","Rockwell Extra Bold","Script MT Bold","Tw Cen MT","Tw Cen MT Condensed","Tw Cen MT Condensed Extra Bold","Algerian","Baskerville Old Face","Bauhaus 93","Bell MT","Berlin Sans FB","Berlin Sans FB Demi","Bernard MT Condensed","Bodoni MT Poster Compressed","Britannic Bold","Broadway","Brush Script MT","Californian FB","Centaur","Chiller","Colonna MT","Cooper Black","Footlight MT Light","Harlow Solid Italic","Harrington","High Tower Text","Jokerman","Kunstler Script","Lucida Bright","Lucida Calligraphy","Lucida Fax","Magneto","Matura MT Script Capitals","Modern No. 20","Niagara Engraved","Niagara Solid","Old English Text MT","Onyx","Parchment","Playbill","Poor Richard","Ravie","Informal Roman","Showcard Gothic","Snap ITC","Stencil","Viner Hand ITC","Vivaldi","Vladimir Script","Wide Latin","Century","Wingdings 2","Wingdings 3","Arial Unicode MS","@Arial Unicode MS","Arial Narrow","Rupee Foradian","Rupee","DevLys 010","Calibri Light","Monoton","Ubuntu Medium","Ubuntu","Ubuntu Light","Yatra One","HelvLight","Lato","Great Vibes"]
    theme_font=[
        (fonts[0],14),
    ]
    # Current Configuration Variables
    config_new_recent_max=5
    config_old_recent_max=5
    config_feature=3
    config_theme_color=9
    config_file_name=__file__.split("\\")[-1].strip(".py")+".config"
    file_not_found=False
    config_new_recent=[]
    config_old_recent=[]

    # Root Window
    root = tk.Tk()
    root.title("Encryption/Decryption")
    root.geometry("800x580")
    # root.configure(background=theme_color1[0])
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    # Reading Config File 
    try:
        config_file=open(config_file_name,"rb+")
        config_file_data=[i.decode().strip("\n") for i in config_file.readlines()]
        if(len(config_file_data)!=3 or config_file_data[0][:11]!="new_recent:" or config_file_data[1][:11]!="old_recent:" or config_file_data[2][:12]!="color_theme:"):
            raise FileNotFoundError
        # print(config_file_data)
        try:
            if(config_file_data[0][11:-1].strip(",")!=''):
                config_new_recent=[i.strip(" ") for i in config_file_data[0][11:].strip(",").split(",")]
            # print(config_new_recent)
            config_theme_color=int(config_file_data[2][12:])
            if(config_file_data[1][11:-1].strip(",")!=''):
                for i in config_file_data[1][11:].strip(",").split(","):
                    tmp=i.strip(" ").split("|")
                    if(i.strip(" ")=='' or len(tmp)==1):
                        raise FileNotFoundError
                    config_old_recent.append([tmp[0],int(tmp[1])])
            # print(config_old_recent)
        except:
            raise FileNotFoundError
        config_file.close()
    except(FileNotFoundError):
        file_not_found=True
    
    #Functions
    def window_exit():
        # print("Configure File")       
        config_file=open(config_file_name,"wb")
        config_file.write("new_recent:".encode())
        for i in config_new_recent:
            config_file.write((i+",").encode())
        config_file.write(("\n").encode())
        config_file.write("old_recent:".encode())
        for i in config_old_recent:
            config_file.write((i[0]+"|"+str(i[1])+",").encode())
        config_file.write(("\n").encode())
        config_file.write(("color_theme:"+str(config_theme_color)).encode())
        config_file.close()
        print("Have a Nice Day")
        root.destroy()
        
    def add_new_file_to_recent(filename):
        if(filename in config_new_recent):
            config_new_recent.remove(filename)
            config_old_recent.insert(0,(filename,2))
            if(len(config_old_recent)>config_old_recent_max):
                config_old_recent.pop()
        elif(filename in [i[0] for i in config_old_recent]):
            for i in config_old_recent:
                if(i[0]==filename):
                    i[1]+=1
        else:
            config_new_recent.insert(0,filename)
            if(len(config_new_recent)>config_new_recent_max):
                config_new_recent.pop()

    # Root Home F1 BUttons 
    def f1_exit_button():
        window_exit()
        # root.destroy()

    def f1_encrypt_open_file():
        f3_head_label.config(text="Encryption of Files")
        f3_add_button.config(command=lambda :f3_add_button_pressed( (("Text files","*.txt*"),("all files","*.*")) ) )
        f3_execute_button.config(text="Encrypt")
        f3_root_open_close_file_frame.tkraise()

    def f1_decrypt_open_file():
        f3_head_label.config(text="Decreption of Files")
        f3_add_button.config(command=lambda :f3_add_button_pressed( (("Secret files","*"+file_extension+"*"),) ) )
        f3_execute_button.config(text="Decrypt")
        f3_root_open_close_file_frame.tkraise()

    def f1_open_encrypt_file():
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
            f2_root_editor_frame.tkraise()
            f2_head_label.config(text="Text Editor : Selected File :- "+filename.split("/")[-1])
            data=open(file_opened,"rb+")
            # f2_test_area.insert(tk.END, decrypt_message(data.read()))
            f2_test_area.insert(tk.END, data.read())
            data.close()
            add_new_file_to_recent(filename)

    def f1_open_editor():
        f2_root_editor_frame.tkraise()

    def f1_button_generate_key():
        pass
    #Root F2 buttons 
    def f2_back_button_pressed():
        global file_opened
        f2_test_area.delete(1.0,tk.END) # For clearing 
        f2_head_label.config(text="Text Editor : No File Selected ")
        # if(file_opened):
            # f2_save_button_pressed()
        f2_save_button.config(state=tk.DISABLED)
        file_opened=None
        f1_root_home_frame.tkraise()

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
            # f2_root_editor_frame.tkraise()
            f2_head_label.config(text="Text Editor : Selected File :- "+filename.split("/")[-1])
            f2_save_button.config(state=tk.NORMAL)       
            data=open(filename,"rb+")
            # f2_test_area.insert(tk.END, decrypt_message(data.read()))
            f2_test_area.insert(tk.END, data.read())
            data.close()
            add_new_file_to_recent(filename)

    # Root F3 Buttons
    def f3_back_button_pressed():
        f3_name_listbox.delete(0,f3_name_listbox.size())
        f3_remove_button.config(state=tk.DISABLED)
        f3_error_message_label.config(text="")
        f3_file_location_entry.delete(0,tk.END)
        f3_file_location_entry.insert(0,"Enter the Location of file to be saved")
        f1_root_home_frame.tkraise()

    def f3_add_button_pressed(filetype):
        filename=filedialog.askopenfilename(
            initialdir = "./",
            title = "Select a File ",
            filetypes = filetype,
            # filetypes = (
            #     ("Text files","*.txt*"),
            #     ("all files","*.*")
            # ),
        )
        if(filename):    
            f3_name_listbox.insert(tk.END,filename)
            f3_remove_button.config(state=tk.NORMAL)
            add_new_file_to_recent(filename)

    def f3_remove_button_pressed():
        local=f3_name_listbox.curselection()
        for i in local:
            f3_name_listbox.delete(i)
        if(len(local)==0):
            f3_error_message_label.config(text="Please Select Something")
        else:
            f3_error_message_label.config(text="")

    def f3_execute_button_pressed():
        print(f3_name_listbox.get(0,f3_name_listbox.size()))

    def f3_decrypt_button_pressed():
        print(f3_name_listbox.get(0,f3_name_listbox.size()))

    def f3_select_destination_button_pressed():
        filedir=filedialog.askdirectory()
        if(filedir):
            # print(filedir)
            f3_file_location_entry.delete(0,tk.END)
            f3_file_location_entry.insert(0,filedir)
    
    # Root F3 Buttons
    def f4_back_button_pressed():
        color_theme(themes_10[config_theme_color])
        f1_root_home_frame.tkraise()

    # Root F4 Frame
    def f4_try_button_pressed():
        if(try_theme!=None):
            print(try_theme)
            color_theme(themes_10[try_theme])

    def f4_apply_button_pressed():
        global config_theme_color
        if(try_theme!=None):
            print(try_theme)
            color_theme(themes_10[try_theme])
            config_theme_color=try_theme

    def f4_theme_button_pressed(i):
        global try_theme
        try_theme=i
        f4_footerbar_theme_label.config(text="Theme "+str(try_theme+1))
    
    def canvas_config(e):
        f4_canvas.config(scrollregion=f4_canvas.bbox("all"))
        # print(e)
        f4_canvas.itemconfig(tk.ALL,width=e.width)
        # f4_canvas.itemconfig(f4_inner_frame_id,x=(e.width-thumb_width)/2)

    def color_theme(theme_color):   
        # button Styles
        def button_type1(widget):
            widget.config(background=theme_color[0],activebackground=theme_color[0],fg=theme_color[-1])
            widget.bind("<Enter>",func=lambda e: widget.config(bg=theme_color[-5],fg=theme_color[1]))
            widget.bind("<Leave>",func=lambda e: widget.config(bg=theme_color[0],fg=theme_color[-1]))

        def button_type2(widget):
            widget.config(background=theme_color[-4],activebackground=theme_color[-4],fg=theme_color[1])
            widget.bind("<Enter>",func=lambda e: widget.config(bg=theme_color[4],fg=theme_color[-1]))
            widget.bind("<Leave>",func=lambda e: widget.config(bg=theme_color[-4],fg=theme_color[1]))

        def button_type1_home_menu(widget):
            widget.config(background=theme_color[1],activebackground=theme_color[1],fg=theme_color[-1])
            widget.bind("<Enter>",func=lambda e: widget.config(fg=theme_color[4]))
            widget.bind("<Leave>",func=lambda e: widget.config(fg=theme_color[-1]))

        def button_type1_theme(widget,i):
            widget.config(background=theme_color[0],activebackground=theme_color[0],fg=theme_color[-1])
            widget.bind("<Enter>",func=lambda e: widget.config(bg=theme_color[-5],fg=theme_color[1]))
            widget.bind("<Leave>",func=lambda e: widget.config(bg=theme_color[0],fg=theme_color[-1]))
            widget.config(command=lambda:f4_theme_button_pressed(i))
            pass
        
        # Root
        root.configure(background=theme_color[0])

        # Root Home Frame F1 
        f1_root_home_frame.config(background=theme_color[0])
        f1_left_sec_brand.config(background=theme_color[0])
        f1_left_sec_brand_name.config(background=theme_color[0],fg=theme_color[-1])
        f1_right_sec.config(background=theme_color[-1])
        f1_left_sec_menu.config(background=theme_color[1])
        
        button_type1_home_menu(f1_left_sec_menu_button_0)
        button_type1_home_menu(f1_left_sec_menu_button_1)
        button_type1_home_menu(f1_left_sec_menu_button_2)
        button_type1_home_menu(f1_left_sec_menu_button_3)
        button_type1_home_menu(f1_left_sec_menu_button_4)
        button_type1_home_menu(f1_left_sec_menu_button_5)
        
        # Root Editor Frame F2
        f2_root_editor_frame.config(background=theme_color[0])
        button_type1(f2_back_button)
        button_type1(f2_open_button)
        button_type1(f2_save_button)
        f2_head_label.config(background=theme_color[0],fg=theme_color[-1])
        f2_test_area.config(background=theme_color[-1],selectbackground=theme_color[-2],fg=theme_color[0])
        f2_text_box_frame.config(bg="Black")

        #Root Open Close Frame F3
        f3_root_open_close_file_frame.config(background=theme_color[-2])
        button_type1(f3_back_button)
        f3_head_label.config(background=theme_color[0],fg=theme_color[-1])
        f3_name_listbox_label.config(background=theme_color[-3],fg=theme_color[0])
        f3_name_listbox.config(background=theme_color[-1],fg=theme_color[0],selectbackground=theme_color[-4],selectforeground=theme_color[1])
        
        f3_execution_frame.config(bg=theme_color[-3])
        f3_file_location_label.config(bg=theme_color[-3],fg=theme_color[0])
        f3_file_location_entry.config(bg=theme_color[-1],fg=theme_color[0])
        f3_add_botton_frame.config(background=theme_color[-1])
        f3_error_message_label.config(background=theme_color[-1])
        button_type1(f3_execute_button)
        button_type2(f3_destination_button)
        button_type2(f3_add_button)
        button_type2(f3_remove_button)

        #Root Setting Frame F4
        button_type1(f4_back_button)
        f4_head_label.config(background=theme_color[0],fg=theme_color[-1])
        f4_theme_frame.config(background=theme_color[3])
        f4_container.config(background=theme_color[-1])
        f4_theme_label.config(background=theme_color[3],fg=theme_color[-1])
        f4_canvas.config(background=theme_color[-2])
        for i in f4_canvas_details["f4_inner_frame"]:
            i.config(background=theme_color[-2])
            
        button_type1_theme(f4_canvas_details["tmp_button"][0],0)
        button_type1_theme(f4_canvas_details["tmp_button"][1],1)
        button_type1_theme(f4_canvas_details["tmp_button"][2],2)
        button_type1_theme(f4_canvas_details["tmp_button"][3],3)
        button_type1_theme(f4_canvas_details["tmp_button"][4],4)
        button_type1_theme(f4_canvas_details["tmp_button"][5],5)
        button_type1_theme(f4_canvas_details["tmp_button"][6],6)
        button_type1_theme(f4_canvas_details["tmp_button"][7],7)
        button_type1_theme(f4_canvas_details["tmp_button"][8],8)
        button_type1_theme(f4_canvas_details["tmp_button"][9],9)

        f4_footerbar_label.config(background=theme_color[-2],fg=theme_color[1])
        f4_footerbar_theme_label.config(background=theme_color[-2],fg=theme_color[1])
        button_type1(f4_footerbar_apply_button)
        button_type2(f4_footerbar_try_button)

        
    #Root Frame 1
    f1_root_home_frame=tk.Frame(root)
    f1_root_home_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
    # f1_root_home_frame.bind("<Configure>",resize)

    # Root Frame 1 Left Navigation
    f1_left_sec=tk.Frame(f1_root_home_frame)
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
    f1_left_sec_menu_button_0=tk.Button(f1_left_sec_menu,text="Exit",command=f1_exit_button)
    f1_left_sec_menu_button_0.pack(side=tk.BOTTOM,fill=tk.X,padx=5,pady=15)
    
    f1_left_sec_menu_button_1=tk.Button(f1_left_sec_menu,text="Encrypt Files",command=f1_encrypt_open_file)
    f1_left_sec_menu_button_2=tk.Button(f1_left_sec_menu,text="Decrypt Files",command=f1_decrypt_open_file)
    f1_left_sec_menu_button_3=tk.Button(f1_left_sec_menu,text="Open Encrypted File",command=f1_open_encrypt_file)
    f1_left_sec_menu_button_4=tk.Button(f1_left_sec_menu,text="Generate a Key",command=f1_button_generate_key)
    f1_left_sec_menu_button_5=tk.Button(f1_left_sec_menu,text="Open Editor",command=f1_open_editor)

    for i in [f1_left_sec_menu_button_1,f1_left_sec_menu_button_2,f1_left_sec_menu_button_3,f1_left_sec_menu_button_4,f1_left_sec_menu_button_5]:
        i.pack(fill=tk.X,padx=10,pady=20)

    for i in [f1_left_sec_menu_button_1,f1_left_sec_menu_button_2,f1_left_sec_menu_button_3,f1_left_sec_menu_button_4,f1_left_sec_menu_button_5,f1_left_sec_menu_button_0]:
        i.config(bd=0,font=(fonts[0],12))

    # Root Frame 1 Right Section
    f1_right_sec=tk.Frame(f1_root_home_frame)
    f1_right_sec.pack(side=tk.RIGHT,expand=1,fill=tk.BOTH)

    f1_right_sec_head=tk.Label(f1_right_sec,text="Recent Files")
    f1_right_sec_head.pack(fill=tk.X,side=tk.TOP)

    login_btn = tk.PhotoImage(file = "./icon/icon (1).png")
    login_btn2 = tk.PhotoImage(file = "./icon/icon (2).png")
    f1_button=tk.Button(f1_right_sec,image=login_btn,borderwidth=0,command=lambda : f1_button.config(image=login_btn2))
    f1_button.pack()

    #Root Frame 2
    f2_root_editor_frame=tk.Frame(root)
    f2_root_editor_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S)

    # Root Frame 2 Head Bar
    f2_head=tk.Frame(f2_root_editor_frame)
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
    f2_text_box_frame=tk.Frame(f2_root_editor_frame)
    f2_text_box_frame.pack(fill=tk.BOTH,expand=True,padx=5,pady=5)

    f2_test_area = tk.Text(f2_text_box_frame,bd=0,height=1,width=1,font=("Corbel", 12),undo=True)
    f2_test_area.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
    f2_text_area_scrollbar=tk.Scrollbar(f2_text_box_frame,command=f2_test_area.yview)
    f2_test_area.config(yscrollcommand=f2_text_area_scrollbar.set)
    f2_text_area_scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

    #Root Frame 3
    f3_root_open_close_file_frame=tk.Frame(root)
    f3_root_open_close_file_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)
    
    # Root Frame 3 Head Bar
    f3_head=tk.Frame(f3_root_open_close_file_frame)
    f3_head.pack(side=tk.TOP,fill=tk.X)

    f3_back_button=tk.Button(f3_head,text="Back",command=f3_back_button_pressed)
    f3_back_button.config(bd=0,font=(fonts[0],10))
    f3_back_button.pack(side=tk.LEFT,fill=tk.BOTH,ipadx=3,ipady=3)

    f3_head_label=tk.Label(f3_head,text="Encryption of Files")
    f3_head_label.config(font=(fonts[0],10),)
    f3_head_label.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

    # Root Frame 3 Rest Page  
    f3_add_frame=tk.Frame(f3_root_open_close_file_frame)
    f3_add_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True,padx=20,pady=20)

    f3_name_listbox_label=tk.Label(f3_add_frame,text="Names",anchor=tk.W)
    f3_name_listbox_label.config(font=theme_font[0])
    f3_name_listbox_label.pack(side=tk.TOP,fill=tk.X,ipady=2)

    f3_name_listbox_frame=tk.Frame(f3_add_frame)
    f3_name_listbox_frame.pack(expand=True,fill=tk.BOTH)

    f3_name_listbox=tk.Listbox(f3_name_listbox_frame,selectmode=tk.MULTIPLE,relief=tk.FLAT,highlightthickness=0,bd=5,activestyle=tk.NONE)
    f3_name_listbox.config(font=theme_font[0])
    f3_name_listbox.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)

    for i in range(50):
        f3_name_listbox.insert(i,"hello "+str(i))
    
    f3_scroll=tk.Scrollbar(f3_name_listbox_frame,command=f3_name_listbox.yview,orient=tk.VERTICAL)
    f3_name_listbox.config(yscrollcommand=f3_scroll.set)
    f3_scroll.pack(side=tk.RIGHT,fill=tk.Y)

    # Root F3 Destination buttons
    f3_execution_frame=tk.Frame(f3_root_open_close_file_frame)
    f3_execution_frame.pack(fill=tk.X,side=tk.BOTTOM,padx=20,pady=20)

    f3_file_location_label=tk.Label(f3_execution_frame,text="Destination Location :",anchor=tk.W,font=theme_font[0])
    f3_file_location_label.pack(side=tk.LEFT,fill=tk.BOTH)

    f3_file_location_entry=tk.Entry(f3_execution_frame,selectborderwidth=0,bd=5,relief=tk.FLAT,font=theme_font[0])
    f3_file_location_entry.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,pady=2,padx=2)
    f3_file_location_entry.insert(0,"Enter the Location of file to be saved")

    f3_execute_button=tk.Button(f3_execution_frame,text="Encrypt",command=f3_execute_button_pressed)
    f3_execute_button.config(bd=0,font=(fonts[0],10))
    f3_execute_button.pack(side=tk.RIGHT,ipadx=5,fill=tk.BOTH)

    f3_destination_button=tk.Button(f3_execution_frame,text="Select Folder",command=f3_select_destination_button_pressed)
    f3_destination_button.config(bd=0,font=(fonts[0],10))
    f3_destination_button.pack(side=tk.RIGHT,ipadx=5,fill=tk.BOTH)

    # Root F3 Add buttons
    f3_add_botton_frame=tk.Frame(f3_root_open_close_file_frame)
    f3_add_botton_frame.pack(fill=tk.X,side=tk.BOTTOM,padx=20)
    
    f3_error_message_label=tk.Label(f3_add_botton_frame)
    f3_error_message_label.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

    f3_remove_button=tk.Button(f3_add_botton_frame,text="Remove Selected",command=f3_remove_button_pressed)
    f3_remove_button.config(bd=0,font=(fonts[0],10))
    f3_remove_button.pack(side=tk.RIGHT,ipadx=10,fill=tk.BOTH)
    f3_remove_button.config(state=tk.DISABLED)

    f3_add_button=tk.Button(f3_add_botton_frame,text="Add File" )
    f3_add_button.config(bd=0,font=(fonts[0],10))
    f3_add_button.pack(side=tk.RIGHT,ipadx=10,fill=tk.BOTH)

    # Root F4 Settings
    f4_root_setting_frame=tk.Frame(root)
    f4_root_setting_frame.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S,)

    # Root Frame 4 Head Bar
    f4_head=tk.Frame(f4_root_setting_frame)
    f4_head.pack(side=tk.TOP,fill=tk.X)

    f4_back_button=tk.Button(f4_head,text="Back",command=f4_back_button_pressed)
    f4_back_button.config(bd=0,font=(fonts[0],10))
    f4_back_button.pack(side=tk.LEFT,fill=tk.BOTH,ipadx=3,ipady=3)

    f4_head_label=tk.Label(f4_head,text="Theme Selection")
    f4_head_label.config(font=(fonts[0],10),)
    f4_head_label.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

    # Root Frame 4 Rest Page
    f4_theme_frame=tk.Frame(f4_root_setting_frame)
    f4_theme_frame.pack(fill=tk.BOTH,expand=True)

    f4_container=tk.Frame(f4_theme_frame)
    f4_container.pack(side=tk.TOP,expand=True,fill=tk.BOTH,padx=20,pady=20)

    f4_theme_label=tk.Label(f4_container,text="Plese Select a Theme give below and see the change",anchor=tk.W,font=theme_font[0])
    f4_theme_label.pack(side=tk.TOP,fill=tk.X)

    f4_canvas=tk.Canvas(f4_container)
    f4_canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

    f4_canvas_frame_scroll=tk.Scrollbar(f4_container,orient=tk.VERTICAL,command=f4_canvas.yview)
    f4_canvas_frame_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    f4_canvas.config(yscrollcommand=f4_canvas_frame_scroll.set)
    
    f4_canvas_details={
        "theme_id":[],
        "f4_inner_frame":[],
        "f4_inner_frame_id":[],
        "tmp_color_frame":[],
        "tmp_button":[],
        "tmp_color_label":[],
    }
    thumb_height=250
    thumb_width=743
    try_theme=None
    for i in range(1,len(themes_10)+1):
        f4_canvas_details["theme_id"].append(i-1)
        f4_canvas_details["f4_inner_frame"].append(
            tk.Frame(f4_canvas,bd=50)
        )
        # print(10,i*10,f4_canvas.winfo_width())
        f4_canvas_details["f4_inner_frame_id"].append(
            f4_canvas.create_window(0,i*thumb_height,window=f4_canvas_details["f4_inner_frame"][-1],anchor=tk.NW,width=thumb_width,height=thumb_height)
        )
        
        f4_canvas_details["tmp_color_frame"].append(
            tk.Frame(f4_canvas_details["f4_inner_frame"][-1],bd=2)
        )
        f4_canvas_details["tmp_color_frame"][-1].pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        f4_canvas_details["tmp_button"].append(
            tk.Button(f4_canvas_details["tmp_color_frame"][-1],text="Theme "+str(i),bd=0,font=(fonts[0],10))
        )
        f4_canvas_details["tmp_button"][-1].pack(side=tk.BOTTOM,fill=tk.X)

        f4_canvas_details["tmp_color_label"].append([])
        for i in themes_10[i-1]:
            f4_canvas_details["tmp_color_label"][-1].append(tk.Label(f4_canvas_details["tmp_color_frame"][-1],background=i))
            f4_canvas_details["tmp_color_label"][-1][-1].pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    
    f4_canvas.bind("<Configure>",func=canvas_config)
    f4_canvas.bind_all("<MouseWheel>",lambda e: f4_canvas.yview_scroll(int(-1*e.delta/120),tk.UNITS))
    
    f4_footerbar=tk.Frame(f4_theme_frame)
    f4_footerbar.pack(side=tk.BOTTOM,fill=tk.BOTH,padx=20,pady=20)

    f4_footerbar_label=tk.Label(f4_footerbar,text="Selected Theme : ",anchor=tk.W,font=theme_font[0])
    f4_footerbar_label.pack(side=tk.LEFT,fill=tk.BOTH)

    f4_footerbar_theme_label=tk.Label(f4_footerbar,text=str(try_theme),anchor=tk.W,font=theme_font[0])
    f4_footerbar_theme_label.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

    f4_footerbar_apply_button=tk.Button(f4_footerbar,text="Apply",font=theme_font[0],bd=0,command=f4_apply_button_pressed)
    f4_footerbar_apply_button.pack(side=tk.RIGHT,fill=tk.BOTH,ipady=2,ipadx=30)

    f4_footerbar_try_button=tk.Button(f4_footerbar,text="Try",font=theme_font[0],bd=0,command=f4_try_button_pressed)
    f4_footerbar_try_button.pack(side=tk.RIGHT,fill=tk.BOTH,ipady=2,ipadx=30)
    
    # Which Page to Be Seen First  
    f4_root_setting_frame.tkraise()
    # f3_root_open_close_file_frame.tkraise()
    # f2_root_editor_frame.tkraise()
    # f1_root_home_frame.tkraise()
    color_theme(themes_10[config_theme_color])
    
    root.protocol("WM_DELETE_WINDOW", window_exit)
    root.mainloop()