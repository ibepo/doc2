# IdeaVim

```shell
let mapleader = " "
set easymotion
set surround
set commentary
set argtextobj
set cursorline
set NERDTree
set textobj-entire
set ReplaceWithRegister
set multiple-cursors
set nu
set hlsearch
set incsearch
set showmode
set showtabline=2
set clipboard=unnamed
set clipboard+=ideaput
set ignorecase smartcase
inoremap jk <Esc>
noremap <leader><leader>r <ESC>:source ~/.ideavimrc<CR>
noremap H ^
noremap L $
noremap <C-O> <ESC>:action Back<CR>
noremap <C-I> <ESC>:action Forward<CR>
noremap <C-k> 5kzz
noremap <C-j> 5jzz
noremap E gT
noremap R gt
nnoremap o $a<cr><esc>
noremap J <ESC>:action EditorJoinLines<CR>
noremap <leader>` <ESC>:action SelectInProjectView<CR>
noremap <leader>j <ESC>:action GotoNextError<CR>
noremap <leader>k <ESC>:action GotoPreviousError<CR>
noremap <leader>e <ESC>:action HideAllWindows<CR>
noremap <leader>l <ESC>:action HighlightUsagesInFile<CR>
noremap <leader>r <ESC>:action Run<CR>
noremap <leader>w <ESC>:action ReformatCode<CR>
noremap <leader>q <ESC>:wq<CR>
noremap <leader>a <ESC>:action ShowErrorDescription<CR>
noremap <leader>t <ESC>:action Refactorings.QuickListPopupAction<CR>
noremap <leader>u <ESC>:action ShowUsages<CR>
noremap <leader>i <ESC>:action Maven.Reimport<CR>
noremap <leader>o <ESC>:action ShowFilePath<CR>
noremap <leader>p <ESC>:action ManageRecentProjects<CR>
noremap <leader>d <ESC>:action ChooseDebugConfiguration<CR>
noremap <leader>g <ESC>:action Generate<CR>

noremap / <ESC>:action Find<CR>
noremap ' <ESC>:action Replace<CR>
noremap g/ <ESC>:action FindInPath<CR>
noremap g' <ESC>:action ReplaceInPath<CR>
nnoremap <leader>s <ESC>:action FileStructurePopup<CR>
nnoremap <leader>f <ESC>:action GotoFile<CR>
nnoremap ;f :action SearchEverywhere<CR>
nnoremap ;g :action FindInPath<CR>
nnoremap ;r :action RecentFiles<CR>

noremap <leader>z <ESC>:action Resume<CR>
noremap <leader>x <ESC>:action StepOver<CR>
noremap <leader>c <ESC>:action SmartStepInto<CR>
noremap <leader>v <ESC>:action EvaluateExpression<CR>
noremap <leader>b <ESC>:action ViewBreakpoints<CR>
noremap <leader>n <ESC>:action ToggleLineBreakpoint<CR>
noremap <leader>m <ESC>:action XDebugger.MuteBreakpoints<CR>
noremap gt <ESC>:action $EditorTranslateAction<CR>
noremap gy <ESC>:action CopyReference<CR>
noremap gi <ESC>:action ShowIntentionActions<CR>
noremap gp <ESC>:action ParameterInfo<CR>
noremap gs <ESC>:action GotoImplementation<CR>
noremap gd <ESC>:action GotoDeclaration<CR>

noremap zo <ESC>:action ExpandRegion<CR>
noremap zf <ESC>:action CollapseRegion<CR>

noremap gx <ESC>:action CloseAllEditorsButActive<CR>
noremap ghc <ESC>:action CallHierarchy<CR>
noremap ght <ESC>:action TypeHierarchy<CR>
noremap ghm <ESC>:action MethodHierarchy<CR>
noremap gj <ESC>:action SliceBackward<CR>
noremap gk <ESC>:action SliceForward<CR>
noremap gc <ESC>:action CompileDirty<CR>
noremap gb <ESC>:action FindBugs.CurrentFileAction<CR>
noremap gn <ESC>:action GotoClass<CR>
noremap gm <ESC>:action GotoSymbol<CR>

noremap \u <ESC>:action ShowUmlDiagramPopup<CR>
noremap \[ <ESC>:action Gitflow.OpenGitflowPopup<CR>
noremap \] <ESC>:action Vcs.QuickListPopupAction<CR>


noremap [[ <ESC>:action MethodUp<CR>
noremap ]] <ESC>:action MethodDown<CR>

nnoremap <Leader>1 1gt
nnoremap <Leader>2 2gt
nnoremap <Leader>3 3gt
nnoremap <Leader>4 4gt
nnoremap <Leader>5 5gt
nnoremap <Leader>6 6gt
nnoremap <Leader>7 7gt
nnoremap <Leader>8 8gt
nnoremap <Leader>9 9gt

```
