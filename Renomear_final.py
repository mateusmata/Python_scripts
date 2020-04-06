import os

os.chdir('D:\Midia\Serie\The Office (US)\Season 1 - Copia') #pasta com arquivos que sofrerão alteração

print (os.getcwd())

for f in os.listdir():                                  #para cada arquivo
    f_name, f_ext = os.path.splitext(f)         
    
    if f_ext=='.srt':                                   # verificar se é .srt
        l_ep = f_name.split('-')
        l_ep = l_ep[1].strip()                          #extrair apenas o episodio
        #print (l_ep)
        for x in os.listdir():
            f2_name, f2_ext = os.path.splitext(x) 
            if f2_ext=='.mkv':                           #encontrar .mkv do mesmo ep      
                vid_ep = f2_name.split('.')
                vid_ep = vid_ep[2]
                if vid_ep==l_ep:  
                    new_name = '{}{}'.format(f2_name, f_ext)
                    os.rename(f, new_name)