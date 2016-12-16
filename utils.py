def _normalise_folder(self, folder_name):
    if isinstance(folder_name, binary_type):
        folder_name = folder_name.decode('ascii')
    if self.folder_encode:
        folder_name = encode_utf7(folder_name)
    return _quote(folder_name)
        
def _do_list(self, cmd, directory, pattern):
    directory = self._normalise_folder(directory)
    pattern = self._normalise_folder(pattern)
    typ, dat = self._imap._simple_command(cmd, directory, pattern)
    self._checkok(cmd, typ, dat)
    typ, dat = self._imap._untagged_response(typ, dat, cmd)
    return self._proc_folder_list(dat)

def _proc_folder_list(self, folder_data):
    # Filter out empty strings and None's.
    # This also deals with the special case of - no 'untagged'
    # responses (ie, no folders). This comes back as [None].
    folder_data = [item for item in folder_data if item not in ('', None)]

    ret = []
    parsed = parse_response(folder_data)
    while parsed:
        # TODO: could be more efficient
        flags, delim, name = parsed[:3]
        parsed = parsed[3:]

        if isinstance(name, (int, long)):
            # Some IMAP implementations return integer folder names
            # with quotes. These get parsed to ints so convert them
            # back to strings.
            name = text_type(name)
        elif self.folder_encode:
            name = decode_utf7(name)

        ret.append((flags, delim, name))
    return ret        
