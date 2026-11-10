import pytest
from unittest.mock import patch, MagicMock
from vuln import get_user, run

def test_get_user_calls_sqlite_and_returns_result():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.execute.return_value = mock_cursor
    with patch('sqlite3.connect', return_value=mock_conn) as mock_connect:
        result = get_user('alice')
        mock_connect.assert_called_once_with('db')
        mock_conn.execute.assert_called_once_with('SELECT * FROM users WHERE name = ?', ('alice',))
        assert result is mock_cursor

def test_run_with_string_calls_subprocess_call():
    with patch('subprocess.call', return_value=0) as mock_call:
        ret = run('ls -l /tmp')
        mock_call.assert_called_once_with(['ls', '-l', '/tmp'], shell=False)
        assert ret == 0

def test_run_with_list_calls_subprocess_call():
    with patch('subprocess.call', return_value=1) as mock_call:
        ret = run(['echo', 'hello'])
        mock_call.assert_called_once_with(['echo', 'hello'], shell=False)
        assert ret == 1