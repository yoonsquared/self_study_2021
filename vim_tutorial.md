# VIM tutorial
## Moving The Cursor
```
- h: left
- j: down
- k: up
- l: right
```

## Quiting
```
- ':wq'
- ':q', ':exit', ZZ
```

## Modes
### Normal Mode
> navigation and some copy paste type of actions
> hjkl works for the cursor movement
gg: first line
G (shift+g): end of line
0: first word of the line
{number}G(shift+g): goes to the {number} line.
x: delete key, delete the char behind the cursor.
u: undo whatever you just did.
dw: deletes a word on the cursor.
dd: delete line.
{number}dd: delete {number} of lines.
w: navigate to next word in the first character.
e: navigate through end of word.
b: navigate backwords.
{number}(w,b,h,j,k,l): navigate through {number} of words forward or backward (or character direction for hjkl)
p: paste

#### cut and paste
> delete and go to line 17 and paste
dd 17G p

### Insert Mode 'i' in normal mode
You can start writing.
esc to go back to normal mode.
 
### visual mode
highlight text by navigating.

