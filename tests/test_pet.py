from api import Pets

pt = Pets()


def test_get_registered():
    status = pt.get_registered()[0]
    users_id = pt.get_registered()[1]
    users_token = pt.get_registered()[2]
    assert status == 200
    assert users_id
    assert users_token


def test_register_and_delete_user():
    status = pt.register_and_delete_user()[0]
    my_id = pt.register_and_delete_user()[1]
    assert status == 200
    assert my_id


def test_get_token():
    status = pt.get_token()[1]
    my_token = pt.get_token()[0]
    my_id = pt.get_token()[2]
    assert status == 200
    assert my_token
    assert my_id


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_get_pet_id():
    status = pt.get_pet_id()
    assert status == 200


def test_patch_pet():
    status = pt.patch_pet()[1]
    pet_id = pt.patch_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_like():
    status = pt.get_pet_like()
    assert status == 200


def test_put_pet_comment():
    status = pt.put_pet_comment()
    assert status == 200


def test_post_pets_list():
    status = pt.post_pets_list()
    assert status == 200


def test_delete_pet_id():
    status = pt.get_pet_id()
    assert status == 200
