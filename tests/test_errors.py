import sys
sys.path.append('..')
import config
import nose.tools

from beanstalk import errors

def test_checkError():
    def t_func(rstring, error):
        nose.tools.assert_raises(error, errors.checkError, rstring)

    errorlist = [(errors.OutOfMemory, 'OUT_OF_MEMORY'),
                 (errors.InternalError, 'INTERNAL_ERROR'),
                 (errors.Draining, 'DRAINING'),
                 (errors.BadFormat, 'BAD_FORMAT'),
                 (errors.UnknownCommand, 'UNKNOWN_COMMAND'),
                 (errors.ExpectedCrlf, 'EXPECTED_CRLF'),
                 (errors.JobTooBig, 'JOB_TOO_BIG'),
                 (errors.NotFound, 'NOT_FOUND'),
                 (errors.NotIgnored, 'NOT_IGNORED')]

    for error, rstring in errorlist:
        yield t_func, rstring, error
