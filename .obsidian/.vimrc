set clipboard=unnamed
nmap ; :
nmap j gj
nmap k gk
nmap H ^
nmap L $
exmap back obcommand app:go-back
nmap <C-o> :back
exmap forward obcommand app:go-forward
nmap <C-i> :forward
exmap togglefold obcommand editor:toggle-fold
nmap zo :togglefold
nmap zc :togglefold
nmap za :togglefold
