def test_home_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json['status'] == 'ready'

def test_invalid_url(client):
    response = client.get('/invalid')

    assert response.status_code == 404
    assert response.json['error'] == 'NotFound'


# def test_raises():
#     with pytest.raises(IntegrityError) as exc_info:
#         handle_error(IntegrityError)
#     assert exc_info.value.args[0] == 'column "student_id" is not unique'