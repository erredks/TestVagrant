from TestVagrant import test_playlist


def test_1():
    userList = ['bhaskar', "digvijay"]
    playList = [['s1', 's2', 's1', 's3', "s2", "s1"], ['s4', 's5', 's6']]
    limit = 2
    test_playlist.playlist(userList, playList, limit)
    assert test_playlist.playlist_dict['bhaskar'] == ['s2', 's1']
    print(test_playlist.playlist_dict)

    new_user = ["bhaskar", 'tarun', 'digvijay']
    new_song = ['k1', 't1', 's5']
    test_playlist.check_playlist(new_user, new_song, limit)
    assert test_playlist.playlist_dict['tarun'] == ['t1']
    # print(playlist_dict)


def test_cheking_greater_limit():
    userList = ['bhaskar', "digvijay"]
    playList = [['s1', 's2', 's1', 's3', "s2", "s1"], ['s4', 's5', 's6']]
    limit = 5
    test_playlist.playlist(userList, playList, limit)
    assert test_playlist.playlist_dict['bhaskar'] == ['s3', 's2', 's1']
    print(test_playlist.playlist_dict)
