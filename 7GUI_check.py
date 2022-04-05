# メインフレームで選択→サブフレームの６つで画面遷移で参考文献を出力するプログラム。
import tkinter as tk

class App(tk.Tk):
    # 呪文
    def __init__(self, *args, **kwargs):
        # 呪文
        tk.Tk.__init__(self, *args, **kwargs)

        # ウィンドウタイトルを決定
        self.title("参考文献")

        # ウィンドウの大きさを決定
        self.geometry("800x600")

        # ウィンドウのグリッドを 1x1 にする
        # この処理をコメントアウトすると配置がズレる
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
#-----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.main_titleLabel = tk.Label(self.main_frame, text="アパサイト-APACITE", font=('Helvetica', '15'))
        self.main_titleLabel.pack(anchor='center', expand=True)
        self.sub_titleLabel = tk.Label(self.main_frame, text="参照したい文献の言語と形式を選択してください", font=('Helvetica', '11'))
        self.sub_titleLabel.pack(anchor='center', expand=True)

        #ラジオボタン作成
        self.main_label1_text =tk.StringVar()
        self.main_label1_text.set("言語をどれか１つ選択する")
        self.main_label1 =tk.Label(self.main_frame, textvariable=self.main_label1_text,font ="50")
        self.main_label1.pack()
        
        self.select_var_lang = tk.IntVar(self.main_frame)
        self.select_var_lang.set(1)
        self.radio1 = tk.Radiobutton(self.main_frame, text='日本語', value=1, variable=self.select_var_lang)
        self.radio1.pack(anchor='center')
        self.radio2 = tk.Radiobutton(self.main_frame, text='英語', value=2, variable=self.select_var_lang)
        self.radio2.pack(anchor='center')
        

        self.main_label2_text =tk.StringVar()
        self.main_label2_text.set("\n形式をどれか１つ選択する")
        self.main_label2 =tk.Label(self.main_frame, textvariable=self.main_label2_text,font ="50")
        self.main_label2.pack()

        self.select_var_for = tk.IntVar(self.main_frame)
        self.select_var_for.set(3)
        self.radio3 = tk.Radiobutton(self.main_frame, text='書籍', value=3, variable=self.select_var_for)
        self.radio3.pack(anchor='center')
        self.radio4 = tk.Radiobutton(self.main_frame, text='論文', value=4, variable=self.select_var_for)
        self.radio4.pack(anchor='center')
        self.radio5 = tk.Radiobutton(self.main_frame, text='ウェブサイト', value=5, variable=self.select_var_for)
        self.radio5.pack(anchor='center')
        # フレーム1に移動するボタン
        self.checkButton = tk.Button(self.main_frame, text="スタートする", command=lambda : self.check())
        self.checkButton.pack()
#--------------------------------------------------------------------------
#-----------------------------------frame1---------------------------------フレーム何個も作ればいいんじゃね
        # 移動先フレーム1作成
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel1 = tk.Label(self.frame1, text="日本語＆書籍", font=('Helvetica', '15'))
        self.titleLabel1.pack(anchor='n', expand=True)
        self.titleLabel1 = tk.Label(self.frame1,
                                   text="事例: 櫻井武(2010).「睡眠の科学ーなぜ眠るのかなぜ目覚めるのかー」. 講談社, 全pp.22. \n※編集者が必要ならタイトルの後に○○編",
                                   font=('Helvetica', '10'))
        self.titleLabel1.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame1, text = '著者').pack(anchor='center')#説明と
        self.author1 = tk.Entry(self.frame1, width=30)#エントリーボタン
        self.author1.pack(anchor='center')

        self.label2 = tk.Label(self.frame1, text = '出版年').pack(anchor='center')
        self.year1 = tk.Entry(self.frame1, width=30)
        self.year1.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame1, text = 'タイトル').pack(anchor='center')
        self.title1 = tk.Entry(self.frame1, width=30)
        self.title1.pack(anchor='center')

        self.label4 = tk.Label(self.frame1, text = '出版社・出版機関').pack(anchor='center')
        self.publisher1 = tk.Entry(self.frame1, width=30)
        self.publisher1.pack(anchor='center')

        self.label5 = tk.Label(self.frame1, text = 'ページ数（数字だけ入力)').pack(anchor='center')
        self.page1 = tk.Entry(self.frame1, width=30)
        self.page1.pack(anchor='center')
        #出力
        self.output_button = tk.Button(self.frame1, text="出力する", command=lambda : self.addAll1())
        self.output_button.pack(anchor='center')
        
        #コピーボタン
        self.copy_button =tk.Button(self.frame1, text="内容をコピー", command=lambda : self.copy_text(self.outputtext1))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext1= tk.Text(self.frame1,width=100,height=2)
        self.outputtext1.pack(anchor='center')#side=tk.LEFT

        # フレーム1からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame1, text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()
#-------------------------------frame2-------------------------------------------
        #移動先フレーム2作成
        self.frame2 =tk.Frame()
        self.frame2.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel2 = tk.Label(self.frame2, text="日本語＆論文", font=('Helvetica', '15'))
        self.titleLabel2.pack(anchor='n', expand=True)
        self.titleLabel2 = tk.Label(self.frame2,
                                   text="例: 古重奈央(2019).「小学校家庭科における片づけの学習の検討」『日本教科教育学会誌』42巻, 3号, pp.55-67. \nurl , (参照 2021-6-21).\n機関名立命館国際研究所とかは書かない",
                                   font=('Helvetica', '10'))
        self.titleLabel2.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame2, text = '著者').pack(anchor='center')#説明と
        self.author2 = tk.Entry(self.frame2, width=30)#エントリーボタン
        self.author2.pack(anchor='center')

        self.label2 = tk.Label(self.frame2, text = '出版年').pack(anchor='center')
        self.year2 = tk.Entry(self.frame2, width=30)
        self.year2.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame2, text = 'タイトル').pack(anchor='center')
        self.title2 = tk.Entry(self.frame2, width=30)
        self.title2.pack(anchor='center')

        self.label4 = tk.Label(self.frame2, text = '研究論集・ジャーナル名').pack(anchor='center')
        self.magazine2 = tk.Entry(self.frame2, width=30)
        self.magazine2.pack(anchor='center')

        self.label5 = tk.Label(self.frame2, text = '巻号').pack(anchor='center')
        self.volume2 = tk.Entry(self.frame2, width=30)
        self.volume2.pack(anchor='center')

        self.label6 = tk.Label(self.frame2, text = '号数').pack(anchor='center')
        self.number2 = tk.Entry(self.frame2, width=30)
        self.number2.pack(anchor='center')

        self.label7 = tk.Label(self.frame2, text = 'ページ数（数字だけ入力　-もいれること)').pack(anchor='center')
        self.page2 = tk.Entry(self.frame2, width=30)
        self.page2.pack(anchor='center')

        self.labe8 = tk.Label(self.frame2, text = 'リンク（閲覧日は自動入力されます)').pack(anchor='center')
        self.link2 = tk.Entry(self.frame2, width=30)
        self.link2.pack(anchor='center')
        #出力
        self.output_button = tk.Button(self.frame2, text="出力する", command=lambda : self.addAll2())
        self.output_button.pack(anchor='center')
        #コピーボタン
        self.copy_button =tk.Button(self.frame2, text="内容をコピー", command=lambda : self.copy_text(self.outputtext2))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext2= tk.Text(self.frame2,width=100,height=2)
        self.outputtext2.pack(anchor='center')#side=tk.LEFT

        # フレーム2からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame2, text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()
#-------------------------------frame3-------------------------------------------
        #移動先フレーム3作成
        self.frame3 =tk.Frame()
        self.frame3.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel3 = tk.Label(self.frame3, text="日本語＆ウェブサイト", font=('Helvetica', '15'))
        self.titleLabel3.pack(anchor='n', expand=True)
        self.titleLabel3 = tk.Label(self.frame3,
                                   text="REUTERS(2022-3-20).「情報ＢＯＸ：米国、ウクライナ難民受け入れが少ない理由」. \nurl , (参照 2021-6-21).\n著者とサイトネームが異なることもある",
                                   font=('Helvetica', '10'))
        self.titleLabel3.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame3, text = '著者・機関名').pack(anchor='center')#説明と
        self.author3 = tk.Entry(self.frame3, width=30)#エントリーボタン
        self.author3.pack(anchor='center')

        self.label = tk.Label(self.frame3, text = '記事の日付').pack(anchor='center')
        self.year3 = tk.Entry(self.frame3, width=30)
        self.year3.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame3, text = 'タイトル').pack(anchor='center')
        self.title3 = tk.Entry(self.frame3, width=30)
        self.title3.pack(anchor='center')

        self.label4 = tk.Label(self.frame3, text = 'サイトネーム').pack(anchor='center')
        self.sitename3 = tk.Entry(self.frame3, width=30)
        self.sitename3.pack(anchor='center')

        self.label5 = tk.Label(self.frame3, text = 'リンク（日付は自動入力される)').pack(anchor='center')
        self.link3 = tk.Entry(self.frame3, width=30)
        self.link3.pack(anchor='center')
        #出力
        self.output_button = tk.Button(self.frame3, text="出力する", command=lambda : self.addAll3())
        self.output_button.pack(anchor='center')
        #コピーボタン
        self.copy_button =tk.Button(self.frame3, text="内容をコピー", command=lambda : self.copy_text(self.outputtext3))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext3= tk.Text(self.frame3,width=100,height=2)
        self.outputtext3.pack(anchor='center')#side=tk.LEFT
        # フレーム3からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame3, text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()
#-------------------------------frame4-------------------------------------------
        #移動先フレーム4作成
        self.frame4 =tk.Frame()
        self.frame4.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel4 = tk.Label(self.frame4, text="英語＆書籍", font=('Helvetica', '15'))
        self.titleLabel4.pack(anchor='n', expand=True)
        self.titleLabel4 = tk.Label(self.frame4,
                                   text="例：Smith, T. (2020). The citation manual for students: A quick guide (2nd ed.). Wiley.",
                                   font=('Helvetica', '10'))
        self.titleLabel4.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame4, text = '著者 ex)Svendsen, S., & Rudd, A., & Gordon, B. S.').pack(anchor='center')#説明と
        self.author4 = tk.Entry(self.frame4, width=30)#エントリーボタン
        self.author4.pack(anchor='center')

        self.label2 = tk.Label(self.frame4, text = '出版年').pack(anchor='center')
        self.year4 = tk.Entry(self.frame4, width=30)
        self.year4.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame4, text = 'タイトル　＊斜体').pack(anchor='center')
        self.title4 = tk.Entry(self.frame4, width=30)
        self.title4.pack(anchor='center')

        self.label4 = tk.Label(self.frame4, text = '出版社・出版機関 ').pack(anchor='center')
        self.publisher4 = tk.Entry(self.frame4, width=30)
        self.publisher4.pack(anchor='center')

        #出力
        self.output_button = tk.Button(self.frame4, text="出力する", command=lambda : self.addAll4())
        self.output_button.pack(anchor='center')
        #コピーボタン
        self.copy_button =tk.Button(self.frame4, text="内容をコピー", command=lambda : self.copy_text(self.outputtext4))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext4= tk.Text(self.frame4,width=100,height=2)
        self.outputtext4.pack(anchor='center')#side=tk.LEFT
        # フレーム4からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame4, text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()
#-------------------------------frame5-------------------------------------------
        #移動先フレーム5作成
        self.frame5 =tk.Frame()
        self.frame5.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel5 = tk.Label(self.frame5, text="英語＆論文", font=('Helvetica', '15'))
        self.titleLabel5.pack(anchor='n', expand=True)
        self.titleLabel5 = tk.Label(self.frame5,
                                   text="例: Tokar, B. (2015). Democracy, localism, and the future of the climate movement. World Futures, 71(3-4), 65-75, link",
                                   font=('Helvetica', '10'))
        self.titleLabel5.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame5, text = '著者 ex)Svendsen, S., & Rudd, A., & Gordon, B. S.').pack(anchor='center')#説明と
        self.author5 = tk.Entry(self.frame5, width=30)#エントリーボタン
        self.author5.pack(anchor='center')

        self.label2 = tk.Label(self.frame5, text = '出版年').pack(anchor='center')
        self.year5 = tk.Entry(self.frame5, width=30)
        self.year5.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame5, text = 'タイトル').pack(anchor='center')
        self.title5 = tk.Entry(self.frame5, width=30)
        self.title5.pack(anchor='center')

        self.label4 = tk.Label(self.frame5, text = '研究論集・ジャーナル名 ＊斜体').pack(anchor='center')
        self.magazine5 = tk.Entry(self.frame5, width=30)
        self.magazine5.pack(anchor='center')

        self.label4 = tk.Label(self.frame5, text = '巻号').pack(anchor='center')
        self.volume5 = tk.Entry(self.frame5, width=30)
        self.volume5.pack(anchor='center')

        self.label4 = tk.Label(self.frame5, text = '号数').pack(anchor='center')
        self.number5 = tk.Entry(self.frame5, width=30)
        self.number5.pack(anchor='center')

        self.label5 = tk.Label(self.frame5, text = 'ページ数（数字だけ入力)').pack(anchor='center')
        self.page5 = tk.Entry(self.frame5, width=30)
        self.page5.pack(anchor='center')

        self.label5 = tk.Label(self.frame5, text = 'リンク').pack(anchor='center')
        self.link5 = tk.Entry(self.frame5, width=30)
        self.link5.pack(anchor='center')
        
        #出力
        self.output_button = tk.Button(self.frame5, text="出力する", command=lambda : self.addAll5())
        self.output_button.pack(anchor='center')
        #コピーボタン
        self.copy_button =tk.Button(self.frame5, text="内容をコピー", command=lambda : self.copy_text(self.outputtext5))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext5= tk.Text(self.frame5,width=100,height=2)
        self.outputtext5.pack(anchor='center')#side=tk.LEFT
        # フレーム5からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame5,text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()
#-------------------------------frame6-------------------------------------------
        #移動先フレーム6作成
        self.frame6 =tk.Frame()
        self.frame6.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel6 = tk.Label(self.frame6, text="英語＆ウェブサイト", font=('Helvetica', '15'))
        self.titleLabel6.pack(anchor='n', expand=True)
        self.titleLabel6 = tk.Label(self.frame6,
                                   text="例: Popkin, G. (2020, August 12). Global warming could unlock carbon from tropical soil. The New York Times. https://www.nytimes.com/2020/08/12/climate/tropical-soils-climate-change.html",
                                   font=('Helvetica', '10'))
        self.titleLabel6.pack(anchor='n', expand=True)
        #専用のentryウィジェット
        self.label1 = tk.Label(self.frame6, text = '著者 ex)Svendsen, S., & Rudd, A., & Gordon, B. S.').pack(anchor='center')#説明と
        self.author6 = tk.Entry(self.frame6, width=30)#エントリーボタン
        self.author6.pack(anchor='center')

        self.label2 = tk.Label(self.frame6, text = '出版年').pack(anchor='center')
        self.year6 = tk.Entry(self.frame6, width=30)
        self.year6.pack(anchor='center')
        
        self.label3 = tk.Label(self.frame6, text = 'タイトル').pack(anchor='center')
        self.title6 = tk.Entry(self.frame6, width=30)
        self.title6.pack(anchor='center')

        self.label4 = tk.Label(self.frame6, text = '出版社・出版機関*斜体（ない場合も）').pack(anchor='center')
        self.publisher6 = tk.Entry(self.frame6, width=30)
        self.publisher6.pack(anchor='center')

        self.label5 = tk.Label(self.frame6, text = 'リンク').pack(anchor='center')
        self.link6 = tk.Entry(self.frame6, width=30)
        self.link6.pack(anchor='center')
        #出力
        self.output_button = tk.Button(self.frame6, text="出力する", command=lambda : self.addAll6())
        self.output_button.pack(anchor='center')
        #コピーボタン
        self.copy_button =tk.Button(self.frame6, text="内容をコピー", command=lambda : self.copy_text(self.outputtext6))
        self.copy_button.pack(anchor='center')
        
        #テキストウィジェット
        self.outputtext6= tk.Text(self.frame6,width=100,height=2)
        self.outputtext6.pack(anchor='center')#side=tk.LEFT
        # フレーム6からmainフレームに戻るボタン
        self.back_button = tk.Button(self.frame6, text="入力ページに戻る", command=lambda : self.changePage(self.main_frame))
        self.back_button.pack(anchor='center')        #main_frameを一番上に表示
        self.main_frame.tkraise()        
#-------------------------------メソッド各種-------------------------------------------
    def changePage(self, page):#引数のページを最前線に表示する
        '''
        画面遷移用の関数
        '''
        #self.reset_all(page)
        page.tkraise()
    def check(self):
        'ラジオボタンで選択したものを変数に変換し、chengepageで特定のフレームに移動する'
        self.lang_variable = self.select_var_lang.get()
        self.for_variable =self.select_var_for.get()
        if self.lang_variable  == 1:
            if self.for_variable ==3:
                self.changePage(self.frame1)
            elif self.for_variable ==4:
                self.changePage(self.frame2)
            else:
                self.changePage(self.frame3)
        if self.lang_variable  == 2:
            if self.for_variable ==3:
                self.changePage(self.frame4)
            elif self.for_variable == 4:
                self.changePage(self.frame5)
            else:
                self.changePage(self.frame6)
    def copy_text(self, outputtext):
        'テキストウィジェットの内容を反映させてボタンを押すとコピーできる仕様'
        text_var = outputtext.get(1.0,"end")
        self.clipboard_clear()
        self.clipboard_append(text_var)
    def addAll1(self):
        self.outputtext1.delete(1.0,"end")
        
        text_frame1 = "{0}({1}).「{2}」.{3}, 全pp.{4}."
        self.outputtext1.insert(1.0,text_frame1.format(self.author1.get(),
                                                     self.year1.get(),
                                                     self.title1.get(),
                                                     self.publisher1.get(),
                                                     self.page1.get())
                          )

    def addAll2(self):
        self.outputtext2.delete(1.0,"end")
        text_frame2 = "{0}({1}).「{2}」.『{3}』{4}巻, {5}号, pp.{6}. {7}" #古重奈央(2019).「小学校家庭科における片づけの学習の検討」『日本教科教育学会誌』42巻, 3号, pp.55-67. \nurl
        self.outputtext2.insert(1.0,text_frame2.format(self.author2.get(),
                                                 self.year2.get(),
                                                 self.title2.get(),
                                                 self.magazine2.get(),
                                                 self.volume2.get(),
                                                 self.number2.get(),
                                                 self.page2.get(),
                                                 self.getDate(self.link2.get()))
                          )
        #確認用　print(self.outputtext2.get(1.0,"end"))
    def addAll3(self):
        self.outputtext3.delete(1.0,"end")
        text_frame3 = "{0}({1}).「{2}」. {3}. {4}."
        self.outputtext3.insert(1.0,text_frame3.format(self.author3.get(),
                                                     self.year3.get(),
                                                     self.title3.get(),
                                                     self.sitename3.get(),
                                                     self.getDate(self.link3.get()))
                          )
    def addAll4(self):
        self.outputtext4.delete(1.0,"end")
        text_frame4 = "{0} ({1}). {2}. {3}."
        self.outputtext4.insert(1.0,text_frame4.format(self.author4.get(),
                                                     self.year4.get(),
                                                     self.title4.get(),
                                                     self.publisher4.get(),
                          ))
    def addAll5(self):
        self.outputtext5.delete(1.0,"end")
        text_frame5 = "{0} ({1}). {2}. {3}, {4}({5}), {6}, {7}"
        self.outputtext5.insert(1.0,text_frame5.format(elf.author5.get(),
                                                 self.year5.get(),
                                                 self.title5.get(),
                                                 self.magazine5.get(),
                                                 self.volume5.get(),
                                                 self.number5.get(),
                                                 self.page5.get(),
                                                 self.link5.get(),
                          ))
    def addAll6(self):
        self.outputtext6.delete(1.0,"end")
        text_frame6 = "{0} ({1}). {2}. {3}. {4}."
        self.outputtext6.insert(1.0,text_frame6.format(self.author6.get(),
                                                     self.year6.get(),
                                                     self.title6.get(),
                                                     self.sitename6.get(),
                                                     self.link6.get())
                          )
    #def clearAll(self, selected_frame):
    #ホームに戻ったときに各要素をクリアにしたかったけどできず
    def getDate(self, link):
        import datetime
        dt = datetime.datetime.today()
        d = dt.date()
        s = link+" ,(最終閲覧日"+str(d)+")"
        return s

if __name__ == "__main__": #ｔｋなんとかとかしなくてもいいやつやな。
    print("下記を参考にしました\n補足:Intextは　Popkin (2020)")
    list1 = ["https://www.lib.niigata-u.ac.jp/learning_support/doc/20210709-3.pdf",
        "http://www.ritsumei.ac.jp/ir/ir-navi/common/pdf/technic/technic_text_01.pdf",
        "https://www.scribbr.com/apa-examples/newspaper-article/"]
    list2 =["新潟大学のページ","立命館大学のページ","英語の参考文献 Scibble"]
    for a in range(3):
        print(list2[a],":",list1[a])
    app = App()

    app.mainloop()

#----(https://qiita.com/seisantaro/items/74ed83fec3d126553245)--
#(https://water2litter.net/rum/post/python_tkinter_clipboard/)
#(https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/)
#専用のentryウィジェット https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/  , https://yuta0306.github.io/tk-entry-default

