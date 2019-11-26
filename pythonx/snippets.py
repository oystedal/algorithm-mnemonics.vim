import vim

def expand(snip, jump_pos=1):
    if snip.tabstop != jump_pos:
        return
    vim.eval('feedkeys("\<C-R>=UltiSnips#ExpandSnippet()\<CR>")')
