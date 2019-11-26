def alias(snip):
    vim.eval('feedkeys("{}\<C-R>=UltiSnips#ExpandSnippet()\<CR>")'.format(snip))
