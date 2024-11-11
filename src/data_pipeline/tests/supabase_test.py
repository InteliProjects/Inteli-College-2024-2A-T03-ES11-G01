import pytest
from unittest.mock import patch, MagicMock, mock_open


from core.supabase_client import clear_bucket, create_bucket, delete_bucket, download_file, get_bucket, list_buckets, upload_file

@pytest.fixture
def mock_supabase():
    with patch('core.supabase_client.supabase') as mock_supabase:
        yield mock_supabase

def test_create_bucket_new(mock_supabase):
    mock_supabase.storage.list_buckets.return_value = []
    mock_supabase.storage.create_bucket.return_value = {"status": "success"}

    result = create_bucket("test_bucket")
    assert result == {"status": "success"}
    mock_supabase.storage.create_bucket.assert_called_with("test_bucket")

# def test_create_bucket_exists(mock_supabase):
#     mock_supabase.storage.list_buckets.return_value = [{"name": "test_bucket"}]
    
#     result = create_bucket("test_bucket")
#     assert result == {"error": "already exists"}

def test_get_bucket(mock_supabase):
    mock_bucket = {"name": "test_bucket"}
    mock_supabase.storage.get_bucket.return_value = mock_bucket

    result = get_bucket("test_bucket")
    assert result == mock_bucket
    mock_supabase.storage.get_bucket.assert_called_with("test_bucket")

def test_clear_bucket(mock_supabase):
    mock_supabase.storage.empty_bucket.return_value = {"status": "success"}

    result = clear_bucket("test_bucket")
    assert result == {"status": "success"}
    mock_supabase.storage.empty_bucket.assert_called_with("test_bucket")

def test_delete_bucket(mock_supabase):
    mock_supabase.storage.delete_bucket.return_value = {"status": "success"}

    result = delete_bucket("test_bucket")
    assert result == {"status": "success"}
    mock_supabase.storage.delete_bucket.assert_called_with("test_bucket")

def test_upload_file(mock_supabase, tmp_path):
    file_path = tmp_path / "test.txt"
    file_content = "content"
    file_path.write_text(file_content)

    mock_supabase.storage.from_.return_value.upload.return_value = {"status": "success"}

    # Use mock_open to mock the behavior of opening the file
    with patch("builtins.open", mock_open(read_data=file_content)) as mock_file:
        result = upload_file("test_bucket", str(file_path), "test.txt")
        assert result == {"status": "success"}
        mock_supabase.storage.from_.assert_called_with("test_bucket")
        mock_supabase.storage.from_().upload.assert_called_with("test.txt", mock_file.return_value)

def test_download_file(mock_supabase, tmp_path):
    local_path = tmp_path / "downloaded.txt"
    mock_supabase.storage.from_.return_value.download.return_value = b"content"

    result = download_file("test_bucket", "test.txt", str(local_path))
    assert result == f"File downloaded successfully to {local_path}"
    assert local_path.read_text() == "content"
    mock_supabase.storage.from_.assert_called_with("test_bucket")
    mock_supabase.storage.from_().download.assert_called_with("test.txt")
