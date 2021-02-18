#遅々として学習が進まない。。焦らず。
#練習！　１７：５１
#練習！　１8：06


def hangman(word):     #当ててほしい単語
    wrong=0       #何回間違えたか
    stages=['',                #↓↓↓↓ステージ
            '_______     ',
            '|     |     ',
            '|     O     ',
            '|    /|\    ',
            '|   / | \   ',
            '|     |     ',
            '|    / \    ',
            '|   /   \   ',
            '|           '
            ]
    rletters=list(word)          #当ててほしい単語を一文字ずつ分解したリスト
    board=['_']*len(word)        #当たった箇所、当たっていない箇所を表示しておく。 wordの中の数だけ持つ 
    win=False              #初期状態はFalseにしておく
    print('文字当てクイズです')

    #以下はゲーム手順のループ

    while wrong <len(stages)-1:         #ステージと同じ回数間違えたら終了 −１はステージ０との整合
        print('\n')            #体裁のために空白を出力
        msg='ドラえもんの登場人物です。１文字を予想してね：'
        char=input(msg)        #入力された解答をcharに入れる
        if char in rletters:       #char がrletters のなかにあったら正解
            cind=rletters.index(char)
            board[cind]=char          #正解したらboardを更新　※['正','_','_']のように
            rletters[cind]='$'     #同じ文字の正解を含む場合に備えて、解答を＄に置き換える
        else:
            wrong+=1          #不正解の場合はWRONGをインクリメント
        print(' '.join(board))  #ステージを一つ表示させるための処理｛わかりにくい｝
                       #仮に全部表示は「'/n'.join(steges)」→リストの文字列を改行コードで結合して出力
        e=wrong +1        #開始インデックス０につき、終了インデックスはWRONG+1
        print('\n'.join(stages[0:e]))   #STAGESからリストをスライスで取り出す。進行通りの表示に。
        if "_" not in board:       #BOARDに＿がなければ　
            print('あなたの勝ち！')
            print(' '.join(board))  #正解の単語も表示　
            win=True
            break
    if not win:       #負けていた場合
        print('/n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は｛｝.'.format(word))

#チャレンジ問題　できた最高

