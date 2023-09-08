from TestVagrant import test_playlist


def test_goodflow():
    userList = ['bhaskar', "digvijay"]
    playList = [['s1', 's2', 's1', 's3', "s2", "s1"], ['s4', 's5', 's6']]
    limit = 2
    test_playlist.create_playlist(userList, playList, limit)
    assert test_playlist.playlist_dict['bhaskar'] == ['s2', 's1']
    print(test_playlist.playlist_dict)

    # callin check_playlist function
    new_user = ["bhaskar", 'tarun', 'digvijay']
    new_song = ['k1', 't1', 's5']
    test_playlist.check_playlist(new_user, new_song, limit, test_playlist.playlist_dict)
    assert test_playlist.playlist_dict['digvijay'] == ['s6', 's5']
    assert test_playlist.playlist_dict['bhaskar'] == ['s1', 'k1']

def test_check_newly_inserted_data():
    new_user = ["bhaskar", 'tarun', 'digvijay']
    new_song = ['k1', 't1', 's5']
    new_dict = {'bhaskar': ['s2', 's1'], 'digvijay': ['s5', 's6']}  # creating valid dictionary
    limit = 2
    test_playlist.check_playlist(new_user, new_song, limit, new_dict)
    assert new_dict['tarun'] == ['t1']
    assert new_dict['bhaskar'] == ['s1', 'k1']
    # print(playlist_dict)


def test_cheking_greater_limit():
    userList = ['bhaskar', "digvijay"]
    playList = [['s1', 's2', 's1', 's3', "s2", "s1"], ['s4', 's5', 's6']]
    limit = 5
    test_playlist.create_playlist(userList, playList, limit)
    assert test_playlist.playlist_dict['bhaskar'] == ['s3', 's2', 's1']
    print(test_playlist.playlist_dict)
