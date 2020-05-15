from libc.stdio cimport fprintf, FILE, fdopen, fflush

def printf(fobj):
    cdef FILE* cfile
    # attach the stream
    cfobj = fdopen(fobj.fileno(), 'w+')

    fprintf(cfobj, "hello world\n");

    # this is required
    fflush(cfobj)

